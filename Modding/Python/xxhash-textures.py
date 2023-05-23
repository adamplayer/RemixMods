import os
import sys
import xxhash

def strip_headers_and_generate_hash(file_path):
    # Read the file and extract the raw data. Thanks @BlueAmulet!
    with open(file_path, 'rb') as file:
        data = file.read()
        
    dwHeight = int.from_bytes(data[12:16], "little")
    dwWidth  = int.from_bytes(data[16:20], "little")
    pfFlags  = int.from_bytes(data[80:84], "little")
    pfFourCC = data[84:88]
    bitCount = int.from_bytes(data[88:92], "little")
        
    mipsize = dwWidth*dwHeight
    if pfFlags & 0x4: # DDPF_FOURCC
        if pfFourCC == b'DXT1': # DXT1 is 4bpp
            mipsize //= 2
    elif pfFlags & 0x20242: # DDPF_ALPHA | DDPF_RGB | DDPF_YUV | DDPF_LUMINANCE
        mipsize = mipsize*bitCount//8
        
    hash_value = xxhash.xxh3_64(data[128:128+mipsize]).hexdigest()
    # Add the 0x that rtx.conf needs
    hash_value = "0x" + hash_value
    
    return hash_value

def generate_hashes_for_folder(folder_path):
    # Create a list to store the hashes
    hashes = []

    # Recursively iterate over all files in the folder
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)

            # Check if the file is a DDS file
            if file_name.lower().endswith('.dds') and os.path.isfile(file_path):
                # Generate the hash for the DDS file
                hash_value = strip_headers_and_generate_hash(file_path)
                hashes.append(f"{hash_value}")

    return hashes

def generate_hashes_for_folder_with_filter(folder_path, file_filter):
    # Create a list to store the hashes, but with a filter
    hashes = []

    # Recursively iterate over all files in the folder
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)

            # Check if the file is a DDS file
            if file_filter in file_path:
                if file_name.lower().endswith('.dds') and os.path.isfile(file_path):
                    # Generate the hash for the DDS file
                    hash_value = strip_headers_and_generate_hash(file_path)
                    hashes.append(f"{hash_value}")

    return hashes

def store_hashes_in_file(hashes, output_file_path):
    # Write the hashes to the output file
    with open(output_file_path, 'w') as output_file:
        for hash_value in hashes:
            output_file.write(f"{hash_value}, ")

    print(f"Hashes stored in {output_file_path}")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Please provide folder path and output text file as parameters.")
    else:
        if len(sys.argv) < 4:
            folder_path = sys.argv[1]
            output_file_path = sys.argv[2]

            hashes = generate_hashes_for_folder(folder_path)
            store_hashes_in_file(hashes, output_file_path)
        else:
            folder_path = sys.argv[1]
            output_file_path = sys.argv[2]
            file_filter = sys.argv[3]
            
            hashes = generate_hashes_for_folder_with_filter(folder_path, file_filter)
            store_hashes_in_file(hashes, output_file_path)
        