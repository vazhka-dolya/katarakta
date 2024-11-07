# katarakta
katarakta is a tool made for Super Mario 64 machinimas that enables you to change Mario's textures quicker and makes it a lot less tedious.
<p align="center">
  <img src="https://github.com/vazhka-dolya/katarakta/blob/main/GitHubImg/katarakta_2.0.0_screenshot_1.png" width="666"/>
</p>

# Features
katarakta's main functionality currently includes the following:
- Applying eye textures
- Applying cap/sidehair/mustache/button textures
- Applying any other texture
- Applying textures to a hi-res folder of other games
- Clearing the hi-res texture folders
- - The `Cache.ini` file also gets deleted if there is one
- Removing the black borders that are sometimes seen around textures after editing them

# Setting Up
Firstly, you need a graphics plugin that supports texture packs, such as GLideN64 (recommended) or RiceVideo. You need to configure the plugin to be able to load the “hi-res” textures, there are numerous tutorials that can be found on how to do this, such as [GlitchyPSI's](https://www.youtube.com/watch?v=AsmwKbv054g), [Team Toad's](https://www.youtube.com/watch?v=o33pdMVl2Ow), or [mine](https://www.youtube.com/watch?v=1VsTe2No9eA) (has English subtitles), which also tries to explain how to set up katarakta (albeit pretty outdated).

## For 2.0.0+
After downloading the archive, extract it somewhere. What you need to run is `katarakta.exe`, you can (and have) to configure it by going to `Options` -> `Settings`.\
It shouldn't be too hard to configure, some settings have hints (red question marks that you can hover your cursor over) that have detailed explanations about said settings.\
After configuring, click `Save`.
## About Linux
Public Test 3 has a Linux version, which I have tested a little on an Arch Linux virtual machine and it seemed to work there, but I can't say for sure if it works on any distribution.\
Running it from the source code or launching the `.exe` through [Wine](https://www.winehq.org/) should also work.

# Frequently Asked Questions
**If I use katarakta for my work, should I credit you?**\
Credit is optional.

**What are additional textures?**\
You know how for one of the methods to make Mario spazz is loading a Super Mario 64 savestate in another game?\
Well, to have Mario's texture changed in that case, you need to have other textures in that game's hi-res textures folder.\
I call these other textures the “additional” textures.\

**What is the `py38` version?**\
The normal version is “compiled” with Python 3.11, and Python does not support Windows 7 starting from 3.9.\
The `py38` version is “complied” with Python 3.8 instead, and that version of Python supports Windows 7 (probably also Vista, but it was not tested on it yet).\
If you are using WINE for katarakta on Linux, then the normal version should work for you.

**Why is the name "katarakta"?**\
It's romanized “cataract” in Russian. Cataract is an *eye* disease and katarakta was originally meant for just *eye* textures and I thought it was funny to name it like that… It was probably a horrible idea, though.

**Is it translated to any other languages?**\
As of 2.0.0, katarakta is translated to Russian and Ukrainian. Both translations were made by me.\
You can also easily create your own translations! Go to the `ExampleLanguage` folder in the `lang` folder to learn more.

**Do you know about SM64 Eye Changer from ImCodist?**\
As you probably guessed by seeing this question here, yes.\
I already knew about it even before creating katarakta (and SM64EC actually inspired me to make katarakta!), but I still decided to create it because I needed it for my own personal use and SM64EC did not have some features I needed, such as the additional textures and ability to change Mario's other textures besides the eyes.
