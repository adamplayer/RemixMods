# Remixing
Congrats on getting the game to accept RTX Remix! Now comes the fun part, remixing!

## What's here
### TextureRemix.py
This takes a folder, ideally exported from the games archive, and creates a usda file of overrides.

#### To use:
1. Download this entire folder, including the `usdFiles` folder
2. Install the python libraries in `requirements.txt`
3. Run the script in terminal with this structure: `python .\TextureRemix.py -d path\to\gameReadyAssets -t [type] -f [filter]`
4. This will create your new `.usda` files in the `usdFiles` folder. To use these, move these files into your `gameReadyAssets` folder, and edit your `mod.usda` file like so:

```
#usda 1.0
(
    subLayers = [
        @./emissiveTextures.usda@,
        @./normalTextures.usda@
    ]
)
```
This will load the new files while keeping your current replacement settings

## Further information and assistance
Join the [RTX Remix Showcase](https://discord.gg/rtxremix) discord server!

## Planned Guides
1. Adding lights, the easy way
2. Quick and easy texture remix
3. Proper texture remix
4. Properly relighting a scene
