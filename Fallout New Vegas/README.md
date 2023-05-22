# Fallout: New Vegas

## Current Status

<!-- Describe how the game functions with the remix modificaitons. Is it wonky and barely playable or could one consider a full playthrough possible? Make sure to warn of any flashing lights! -->

Working but struggles with multiple issues:
- Multithreaded loaded seems to crash Bridge on texture loads
- Lighting is originally done <!--Very Poorly... --> through pixel shaders, and is not able to be translated into the remix pipeline currently.

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

> **Note**
> This is really work in progress guide. Included in the repo are mine own ini's and conf's that _may_ work right out the box. They may also induce constant crashes...

1. (Re)install a fresh copy of the game.
2. Follow the Viva New Vegas guide.
    - Avoid installing any mods that enhance the visuals of the game. These may or may not cause problems with RTX Remix.
3. Install the _latest_ Remix builds.
4. Apply the `New Vegas Multithread fix` -- See discord for this one.
5. Rerun the `FalloutNVLauncher.exe`.
6. Set the game to `High` to enable further LOD distances.
    - It may be better to use BethINI for setting up the ini files since it has much more reasonable settings, as well as cleaning up the ini to not include so much bloat.
1. Change the line `bBackground Keyboard=1` in `Fallout.INI` and `FalloutPrefs.ini` to `bBackground Keyboard=0`. Otherwise you won't be able to open the RTX-Remix menu.
6. Launch the game with the `FalloutNV.exe`. Don't use Mod Organizer as it changes the ini files.

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

Since these games have a several render passes going on, there's quite a lot of textures that need marked as ignore. The actual apperance of what the textures are sometimes does not match what it is in the game. This makes things a bit difficult when digging through so many textures. If you suddenly have a dark dome texture around you, it's likely a dust texture that needs marked as ignore.

---