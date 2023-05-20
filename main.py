#GPL-3.0-only

import os
import configparser
import shutil

class Options():
    SM64Dir = ""
    AddDir = ""
    Eyes1 = ""
    Eyes2 = ""
    Eyes3 = ""
    AddEyes1 = ""
    AddEyes2 = ""
    AddEyes3 = ""

Option = Options()

Config = configparser.ConfigParser()

def LoadConfig():
    Config.read("config.txt")
    if "PATHS" in Config:
        ConfigSecond = Config["PATHS"]

        Option.SM64Dir = ConfigSecond.get("SM64Dir", Option.SM64Dir)
        Option.AddDir = ConfigSecond.get("AddDir", Option.AddDir)
        Option.Eyes1 = ConfigSecond.get("Eyes1", Option.Eyes1)
        Option.Eyes2 = ConfigSecond.get("Eyes2", Option.Eyes2)
        Option.Eyes3 = ConfigSecond.get("Eyes3", Option.Eyes3)
        Option.AddEyes1 = ConfigSecond.get("AddEyes1", Option.AddEyes1)
        Option.AddEyes2 = ConfigSecond.get("AddEyes2", Option.AddEyes2)
        Option.AddEyes3 = ConfigSecond.get("AddEyes3", Option.AddEyes3)

LoadConfig()

def CopyEyes(Type, FolderName):
    if Type == "SM64Dir":
        Path = Option.SM64Dir
        try:
            shutil.copyfile("eyes\\{}\\{}.png".format(FolderName, Option.Eyes1), "{}{}.png".format(Path, Option.Eyes1))
            shutil.copyfile("eyes\\{}\\{}.png".format(FolderName, Option.Eyes2), "{}{}.png".format(Path, Option.Eyes2))
            shutil.copyfile("eyes\\{}\\{}.png".format(FolderName, Option.Eyes3), "{}{}.png".format(Path, Option.Eyes3))
        except:
            print("An error occured!\nMake sure that:\n-A folder with that name exists\n-You entered the correct path in config.txt\n-You entered the correct eye texture name in config.txt")
    if Type == "AddDir":
        Path = Option.AddDir
        try:
            shutil.copyfile("eyes\\{}\\{}.png".format(FolderName, Option.AddEyes1), "{}{}.png".format(Path, Option.AddEyes1))
            shutil.copyfile("eyes\\{}\\{}.png".format(FolderName, Option.AddEyes2), "{}{}.png".format(Path, Option.AddEyes2))
            shutil.copyfile("eyes\\{}\\{}.png".format(FolderName, Option.AddEyes3), "{}{}.png".format(Path, Option.AddEyes3))
        except:
            print("An error occured!\nMake sure that:\n-A folder with that name exists\n-You entered the correct path in config.txt\n-You entered the correct eye texture name in config.txt")

print("Welcome to katarakta!\nType help to view all commands and what they do.\nMake sure to also check config.txt if you didn't already, there is some vital stuff.")
while True:
    Command = input("> ")
    if Command == "help":
        print("Commands:\nhelp - Displays this message.\ncopys - Copies the eye textures from the eyes folder to your SM64 folder.\ncopya - Copies the eye textures from the eyes folder to your additional folder.\nquit - Quit katarakta.\n")
    elif Command == "copys":
        FolderName = input("Folder name: ")
        CopyEyes("SM64Dir", FolderName)
    elif Command == "copya":
        FolderName = input("Folder name: ")
        CopyEyes("AddDir", Foldername)
    elif Command == "quit":
        quit()
    else:
        print("Command not found!")
