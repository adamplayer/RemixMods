# Fallout: New Vegas

## Current Status

<!-- Describe how the game functions with the remix modificaitons. Is it wonky and barely playable or could one consider a full playthrough possible? Make sure to warn of any flashing lights! -->

Howdy partner, we're all still figuring this dozzy out. Seems like the those giant geckos really doesn't want to be path traced...Don't worry, with enough time, effort, and praying to Todd Howard, anything is possible!

---

## Requirements

<!-- Table of Requirements
| Program | Notes |
| - | - |
| XYZ | Foobar | -->

- Refer to [Viva New Vegas](https://vivanewvegas.moddinglinked.com/index.html) for install instructions for getting the game running in 2023.

- GOG copies of the game are typically easier to debug when it  breaks. 

## Step by step

<!-- List out the steps required to get working. Make sure to refer to the specific game `folders` that each `file` or action takes place in. Refer to the repo as _this_ folder. -->

1. (Re)install a fresh copy of the game.
2. Perform the Initial Setup and MO2 sections of Viva New Vegas. Skip the `falloutcustom.ini` section in MO2.
3. Install xNVSE, JNI, and Crash Logger. Don't continue the guide, do not pass go.
4. Install the latest Remix builds.
5. Adjust your `DXVK.conf`:
```
d3d9.shadermodel = 2
d3d9.floatEmulation = strict
```
6. Rerun the `FalloutNVLauncher.exe` to get a new ini.
6. Launch the game with the `FalloutNV.exe`
6. ???
7. Profit

## Optional

<!-- Describe any optional programs or steps here. Commonly, it's adding an `asi` mod to the game requiring this brief discription:

Widescreen fix:
> This game has a Widescreenfix available! This greatly enhances the core game to improve compatiablity with modern systems and allows for easy window mode amoung other things. In order to use both RTXRemix and the Widescreenfix, rename `d3d9.dll` from the RTXRemix files to `d3d9.asi`. You can configure the Widescreenfix in the `scripts` folder.

Silentpatch:
> This game has a Silentpatch available! This greatly enhances the core game to improve compatiablity with modern systems and allows for easy window mode amoung other things. In order to use both RTXRemix and the Silentpatch, rename `d3d9.dll` from the RTXRemix files to `d3d9.asi`. You can configure Silentpatch in the `scripts` folder. -->

Backup your _entire_ game instance whenever you get it working if you have the space. The game typically breaks itself into a state where it won't run anymore and the easiest way to fix it just a clean slate.

### Notes

<!-- List things things that don't fit anywhere else. --> 

These Bethesda games are probably the one of the most unstable ones to be remixed. Be prepared to reinstall it frequently.

---

## Remix and New Vegas

Since these games have a several render passes going on, there's quite a lot of textures that need marked as ignore. The actual apperance of what the textures are sometimes does not match what it is in the game. This makes things a bit difficult when digging through so many textures.

