import sys
import os

def main():
    input_file = sys.argv[1]
    template_file = sys.argv[2]
    outputFileName = template_file + "_mod.usda"
    
    with open(input_file, "r") as f:
        dirtyhashes = f.read().split(", ")
        
    hashes = []
    for string in dirtyhashes:
        string = string.upper()
        hashes.append(string.replace("0X","mat_"))

    with open(template_file, "r") as f:
        template = f.read()
    
    with open("usda_header", "r") as f:
        header = f.read()

    with open("usda_footer", "r") as f:
        footer = f.read() 
    
    output = header
    
    for hash in hashes:
        foobar = template.replace("INPUTHASH", hash)
        output = output + foobar
        
    output = output + footer
    
    with open(outputFileName, "w") as f:
        f.write(output)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Please provide the texture hash  and template file as command-line arguments.")
        print("For example:")
        print("python hashToMod.py HASH ignoreTexture")
    else:
        main()