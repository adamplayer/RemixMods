# Need for Speed Underground 2 Remixed

<!-- Brief discription -->
Likely one of the best game suited for a remix. This one performs really well and has a ton of lights that can be added.

## Current Status

<!-- Describe how the game functions with the remix modificaitons. Is it wonky and barely playable or could one consider a full playthrough possible? Make sure to warn of any flashing lights! -->

- Culling is quite a problem. The game did not have backface culling so it instead culled harshly with things outside of the camera.

- My textures are rough and needs a lot of polish and work.

## Requirements

<!-- Table of Requirements
| Program | Notes |
| - | - |
| XYZ | Foobar | -->

- Copy of NFSU2
- Widescreenfix applied to it

---

## Step by step

<!-- List out the steps required to get working. Make sure to refer to the specific game `folders` that each `file` or action takes place in. Refer to the repo as _this_ folder. -->

### Stable Release

_**Coming Soon**_

1. Download and apply the _latest_ remix builds from Nvidia. Both the bridge and dxvk remix!
2. Download the latest release from this repo, open the archive and just paste it over.
3. Launch the game

### Pre-Release

> **Warning**
> These are not in a complete state. Set your expectations low.

1. Download and apply the _latest_ remix builds from Nvidia. Both the bridge and dxvk remix!
2. Get the latest pre-release from releases.
3. Drag the files into your game folder.
4. Launch the game!

#### Updating

> **Note**
> The textures are _not_ version tracked, so they won't be updated outside of releases.

1. Grab the base rtx.conf from here and place it your game folder.
2. Get the mod.usda.
3. Place it in the correct folder: `NFSU2/rtx-remix/mods/gameReadyAssets/`
5. Launch the game.

## Optional

<!-- Describe any optional programs or steps here. Commonly, it's adding an `asi` mod to the game requiring this brief discription:

Widescreen fix:
> This game has a Widescreenfix available! This greatly enhances the core game to improve compatiablity with modern systems and allows for easy window mode amoung other things. In order to use both RTXRemix and the Widescreenfix, rename `d3d9.dll` from the RTXRemix files to `d3d9.asi`. You can configure the Widescreenfix in the `scripts` folder.

Silentpatch:
> This game has a Silentpatch available! This greatly enhances the core game to improve compatiablity with modern systems and allows for easy window mode amoung other things. In order to use both RTXRemix and the Silentpatch, rename `d3d9.dll` from the RTXRemix files to `d3d9.asi`. You can configure Silentpatch in the `scripts` folder. -->

Back up your entire game folder once you get the game running! _Then_ apply rtxremix to it.

There are several remix mods in the works. See the discord for the latest information.

### Notes

<!-- List things things that don't fit anywhere else. --> 

**This is a work in progress.** 

#### Todo

- [ ] Update existing lights to use fixed exposure
- [ ] Complete adding lights to world
- [ ] Redo upscaled textures
- [ ] Redo main menu scene
- [ ] Redo garage scene
- [ ] Shop scenes
- [ ] Redo emissives to realistic scale