# katarakta
katarakta is a tool made for Super Mario 64 machinimas that enables you to change Mario's textures quicker and makes it a lot less tedious.

# <img align="right" src="https://github.com/vazhka-dolya/katarakta/blob/main/GitHubImg/katarakta_PT3_screenshot_1.png" width="240"/> Features
katarakta's main functionality currently includes the following (functions that are only available in the [***latest Public Test***](https://github.com/vazhka-dolya/katarakta/releases/tag/vpt3) version marked in ***bold italic***):
- Applying eye textures;
- Applying cap/sidehair/mustache/button textures;
- Applying textures to a hi-res folder of another game (useful for stuff like spazzing; ***This feature is completely reworked in the Public Test 3 version and allows you to apply textures to more than one other game***);
- ***Applying any other texture***;
- Clearing the hi-res texture folders;
- - The `Cache.ini` file also gets deleted if there is one;
- ***Removing the black borders that are sometimes seen around textures after editing them***;

# Setting Up
Firstly, you need a graphics plugin that supports texture packs, such as GLideN64 (recommended) or RiceVideo. You need to configure the plugin to be able to load the «hi-res» textures, there are numerous tutorials that can be found on how to do this, such as [GlitchyPSI's](https://www.youtube.com/watch?v=AsmwKbv054g), [Team Toad's](https://www.youtube.com/watch?v=o33pdMVl2Ow), or [mine](https://www.youtube.com/watch?v=1VsTe2No9eA) (has English subtitles), which also tries to explain how to set up katarakta (albeit pretty outdated).

## For Public Test 3 
After downloading the archive, extract it somewhere. What you need to run is `katarakta.exe`, you can (and have) to configure it by going to `Options` -> `Settings`.\
It shouldn't be too hard to configure, some settings have hints (red question marks that you can hover your cursor over) that have detailed explanations about said settings.\
After configuring, click `Save`.
## For 1.4.0–1.4.13 and Public Test 1 & 2
After downloading the archive, extract it somewhere. What you need to run is `katarakta.exe`, you can (and have) to configure it by going to `Options` -> `Settings`.\
In the Settings, you need to put the path to the Super Mario 64 hi-res folder, this path should be the same as the graphics plugin's texture pack path, but include `/SUPER MARIO 64/` (or whatever the game's name is for you, but it's most likely `SUPER MARIO 64` unless you are using a ROM hack or something) in the end. An example of a correct path would be `D:/Project64/Plugin/GFX/hires_texture/SUPER MARIO 64/`.\
After configuring, click `Save`.
## For 1.0.0–1.3.0
Configuring 1.0.0–1.3.0 should be mostly the same as it is with the newer versions, but done inside a text editor instead of a GUI for settings.\
After downloading the archive, extract it somewhere. Open `config.txt` and follow the instructions. There are also guides in Ukrainian and Russian.\
What you need to run is `katarakta.exe`\
`kataraktaConsole.exe` is, obviously, the console version of katarakta, this version was made for testing, it lacks some features the GUI version has and you probably would not want to use that.
## About Linux
There's currently no Linux version, but I will probably make one in the future when I'm not lazy.\
Right now you can either download the source code and run it from there, or use WINE (I tested both methods and they worked for me).

# Frequently Asked Questions
**If I use katarakta for my work, should I credit you?**\
Credit is optional.

**What are additional textures?**\
You know how for one of the methods to make Mario spazz is loading a Super Mario 64 savestate in another game?\
Well, to have Mario's texture changed in that case, you need to have other textures in that game's hi-res textures folder.\
I call these other textures the "additional" textures.\
If you are using the Public Test 2 version, you can turn them off in the Settings if you don't need them.

**What is the `py38` version?**\
The normal version is «compiled» with Python 3.11, and Python does not support Windows 7 starting from 3.9.\
The `py38` version is «complied» with Python 3.8 instead, and that version of Python supports Windows 7 (and maybe also Vista).\
If you are using WINE for katarakta on Linux, then the normal version should work for you.

**Why is the name "katarakta"?**\
It's romanized "cataract" in Russian. It doesn't really have any meaning and I just thought it was funny.

**Is it translated to any other languages?**\
As of 1.4.13 and Public Test 1, katarakta is translated to Ukrainian, Russian and Kazakh (Cyrillic and Latin).\
Kazakh was removed in Public Test 2 because it's hard to maintain and no one uses it anyway.
Starting from Public Test 1, you can also easily create your own translations! Go to the `ExampleLanguage` folder in the `lang` folder to learn more.

**Do you know about SM64 Eye Changer from ImCodist?**\
As you probably guessed by seeing this question here, yes.\
I already knew about it even before creating katarakta (and SM64EC actually inspired me to make katarakta!), but I still decided to create it because I needed it for my own personal use and SM64EC did not have some features I needed, such as the additional textures and ability to change Mario's other textures besides the eyes.

.

..

...

also please forgive me for all the atrocities i did in the code
