# Warning
I am slowly moving on from developing *katarakta*, and I'm now working on rewriting it as an [M64MM3](https://github.com/projectcomet64/M64MM) add-on currently called *kataraktaCS* (*kCS* for short). *kataraktaCS* will have way more functionality, will be quicker and more lightweight, and will be easier to use than the original *katarakta*. Though, I do plan for *katarakta* to have an update with some features from the [Public Test 4 version](https://github.com/vazhka-dolya/katarakta/releases/tag/vpt4) added, but nothing major after that. Light maintenance, such as bugfixes or very small additions, is also planned.

*kataraktaCS* is still not released, though (and I have no idea when it will be), so you can keep using *katarakta* for now without any worries.

# katarakta
<img alt="GitHub Downloads (all assets, all releases)" src="https://img.shields.io/github/downloads/vazhka-dolya/katarakta/total?style=plastic&label=total%20downloads&color=0260A4">

*katarakta* is a tool made for Super Mario 64 machinimas that enables you to change Mario's textures quicker and makes it a lot less tedious.

<p align="center">
  <img src="https://github.com/vazhka-dolya/katarakta/blob/main/GitHubImg/katarakta_2.0.0_screenshot_1.png" width="666"/>
</p>

# Features
*katarakta*'s main functionality currently includes the following:
- Applying eye/cap/sidehair/mustache/button textures
- Applying any other texture
- Applying textures to a hi-res folder of other games
- Clearing the hi-res texture folders
- - The `Cache.ini` file also gets deleted if there is one
- Removing the black borders that are sometimes seen around textures after editing them

Additionally, the following features are present in the [latest Public Test version](https://github.com/vazhka-dolya/katarakta/releases/tag/vpt4):
- Dynamically changing textures in the game's RAM (only RGBA16 for now)
- Changing the eye states
- Dynamically [fixing black textures](https://github.com/vazhka-dolya/sm64_save_state_fixer) in the game's RAM

Also check out my add-ons for [M64MM3](https://github.com/projectcomet64/M64MM) — [BodyStates](https://github.com/vazhka-dolya/bodystates), [Tiny-Huge Tweaks](https://github.com/vazhka-dolya/TinyHugeTweaks), and [ChameleonCK](https://github.com/vazhka-dolya/ChameleonCK)!

# Setting Up
Firstly, you need a graphics plugin that supports texture packs, such as GLideN64 (recommended) or RiceVideo. You need to configure the plugin to be able to load the “hi-res” textures, there are numerous tutorials that can be found on how to do this, such as [GlitchyPSI's](https://www.youtube.com/watch?v=AsmwKbv054g), [Team Toad's](https://www.youtube.com/watch?v=o33pdMVl2Ow), or [mine](https://www.youtube.com/watch?v=1VsTe2No9eA) (has English subtitles), which also tries to explain how to set up katarakta (albeit pretty outdated).

After downloading the archive, extract it somewhere. What you need to run is `katarakta.exe`, you can (and have) to configure it by going to `Options` -> `Settings`. It shouldn't be too hard to configure, and some settings have hints (red question marks that you can hover your cursor over) that have detailed explanations about said settings.

<details>
  <summary>About Linux</summary>

So far, I haven't really paid much attention to Linux, because things like Project64 and [M64MM3](https://github.com/projectcomet64/M64MM) don't have Linux versions either and require you to use [Wine](https://www.winehq.org/), which should work completely fine with katarakta, too. You can also run katarakta from source, and I don't think it will have problems on other platforms since katarakta shouldn't contain anything Windows-specific.

Public Test 3 has a Linux version, which I have tested a little on an Arch Linux virtual machine and it seemed to work there, but I can't say for sure if it works on any other distribution.

</details>

<details>
  <summary>About older versions</summary>

### For Public Test 3
Same as for 2.0.0+
### For 1.4.0–1.4.13 and Public Test 1 & 2
After downloading the archive, extract it somewhere. What you need to run is `katarakta.exe`, you can (and have) to configure it by going to `Options` -> `Settings`.\
In the Settings, you need to put the path to the Super Mario 64 hi-res folder, this path should be the same as the graphics plugin's texture pack path, but include `/SUPER MARIO 64/` (or whatever the game's name is for you, but it's most likely `SUPER MARIO 64` unless you are using a ROM hack or something) in the end. An example of a correct path would be `D:/Project64/Plugin/GFX/hires_texture/SUPER MARIO 64/`.\
After configuring, click `Save`.
### For 1.0.0–1.3.0
Configuring 1.0.0–1.3.0 should be mostly the same as it is with the newer versions, but done inside a text editor instead of a GUI for settings.\
After downloading the archive, extract it somewhere. Open `config.txt` and follow the instructions. There are also guides in Ukrainian and Russian.\
What you need to run is `katarakta.exe`\
`kataraktaConsole.exe` is, obviously, the console version of katarakta, this version was made for testing, it lacks some features the GUI version has and you probably would not want to use that.
## Languages in older versions
### 1.0.0–1.4.2
These versions are translated to Russian and Ukrainian.
### 1.4.3–1.4.13
These versions are translated to Russian, Ukrainian, and Kazakh (both Cyrillic and Latin alphabets). The Kazakh translation was made by [RMSM64](https://www.youtube.com/@rmsm64).
### Public Test 1
This version is translated to Russian, Ukrainian, and Kazakh (both Cyrillic and Latin alphabets). It also now allows you to create custom translations.
### Public Test 2 & Public Test 3
This version is translated to Russian and Ukrainian. The Kazakh translation was removed in Public Test 2 because it was hard to maintain and no one used it anyway.

</details>

# Frequently Asked Questions
**If I use katarakta for my work, should I credit you?**\
Credit is optional.

**What are additional textures?**\
You know how for one of the methods to make Mario spazz is loading a Super Mario 64 savestate in another game?\
Well, to have Mario's texture changed in that case, you need to have other textures in that game's hi-res textures folder.\
I call these other textures the “additional” textures.

**What is the `py38` version?**\
The Normal version is “compiled” with Python 3.11, and Python does not support Windows 7 starting from 3.9.\
The `py38` version is “compiled” with Python 3.8 instead, and that version of Python supports Windows 7 (probably also Vista, but it was not tested on it yet).\
If you are using Wine for katarakta on Linux, then the Normal version should work for you.

**What does “katarakta” mean?**\
It's romanized “cataract” in Russian (“катаракта”). Cataract is an *eye* disease and katarakta was originally meant for just *eye* textures and I thought it was funny to name it like that… It was probably a horrible idea, though.

**Is it translated to any other languages?**\
katarakta is currently translated to Russian and Ukrainian. Both translations were made by me.\
You can also easily create your own translations! Go to the `ExampleLanguage` folder in the `lang` folder to learn more.

**Why does it have a Color Code Converter?**\
I don't know why I have added that. It will be gone in the next minor update (2.1.0) and is already gone in [Public Test 4](https://github.com/vazhka-dolya/katarakta/releases/tag/vpt4).

**Do you know about SM64 Eye Changer from ImCodist?**\
As you probably guessed by seeing this question here, yes.\
I already knew about it even before creating katarakta (and SM64EC actually inspired me to make katarakta!), but I still decided to create it because I needed it for my own personal use and SM64EC did not have some features I needed, such as the additional textures and ability to change Mario's other textures besides the eyes.

# Legal Notice
This program is not affiliated with or sponsored by Nintendo and does not claim ownership over any\nof Nintendo's intellectual property used (such as the characters in the loading screens).
