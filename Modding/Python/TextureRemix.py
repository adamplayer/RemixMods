import os
import argparse
import xxhash
import re

def generate_hashes(file_path):
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

    return hash_value

def remove_duplicates(arr):
    seen = set()
    result = []
    
    for item in arr:
        if item[0] not in seen:
            seen.add(item[0])
            result.append(item)
    
    return result


def modWriter(template_file, inputArray):
    print(f"Creating USDA file...")
    # print(inputArray)
    # print(template_file)
    outputFileName = "usdFiles\\" + template_file + ".usda"

    with open(os.getcwd() + "\\usdFiles\\" + template_file + ".txt", "r") as f:
        template = f.read()
    
    with open("usdFiles\\usda_header.txt", "r") as f:
        header = f.read()

    with open("usdFiles\\usda_footer.txt", "r") as f:
        footer = f.read() 

    layers = ''

    foo = "INPUTHASH"
    bar = "NORMALHASH"
    baz = "EMISSIVEHASH"

    if template_file == "normalTextures":
        for x in range(len(inputArray)):
            temp1 = template.replace(foo, inputArray[x][0].upper())
            temp2 = temp1.replace(bar, inputArray[x][1])
            layers += temp2
    elif template_file == "emissiveTextures":
        for x in range(len(inputArray)):
            temp1 = template.replace(foo, inputArray[x][0].upper())
            temp2 = temp1.replace(baz, inputArray[x][1])
            layers += temp2
        
    output = header + layers + footer

    with open(outputFileName, "w") as f:
        f.write(output)
    print(f"Done!\n")
    return




def TextureRemix(directory, type_filter, name_filter):
    
    # The dev zone

    # Hardcode some filters just to get the ball rolling
    filters = ['_em', '_n', '_m', '_o', '_g']
    diffusehash = [] # Where we're going to store the diffuse textures.
    normalhash = [] # Store the normies here with it's matching parent texture
    emissivehash = [] 
    # opacityhash = [] # For a later date.
    # metalichash = [] # Rainy day

    # Make sure directory exists
    if not os.path.exists(directory):
        print(f'The directory {directory} does not exist.')
        return

    # Check type_filter validity
    if type_filter.lower() not in ['normal', 'emissive']:
        print(f'The type_filter {type_filter} is not valid.')
        return

    print(f'Searching for {type_filter}s with name containing "{name_filter}" in {directory}.')

    # Iterate over the directory content
    print(f"Generating Diffuse Hashes..")
    for root, dirs, files in os.walk(directory):
        for file in files:
            # print(file_path)
            if any(filter in file for filter in filters):
                pass
            else:
                file_path = os.path.join(root, file)
                diffusehash.append([file, generate_hashes(file_path)])

    print(f"Removing duplicate hashes...")
    diffusehash = remove_duplicates(diffusehash)
    # print(diffusehash)
    print(f"Done!\n")

    if type_filter.lower() == 'normal':
        print(f"Generating Normal Hashes..")
        templateFile="normalTextures"
        for root, dirs, files in os.walk(directory):
            for file in files:
                # print(file_path)
                if '_n' in file:
                    file_path = os.path.join(root, file)
                    normalhash.append([file_path, generate_hashes(file_path)])
                else:
                    pass
        print(f"Done!\n")
        # print(normalhash)

        print(f"Pairing up normals with their original texture")
        matches = [] # [(diffuseHash, normalMapLocation)]
        for diffuse_index in range(len(diffusehash)):
            diffuse_value = str(diffusehash[diffuse_index][0])[:-4]
            for normal_index in range(len(normalhash)):
                normal_value = str(normalhash[normal_index][0])[:-6]
                if diffuse_value in normal_value: # Set to `in` for fuzzy match and `==` for absolutes.
                    matches.append((str(diffusehash[diffuse_index][1]), str(normalhash[normal_index][0]))) 

        # print(matches)
        matches = remove_duplicates(matches)

        print(matches)

        print(f"Done!\n")

        modWriter(templateFile, matches)

 
    elif type_filter.lower() == 'emissive':
        print(f"Generating Emissive Hashes.. \n")
        templateFile="emissiveTextures"
        for root, dirs, files in os.walk(directory):
            for file in files:
                if '_em' in file:
                    file_path = os.path.join(root, file)
                    emissivehash.append([file_path, generate_hashes(file_path)])
        
        print(f"Done!\n")

        print(f"Pairing up emissives with their original texture")
        matches = [] 
        for diffuse_index in range(len(diffusehash)):
            diffuse_value = str(diffusehash[diffuse_index][0])[:-4]
            for emissive_index in range(len(emissivehash)):
                emissive_value = str(emissivehash[emissive_index][0])[:-6]
                if diffuse_value in emissive_value: 
                    emissive_file_path = str(emissivehash[emissive_index][0])
                    emissive_file_path = emissive_file_path.replace('.\\gameReadyAssets\\', './')
                    matches.append((str(diffusehash[diffuse_index][1]), emissive_file_path))


        matches = remove_duplicates(matches)

        print(matches)

        modWriter(templateFile, matches)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate hashes for DDS textures in a given directory based on a filter.")
    parser.add_argument('-d', '--directory', help='The directory to be searched', required=True)
    parser.add_argument('-t', '--type', help='Type to be searched. Should be Emissive, Normal, Metalic, Opacity', required=True)
    parser.add_argument('-f', '--filter', help='Filter string. Examples: _em, _n, _m, _o, _g', required=True)

    args = parser.parse_args()

    TextureRemix(args.directory, args.type, args.filter)
