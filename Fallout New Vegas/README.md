# Fallout: New Vegas

## Current Status

<!-- Describe how the game functions with the remix modificaitons. Is it wonky and barely playable or could one consider a full playthrough possible? Make sure to warn of any flashing lights! -->

Working but struggles with multiple issues:
- ~~Multithreaded loaded seems to crash Bridge on texture loads~~ Fixed with BlueAmulet's hotfix.
- Lighting is originally done <!--Very Poorly... --> through pixel shaders, and is not able to be translated into the remix pipeline currently. _BlueAmulet has a proof of concept to fix this_

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
> This is really work in progress guide. The steps to get it working change daily or even hourly. This is a very good baseline but there will likely be new informarion in the discord that may contradict things here. Included in the repo are mine own ini's and conf's that _may_ work right out the box. They may also induce constant crashes...

1. (Re)install a fresh copy of the game.
2. Follow the Viva New Vegas guide.
    - Avoid installing any mods that enhance the visuals of the game. These may or may not cause problems with RTX Remix.
3. Install the _latest_ Remix builds.
4. Apply BlueAmulet's [temporary fix](https://github.com/BlueAmulet/bridge-remix/releases/tag/remix-mbc_hack) for multithreading from his repo. 
5. Run the `FalloutNVLauncher.exe` to get the baseline inis setup. 
6. Now use BethINI to setup the INIs used in Mod Organizer. 
    1. Change the target(?) to be the MO2 inis
    2. Set the game to `High` preset with the tweaks enabled. 
    3. Run through the settings and turn off all shaders, reflections, special effects, and shadows. 
    4. In the custom tab, under the controls section set `bBackground Keyboard=1` to `0`. Otherwise you won't be able to open the RTX-Remix menu.
    5. Save and Exit BethINI
6. Use Mod Organizer 2 to launch the game. 

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