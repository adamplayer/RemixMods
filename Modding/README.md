# Remixing
Congrats on getting the game to accept RTXRemix! Now comes the fun part, remixing.

## What's here
### `xxhash_texture.py`
This let's you generate hashes quickly if you are able to extract them from the game's files. 

#### Usage:

```xxhash_texture.py path/to/textures output.txt [optional string filter]```


### `hashToMod.py`
This takes those hashes, and creates a `usda` file that you (will evenutally) be able to set the material parameters.

#### Usage:
`hashToMod.py csvHashes.txt materialType output.usda`