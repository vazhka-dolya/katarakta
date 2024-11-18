#GPL-3.0-only

import os
import configparser
import shutil
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QToolTip, QStyledItemDelegate, QApplication, QMainWindow, QMessageBox, QWidget, QSplashScreen, QAction, QFileDialog, QStyleFactory, QCommonStyle, QListWidgetItem, QTreeView, QFileSystemModel, QSizePolicy
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QPixmap, QIcon, QPalette, QColor
from PyQt5.Qt import QPropertyAnimation
import sys
import random
import requests
import pyclip
import locale
from PIL import Image
from datetime import datetime

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
if hasattr(QStyleFactory, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

os.environ["QT_ENABLE_HIGHDPI_SCALING"]   = "1"
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
os.environ["QT_SCALE_FACTOR"]             = "1"

class Options():
    HiResDir = ""
    SM64Name = ""
    AddNames = ""
    
    Eyes1 = ""
    Eyes2 = ""
    Eyes3 = ""
    
    Cap = ""
    Hair = ""
    Mustache = ""
    Button = ""
    
    Language = ""

class OtherTextures():
    ApplyEverything = ""
    Textures = []
    Display1 = ""
    Display2 = ""
    Display3 = ""
    Display4 = ""

AppVersion = "2.0.2"
AppEdition = "Normal"

Option = Options()

class LanguageText():
    pass

global BG_OptionMode
global AddNamesList
global ApplyDropdownConnected
ApplyDropdownConnected = False
global SW_AIToolTip
SW_AIToolTip = ""

Language = LanguageText()

Config = configparser.ConfigParser()

def CreateConfig():
    CreatedConfig = configparser.ConfigParser()
    SetLanguage = "English"
    CreatedConfig["PATHS"] = {
        "hiresdir": "",
        "sm64name": "SUPER MARIO 64",
        "addnames": "",
        "eyes1": "#6B8D43C4#0#2_all",
        "eyes2": "#9FBECEF9#0#2_all",
        "eyes3": "#5D6B0678#0#2_all",
        "cap": "#905D3214#0#2_all",
        "hair": "#2BEA0A29#0#2_all",
        "mustache": "#E9FCBF74#0#2_all",
        "button": "#19442FC9#0#2_all",
        }
    CreatedConfig["OPTIONS"] = {
        "language": SetLanguage,
        "startupcheckforupdates": "1",
        "startupstayontop": "0",
        "darkmode": "0",
        "donotmoveswitchvertically": "0",
        "eyeborderswarning": "0",
        "bg_mode": "color",
        "bg_color": "#AAAAAA",
        "bg_checkerboard": "1",
        "bg_gradient1": "#7F603C",
        "bg_gradient2": "#FEC179",
        "textureborder": "1",
        "eyelisticons": "1",
        "eyelisticonbg": "1",
        "eyelistrowheight": "0"
        }
    with open("config.ini","w") as _ConfigFile:
        CreatedConfig.write(_ConfigFile)

if os.path.exists("config.ini") is True:
    pass
else:
    CreateConfig()
    

if os.path.isfile("migrateconfig.ini"):
    MigrateConfig = configparser.ConfigParser()
    
    Config.read("migrateconfig.ini", encoding = "utf-8")
    ConfigSecond = Config["PATHS"]
    if Config.has_option("PATHS", "HiResDir") == True:
        Option.HiResDir = ConfigSecond.get("HiResDir")
    
        Option.SM64Name = ConfigSecond.get("SM64Name")
        Option.AddNames = ConfigSecond.get("AddNames")
        Option.Eyes1 = ConfigSecond.get("Eyes1")
        Option.Eyes2 = ConfigSecond.get("Eyes2")
        Option.Eyes3 = ConfigSecond.get("Eyes3")
        Option.Cap = ConfigSecond.get("Cap")
        Option.Hair = ConfigSecond.get("Hair")
        Option.Mustache = ConfigSecond.get("Mustache")
        Option.Button = ConfigSecond.get("Button")
    else:
        Option.HiResDir = os.path.dirname(ConfigSecond.get("SM64Dir").rstrip("/\\")) + "/" # This gets the path but one directory up

        OldSM64Name = os.path.basename(ConfigSecond.get("SM64Dir").rstrip("/\\")) # This gets the last folder's name in a path
        Option.SM64Name = OldSM64Name
        Option.AddNames = os.path.basename(ConfigSecond.get("AddDir").rstrip("/\\"))
        Option.Eyes1 = ConfigSecond.get("Eyes1").lstrip(OldSM64Name)
        Option.Eyes2 = ConfigSecond.get("Eyes2").lstrip(OldSM64Name)
        Option.Eyes3 = ConfigSecond.get("Eyes3").lstrip(OldSM64Name)
        Option.Cap = ConfigSecond.get("Cap").lstrip(OldSM64Name)
        Option.Hair = ConfigSecond.get("Hair").lstrip(OldSM64Name)
        Option.Mustache = ConfigSecond.get("Mustache").lstrip(OldSM64Name)
        Option.Button = ConfigSecond.get("Button").lstrip(OldSM64Name)

    ConfigSecond = Config["OPTIONS"]
    Option.Language = ConfigSecond.get("Language", Option.Language)
    Option.StartUpCheckForUpdates = ConfigSecond.get("StartUpCheckForUpdates")
    Option.StartUpStayOnTop = ConfigSecond.get("StartUpStayOnTop")
    Option.DarkMode = ConfigSecond.get("DarkMode")
    Option.DoNotMoveSwitchVertically = ConfigSecond.get("DoNotMoveSwitchVertically")
    Option.EyeBordersWarning = ConfigSecond.get("EyeBordersWarning")

    MigrateConfig["PATHS"] = {
        "hiresdir": Option.HiResDir,
        "sm64name": Option.SM64Name,
        "addnames": Option.AddNames,
        "eyes1": Option.Eyes1,
        "eyes2": Option.Eyes2,
        "eyes3": Option.Eyes3,
        "cap": Option.Cap,
        "hair": Option.Hair,
        "mustache": Option.Mustache,
        "button": Option.Button
        }
    MigrateConfig["OPTIONS"] = {
        "language": Option.Language,
        "startupcheckforupdates": "1",
        "startupstayontop": "0",
        "darkmode": "0",
        "donotmoveswitchvertically": "0",
        "eyeborderswarning": "0",
        "bg_mode": "color",
        "bg_color": "#AAAAAA",
        "bg_checkerboard": "1",
        "bg_gradient1": "#7F603C",
        "bg_gradient2": "#FEC179",
        "textureborder": "1",
        "eyelisticons": "1",
        "eyelisticonbg": "1",
        "eyelistrowheight": "0"
        }
    with open("config.ini","w") as _ConfigFile:
        MigrateConfig.write(_ConfigFile)
    try:
        shutil.rmtree("img/")
    except:
        pass
    try:
        shutil.rmtree("lang/")
    except:
        pass
    try:
        shutil.rmtree("resources/img/")
    except:
        pass
    try:
        shutil.rmtree("resources/loading/")
    except:
        pass
    try:
        shutil.rmtree("resources/lang/English")
    except:
        pass
    try:
        shutil.rmtree("resources/lang/Russian")
    except:
        pass
    try:
        shutil.rmtree("resources/lang/Ukrainian")
    except:
        pass
    try:
        shutil.rmtree("loading/")
    except:
        pass
    try:
        os.remove("updater.exe")
    except:
        pass

    LatestVersion = "katarakta " + AppVersion
    StrippedVersion = LatestVersion.strip("katarakta ")
    if AppEdition == "Normal":
        shutil.copytree("updater/katarakta-{}/resources/".format(StrippedVersion), "resources/", dirs_exist_ok=True)
        shutil.move("updater/katarakta-{}/updater.exe".format(StrippedVersion), "updater.exe")
    elif AppEdition == "py38":
        shutil.copytree("updater/katarakta-{}-py38/resources".format(StrippedVersion), "resources/", dirs_exist_ok=True)
        shutil.move("updater/katarakta-{}-py38/updater.exe".format(StrippedVersion), "updater.exe")
    os.remove("migrateconfig.ini")

def LoadConfig():
    Config.read("config.ini", encoding = "utf-8")
    ConfigSecond = Config["PATHS"]

    Option.HiResDir = ConfigSecond.get("HiResDir", Option.HiResDir)
    Option.SM64Name = ConfigSecond.get("SM64Name", Option.SM64Name)
    Option.AddNames = ConfigSecond.get("AddNames", Option.AddNames)
    Option.Eyes1 = ConfigSecond.get("Eyes1", Option.Eyes1)
    Option.Eyes2 = ConfigSecond.get("Eyes2", Option.Eyes2)
    Option.Eyes3 = ConfigSecond.get("Eyes3", Option.Eyes3)
    Option.Cap = ConfigSecond.get("Cap", Option.Cap)
    Option.Hair = ConfigSecond.get("Hair", Option.Hair)
    Option.Mustache = ConfigSecond.get("Mustache", Option.Mustache)
    Option.Button = ConfigSecond.get("Button", Option.Button)
        
    ConfigSecond = Config["OPTIONS"]
    Option.Language = ConfigSecond.get("Language", Option.Language)
    Option.StartUpCheckForUpdates = ConfigSecond.get("StartUpCheckForUpdates")
    Option.StartUpStayOnTop = ConfigSecond.get("StartUpStayOnTop")
    Option.DarkMode = ConfigSecond.get("DarkMode")
    Option.DoNotMoveSwitchVertically = ConfigSecond.get("DoNotMoveSwitchVertically")
    Option.EyeBordersWarning = ConfigSecond.get("EyeBordersWarning")
    Option.BG_Mode = ConfigSecond.get("bg_mode")
    Option.BG_Color = ConfigSecond.get("bg_color")
    Option.BG_Checkerboard = ConfigSecond.get("bg_checkerboard")
    Option.BG_Gradient1 = ConfigSecond.get("bg_gradient1")
    Option.BG_Gradient2 = ConfigSecond.get("bg_gradient2")
    Option.TextureBorder = ConfigSecond.get("textureborder")
    Option.EyeListIcons = ConfigSecond.get("eyelisticons")
    Option.EyeListIconBG = ConfigSecond.get("eyelisticonbg")
    Option.EyeListRowHeight = ConfigSecond.get("eyelistrowheight")

LoadConfig()

def LoadLanguage():
    ConfigLang = configparser.ConfigParser()
    Config.read("resources/lang/{}/properties.ini".format(Option.Language), encoding = "utf-8")
    ConfigLanguage = Config["PROPERTIES"]
    Language.Properties_InnerName =      ConfigLanguage.get("Properties_InnerName")
    Language.Properties_Name =           ConfigLanguage.get("Properties_Name")
    Language.Properties_Translator =     ConfigLanguage.get("Properties_Translator")
    Language.Properties_Revision =       ConfigLanguage.get("Properties_Revision")
    Language.Properties_MadeForVersion = ConfigLanguage.get("Properties_MadeForVersion")
    
    if os.path.exists("resources/lang/{}/".format(Option.Language)) and Option.Language != "English":
        Config.read("resources/lang/{}/text.ini".format(Option.Language), encoding = "utf-8")
        ConfigLanguage = Config["MAINWINDOW"]
        Language.MW_Title =                     ConfigLanguage.get("MW_Title")
        Language.MW_ApplySM64 =                 ConfigLanguage.get("MW_ApplySM64")
        Language.MW_groupBox =                  ConfigLanguage.get("MW_groupBox")
        Language.MW_menuHelp =                  ConfigLanguage.get("MW_menuHelp")
        Language.MW_actionAbout =               ConfigLanguage.get("MW_actionAbout")
        Language.MW_Refresh =                   ConfigLanguage.get("MW_Refresh")
        Language.MW_SwitchItemsButton =         ConfigLanguage.get("MW_SwitchItemsButton")
        Language.MW_menuOptions =               ConfigLanguage.get("MW_menuOptions")
        Language.MW_submenuHiRes =              ConfigLanguage.get("MW_submenuHiRes")
        Language.MW_HiResClearSM64 =            ConfigLanguage.get("MW_HiResClearSM64")
        Language.MW_HiResCleadAdd =             ConfigLanguage.get("MW_HiResCleadAdd")
        Language.MW_HiResOpenSM64 =             ConfigLanguage.get("MW_HiResOpenSM64")
        Language.MW_HiResOpenAdd =              ConfigLanguage.get("MW_HiResOpenAdd")
        Language.MW_actionOpenKataraktaFolder = ConfigLanguage.get("MW_actionOpenKataraktaFolder")
        Language.MW_actionSettings =            ConfigLanguage.get("MW_actionSettings")
        Language.MW_actionOpenCcconv =          ConfigLanguage.get("MW_actionOpenCcconv")
        Language.MW_actionStayOnTop =           ConfigLanguage.get("MW_actionStayOnTop")
        Language.MW_actionUpdate =              ConfigLanguage.get("MW_actionUpdate")
        Language.MW_actionDarkMode =            ConfigLanguage.get("MW_actionDarkMode")
        Language.MW_submenuEyeBorders =         ConfigLanguage.get("MW_submenuEyeBorders")
        Language.MW_EyeBordersCurrent =         ConfigLanguage.get("MW_EyeBordersCurrent")
        Language.MW_EyeBordersAll =             ConfigLanguage.get("MW_EyeBordersAll")
        Language.MW_EBCPopupWarning =           ConfigLanguage.get("MW_EBCPopupWarning")
        Language.MW_EBCPopupText =              ConfigLanguage.get("MW_EBCPopupText")
        Language.MW_EBCPopupInfoText =          ConfigLanguage.get("MW_EBCPopupInfoText")
        Language.MW_EBAPopupWarning =           ConfigLanguage.get("MW_EBAPopupWarning")
        Language.MW_EBAPopupText =              ConfigLanguage.get("MW_EBAPopupText")
        Language.MW_EBAPopupInfoText =          ConfigLanguage.get("MW_EBAPopupInfoText")
        
        ConfigLanguage = Config["ABOUTWINDOW"]
        Language.AW_Title =            ConfigLanguage.get("AW_Title")
        Language.AW_LabelName =        ConfigLanguage.get("AW_LabelName")
        Language.AW_LabelVersion =     ConfigLanguage.get("AW_LabelVersion")
        Language.AW_LabelEdition =     ConfigLanguage.get("AW_LabelEdition")
        Language.AW_LabelAuthor =      ConfigLanguage.get("AW_LabelAuthor")
        Language.AW_SpecialThanks =    ConfigLanguage.get("AW_SpecialThanks")
        Language.AW_LabelAddInfo =     ConfigLanguage.get("AW_LabelAddInfo")
        Language.AW_LabelReportIssue = ConfigLanguage.get("AW_LabelReportIssue")
        Language.AW_LabelLegalNotice = ConfigLanguage.get("AW_LabelLegalNotice")

        ConfigLanguage = Config["UPDATEWINDOW"]
        Language.UW_Title =                  ConfigLanguage.get("UW_Title")
        Language.UW_UpdateCheckLabel =       ConfigLanguage.get("UW_UpdateCheckLabel")
        Language.UW_YourVersionLabel =       ConfigLanguage.get("UW_YourVersionLabel")
        Language.UW_LatestVersionLabel =     ConfigLanguage.get("UW_LatestVersionLabel")
        Language.UW_AllReleasesLink =        ConfigLanguage.get("UW_AllReleasesLink")
        Language.UW_VersionIsLatest =        ConfigLanguage.get("UW_VersionIsLatest")
        Language.UW_VersionIsOutdated =      ConfigLanguage.get("UW_VersionIsOutdated")
        Language.UW_VersionCannotCheck =     ConfigLanguage.get("UW_VersionCannotCheck")
        Language.UW_textBrowserDescription = ConfigLanguage.get("UW_textBrowserDescription")
        Language.UW_LaunchUpdater =          ConfigLanguage.get("UW_LaunchUpdater")

        ConfigLanguage = Config["SETTINGSWINDOW"]
        Language.SW_Title =                          ConfigLanguage.get("SW_Title")
        Language.SW_groupLanguage =                  ConfigLanguage.get("SW_groupLanguage")
        Language.SW_Translator =                     ConfigLanguage.get("SW_Translator")
        Language.SW_labelLanguageRestart =           ConfigLanguage.get("SW_labelLanguageRestart")
        Language.SW_groupUpdates =                   ConfigLanguage.get("SW_groupUpdates")
        Language.SW_checkUpdates =                   ConfigLanguage.get("SW_checkUpdates")
        Language.SW_labelUpdates =                   ConfigLanguage.get("SW_labelUpdates")
        Language.SW_groupMisc =                      ConfigLanguage.get("SW_groupMisc")
        Language.SW_checkStayOnTop =                 ConfigLanguage.get("SW_checkStayOnTop")
        Language.SW_TabGeneral =                     ConfigLanguage.get("SW_TabGeneral")
        Language.SW_labelHiResSM64 =                 ConfigLanguage.get("SW_labelHiResSM64")
        Language.SW_groupSM64 =                      ConfigLanguage.get("SW_groupSM64")
        Language.SW_labelEyesOpen =                  ConfigLanguage.get("SW_labelEyesOpen")
        Language.SW_labelEyesHalfopen =              ConfigLanguage.get("SW_labelEyesHalfopen")
        Language.SW_labelEyesClosed =                ConfigLanguage.get("SW_labelEyesClosed")
        Language.SW_labelCap =                       ConfigLanguage.get("SW_labelCap")
        Language.SW_labelSidehair =                  ConfigLanguage.get("SW_labelSidehair")
        Language.SW_labelMustache =                  ConfigLanguage.get("SW_labelMustache")
        Language.SW_labelButton =                    ConfigLanguage.get("SW_labelButton")
        Language.SW_groupNames =                     ConfigLanguage.get("SW_groupNames")
        Language.SW_labelSM64Name =                  ConfigLanguage.get("SW_labelSM64Name")
        Language.SW_labelAddNames =                  ConfigLanguage.get("SW_labelAddNames")
        Language.SW_TabTextures =                    ConfigLanguage.get("SW_TabTextures")
        Language.SW_pushClose =                      ConfigLanguage.get("SW_pushClose")
        Language.SW_pushApply =                      ConfigLanguage.get("SW_pushApply")
        Language.SW_pushApplyClose =                 ConfigLanguage.get("SW_pushApplyClose")
        Language.SW_CheckDoNotMoveSwitchVertically = ConfigLanguage.get("SW_CheckDoNotMoveSwitchVertically")
        Language.SW_CheckEyeBordersWarning =         ConfigLanguage.get("SW_CheckEyeBordersWarning")
        Language.SW_labelLanguageRevision =          ConfigLanguage.get("SW_labelLanguageRevision")
        Language.SW_labelLanguageMadeForVersion =    ConfigLanguage.get("SW_labelLanguageMadeForVersion")
        Language.SW_Unspecified =                    ConfigLanguage.get("SW_Unspecified")
        Language.SW_BG_ButtonConfigure =             ConfigLanguage.get("SW_BG_ButtonConfigure")
        Language.SW_BG_ButtonReset =                 ConfigLanguage.get("SW_BG_ButtonReset")
        Language.SW_BG_Label =                       ConfigLanguage.get("SW_BG_Label")
        Language.SW_CheckTextureBorder =             ConfigLanguage.get("SW_CheckTextureBorder")
        Language.SW_AI =                             ConfigLanguage.get("SW_AI")
        Language.SW_ToolTipPath1 =                   ConfigLanguage.get("SW_ToolTipPath1")
        Language.SW_ToolTipMainTextureNames1 =       ConfigLanguage.get("SW_ToolTipMainTextureNames1")
        Language.SW_ToolTipMainTextureNames2 =       ConfigLanguage.get("SW_ToolTipMainTextureNames2")
        Language.SW_ToolTipGameNames1 =              ConfigLanguage.get("SW_ToolTipGameNames1")
        Language.SW_ToolTipGameNames2 =              ConfigLanguage.get("SW_ToolTipGameNames2")
        Language.SW_TabAppearance =                  ConfigLanguage.get("SW_TabAppearance")
        Language.SW_groupEyeBG =                     ConfigLanguage.get("SW_groupEyeBG")
        Language.SW_groupEyeList =                   ConfigLanguage.get("SW_groupEyeList")
        Language.SW_CheckEyeListIcons =              ConfigLanguage.get("SW_CheckEyeListIcons")
        Language.SW_CheckEyeListIconBG =             ConfigLanguage.get("SW_CheckEyeListIconBG")
        Language.SW_LabelEyeListWarning =            ConfigLanguage.get("SW_LabelEyeListWarning")
        Language.SW_LabelEyeListDemo =               ConfigLanguage.get("SW_LabelEyeListDemo")
        Language.SW_LabelRowHeight =                 ConfigLanguage.get("SW_LabelRowHeight")

        ConfigLanguage = Config["CCCONV"]
        Language.Ccconv_ChooseOpenFile = ConfigLanguage.get("Ccconv_ChooseOpenFile")
        Language.Ccconv_TxtDocument    = ConfigLanguage.get("Ccconv_TxtDocument")
        Language.Ccconv_ChooseSaveFile = ConfigLanguage.get("Ccconv_ChooseSaveFile")
        Language.Ccconv_Title          = ConfigLanguage.get("Ccconv_Title")
        Language.Ccconv_InputCC        = ConfigLanguage.get("Ccconv_InputCC")
        Language.Ccconv_OutputCC       = ConfigLanguage.get("Ccconv_OutputCC")
        Language.Ccconv_ButtonConvert  = ConfigLanguage.get("Ccconv_ButtonConvert")
        Language.Ccconv_ButtonPaste    = ConfigLanguage.get("Ccconv_ButtonPaste")
        Language.Ccconv_ButtonCopy     = ConfigLanguage.get("Ccconv_ButtonCopy")
        Language.Ccconv_ButtonExport   = ConfigLanguage.get("Ccconv_ButtonExport")
        Language.Ccconv_ButtonImport   = ConfigLanguage.get("Ccconv_ButtonImport")
        
    else:
        Option.Language = "English"

LoadLanguage()

class AILanguageDelegate(QStyledItemDelegate):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.AIToolTip = "123"
    
    def SetToolTip(self):
        global SW_AIToolTip
        self.AIToolTip = SW_AIToolTip
    
    def paint(self, Painter, _Option, Index):
        super().paint(Painter, _Option, Index)
        AIIcon = Index.data(Qt.UserRole + 1)
        if AIIcon:
            IconRect = _Option.rect
            IconRect.setLeft(_Option.rect.right() - _Option.rect.height())
            AIIcon.paint(Painter, IconRect, Qt.AlignRight)
            Index.model().setData(Index, IconRect, Qt.UserRole + 2)
    
    def SizeHint(self, _Option, Index):
        Size = super().SizeHint(_Option, Index)
        Size.setWidth(Size.width() + Size.height())
        return Size
    
    def helpEvent(self, event, View, _Option, Index):
        if event.type() == event.ToolTip:
            AIIconRect = Index.data(Qt.UserRole + 2)
            if AIIconRect and AIIconRect.contains(event.pos()):
                QToolTip.showText(event.globalPos(), self.AIToolTip, View)
                return True
        return super().helpEvent(event, View, _Option, Index)

# Find Folders in eyes/ and chmb/
EyeFolders = os.listdir("eyes/")
CHMBFolders = os.listdir("chmb/")
FolderName = ""

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        Config.read("config.ini", encoding = "utf-8")
        ConfigSecond = Config["OPTIONS"]
        super().__init__()
        self.Mode = "Eyes"
        global DefaultPalette
        DefaultPalette = QPalette()
        DefaultPalette = app.palette()
        DefaultPalette.setColor(QPalette.Link, QColor(0, 0, 255))
        global DarkPalette
        DarkPalette = QPalette()
        DarkPalette.setColor(QPalette.Window, QColor(53, 53, 53))
        DarkPalette.setColor(QPalette.WindowText, Qt.white)
        DarkPalette.setColor(QPalette.Base, QColor(42, 42, 42))
        DarkPalette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        DarkPalette.setColor(QPalette.ToolTipBase, Qt.black)
        DarkPalette.setColor(QPalette.ToolTipText, Qt.white)
        DarkPalette.setColor(QPalette.Text, Qt.white)
        DarkPalette.setColor(QPalette.Button, QColor(53, 53, 53))
        DarkPalette.setColor(QPalette.ButtonText, Qt.white)
        DarkPalette.setColor(QPalette.BrightText, Qt.red)
        DarkPalette.setColor(QPalette.Link, QColor(42, 130, 218))
        DarkPalette.setColor(QPalette.Highlight, QColor(30, 91, 153))
        DarkPalette.setColor(QPalette.HighlightedText, Qt.white)
        DarkPalette.setColor(QPalette.Disabled, QPalette.ButtonText, QtCore.Qt.darkGray)
        DarkPalette.setColor(QPalette.Disabled, QPalette.WindowText, Qt.darkGray)
        DarkPalette.setColor(QPalette.Disabled, QPalette.Text, QtCore.Qt.darkGray)
        DarkPalette.setColor(QPalette.Disabled, QPalette.Light, QColor(53, 53, 53))
        
    def closeEvent(self,event):
        sys.exit(0)
        
    def resizeEvent(self, resizeEvent):
        #289
        #518 normal
        #386 hideadd
        #210 normal listWidget
        self.listWidget.resize((MainWindow.width() - 159), (MainWindow.height() - 67))
        self.groupBox.move((MainWindow.width() - 131), self.groupBox.pos().y())
        self.ApplySM64.move((MainWindow.width() - 132), self.ApplySM64.pos().y())
        self.ApplyDropdown.move((MainWindow.width() - 40), self.ApplySM64.pos().y())
        if Option.DoNotMoveSwitchVertically == "1":
            self.SwitchItemsButton.move((MainWindow.width() - 132), 490)
        else:
            self.SwitchItemsButton.move((MainWindow.width() - 132), (MainWindow.height() - 74))
    
    def OpenAboutWindow(self):
        self.AboutWindow = QtWidgets.QMainWindow()
        self.AboutWindowUi = Ui_AboutWindow()
        self.AboutWindowUi.setupUi(self.AboutWindow)
        self.AboutWindow.show()
        
    def OpenUpdateWindow(self):
        self.UpdateWindow = QtWidgets.QMainWindow()
        self.UpdateWindowUi = Ui_UpdateWindow()
        self.UpdateWindowUi.setupUi(self.UpdateWindow)
        self.UpdateWindow.show()

    def OpenSettingsWindow(self):
        self.SettingsWindow = QtWidgets.QMainWindow()
        self.SettingsWindowUi = Ui_SettingsWindow()
        self.SettingsWindowUi.setupUi(self.SettingsWindow)
        self.SettingsWindow.show()

    def OpenCcconv(self):
        self.Ccconv = QtWidgets.QMainWindow()
        self.CcconvUi = Ui_ccconvWindow()
        self.CcconvUi.setupUi(self.Ccconv)
        self.Ccconv.show()

    def CheckUpdatesStartUp(self):
        try:
            LatestResponse = requests.get("https://api.github.com/repos/vazhka-dolya/katarakta/releases/latest")
            LatestVersion = LatestResponse.json()["name"]
            if ("katarakta " + AppVersion) == LatestVersion:
                pass
            else:
                self.OpenUpdateWindow()
        except:
            pass
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(369, 563)

        fontsmaller = QtGui.QFont()
        fontsmaller.setPointSize(8)
        fontNine = QtGui.QFont()
        fontNine.setPointSize(9)

        #MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.World))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setFont(fontsmaller)
        
        MainWindow.setWindowIcon(QtGui.QIcon("resources/img/Icon.png"))

        if Option.StartUpCheckForUpdates == "1":
            self.CheckUpdatesStartUp()
        
        CopyEyesErrorBoxTitle = ""
        CopyEyesErrorBoxMessage = ""

        #Found eye folders label
        #self.label = QtWidgets.QLabel(self.centralwidget)
        #self.label.setGeometry(QtCore.QRect(30, 10, 101, 16))
        #self.label.setObjectName("label")

        #Displaying eye textures
        TextureTitleFont = QtGui.QFont()
        TextureTitleFont.setPointSize(10)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(238, 10, 113, 341))
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setFlat(True)
        self.groupBox.setAlignment(Qt.AlignHCenter)
        self.groupBox.setStyleSheet("border:0; QGroupBox{padding-top:15px; margin-top:-15px}")
        self.groupBox.setFont(TextureTitleFont)
        
        self.DisplayLabelBg = QtWidgets.QLabel(self.groupBox)
        self.DisplayLabelBg.setObjectName("DisplayLabelBg")
        self.DisplayLabelBg.setEnabled(True)
        self.DisplayLabelBg.setText("")
        self.DisplayLabelBg.setGeometry(0, 6, self.groupBox.width(), 500)
        self.DisplayLabelBg.lower()

        #Option.BG_Mode = ConfigSecond.get("bg_mode")
        #Option.BG_Color = ConfigSecond.get("bg_color")
        #Option.BG_Checkerboard = ConfigSecond.get("bg_checkerboard")
        #Option.BG_Gradient1 = ConfigSecond.get("bg_gradient1")
        #Option.BG_Gradient2 = ConfigSecond.get("bg_gradient2")
        
        self.SM64DisplayLabel1 = QtWidgets.QLabel(self.groupBox)
        self.SM64DisplayLabel1.setEnabled(True)
        #self.SM64DisplayLabel1.setGeometry(QtCore.QRect(14, 20, 101, 101))
        self.SM64DisplayLabel1.setGeometry(QtCore.QRect(6, 12, 101, 101))
        self.SM64DisplayLabel1.setText("")
        self.SM64DisplayLabel1.setPixmap(QtGui.QPixmap("resources/img/PlaceHolderEye1.png"))
        self.SM64DisplayLabel1.setScaledContents(True)
        self.SM64DisplayLabel1.setObjectName("SM64DisplayLabel1")
        
        self.SM64DisplayLabel2 = QtWidgets.QLabel(self.groupBox)
        #self.SM64DisplayLabel2.setGeometry(QtCore.QRect(14, 127, 101, 101))
        self.SM64DisplayLabel2.setGeometry(QtCore.QRect(6, self.SM64DisplayLabel1.y() + 111, 101, 101))
        self.SM64DisplayLabel2.setText("")
        self.SM64DisplayLabel2.setPixmap(QtGui.QPixmap("resources/img/PlaceHolderEye2.png"))
        self.SM64DisplayLabel2.setScaledContents(True)
        self.SM64DisplayLabel2.setObjectName("SM64DisplayLabel2")
        
        self.SM64DisplayLabel3 = QtWidgets.QLabel(self.groupBox)
        #self.SM64DisplayLabel3.setGeometry(QtCore.QRect(14, 234, 101, 101))
        self.SM64DisplayLabel3.setGeometry(QtCore.QRect(6, self.SM64DisplayLabel2.y() + 111, 101, 101))
        self.SM64DisplayLabel3.setText("")
        self.SM64DisplayLabel3.setPixmap(QtGui.QPixmap("resources/img/PlaceHolderEye3.png"))
        self.SM64DisplayLabel3.setScaledContents(True)
        self.SM64DisplayLabel3.setObjectName("SM64DisplayLabel3")
        
        self.SM64DisplayLabel4 = QtWidgets.QLabel(self.groupBox)
        #self.SM64DisplayLabel4.setGeometry(QtCore.QRect(14, 341, 101, 101))
        self.SM64DisplayLabel4.setGeometry(QtCore.QRect(6, self.SM64DisplayLabel3.y() + 111, 101, 101))
        self.SM64DisplayLabel4.setText("")
        self.SM64DisplayLabel4.setScaledContents(True)
        self.SM64DisplayLabel4.setObjectName("SM64DisplayLabel4")

        if Option.TextureBorder == "1":
            self.SM64DisplayLabel1.setStyleSheet("border: 1px solid;")
            self.SM64DisplayLabel2.setStyleSheet("border: 1px solid;")
            self.SM64DisplayLabel3.setStyleSheet("border: 1px solid;")
            self.SM64DisplayLabel4.setStyleSheet("border: 1px solid;")

        MainWindow.setCentralWidget(self.centralwidget)

        # Apply buttons
        # rip ApplyAdd
        # ▼
        self.ApplySM64 = QtWidgets.QPushButton(self.centralwidget)
        self.ApplySM64.setObjectName("ApplySM64")
        self.ApplySM64.setStyleSheet("font-size: 11px")

        self.ApplyDropdown = QtWidgets.QPushButton(self.centralwidget)
        self.ApplyDropdown.setObjectName("ApplyDropdown")
        self.ApplyDropdown.setText("▼")
        self.AddNamesContext = QtWidgets.QMenu(self)

        # Eyes list
        self.listWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.listWidget.header().setStretchLastSection(False)
        self.listWidget.header().setSectionResizeMode(QtWidgets.QHeaderView.Stretch) #QtWidgets.QHeaderView.ResizeToContents
        self.listWidget.setHeaderHidden(True)
        self.listWidget.setGeometry(QtCore.QRect(18, 16, 210, 495))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setFont(fontNine)

        #self.listWidget.addItems(EyeFolders)
        self.RefreshEyeList()

        self.listWidget.itemSelectionChanged.connect(self.OnSelectionChanged)

        #Refresh eye list button
        self.Refresh = QtWidgets.QPushButton(self.centralwidget)
        self.Refresh.setGeometry(QtCore.QRect(369, 489, 130, 23))
        self.Refresh.setObjectName("RefreshButton")
        self.Refresh.clicked.connect(lambda: self.RefreshEyeList())
        self.Refresh.hide()

        #Switch to cap, hair etc. from eyes and vice versa button
        self.SwitchItemsButton = QtWidgets.QPushButton(self.centralwidget)
        #self.SwitchItemsButton.setGeometry(QtCore.QRect(237, 489, 130, 23))
        #self.SwitchItemsButton.setGeometry(QtCore.QRect(237, 489, 262, 23))
        self.SwitchItemsButton.setObjectName("SwitchButton")
        self.SwitchItemsButton.clicked.connect(lambda: self.SwitchItems())
        #▲▼

        global DarkMode
        if Option.DarkMode == "0":
            DarkMode = 0
        else:
            DarkMode = 1
        

        #Menu bar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 518, 21))
        self.menubar.setObjectName("menubar")
        
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        self.actionRefresh = QtWidgets.QAction(self.menubar)
        self.actionRefresh.setObjectName("actionRefresh")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")

        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionSettings.triggered.connect(self.OpenSettingsWindow)
        
        self.actionDarkMode = QtWidgets.QAction(MainWindow)
        self.actionDarkMode.setObjectName("actionSettings")
        self.actionDarkMode.setCheckable(True)
        self.actionDarkMode.triggered.connect(self.DarkModeSwitch)
        
        self.submenuHiRes = QtWidgets.QMenu(MainWindow)
        self.submenuHiRes.setObjectName("actionHiRes")
        self.HiResClearSM64 = self.submenuHiRes.addAction("ClearSM64")
        self.HiResClearSM64.triggered.connect(self.ClearSM64)
        self.HiResClearAdd = self.submenuHiRes.addAction("ClearAdd")
        self.HiResClearAdd.triggered.connect(self.ClearAdd)
        self.submenuHiRes.addSeparator()
        self.HiResOpenSM64 = self.submenuHiRes.addAction("OpenSM64")
        self.HiResOpenSM64.triggered.connect(self.OpenSM64)
        self.actionOpenKataraktaFolder = QtWidgets.QAction(MainWindow)
        self.actionOpenKataraktaFolder.setObjectName("actionOpenKataraktaFolder")
        self.actionOpenKataraktaFolder.triggered.connect(self.OpenKataraktaFolder)
        self.actionOpenCcconv = QtWidgets.QAction(MainWindow)
        self.actionOpenCcconv.setObjectName("actionOpenCcconv")
        self.actionOpenCcconv.triggered.connect(self.OpenCcconv)
        self.actionStayOnTop = QtWidgets.QAction(MainWindow)
        self.actionStayOnTop.setObjectName("actionStayOnTop")
        self.actionStayOnTop.setCheckable(True)
        self.actionStayOnTop.triggered.connect(self.StayOnTop)
        self.submenuEyeBorders = QtWidgets.QMenu(MainWindow)
        self.submenuEyeBorders.setObjectName("submenuEyeBorders")
        self.EyeBordersCurrent = self.submenuEyeBorders.addAction("Current")
        self.EyeBordersAll = self.submenuEyeBorders.addAction("All")
        self.actionRefresh = QtWidgets.QAction(MainWindow)
        self.actionRefresh.setObjectName("actionRefresh")
        self.actionRefresh.triggered.connect(self.RefreshEyeList)

        if Option.StartUpStayOnTop == "1":
            self.actionStayOnTop.setChecked(True)
            self.StayOnTop()
        
        if Option.DarkMode == "1":
            self.actionDarkMode.setChecked(True)
        
        self.menuOptions.addMenu(self.submenuHiRes)
        self.menuOptions.addAction(self.actionOpenKataraktaFolder)
        self.menuOptions.addMenu(self.submenuEyeBorders)
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.actionSettings)
        self.menuOptions.addAction(self.actionOpenCcconv)
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.actionStayOnTop)
        self.menuOptions.addAction(self.actionDarkMode)
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.actionRefresh)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuOptions.menuAction())

        self.actionUpdate = QtWidgets.QAction(MainWindow)
        self.actionUpdate.setObjectName("actionUpdate")
        self.actionUpdate.triggered.connect(self.OpenUpdateWindow)
        
        self.actionRefresh.triggered.connect(self.RefreshEyeList)
        self.EyeBordersCurrent.setEnabled(False)
        
        self.menubar.addAction(self.actionUpdate)
        
        self.menubar.addAction(self.menuHelp.menuAction())

        self.actionAbout.triggered.connect(self.OpenAboutWindow)
        
        self.ApplySM64.setEnabled(False)
        
        self.ApplySM64.clicked.connect(lambda: self.CopyEyes("SM64Dir", (self.listWidget.selectedIndexes()[0].data(Qt.DisplayRole))))
        self.EyeBordersCurrent.triggered.connect(lambda: self.RemoveEyeBorders("Current"))
        self.EyeBordersAll.triggered.connect(lambda: self.RemoveEyeBorders("All"))
        
        self.retranslateUiEnglish(MainWindow)
        if Language.Properties_InnerName != "English":
            self.retranslateUiOther(MainWindow)
        self.Update()
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.DarkModeSwitch()
        self.HideAdditional()
        
    def PopulateTree(self, Directory):
        self.listWidget.clear()
        self.PopulateSubdirectories(self.listWidget.invisibleRootItem(), Directory)

    def PopulateSubdirectories(self, ParentItem, Directory):
        # Iterate through subdirectories
        for ItemName in os.listdir(Directory):
            ItemPath = os.path.join(Directory, ItemName)
            if os.path.isdir(ItemPath):
                # Create tree item for the subdirectory
                DirItem = QtWidgets.QTreeWidgetItem(ParentItem, [ItemName])
                DirItem.setData(0, Qt.UserRole, ItemPath)

                # Set directory's icon
                if Option.EyeListIcons == "1":
                    PNGIcon = self.FindPNGIcon(ItemPath)
                    if PNGIcon:
                        if Option.EyeListIconBG == "1":
                            ColorPNGIcon = QtGui.QPixmap(QPixmap(PNGIcon).size())
                            ColorPNGIcon.fill(QtGui.QColor(Option.BG_Color))
                            IconPainter = QtGui.QPainter(ColorPNGIcon)
                            IconPainter.drawPixmap(0, 0, QPixmap(PNGIcon))
                            IconPainter.end()
                            DirItem.setIcon(0, QIcon(QPixmap(ColorPNGIcon)))
                        else:
                            DirItem.setIcon(0, QIcon(QPixmap(PNGIcon)))

                # Recursively populate subdirectories
                self.PopulateSubdirectories(DirItem, ItemPath)

    def FindPNGIcon(self, Directory):
        # Look for a PNG file inside the directory
        DirectoryIconName = "DirectoryIcon.png"
        if os.path.exists(os.path.join(Directory, DirectoryIconName)):
            return os.path.join(Directory, DirectoryIconName)
        elif (self.Mode == "Eyes") and (os.path.exists(os.path.join(Directory, Option.SM64Name + Option.Eyes1 + ".png"))):
                return os.path.join(Directory, Option.SM64Name + Option.Eyes1 + ".png")
        elif (self.Mode == "CHMB") and (os.path.exists(os.path.join(Directory, Option.SM64Name + Option.Cap + ".png"))):
                return os.path.join(Directory, Option.SM64Name + Option.Cap + ".png")
        else:
            for FileName in os.listdir(Directory):
                if FileName.lower().endswith(".png"):
                    return os.path.join(Directory, FileName)
            return None
    
    def RemoveEyeBorders(self, mode):
        if mode == "All":
            self.PopupWarning("All")
            if PopupText == "&Yes":
                PNGFiles = []
                for i in ["eyes/", "chmb/"]:
                    for Root, Dirs, Files in os.walk(i):
                        for File in Files:
                            if File.endswith(".png"):
                                PNGFiles.append(os.path.abspath(os.path.join(Root, File)))
                for i in PNGFiles:
                    self.MakeNeighborsTransparent(i)
        else:
            self.PopupWarning("Current")
                
            if PopupText == "&Yes":
                #print("chosen yes")
                FolderNames = self.listWidget.selectedItems()
                if not FolderNames:
                    return
                FolderName = FolderNames[0]
                PathToTextures = FolderName.data(0, Qt.UserRole)
                TextureList = []
                if (os.path.isfile("{}/other.ini".format(PathToTextures)) == True):
                    Config.read("{}/other.ini".format(PathToTextures), encoding = "utf-8")
                    ConfigOther = Config["OTHER"]
                    OtherTextures.ApplyEverything = ConfigOther.get("Other_ApplyEverything", OtherTextures.ApplyEverything)
                    OtherTextures.Textures = ConfigOther.get("Other_Textures", OtherTextures.Textures).split(";")
                    if OtherTextures.ApplyEverything == "1":
                        for i in os.listdir("{}/".format(PathToTextures)):
                            if i.endswith(".png"):
                                TextureList.append(i[:-4])
                    else:
                        for i in OtherTextures.Textures:
                            try:
                                #TextureList.append(i)
                                #for i in TextureList:
                                self.MakeNeighborsTransparent("{}/{}.png".format(PathToTextures, i))
                            except:
                                pass
                    for i in TextureList:
                        if i == "":
                            TextureList.remove(i)
                else:
                    TextureList = [Option.Eyes1, Option.Eyes2, Option.Eyes3, Option.Cap, Option.Hair, Option.Mustache, Option.Button]
                for i in TextureList:
                    if os.path.isfile("{}/{}.png".format(PathToTextures, Option.SM64Name + i)):
                        self.MakeNeighborsTransparent("{}/{}.png".format(PathToTextures, Option.SM64Name + i))
                    #else:
                        #print("path {}/{}.png is false".format(PathToTextures, i))
    
    def PopupWarning(self, mode):
        msgbox = QtWidgets.QMessageBox()
        if mode == "Current":
            if Option.EyeBordersWarning == "1":
                global PopupText
                PopupText = "&Yes"
                return PopupText
            msgbox.setWindowTitle("Warning")
            msgbox.setText("Are you sure you want to remove the borders?")
            msgbox.setInformativeText("This pop-up can be disabled in the settings.")
            if Option.Language != "English":
                msgbox.setWindowTitle(Language.MW_EBCPopupWarning)
                msgbox.setText(Language.MW_EBCPopupText)
                msgbox.setInformativeText(Language.MW_EBCPopupInfoText)
            #if DarkMode == 1:
            msgbox.setWindowIcon(QIcon("resources/img/EyeBordersCurrent.png"))
            #else:
            #    msgbox.setWindowIcon(QIcon("resources/img/DarkMode/EyeBordersCurrent.png"))
        elif mode == "All":
            msgbox.setWindowTitle("Warning")
            msgbox.setText("Are you sure you want to remove the borders for ALL textures?")
            msgbox.setInformativeText("At least make a backup before doing it, this action cannot be undone.")
            if Option.Language != "English":
                msgbox.setWindowTitle(Language.MW_EBAPopupWarning)
                msgbox.setText(Language.MW_EBAPopupText)
                msgbox.setInformativeText(Language.MW_EBAPopupInfoText)
            msgbox.setWindowIcon(QIcon("resources/img/EyeBordersAll"))
        msgbox.setIcon(QtWidgets.QMessageBox.Question)
        msgbox.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        msgbox.setDefaultButton(QtWidgets.QMessageBox.Yes)
        msgbox.buttonClicked.connect(self.PopupGetText)
        runmsgbox = msgbox.exec_()
                    
    def PopupGetText(self, i):
        global PopupText
        PopupText = i.text()
    
    def MakeNeighborsTransparent(self, ImagePath):
        _Image = Image.open(ImagePath).convert("RGBA")
        Data = _Image.getdata()
        NewData = []
        for i in Data:
            if i[3] <= 4:
                NewData.append((0, 0, 0, 0))
            else:
                NewData.append(i)
        _Image.putdata(NewData)
        _Image.save(ImagePath)
        
        _Image = Image.open(ImagePath)
        Width, Height = _Image.size
        
        # The entire rest of this function was written by Discord's Clyde
        # The only thing I did here was rename variables and edit the comments a bit
    
        # Create a new image with the same size and transparent background
        NewImage = Image.new("RGBA", (Width, Height), (0, 0, 0, 0))
    
        for y in range(Height):
            for x in range(Width):
                # Get the pixel and its alpha value
                Pixel = _Image.getpixel((x, y))
                Alpha = Pixel[3]
    
                if Alpha != 0:
                    # Make the current pixel opaque in the new image
                    NewImage.putpixel((x, y), Pixel)
    
                    # Neighboring pixels
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            nx = x + dx
                            ny = y + dy
    
                            # Check if the neighboring pixel is within the image boundaries
                            if 0 <= nx < Width and 0 <= ny < Height:
                                # Make the neighboring pixel opaque with transparency of 1 in the new image
                                if _Image.getpixel((nx, ny))[3] == 0:
                                    NewImage.putpixel((nx, ny), (Pixel[0], Pixel[1], Pixel[2], 1))
        NewImage.save(ImagePath)
    
    def HideAdditional(self):
        self.SwitchItemsButton.setGeometry(QtCore.QRect(237, 489, 115, 23))
        MainWindow.setMinimumSize(369, 563)
        MainWindow.resize(369, 563)

    def DarkModeSwitch(self):
        if os.path.exists("config.ini") is True:
            pass
        else:
            CreateConfig()
        Config = configparser.ConfigParser()
        Config.read("config.ini")
        
        global DarkMode
        if DarkMode == 1:
            app.setStyle("Fusion")
            app.setPalette(DarkPalette)
            
            self.actionAbout.setIcon(QIcon("resources/img/Icon.png"))
            
            self.submenuHiRes.setIcon(QIcon("resources/img/DarkMode/HiResMain.png"))
            self.actionSettings.setIcon(QIcon("resources/img/DarkMode/Settings.png"))
            self.HiResClearSM64.setIcon(QIcon("resources/img/DarkMode/HiResClear.png"))
            self.HiResClearAdd.setIcon(QIcon("resources/img/DarkMode/HiResClearAdd.png"))
            self.HiResOpenSM64.setIcon(QIcon("resources/img/DarkMode/HiResOpen.png"))
            self.actionOpenKataraktaFolder.setIcon(QIcon("resources/img/DarkMode/OpenKataraktaFolder.png"))
            self.actionOpenCcconv.setIcon(QIcon("resources/img/DarkMode/ccconv.png"))
            self.actionStayOnTop.setIcon(QIcon("resources/img/DarkMode/StayOnTop.png"))
            #self.DarkModeButton.setIcon(QIcon("resources/img/ModeLight.png"))
            self.actionDarkMode.setIcon(QIcon("resources/img/ModeLight.png"))
            #self.EyesAddButton.setIcon(QIcon("resources/img/DarkMode/TexturesAdd.png"))
            #self.EyesRemoveButton.setIcon(QIcon("resources/img/DarkMode/TexturesRemove.png"))
            self.submenuEyeBorders.setIcon(QIcon("resources/img/DarkMode/EyeBorders.png"))
            self.EyeBordersCurrent.setIcon(QIcon("resources/img/DarkMode/EyeBordersCurrent.png"))
            self.EyeBordersAll.setIcon(QIcon("resources/img/DarkMode/EyeBordersAll.png"))
            self.actionRefresh.setIcon(QIcon("resources/img/DarkMode/Refresh.png"))

            if Option.TextureBorder == "1" and Option.BG_Mode == "default":
                self.SM64DisplayLabel1.setStyleSheet(f"border: 1px solid white;")
                self.SM64DisplayLabel2.setStyleSheet(f"border: 1px solid white;")
                self.SM64DisplayLabel3.setStyleSheet(f"border: 1px solid white;")
                self.SM64DisplayLabel4.setStyleSheet(f"border: 1px solid white;")
            
            DarkMode = 0
            Config.set("OPTIONS", "DarkMode", "1")
        else:
            app.setStyle("windowsvista")
            app.setPalette(DefaultPalette)
            
            self.actionAbout.setIcon(QIcon("resources/img/Icon.png"))
            
            self.submenuHiRes.setIcon(QIcon("resources/img/HiResMain.png"))
            self.actionSettings.setIcon(QIcon("resources/img/Settings.png"))
            self.HiResClearSM64.setIcon(QIcon("resources/img/HiResClear.png"))
            self.HiResClearAdd.setIcon(QIcon("resources/img/HiResClearAdd.png"))
            self.HiResOpenSM64.setIcon(QIcon("resources/img/HiResOpen.png"))
            self.actionOpenKataraktaFolder.setIcon(QIcon("resources/img/OpenKataraktaFolder.png"))
            self.actionOpenCcconv.setIcon(QIcon("resources/img/ccconv.png"))
            self.actionStayOnTop.setIcon(QIcon("resources/img/StayOnTop.png"))
            #self.DarkModeButton.setIcon(QIcon("resources/img/ModeDark.png"))
            self.actionDarkMode.setIcon(QIcon("resources/img/ModeDark.png"))
            #self.EyesAddButton.setIcon(QIcon("resources/img/TexturesAdd.png"))
            #self.EyesRemoveButton.setIcon(QIcon("resources/img/TexturesRemove.png"))
            self.submenuEyeBorders.setIcon(QIcon("resources/img/EyeBorders.png"))
            self.EyeBordersCurrent.setIcon(QIcon("resources/img/EyeBordersCurrent.png"))
            self.EyeBordersAll.setIcon(QIcon("resources/img/EyeBordersAll.png"))
            self.actionRefresh.setIcon(QIcon("resources/img/Refresh.png"))

            if Option.TextureBorder == "1" and Option.BG_Mode == "default":
                self.SM64DisplayLabel1.setStyleSheet(f"border: 1px solid black;")
                self.SM64DisplayLabel2.setStyleSheet(f"border: 1px solid black;")
                self.SM64DisplayLabel3.setStyleSheet(f"border: 1px solid black;")
                self.SM64DisplayLabel4.setStyleSheet(f"border: 1px solid black;")
            
            DarkMode = 1
            Config.set("OPTIONS", "DarkMode", "0")
            
        with open("config.ini", "w") as ConfigFile:
            Config.write(ConfigFile)
        self.RefreshEyeList()
        #▲▼
        
    def Update(self):
        self.menuHelp.adjustSize()
        self.menuOptions.adjustSize()
    
    def ApplyDropdownContext(self):
        global ApplyDropdownConnected
        ApplyDropdownConnected = True
        self.AddNamesContext.clear()
        global AddNamesList
        for i in AddNamesList:
            AddAction = QAction(i, self)
            AddAction.triggered.connect(lambda checked, ActionName = i: self.CopyEyes(ActionName, (self.listWidget.selectedIndexes()[0].data(Qt.DisplayRole))))
            self.AddNamesContext.addAction(AddAction)
        self.AddNamesContext.exec_(self.cursor().pos())
    
    def GetAddNames(self):
        global AddNamesList
        AddNamesList = Option.AddNames.split(";")
        for i in AddNamesList:
            if (i == "") or (i == " ") or (i == None):
                AddNamesList.remove(i)
        # Repeating this two times is intentional since if you do this only one time while having a ";" at the end of Option.AddNames, you'll still have a "" at the end of the list for some reason
        for i in AddNamesList:
            if (i == "") or (i == " ") or (i == None):
                AddNamesList.remove(i)
        return AddNamesList
    
    def RefreshEyeList(self):
        EyeFolders = os.listdir("eyes/")
        CHMBFolders = os.listdir("chmb/")
        self.GetAddNames()
        global ApplyDropdownConnected
        
        self.setStyleSheet("QTreeView::item { padding: "+Option.EyeListRowHeight+"px }")
        
        if ApplyDropdownConnected == True:
            self.ApplyDropdown.clicked.disconnect()
        self.ApplyDropdown.clicked.connect(self.ApplyDropdownContext)
        ApplyDropdownConnected = True
        if len(AddNamesList) == 0:
            self.ApplyDropdown.setEnabled(False)

        if self.Mode == "Eyes":
            self.PopulateTree("eyes/")
                
            self.ApplySM64.setGeometry(QtCore.QRect((MainWindow.width() - 132), 354, 94, 23))
            self.ApplyDropdown.setGeometry(QtCore.QRect(self.ApplySM64.pos().x() + 92, self.ApplySM64.pos().y(), 23, 23))
        else:
            self.PopulateTree("chmb/")
                    
            self.ApplySM64.setGeometry(QtCore.QRect((MainWindow.width() - 132), 465, 94, 23))
            self.ApplyDropdown.setGeometry(QtCore.QRect(self.ApplySM64.pos().x() + 92, self.ApplySM64.pos().y(), 23, 23))
        self.listWidget.clearSelection()
        try:
            self.ApplySM64.setEnabled(False)
            self.ApplyDropdown.setEnabled(False)
            if self.Mode == "Eyes":
                self.SM64DisplayLabel1.setPixmap(QtGui.QPixmap("resources/img/PlaceHolderEye1.png"))
                self.SM64DisplayLabel2.setPixmap(QtGui.QPixmap("resources/img/PlaceHolderEye2.png"))
                self.SM64DisplayLabel3.setPixmap(QtGui.QPixmap("resources/img/PlaceHolderEye3.png"))
                self.SM64DisplayLabel4.setPixmap(QtGui.QPixmap())
            if self.Mode == "CHMB":
                self.SM64DisplayLabel1.setPixmap(QtGui.QPixmap("resources/img/PlaceHolderCap.png"))
                self.SM64DisplayLabel2.setPixmap(QtGui.QPixmap("resources/img/PlaceHolderHair.png"))
                self.SM64DisplayLabel3.setPixmap(QtGui.QPixmap("resources/img/PlaceHolderMustache.png"))
                self.SM64DisplayLabel4.setPixmap(QtGui.QPixmap("resources/img/PlaceHolderButton.png"))
                #.scaled(101, 101, transformMode=QtCore.Qt.FastTransformation)
        except:
            pass
        
        if Option.BG_Mode == "default":
            self.DisplayLabelBg.hide()
            try:
                if DarkMode == "1":
                    self.SM64DisplayLabel1.setStyleSheet(f"border: 1px solid white;")
                    self.SM64DisplayLabel2.setStyleSheet(f"border: 1px solid white;")
                    self.SM64DisplayLabel3.setStyleSheet(f"border: 1px solid white;")
                    self.SM64DisplayLabel4.setStyleSheet(f"border: 1px solid white;")
                else:
                    self.SM64DisplayLabel1.setStyleSheet(f"border: 1px solid black;")
                    self.SM64DisplayLabel2.setStyleSheet(f"border: 1px solid black;")
                    self.SM64DisplayLabel3.setStyleSheet(f"border: 1px solid black;")
                    self.SM64DisplayLabel4.setStyleSheet(f"border: 1px solid black;")
            except:
                pass

        elif Option.BG_Mode == "color":
            try:
                self.DisplayLabelBg.setStyleSheet(f"background-color: {Option.BG_Color}")
                self.DisplayLabelBg.show()
            except:
                pass

            if Option.TextureBorder == "1":
                BorderColor = QColor()
                if (QColor(Option.BG_Color).getRgb()[0]) < 160 and (QColor(Option.BG_Color).getRgb()[0] > 100) and (QColor(Option.BG_Color).getRgb()[1]) < 160 and (QColor(Option.BG_Color).getRgb()[1] > 100) and (QColor(Option.BG_Color).getRgb()[2]) < 160 and (QColor(Option.BG_Color).getRgb()[2] > 100):
                    BorderColor.setRgb(0, 0, 0, 255)
                else:
                    BorderColor.setRgb(255 - QColor(Option.BG_Color).getRgb()[0], 255 - QColor(Option.BG_Color).getRgb()[1], 255 - QColor(Option.BG_Color).getRgb()[2], 255)
                self.SM64DisplayLabel1.setStyleSheet(f"border: 1px solid {QColor(BorderColor).name(QColor.HexRgb)};")
                self.SM64DisplayLabel2.setStyleSheet(f"border: 1px solid {QColor(BorderColor).name(QColor.HexRgb)};")
                self.SM64DisplayLabel3.setStyleSheet(f"border: 1px solid {QColor(BorderColor).name(QColor.HexRgb)};")
                self.SM64DisplayLabel4.setStyleSheet(f"border: 1px solid {QColor(BorderColor).name(QColor.HexRgb)};")
        elif Option.BG_Mode == "checkerboard":
            try:
                self.DisplayLabelBg.setStyleSheet(f"background-image: url(resources/img/TextureBackground{Option.BG_Checkerboard}.png)")
                self.DisplayLabelBg.show()
            except:
                pass
            
            self.SM64DisplayLabel1.setStyleSheet(f"border: 3px dashed red;")
            self.SM64DisplayLabel2.setStyleSheet(f"border: 3px dashed red;")
            self.SM64DisplayLabel3.setStyleSheet(f"border: 3px dashed red;")
            self.SM64DisplayLabel4.setStyleSheet(f"border: 3px dashed red;")
        elif Option.BG_Mode == "gradient":
            try:
                self.DisplayLabelBg.setStyleSheet("background-color: qlineargradient(x1: 0, x2: 1, stop: 0 {}, stop: 1 {})".format(Option.BG_Gradient1, Option.BG_Gradient2))
                self.DisplayLabelBg.show()
            except:
                pass

            if Option.TextureBorder == "1":
                BorderColor1 = QColor()
                BorderColor2 = QColor()
                if (QColor(Option.BG_Gradient1).getRgb()[0]) < 160 and (QColor(Option.BG_Gradient1).getRgb()[0] > 100) and (QColor(Option.BG_Gradient1).getRgb()[1]) < 160 and (QColor(Option.BG_Gradient1).getRgb()[1] > 100) and (QColor(Option.BG_Gradient1).getRgb()[2]) < 160 and (QColor(Option.BG_Gradient1).getRgb()[2] > 100):
                    BorderColor1.setRgb(0, 0, 0, 255)
                else:
                    BorderColor1.setRgb(255 - QColor(Option.BG_Gradient1).getRgb()[0], 255 - QColor(Option.BG_Gradient1).getRgb()[1], 255 - QColor(Option.BG_Gradient1).getRgb()[2], 255)
                if (QColor(Option.BG_Gradient2).getRgb()[0]) < 160 and (QColor(Option.BG_Gradient2).getRgb()[0] > 100) and (QColor(Option.BG_Gradient2).getRgb()[1]) < 160 and (QColor(Option.BG_Gradient2).getRgb()[1] > 100) and (QColor(Option.BG_Gradient2).getRgb()[2]) < 160 and (QColor(Option.BG_Gradient2).getRgb()[2] > 100):
                    BorderColor2.setRgb(0, 0, 0, 255)
                else:
                    BorderColor2.setRgb(255 - QColor(Option.BG_Gradient2).getRgb()[0], 255 - QColor(Option.BG_Gradient2).getRgb()[1], 255 - QColor(Option.BG_Gradient2).getRgb()[2], 255)
                self.SM64DisplayLabel1.setStyleSheet(f"border: 1px solid; border-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop: 0 {QColor(BorderColor1).name(QColor.HexRgb)}, stop: 1 {QColor(BorderColor2).name(QColor.HexRgb)}) {QColor(BorderColor2).name(QColor.HexRgb)} qlineargradient(x1:0, y1:0, x2:1, y2:0, stop: 0 {QColor(BorderColor1).name(QColor.HexRgb)}, stop: 1 {QColor(BorderColor2).name(QColor.HexRgb)}) {QColor(BorderColor1).name(QColor.HexRgb)};")
                self.SM64DisplayLabel2.setStyleSheet(f"border: 1px solid; border-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop: 0 {QColor(BorderColor1).name(QColor.HexRgb)}, stop: 1 {QColor(BorderColor2).name(QColor.HexRgb)}) {QColor(BorderColor2).name(QColor.HexRgb)} qlineargradient(x1:0, y1:0, x2:1, y2:0, stop: 0 {QColor(BorderColor1).name(QColor.HexRgb)}, stop: 1 {QColor(BorderColor2).name(QColor.HexRgb)}) {QColor(BorderColor1).name(QColor.HexRgb)};")
                self.SM64DisplayLabel3.setStyleSheet(f"border: 1px solid; border-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop: 0 {QColor(BorderColor1).name(QColor.HexRgb)}, stop: 1 {QColor(BorderColor2).name(QColor.HexRgb)}) {QColor(BorderColor2).name(QColor.HexRgb)} qlineargradient(x1:0, y1:0, x2:1, y2:0, stop: 0 {QColor(BorderColor1).name(QColor.HexRgb)}, stop: 1 {QColor(BorderColor2).name(QColor.HexRgb)}) {QColor(BorderColor1).name(QColor.HexRgb)};")
                self.SM64DisplayLabel4.setStyleSheet(f"border: 1px solid; border-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop: 0 {QColor(BorderColor1).name(QColor.HexRgb)}, stop: 1 {QColor(BorderColor2).name(QColor.HexRgb)}) {QColor(BorderColor2).name(QColor.HexRgb)} qlineargradient(x1:0, y1:0, x2:1, y2:0, stop: 0 {QColor(BorderColor1).name(QColor.HexRgb)}, stop: 1 {QColor(BorderColor2).name(QColor.HexRgb)}) {QColor(BorderColor1).name(QColor.HexRgb)};")
        else:
            self.DisplayLabelBg.hide()
            try:
                if DarkMode == "1":
                    self.SM64DisplayLabel1.setStyleSheet("border: 1px solid white;")
                    self.SM64DisplayLabel2.setStyleSheet("border: 1px solid white;")
                    self.SM64DisplayLabel3.setStyleSheet("border: 1px solid white;")
                    self.SM64DisplayLabel4.setStyleSheet("border: 1px solid white;")
                else:
                    self.SM64DisplayLabel1.setStyleSheet("border: 1px solid black;")
                    self.SM64DisplayLabel2.setStyleSheet("border: 1px solid black;")
                    self.SM64DisplayLabel3.setStyleSheet("border: 1px solid black;")
                    self.SM64DisplayLabel4.setStyleSheet("border: 1px solid black;")
            except:
                pass
        if Option.TextureBorder == "0":
            self.SM64DisplayLabel1.setStyleSheet("")
            self.SM64DisplayLabel2.setStyleSheet("")
            self.SM64DisplayLabel3.setStyleSheet("")
            self.SM64DisplayLabel4.setStyleSheet("")
                
    def SwitchItems(self):
        if self.Mode == "Eyes":
            self.Mode = "CHMB"
            
            self.groupBox.setGeometry(QtCore.QRect(QtCore.QRect(self.groupBox.pos().x(), self.groupBox.pos().y(), 128, 452)))
            
            self.Update()
            
            self.SM64DisplayLabel1.setPixmap(QtGui.QPixmap("resources/img/PlaceHolderCap.png"))
            self.SM64DisplayLabel2.setPixmap(QtGui.QPixmap("resources/img/PlaceHolderHair.png"))
            self.SM64DisplayLabel3.setPixmap(QtGui.QPixmap("resources/img/PlaceHolderMustache.png"))
            self.SM64DisplayLabel4.setPixmap(QtGui.QPixmap("resources/img/PlaceHolderButton.png"))
            
            self.SM64DisplayLabel4.show()
            
        else:
            self.Mode = "Eyes"
            
            self.groupBox.setGeometry(QtCore.QRect(self.groupBox.pos().x(), self.groupBox.pos().y(), 128, 341))

            self.Update()

            self.SM64DisplayLabel1.setPixmap(QtGui.QPixmap("resources/img/PlaceHolderEye1.png"))
            self.SM64DisplayLabel2.setPixmap(QtGui.QPixmap("resources/img/PlaceHolderEye2.png"))
            self.SM64DisplayLabel3.setPixmap(QtGui.QPixmap("resources/img/PlaceHolderEye3.png"))

            self.SM64DisplayLabel4.hide()
        self.RefreshEyeList()

    def OnSelectionChanged(self):
        FolderNames = self.listWidget.selectedItems()
        if not FolderNames:
            return
        FolderName = FolderNames[0]
        PathToTextures = FolderName.data(0, Qt.UserRole)
        CheckSM64 = 0
        if self.Mode == "Eyes":
            if os.path.isfile("{}/other.ini".format(PathToTextures)) == True:
                self.SM64DisplayLabel1.setPixmap(QtGui.QPixmap("resources/img/PlaceHolderOther.png"))
                self.SM64DisplayLabel2.setPixmap(QtGui.QPixmap("resources/img/PlaceHolderOther.png"))
                self.SM64DisplayLabel3.setPixmap(QtGui.QPixmap("resources/img/PlaceHolderOther.png"))
                self.SM64DisplayLabel4.setPixmap(QtGui.QPixmap())
                
                Config.read("{}/other.ini".format(PathToTextures), encoding = "utf-8")
                ConfigOther = Config["OTHER"]
                OtherTextures.ApplyEverything = ConfigOther.get("Other_ApplyEverything", OtherTextures.ApplyEverything)
                OtherTextures.Textures = ConfigOther.get("Other_Textures", OtherTextures.Textures)
                OtherTextures.Display1 = ConfigOther.get("Other_Display1", OtherTextures.Display1)
                OtherTextures.Display2 = ConfigOther.get("Other_Display2", OtherTextures.Display2)
                OtherTextures.Display3 = ConfigOther.get("Other_Display3", OtherTextures.Display3)
                OtherTextures.Display4 = ""
                
                if OtherTextures.Textures != "":
                    CheckSM64 += 1
                if OtherTextures.ApplyEverything == "1":
                    CheckSM64 += 1
                
                if OtherTextures.Display1 != "":
                    self.SM64DisplayLabel1.setPixmap(QtGui.QPixmap("{}/{}.png".format(PathToTextures, OtherTextures.Display1)))
                if OtherTextures.Display2 != "":
                    self.SM64DisplayLabel2.setPixmap(QtGui.QPixmap("{}/{}.png".format(PathToTextures, OtherTextures.Display2)))
                if OtherTextures.Display3 != "":
                    self.SM64DisplayLabel3.setPixmap(QtGui.QPixmap("{}/{}.png".format(PathToTextures, OtherTextures.Display3)))
                if OtherTextures.Display4 != "":
                    self.SM64DisplayLabel4.setPixmap(QtGui.QPixmap("{}/{}.png".format(PathToTextures, OtherTextures.Display4)))
            else:
                self.SM64DisplayLabel1.setPixmap(QtGui.QPixmap("resources/img/PlaceHolderEye1.png"))
                self.SM64DisplayLabel2.setPixmap(QtGui.QPixmap("resources/img/PlaceHolderEye2.png"))
                self.SM64DisplayLabel3.setPixmap(QtGui.QPixmap("resources/img/PlaceHolderEye3.png"))
                
                if os.path.exists("{}/{}.png".format(PathToTextures, Option.SM64Name + Option.Eyes1)):
                    self.SM64DisplayLabel1.setPixmap(QtGui.QPixmap("{}/{}.png".format(PathToTextures, Option.SM64Name + Option.Eyes1)))
                    CheckSM64 += 1
                if os.path.exists("{}/{}.png".format(PathToTextures, Option.SM64Name + Option.Eyes2)):
                    self.SM64DisplayLabel2.setPixmap(QtGui.QPixmap("{}/{}.png".format(PathToTextures, Option.SM64Name + Option.Eyes2)))
                    CheckSM64 += 1
                if os.path.exists("{}/{}.png".format(PathToTextures, Option.SM64Name + Option.Eyes3)):
                    self.SM64DisplayLabel3.setPixmap(QtGui.QPixmap("{}/{}.png".format(PathToTextures, Option.SM64Name + Option.Eyes3)))
                    CheckSM64 += 1
        else:
            if os.path.isfile("{}/other.ini".format(PathToTextures)) == True:
                self.SM64DisplayLabel1.setPixmap(QtGui.QPixmap("resources/img/PlaceHolderOther.png"))
                self.SM64DisplayLabel2.setPixmap(QtGui.QPixmap("resources/img/PlaceHolderOther.png"))
                self.SM64DisplayLabel3.setPixmap(QtGui.QPixmap("resources/img/PlaceHolderOther.png"))
                self.SM64DisplayLabel4.setPixmap(QtGui.QPixmap("resources/img/PlaceHolderOther.png"))
                
                Config.read("{}/other.ini".format(PathToTextures), encoding = "utf-8")
                ConfigOther = Config["OTHER"]
                OtherTextures.ApplyEverything = ConfigOther.get("Other_ApplyEverything", OtherTextures.ApplyEverything)
                OtherTextures.Textures = ConfigOther.get("Other_Textures", OtherTextures.Textures)
                OtherTextures.Display1 = ConfigOther.get("Other_Display1", OtherTextures.Display1)
                OtherTextures.Display2 = ConfigOther.get("Other_Display2", OtherTextures.Display2)
                OtherTextures.Display3 = ConfigOther.get("Other_Display3", OtherTextures.Display3)
                OtherTextures.Display4 = ConfigOther.get("Other_Display4", OtherTextures.Display4)
                
                if OtherTextures.Textures != "":
                    CheckSM64 += 1
                if OtherTextures.ApplyEverything == "1":
                    CheckSM64 += 1
                
                if OtherTextures.Display1 != "":
                    self.SM64DisplayLabel1.setPixmap(QtGui.QPixmap("{}/{}.png".format(PathToTextures, OtherTextures.Display1)))
                if OtherTextures.Display2 != "":
                    self.SM64DisplayLabel2.setPixmap(QtGui.QPixmap("{}/{}.png".format(PathToTextures, OtherTextures.Display2)))
                if OtherTextures.Display3 != "":
                    self.SM64DisplayLabel3.setPixmap(QtGui.QPixmap("{}/{}.png".format(PathToTextures, OtherTextures.Display3)))
                if OtherTextures.Display4 != "":
                    self.SM64DisplayLabel4.setPixmap(QtGui.QPixmap("{}/{}.png".format(PathToTextures, OtherTextures.Display4)))
            
            else:
                self.SM64DisplayLabel1.setPixmap(QtGui.QPixmap("resources/img/PlaceHolderCap.png"))
                self.SM64DisplayLabel2.setPixmap(QtGui.QPixmap("resources/img/PlaceHolderHair.png"))
                self.SM64DisplayLabel3.setPixmap(QtGui.QPixmap("resources/img/PlaceHolderMustache.png"))
                self.SM64DisplayLabel4.setPixmap(QtGui.QPixmap("resources/img/PlaceHolderButton.png"))
                
                if os.path.exists("{}/{}.png".format(PathToTextures, Option.SM64Name + Option.Cap)):
                    self.SM64DisplayLabel1.setPixmap(QtGui.QPixmap("{}/{}.png".format(PathToTextures, Option.SM64Name + Option.Cap)))
                    CheckSM64 += 1
                if os.path.exists("{}/{}.png".format(PathToTextures, Option.SM64Name + Option.Hair)):
                    self.SM64DisplayLabel2.setPixmap(QtGui.QPixmap("{}/{}.png".format(PathToTextures, Option.SM64Name + Option.Hair)))
                    CheckSM64 += 1
                if os.path.exists("{}/{}.png".format(PathToTextures, Option.SM64Name + Option.Mustache)):
                    self.SM64DisplayLabel3.setPixmap(QtGui.QPixmap("{}/{}.png".format(PathToTextures, Option.SM64Name + Option.Mustache)))
                    CheckSM64 += 1
                if os.path.exists("{}/{}.png".format(PathToTextures, Option.SM64Name + Option.Button)):
                    self.SM64DisplayLabel4.setPixmap(QtGui.QPixmap("{}/{}.png".format(PathToTextures, Option.SM64Name + Option.Button)))
                    CheckSM64 += 1
                
        if CheckSM64 > 0:
            self.ApplySM64.setEnabled(True)
            if len(AddNamesList) != 0:
                self.ApplyDropdown.setEnabled(True)
        else:
            self.ApplySM64.setEnabled(False)
            self.ApplyDropdown.setEnabled(False)
        if (CheckSM64 > 0) or (CheckSM64 > 0):
            self.EyeBordersCurrent.setEnabled(True)
        else:
            self.EyeBordersCurrent.setEnabled(False)
            
        if OtherTextures.ApplyEverything == "1":
            self.ApplySM64.setEnabled(True)
            self.ApplyDropdown.setEnabled(True)
            

    def CopyEyes(self, Type, FolderName):
        #PathToTextures = self.ListModel.filePath(self.listWidget.selectedIndexes()[0])
        FolderNames = self.listWidget.selectedItems()
        if not FolderNames:
            return
        FolderName = FolderNames[0]
        PathToTextures = FolderName.data(0, Qt.UserRole)
        
        if os.path.isfile("{}cache.ini".format(Option.HiResDir + Option.SM64Name + "/")):
            os.remove("{}cache.ini".format(Option.HiResDir + Option.SM64Name + "/"))
        
        if os.path.isfile("{}Cache.ini".format(Option.HiResDir + Option.SM64Name + "/")):
            os.remove("{}cache.ini".format(Option.HiResDir + Option.SM64Name + "/"))
        
        self.GetAddNames()
        for i in AddNamesList:
            
            if os.path.isfile("{}cache.ini".format(Option.HiResDir + i + "/")):
                os.remove("{}cache.ini".format(Option.HiResDir + i + "/"))
            
            if os.path.isfile("{}Cache.ini".format(Option.HiResDir + i + "/")):
                os.remove("{}cache.ini".format(Option.HiResDir + i + "/"))
        
        EyeList = [Option.Eyes1, Option.Eyes2, Option.Eyes3]
        CHMBList = [Option.Cap, Option.Hair, Option.Mustache, Option.Button]
            
        if self.Mode == "Eyes":
            if Type == "SM64Dir":
                Path = Option.HiResDir
                if os.path.isfile("{}/other.ini".format(PathToTextures)) == True:
                    Config.read("{}/other.ini".format(PathToTextures), encoding = "utf-8")
                    ConfigOther = Config["OTHER"]
                    OtherTextures.ApplyEverything = ConfigOther.get("Other_ApplyEverything", OtherTextures.ApplyEverything)
                    OtherTextures.Textures = ConfigOther.get("Other_Textures", OtherTextures.Textures).split(";")
                    OtherTextures.Display1 = ConfigOther.get("Other_Display1", OtherTextures.Display1)
                    OtherTextures.Display2 = ConfigOther.get("Other_Display2", OtherTextures.Display2)
                    OtherTextures.Display3 = ConfigOther.get("Other_Display3", OtherTextures.Display3)
                    NewOtherTextures = []
                    for i in OtherTextures.Textures:
                        if i.find("#") != -1:
                            NewOtherTextures.append(i[i.find("#"):])
                    if OtherTextures.ApplyEverything == "1":
                        if os.path.exists(Option.HiResDir + Option.SM64Name + "/") == False:
                            os.mkdir(Option.HiResDir + Option.SM64Name + "/")
                        for i in os.listdir("{}/".format(PathToTextures)):
                            if i.endswith(".png"):
                                if i.find("#") != -1:
                                    shutil.copyfile("{}/{}".format(PathToTextures, i), "{}{}".format(Option.HiResDir + Option.SM64Name + "/", Option.SM64Name + i[i.find("#"):]))
                    else:
                        for i, j in zip(NewOtherTextures, OtherTextures.Textures):
                            try:
                                if os.path.exists(Option.HiResDir + Option.SM64Name + "/") == False:
                                    os.mkdir(Option.HiResDir + Option.SM64Name + "/")
                                shutil.copyfile("{}/{}.png".format(PathToTextures, j), "{}{}.png".format(Option.HiResDir + Option.SM64Name + "/", Option.SM64Name + i))
                            except:
                                pass
                else:
                    for i in EyeList:
                        try:
                            if os.path.exists(Option.HiResDir + Option.SM64Name + "/") == False:
                                os.mkdir(Option.HiResDir + Option.SM64Name + "/")
                            shutil.copyfile("{}/{}.png".format(PathToTextures, Option.SM64Name + i), "{}{}.png".format(Option.HiResDir + Option.SM64Name + "/" + Option.SM64Name, i))
                        except:
                            pass
            else:
                if os.path.isfile("{}/other.ini".format(PathToTextures)) == True:
                    Config.read("{}/other.ini".format(PathToTextures), encoding = "utf-8")
                    ConfigOther = Config["OTHER"]
                    OtherTextures.ApplyEverything = ConfigOther.get("Other_ApplyEverything", OtherTextures.ApplyEverything)
                    OtherTextures.Textures = ConfigOther.get("Other_Textures", OtherTextures.Textures).split(";")
                    OtherTextures.Display1 = ConfigOther.get("Other_Display1", OtherTextures.Display1)
                    OtherTextures.Display2 = ConfigOther.get("Other_Display2", OtherTextures.Display2)
                    OtherTextures.Display3 = ConfigOther.get("Other_Display3", OtherTextures.Display3)
                    NewOtherTextures = []
                    for i in OtherTextures.Textures:
                        if i.find("#") != -1:
                            NewOtherTextures.append(i[i.find("#"):])
                    if OtherTextures.ApplyEverything == "1":
                        if os.path.exists(Option.HiResDir + Type + "/") == False:
                            os.mkdir(Option.HiResDir + Type + "/")
                        for i in os.listdir("{}/".format(PathToTextures)):
                            if i.endswith(".png"):
                                if i.find("#") != -1:
                                    shutil.copyfile("{}/{}".format(PathToTextures, i), "{}{}".format(Option.HiResDir + Type + "/", Type + i[i.find("#"):]))
                    else:
                        for i, j in zip(NewOtherTextures, OtherTextures.Textures):
                            try:
                                if os.path.exists(Option.HiResDir + Type + "/") == False:
                                    os.mkdir(Option.HiResDir + Type + "/")
                                shutil.copyfile("{}/{}.png".format(PathToTextures, j), "{}{}.png".format(Option.HiResDir + Type + "/", Type + i))
                            except:
                                pass
                else:
                    for i in EyeList:
                        try:
                            if os.path.exists(Option.HiResDir + Type + "/") == False:
                                os.mkdir(Option.HiResDir + Type + "/")
                            shutil.copyfile("{}/{}.png".format(PathToTextures, Option.SM64Name + i), "{}{}.png".format(Option.HiResDir + Type + "/" + Type, i))
                        except:
                            pass

        else:
            if Type == "SM64Dir":
                if os.path.isfile("{}/other.ini".format(PathToTextures)) == True:
                    Config.read("{}/other.ini".format(PathToTextures), encoding = "utf-8")
                    ConfigOther = Config["OTHER"]
                    OtherTextures.ApplyEverything = ConfigOther.get("Other_ApplyEverything", OtherTextures.ApplyEverything)
                    OtherTextures.Textures = ConfigOther.get("Other_Textures", OtherTextures.Textures).split(";")
                    OtherTextures.Display1 = ConfigOther.get("Other_Display1", OtherTextures.Display1)
                    OtherTextures.Display2 = ConfigOther.get("Other_Display2", OtherTextures.Display2)
                    OtherTextures.Display3 = ConfigOther.get("Other_Display3", OtherTextures.Display3)
                    OtherTextures.Display4 = ConfigOther.get("Other_Display4", OtherTextures.Display4)
                    NewOtherTextures = []
                    for i in OtherTextures.Textures:
                        if i.find("#") != -1:
                            NewOtherTextures.append(i[i.find("#"):])
                    if OtherTextures.ApplyEverything == "1":
                        if os.path.exists(Option.HiResDir + Option.SM64Name + "/") == False:
                            os.mkdir(Option.HiResDir + Option.SM64Name + "/")
                        for i in os.listdir("{}/".format(PathToTextures)):
                            if i.endswith(".png"):
                                if i.find("#") != -1:
                                    shutil.copyfile("{}/{}".format(PathToTextures, i), "{}{}".format(Option.HiResDir + Option.SM64Name + "/", Option.SM64Name + i[i.find("#"):]))
                    else:
                        for i, j in zip(NewOtherTextures, OtherTextures.Textures):
                            try:
                                if os.path.exists(Option.HiResDir + Option.SM64Name + "/") == False:
                                    os.mkdir(Option.HiResDir + Option.SM64Name + "/")
                                shutil.copyfile("{}/{}.png".format(PathToTextures, j), "{}{}.png".format(Option.HiResDir + Option.SM64Name + "/", Option.SM64Name + i))
                            except:
                                pass
                else:
                    for i in CHMBList:
                        try:
                            if os.path.exists(Option.HiResDir + Option.SM64Name + "/") == False:
                                os.mkdir(Option.HiResDir + Option.SM64Name + "/")
                            shutil.copyfile("{}/{}.png".format(PathToTextures, Option.SM64Name + i), "{}{}.png".format(Option.HiResDir + Option.SM64Name + "/" + Option.SM64Name, i))
                        except:
                            pass
                
            else:
                if os.path.isfile("{}/other.ini".format(PathToTextures)) == True:
                    Config.read("{}/other.ini".format(PathToTextures), encoding = "utf-8")
                    ConfigOther = Config["OTHER"]
                    OtherTextures.ApplyEverything = ConfigOther.get("Other_ApplyEverything", OtherTextures.ApplyEverything)
                    OtherTextures.Textures = ConfigOther.get("Other_Textures", OtherTextures.Textures).split(";")
                    OtherTextures.Display1 = ConfigOther.get("Other_Display1", OtherTextures.Display1)
                    OtherTextures.Display2 = ConfigOther.get("Other_Display2", OtherTextures.Display2)
                    OtherTextures.Display3 = ConfigOther.get("Other_Display3", OtherTextures.Display3)
                    OtherTextures.Display4 = ConfigOther.get("Other_Display4", OtherTextures.Display4)
                    NewOtherTextures = []
                    for i in OtherTextures.Textures:
                        if i.find("#") != -1:
                            NewOtherTextures.append(i[i.find("#"):])
                    if OtherTextures.ApplyEverything == "1":
                        if os.path.exists(Option.HiResDir + Type + "/") == False:
                            os.mkdir(Option.HiResDir + Type + "/")
                        for i in os.listdir("{}/".format(PathToTextures)):
                            if i.endswith(".png"):
                                if i.find("#") != -1:
                                    shutil.copyfile("{}/{}".format(PathToTextures, i), "{}{}".format(Option.HiResDir + Type + "/", Type + i[i.find("#"):]))
                    else:
                        for i, j in zip(NewOtherTextures, OtherTextures.Textures):
                            try:
                                if os.path.exists(Option.HiResDir + Type + "/") == False:
                                    os.mkdir(Option.HiResDir + Type + "/")
                                shutil.copyfile("{}/{}.png".format(PathToTextures, j), "{}{}.png".format(Option.HiResDir + Type + "/", Type + i))
                            except:
                                pass
                else:
                    for i in CHMBList:
                        try:
                            if os.path.exists(Option.HiResDir + Type + "/") == False:
                                os.mkdir(Option.HiResDir + Type + "/")
                            shutil.copyfile("{}/{}.png".format(PathToTextures, Option.SM64Name + i), "{}{}.png".format(Option.HiResDir + Type + "/" + Type, i))
                        except:
                            pass

    def OpenSM64(self):
        os.startfile(Option.HiResDir)

    def OpenAdd(self):
        os.startfile(Option.HiResDir)

    def OpenKataraktaFolder(self):
        os.startfile(os.getcwd())

    def ClearSM64(self):
        if Option.HiResDir != "":
            for i in os.listdir(Option.HiResDir + Option.SM64Name + "/"):
                if os.path.isfile(Option.HiResDir + Option.SM64Name + "/" + i):
                    os.remove(Option.HiResDir + Option.SM64Name + "/" + i)
                elif os.path.isdir(Option.HiResDir + Option.SM64Name + "/" + i):
                    shutil.rmtree(Option.HiResDir + Option.SM64Name + "/" + i + "/")
        
    def ClearAdd(self):
        if Option.AddNames != "":
            global AddNamesList
            self.GetAddNames()
            for AddGame in AddNamesList:
                if os.path.exists(Option.HiResDir + AddGame + "/") == True:
                    for i in os.listdir(Option.HiResDir + AddGame + "/"):
                        if os.path.isfile(Option.HiResDir + AddGame + "/" + i):
                            os.remove(Option.HiResDir + AddGame + "/" + i)
                        elif os.path.isdir(Option.HiResDir + AddGame + "/" + i):
                            shutil.rmtree(Option.HiResDir + AddGame + "/" + i + "/")

    def StayOnTop(self):
        if self.actionStayOnTop.isChecked() == True:
            MainWindow.setWindowFlags(MainWindow.windowFlags() | Qt.WindowStaysOnTopHint)
            MainWindow.show()
        else:
            MainWindow.setWindowFlags(MainWindow.windowFlags() & ~QtCore.Qt.WindowStaysOnTopHint)
            MainWindow.show()

    def retranslateUiEnglish(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "katarakta {} ({})".format(AppVersion, AppEdition)))
        self.ApplySM64.setText(_translate("MainWindow", "Apply"))
        self.groupBox.setTitle(_translate("MainWindow", ""))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.Refresh.setText(_translate("MainWindow", "Refresh"))
        self.SwitchItemsButton.setText(_translate("MainWindow", "Switch"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.submenuHiRes.setTitle(_translate("MainWindow", "Hi-res folders"))
        self.HiResClearSM64.setText(_translate("MainWindow", "Clear SM64"))
        self.HiResClearAdd.setText(_translate("MainWindow", "Clear Additional"))
        self.HiResOpenSM64.setText(_translate("MainWindow", "Open hi-res folder"))
        self.actionOpenKataraktaFolder.setText(_translate("MainWindow", "Open katarakta folder"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionOpenCcconv.setText(_translate("MainWindow", "Color Code Converter"))
        self.actionStayOnTop.setText(_translate("MainWindow", "Stay on Top"))
        self.actionUpdate.setText(_translate("MainWindow", "Check for Updates"))
        self.actionRefresh.setText(_translate("MainWindow", "Refresh List"))
        self.actionDarkMode.setText(_translate("MainWindow", "Dark Mode"))
        self.submenuEyeBorders.setTitle(_translate("MainWindow", "Remove Texture Borders"))
        self.EyeBordersCurrent.setText(_translate("MainWindow", "Currently Selected"))
        self.EyeBordersAll.setText(_translate("MainWindow", "Every Texture"))

    def retranslateUiOther(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "{} {} ({})".format(Language.MW_Title, AppVersion, AppEdition)))
        setTextList = [
                    [self.ApplySM64,                 Language.MW_ApplySM64],
                    [self.actionAbout,               Language.MW_actionAbout],
                    [self.Refresh,                   Language.MW_Refresh],
                    [self.SwitchItemsButton,         Language.MW_SwitchItemsButton],
                    [self.HiResClearSM64,            Language.MW_HiResClearSM64],
                    [self.HiResClearAdd,             Language.MW_HiResCleadAdd],
                    [self.HiResOpenSM64,             Language.MW_HiResOpenSM64],
                    [self.actionOpenKataraktaFolder, Language.MW_actionOpenKataraktaFolder],
                    [self.actionSettings,            Language.MW_actionSettings],
                    [self.actionOpenCcconv,          Language.MW_actionOpenCcconv],
                    [self.actionStayOnTop,           Language.MW_actionStayOnTop],
                    [self.actionUpdate,              Language.MW_actionUpdate],
                    [self.actionRefresh,             Language.MW_Refresh],
                    [self.actionDarkMode,            Language.MW_actionDarkMode],
                    [self.EyeBordersCurrent,         Language.MW_EyeBordersCurrent],
                    [self.EyeBordersAll,             Language.MW_EyeBordersAll]
                    ]
        setTitleList = [
                    [self.groupBox,                  ""],
                    [self.menuHelp,                  Language.MW_menuHelp],
                    [self.menuOptions,               Language.MW_menuOptions],
                    [self.submenuHiRes,              Language.MW_submenuHiRes],
                    [self.submenuEyeBorders,         Language.MW_submenuEyeBorders],
                    ]
        
        # if second item in the list is not "" or None, then apply that text
        for i in setTextList:
            #print("setTextList:\n\"{}\", \"{}\"".format(i[0], i[1]))
            if (i[1] != "") and (i[1] != None):
                i[0].setText(_translate("MainWindow", i[1]))
        for i in setTitleList:
            #print("setTitleList:\n\"{}\", \"{}\"".format(i[0], i[1]))
            if (i[1] != "") and (i[1] != None):
                i[0].setTitle(_translate("MainWindow", i[1]))

class Ui_AboutWindow(object):
    def setupUi(self, AboutWindow):

        AboutWindow.setObjectName("About katarakta")
        AboutWindow.resize(520, 381)
        AboutWindow.setWindowFlags(AboutWindow.windowFlags() | Qt.WindowStaysOnTopHint)
        
        # Pride Month easter egg
        # It's a very important feature I swear!!!
        self.LabelPride = QtWidgets.QLabel(AboutWindow)
        self.LabelPride.setObjectName("LabelPride")
        self.LabelPride.setHidden(True)
        self.LabelPride.setGeometry(QtCore.QRect(240, 5, 271, 25))
        self.LabelPride.setAlignment(Qt.AlignCenter)
        self.LabelPride.setStyleSheet("font-size: 16px")
        global IconClickedTimes
        IconClickedTimes = 0
        
        self.LabelName = QtWidgets.QLabel(AboutWindow)
        self.LabelName.setGeometry(QtCore.QRect(240, 20, 271, 71))
        self.LabelName.setObjectName("LabelName")
        self.LabelName.setStyleSheet("font-size: 64px")
        self.LabelVersion = QtWidgets.QLabel(AboutWindow)
        self.LabelVersion.setGeometry(QtCore.QRect(240, 90, 181, 20))
        self.LabelVersion.setObjectName("LabelVersion")
        self.LabelVersion.setStyleSheet("font-size: 24px")
        self.LabelAuthor = QtWidgets.QLabel(AboutWindow)
        self.LabelAuthor.setGeometry(QtCore.QRect(20, 230, 481, 16))
        self.LabelAuthor.setObjectName("LabelAuthor")
        self.LabelAuthor.setOpenExternalLinks(True)
        self.LabelAuthor.setStyleSheet("font-size: 11px")
        self.LabelVersion.setStyleSheet("font-size: 24px")
        self.LabelIcon = QtWidgets.QLabel(AboutWindow)
        self.LabelIcon.setGeometry(QtCore.QRect(20, 20, 201, 201))
        self.LabelIcon.setText("")
        self.LabelIcon.setPixmap(QtGui.QPixmap("resources/img/768icon.png"))
        self.LabelIcon.setScaledContents(True)
        self.LabelIcon.setObjectName("LabelIcon")
        self.LabelIcon.mousePressEvent = self.ShowTheGay
        self.LabelAddInfo = QtWidgets.QLabel(AboutWindow)
        self.LabelAddInfo.setGeometry(QtCore.QRect(240, 155, 481, 16))
        self.LabelAddInfo.setObjectName("LabelAddInfo")
        self.LabelAddInfo.setOpenExternalLinks(True)
        self.LabelAddInfo.setStyleSheet("font-size: 11px")
        self.LineLegalNotice = QtWidgets.QFrame(AboutWindow)
        self.LineLegalNotice.setObjectName("LineLegalNotice")
        self.LineLegalNotice.setGeometry(QtCore.QRect(20, 310, 481, 3))
        self.LineLegalNotice.setFrameShape(QtWidgets.QFrame.HLine)
        self.LineLegalNotice.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.LabelLegalNotice = QtWidgets.QLabel(AboutWindow)
        self.LabelLegalNotice.setGeometry(QtCore.QRect(20, 328, 481, 30))
        self.LabelLegalNotice.setObjectName("LabelLegalNotice")
        self.LabelLegalNotice.setAlignment(Qt.AlignCenter)
        self.LabelLegalNotice.setStyleSheet("font-size: 11px")
        
        AboutWindow.setFixedSize(AboutWindow.size())
        AboutWindow.setWindowFlags(AboutWindow.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint & ~QtCore.Qt.WindowMinimizeButtonHint )
        
        AboutWindow.setWindowIcon(QtGui.QIcon("resources/img/Icon.png"))
        
        self.retranslateUiEnglish(AboutWindow)
        if Language.Properties_InnerName != "English":
            self.retranslateUiOther(AboutWindow)
        self.Update()
        
        QtCore.QMetaObject.connectSlotsByName(AboutWindow)
        
    def ShowTheGay(self, AboutWindow):
        global IconClickedTimes
        IconClickedTimes += 1
        if IconClickedTimes >= 5:
            CurrentMonth = datetime.now().month
            if str(CurrentMonth) == "6":
                PrideText = ["H", "a", "p", "p", "y ", "P", "r", "i", "d", "e ", "M", "o", "n", "t", "h"]
                PrideColors = ["#FDD817", "#66338B", "#7BCCE5", "#F4AEC8", "#FFFFFF", "#F4AEC8", "#7BCCE5", "#945516", "#000000", "#E22016", "#F28917", "#EFE524", "#78B82A", "#2C58A4", "#6D2380"]
                ColoredText = ""
                for Letter, Color in zip(PrideText, PrideColors):
                    ColoredText += f"<font color=\"{Color}\">{Letter}</font>"
                ColoredText += "!"
                self.LabelPride.setStyleSheet("background-color: #858585; font-size: 16px")
                self.LabelPride.setText(ColoredText)
                self.LabelPride.setHidden(False)
            else:
                self.LabelPride.setText("Not yet ;)")
                self.LabelPride.setStyleSheet("font-size: 16px")
                self.LabelPride.setHidden(False)
        
    def Update(self):
        self.LabelName.adjustSize()
        self.LabelVersion.adjustSize()
        self.LabelAuthor.adjustSize()
        self.LabelAddInfo.adjustSize()
    
    def retranslateUiEnglish(self, AboutWindow):
        _translate = QtCore.QCoreApplication.translate
        AboutWindow.setWindowTitle(_translate("AboutWindow", "About katarakta"))
        self.LabelName.setText(_translate("AboutWindow", "katarakta"))
        self.LabelVersion.setText(_translate("AboutWindow", "Version: {}\nEdition: {}".format(AppVersion, AppEdition)))
        self.LabelAuthor.setText(_translate("AboutWindow", "By DanilAstroid (<a href = 'https://www.youtube.com/channel/UCCrO_HQsasKN7Zwlp3D8UWQ'>YouTube</a>, <a href = 'https://github.com/vazhka-dolya/'>GitHub</a>).<br><br>Thanks to the following people for testing katarakta:<br>• @Blender_Blenderovych (<a href = 'https://www.youtube.com/channel/UCGxro_VNeDQBY9k8_jitMCw'>YouTube 1</a>, <a href = 'https://www.youtube.com/channel/UCBkB7pjgU1cjKvjg_OzjzIg'>YouTube 2</a>)<br>• @SDRM45 (<a href = 'https://www.youtube.com/channel/UC-3gc0FmQA2_Z2-MIS5sZNQ'>YouTube</a>)"))
        self.LabelAddInfo.setText(_translate("AboutWindow", "This project uses the GNU General Public License v3.0<br><br><a href = 'https://github.com/vazhka-dolya/katarakta/issues/'>Report issues</a>"))
        self.LabelLegalNotice.setText(_translate("AboutWindow", "This program is not affiliated with or sponsored by Nintendo and does not claim ownership over any\nof Nintendo's intellectual property used (such as the characters in the loading screens)."))

    def retranslateUiOther(self, AboutWindow):
        _translate = QtCore.QCoreApplication.translate
        AboutWindow.setWindowTitle(_translate("AboutWindow", Language.AW_Title))
        self.LabelName.setText(_translate("AboutWindow", Language.AW_LabelName))
        self.LabelVersion.setText(_translate("AboutWindow", "{} {}\n{} {}".format(Language.AW_LabelVersion, AppVersion, Language.AW_LabelEdition, AppEdition)))
        self.LabelAuthor.setText(_translate("AboutWindow", "{} DanilAstroid (<a href = 'https://www.youtube.com/channel/UCCrO_HQsasKN7Zwlp3D8UWQ'>YouTube</a>, <a href = 'https://github.com/vazhka-dolya/'>GitHub</a>).<br><br>{}<br>@Blender_Blenderovych (<a href = 'https://www.youtube.com/channel/UCGxro_VNeDQBY9k8_jitMCw'>YouTube 1</a>, <a href = 'https://www.youtube.com/channel/UCBkB7pjgU1cjKvjg_OzjzIg'>YouTube 2</a>)<br>@SDRM45 (<a href = 'https://www.youtube.com/channel/UC-3gc0FmQA2_Z2-MIS5sZNQ'>YouTube</a>)".format(Language.AW_LabelAuthor, Language.AW_SpecialThanks)))
        self.LabelAddInfo.setText(_translate("AboutWindow", "{}<br><br><a href = 'https://github.com/vazhka-dolya/katarakta/issues/'>{}</a>".format(Language.AW_LabelAddInfo, Language.AW_LabelReportIssue)))
        self.LabelLegalNotice.setText(_translate("AboutWindow", Language.AW_LabelLegalNotice))

class Ui_UpdateWindow(object):
    def setupUi(self, UpdateWindow):

        if not UpdateWindow.objectName():
            UpdateWindow.setObjectName("UpdateWindow")
        
        UpdateWindow.setStyleSheet("font-size: 11px")
        UpdateWindow.resize(480, 336)
        self.UpdateCheckLabel = QtWidgets.QLabel(UpdateWindow)
        self.UpdateCheckLabel.setObjectName("UpdateCheckLabel")
        self.UpdateCheckLabel.setGeometry(QtCore.QRect(90, 10, 171, 31))
        self.UpdateCheckLabel.setStyleSheet("font-size: 24px")
        self.YourVersionLabel = QtWidgets.QLabel(UpdateWindow)
        self.YourVersionLabel.setObjectName("YourVersionLabel")
        self.YourVersionLabel.setGeometry(QtCore.QRect(10, 70, 131, 21))
        self.YourVersionLabel.setStyleSheet("font-size: 16px")
        self.LatestVersionLabel = QtWidgets.QLabel(UpdateWindow)
        self.LatestVersionLabel.setObjectName("LatestVersionLabel")
        self.LatestVersionLabel.setGeometry(QtCore.QRect(10, 95, 201, 61))
        self.LatestVersionLabel.setStyleSheet("font-size: 16px")
        self.IconLabel = QtWidgets.QLabel(UpdateWindow)
        self.IconLabel.setObjectName("IconLabel")
        self.IconLabel.setGeometry(QtCore.QRect(10, 0, 71, 71))
        self.IconLabel.setPixmap(QPixmap("resources/img/update256.png"))
        self.IconLabel.setScaledContents(True)
        self.StatusLabel = QtWidgets.QLabel(UpdateWindow)
        self.StatusLabel.setObjectName("StatusLabel")
        self.StatusLabel.setGeometry(QtCore.QRect(90, 45, 111, 31))
        self.StatusLabel.setOpenExternalLinks(True)
        font2 = QtGui.QFont()
        font2.setPointSize(10)
        self.StatusLabel.setFont(font2)
        self.textBrowser = QtWidgets.QTextBrowser(UpdateWindow)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setGeometry(QtCore.QRect(10, 136, 460, 189))
        self.textBrowser.setAutoFillBackground(False)
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowserDescription = QtWidgets.QLabel(UpdateWindow)
        self.textBrowserDescription.setObjectName("textBrowserDescription")
        self.textBrowserDescription.setGeometry(QtCore.QRect(10, 115, 460, 22))
        self.LaunchUpdater = QtWidgets.QPushButton(UpdateWindow)
        self.LaunchUpdater.setGeometry(QtCore.QRect(300, 43, 166, 23))
        self.LaunchUpdater.setObjectName("OpenUpdater")
        self.LaunchUpdater.hide()
        self.LaunchUpdater.clicked.connect(lambda: self.LaunchUpdaterFunction())
        UpdateWindow.setFixedSize(UpdateWindow.size())
        UpdateWindow.setWindowFlags(UpdateWindow.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint & ~QtCore.Qt.WindowMinimizeButtonHint )

        try:
            LatestResponse = requests.get("https://api.github.com/repos/vazhka-dolya/katarakta/releases/latest")
            LatestVersion = LatestResponse.json()["name"]
            LatestBody = LatestResponse.json()["body"]
            if ("katarakta " + AppVersion) == LatestVersion:
                IsLatestVersion = True
            else:
                IsLatestVersion = False
        except:
            IsLatestVersion = "Unknown"
            LatestVersion = "Unknown"
            LatestBody = "Unknown"

        self.textBrowser.setHtml(QtCore.QCoreApplication.translate("UpdateWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n<html><head></head><body>{}</p></body></html>".format(str(LatestBody.replace("\r\n", "<br>"))), None))
        self.textBrowser.setMarkdown(QtCore.QCoreApplication.translate("UpdateWindow", LatestBody))
        
        self.retranslateUiEnglish(UpdateWindow)
        if Language.Properties_InnerName != "English":
            self.retranslateUiOther(UpdateWindow)
        self.Update()

        QtCore.QMetaObject.connectSlotsByName(UpdateWindow)
        
        try:
            UpdateWindow.setWindowIcon(QtGui.QIcon("resources/img/update64.png"))
        except:
            pass

        if Language.Properties_InnerName == "English":
            _translate = QtCore.QCoreApplication.translate
            self.retranslateUiEnglish(UpdateWindow)
            self.UpdateCheckLabel.setText("Update Checker")
            self.YourVersionLabel.setText("Your version: katarakta {}".format(str(AppVersion)))
            self.LatestVersionLabel.setText("Latest version on Github: {}".format(str(LatestVersion)))
            if IsLatestVersion == True:
                self.StatusLabel.setText("You have the latest version! <a href = 'https://github.com/vazhka-dolya/katarakta/releases'>All releases on GitHub</a>")
            elif IsLatestVersion == False:
                self.StatusLabel.setText("You have an outdated version!")
                self.LaunchUpdater.show()
            else:
                self.StatusLabel.setText("Could not check for the latest version. <a href = 'https://github.com/vazhka-dolya/katarakta/releases>All releases on GitHub</a>")
            self.textBrowserDescription.setText("Update's changelog:")
            self.LaunchUpdater.setText("Launch Updater")
            self.Update()

        else:
            _translate = QtCore.QCoreApplication.translate
            self.retranslateUiOther(UpdateWindow)
            self.UpdateCheckLabel.setText(Language.UW_UpdateCheckLabel)
            self.YourVersionLabel.setText("{} katarakta {}".format(Language.UW_YourVersionLabel, str(AppVersion)))
            self.LatestVersionLabel.setText("{} {}".format(Language.UW_LatestVersionLabel, str(LatestVersion)))
            if IsLatestVersion == True:
                self.StatusLabel.setText("{} <a href = 'https://github.com/vazhka-dolya/katarakta/releases'>{}</a>".format(Language.UW_VersionIsLatest, Language.UW_AllReleasesLink))
            elif IsLatestVersion == False:
                self.StatusLabel.setText(Language.UW_VersionIsOutdated)
                self.LaunchUpdater.show()
            else:
                self.StatusLabel.setText("{} <a href = 'https://github.com/vazhka-dolya/katarakta/releases'>{}</a>".format(Language.UW_VersionCannotCheck, Language.UW_AllReleasesLink))
            self.textBrowserDescription.setText(Language.UW_textBrowserDescription)
            self.LaunchUpdater.setText(Language.UW_LaunchUpdater)
            self.Update()
        
        QtCore.QMetaObject.connectSlotsByName(UpdateWindow)
        
        UpdateWindow.setWindowFlags(UpdateWindow.windowFlags() | Qt.WindowStaysOnTopHint)
        UpdateWindow.show()

    def LaunchUpdaterFunction(self):
        os.startfile("updater.exe")
        sys.exit(0)
        
    def Update(self):
        self.UpdateCheckLabel.adjustSize()
        self.YourVersionLabel.adjustSize()
        self.LatestVersionLabel.adjustSize()
        self.StatusLabel.adjustSize()
    
    def retranslateUiEnglish(self, UpdateWindow):
        _translate = QtCore.QCoreApplication.translate
        UpdateWindow.setWindowTitle(_translate("UpdateWindow", "Update check"))
    
    def retranslateUiOther(self, UpdateWindow):
        _translate = QtCore.QCoreApplication.translate
        UpdateWindow.setWindowTitle(_translate("UpdateWindow", Language.UW_Title))
    
class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        #.setFont(fontsmaller)

        SettingsWindow.resize(550, 520)
        SettingsWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.World))
        SettingsWindow.setFixedSize(SettingsWindow.size())
        SettingsWindow.setWindowIcon(QtGui.QIcon("resources/img/Settings.png"))
        SettingsWindow.setStyleSheet("font-size: 11px")

        self.tabWidget = QtWidgets.QTabWidget(SettingsWindow)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 531, 476))
        self.tabWidget.setObjectName("tabWidget")
        
        self.TabGeneral = QtWidgets.QWidget()
        self.TabGeneral.setObjectName("TabGeneral")
        
        self.groupLanguage = QtWidgets.QGroupBox(self.TabGeneral)
        self.groupLanguage.setGeometry(QtCore.QRect(10, 0, 506, 91))
        self.groupLanguage.setObjectName("groupLanguage")
        
        self.labelLanguage = QtWidgets.QLabel(self.groupLanguage)
        self.labelLanguage.setGeometry(QtCore.QRect(50, 14, 360, 31))
        self.labelLanguage.setStyleSheet("font-size: 16px")
        
        self.labelTranslator = QtWidgets.QLabel(self.groupLanguage)
        self.labelTranslator.setGeometry(QtCore.QRect(50, 33, 360, 31))
        self.labelTranslator.setObjectName("labelLanguage")
        
        self.labelLanguageRestart = QtWidgets.QLabel(self.groupLanguage)
        self.labelLanguageRestart.setGeometry(QtCore.QRect(256, 48, 290, 44))
        self.labelLanguageRestart.setObjectName("labelLanguageRestart")
        
        self.labelLanguageRevision = QtWidgets.QLabel(self.groupLanguage)
        self.labelLanguageRevision.setGeometry(QtCore.QRect(266, 5, 225, 44))
        self.labelLanguageRevision.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.labelLanguageRevision.setObjectName("labelLanguageRevision")
        
        self.labelLanguageMadeForVersion = QtWidgets.QLabel(self.groupLanguage)
        self.labelLanguageMadeForVersion.setGeometry(QtCore.QRect(266, 20, 225, 44))
        self.labelLanguageMadeForVersion.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.labelLanguageMadeForVersion.setObjectName("labelLanguageMadeForVersion")
        
        self.comboLanguage = QtWidgets.QComboBox(self.groupLanguage)
        self.comboLanguage.setGeometry(QtCore.QRect(10, 60, 241, 22))
        self.comboLanguage.setObjectName("comboLanguage")
        self.Model = QStandardItemModel()
        self.comboLanguage.setModel(self.Model)
        self.Delegate = AILanguageDelegate()
        self.comboLanguage.setItemDelegate(self.Delegate)

        global LangFolder
        LangFolder = "resources/lang/"
        global LanguageList
        LanguageList = os.listdir(LangFolder)
        
        _translate = QtCore.QCoreApplication.translate
        LangList = []
        for Index, _Language in enumerate(LanguageList):
            if not os.path.isdir(LangFolder + _Language):
                continue
            Config.read("{}{}/properties.ini".format(LangFolder, _Language), encoding = "utf-8")
            PropertiesConfig = Config["PROPERTIES"]
            DoNotDisplayName = ""
            DoNotDisplayName = PropertiesConfig.get("Properties_DoNotDisplay", DoNotDisplayName)
            if DoNotDisplayName == "0":
                LangList.append(_Language)
            
        for Index, _Language in enumerate(LangList):
            Item = QStandardItem("")
            Config.read("{}{}/properties.ini".format(LangFolder, _Language), encoding = "utf-8")
            PropertiesConfig = Config["PROPERTIES"]
            ItemName = ""
            ItemName = PropertiesConfig.get("Properties_Name", ItemName)
            Item.setText(ItemName)
            Item.setIcon(QIcon("{}{}/flag.png".format(LangFolder, _Language)))
            if PropertiesConfig.get("Properties_AI", "0") == "1":
                Item.setData(QIcon("resources/img/AI.png"), Qt.UserRole + 1)
            
            self.Model.appendRow(Item)

        self.labelFlagBackground = QtWidgets.QLabel(self.groupLanguage)
        self.labelFlagBackground.setGeometry(QtCore.QRect(7, 17, 37, 37))
        self.labelFlagBackground.setText("")
        self.labelFlagBackground.setScaledContents(True)
        self.labelFlagBackground.setObjectName("labelFlagBackground")
        if DarkMode == 1:
            self.labelFlagBackground.setPixmap(QtGui.QPixmap("resources/img/FlagBackground.png"))
        else:
            self.labelFlagBackground.hide()
        
        self.labelLanguageFlag = QtWidgets.QLabel(self.groupLanguage)
        self.labelLanguageFlag.setGeometry(QtCore.QRect(10, 20, 31, 31))
        self.labelLanguageFlag.setText("")
        self.labelLanguageFlag.setScaledContents(True)
        self.labelLanguageFlag.setObjectName("labelLanguageFlag")

        def FindLanguage():
            #print(Language.Properties_Name)
            #print(self.comboLanguage.findText(Language.Properties_Name, QtCore.Qt.MatchFixedString))
            self.comboLanguage.setCurrentIndex(self.comboLanguage.findText(Language.Properties_Name, QtCore.Qt.MatchFixedString))
        FindLanguage()

        def CheckLanguage():
            global ChosenLanguage
            
            #print(self.comboLanguage.currentIndex())
            #print(LanguageList[self.comboLanguage.currentIndex()])
            
            Config.read("{}{}/properties.ini".format(LangFolder, LangList[self.comboLanguage.currentIndex()]), encoding = "utf-8")
            PropertiesConfig = Config["PROPERTIES"]
            ItemInnerName = ""
            ItemInnerName = PropertiesConfig.get("Inner_Name", ItemInnerName)
            ItemName = ""
            ItemName = PropertiesConfig.get("Properties_Name", ItemName)
            ItemTranslator = ""
            ItemTranslator = PropertiesConfig.get("Properties_Translator", ItemTranslator)
            ItemRevision = ""
            ItemRevision = PropertiesConfig.get("Properties_Revision", ItemRevision)
            ItemVersion = ""
            ItemVersion = PropertiesConfig.get("Properties_MadeForVersion", ItemVersion)
            self.labelTranslator.setText("By: {}".format(ItemTranslator))
            self.labelLanguageRevision.setText("Language revision: {}".format(ItemRevision))
            self.labelLanguageMadeForVersion.setText("Made for version: {}".format(ItemVersion))
            if Language.Properties_InnerName != "English":
                if (ItemRevision == "") or (ItemRevision == None) or (ItemRevision == " "):
                    ItemRevision = Language.SW_Unspecified
                if (ItemVersion == "") or (ItemVersion == None) or (ItemVersion == " "):
                    ItemVersion = Language.SW_Unspecified
                if Language.SW_Translator != "":
                    self.labelTranslator.setText("{} {}".format(Language.SW_Translator, ItemTranslator))
                if Language.SW_labelLanguageRevision != "":
                    self.labelLanguageRevision.setText("{} {}".format(Language.SW_labelLanguageRevision, ItemRevision))
                if Language.SW_labelLanguageMadeForVersion != "":
                    self.labelLanguageMadeForVersion.setText("{} {}".format(Language.SW_labelLanguageMadeForVersion, ItemVersion))
            
            try:
                self.labelLanguageFlag.setPixmap(QtGui.QPixmap("{}{}/flag.png".format(LangFolder, LangList[self.comboLanguage.currentIndex()])))
            except:
                self.labelLanguageFlag.setPixmap(QtGui.QPixmap("resources/img/LangUnknown.png"))
                
            try:
                self.labelLanguage.setText(_translate("SettingsWindow", ItemName.format(LangFolder, LangList[self.comboLanguage.currentIndex()])))
            except:
                self.labelLanguage.setText(_translate("SettingsWindow", "Unknown"))

            ChosenLanguage = LangList[self.comboLanguage.currentIndex()]

        CheckLanguage()
        self.comboLanguage.currentIndexChanged.connect(CheckLanguage)
        
        self.groupUpdates = QtWidgets.QGroupBox(self.TabGeneral)
        self.groupUpdates.setGeometry(QtCore.QRect(10, 90, 506, 101))
        self.groupUpdates.setObjectName("groupBox")
        self.checkUpdates = QtWidgets.QCheckBox(self.groupUpdates)
        self.checkUpdates.setGeometry(QtCore.QRect(10, 20, 501, 17))
        self.checkUpdates.setObjectName("checkBox")
        self.labelUpdates = QtWidgets.QLabel(self.groupUpdates)
        self.labelUpdates.setGeometry(QtCore.QRect(10, 32, 501, 66))
        self.labelUpdates.setObjectName("labelUpdates")
        
        self.groupMisc = QtWidgets.QGroupBox(self.TabGeneral)
        self.groupMisc.setGeometry(QtCore.QRect(10, 190, 506, 241))
        self.groupMisc.setObjectName("groupMisc")
        self.checkStayOnTop = QtWidgets.QCheckBox(self.groupMisc)
        self.checkStayOnTop.setGeometry(QtCore.QRect(10, 20, 501, 17))
        self.checkStayOnTop.setObjectName("checkStayOnTop")
        self.CheckDoNotMoveSwitchVertically = QtWidgets.QCheckBox(self.groupMisc)
        self.CheckDoNotMoveSwitchVertically.setGeometry(QtCore.QRect(10, 41, 501, 17))
        self.CheckDoNotMoveSwitchVertically.setObjectName("CheckDoNotMoveSwitchVertically")
        self.CheckEyeBordersWarning = QtWidgets.QCheckBox(self.groupMisc)
        self.CheckEyeBordersWarning.setGeometry(QtCore.QRect(10, 62, 501, 17))
        self.CheckEyeBordersWarning.setObjectName("CheckEyeBordersWarning")

        if Option.StartUpCheckForUpdates == "1":
            self.checkUpdates.setChecked(True)

        def CheckStartUpCheckForUpdates():
            global StartUpCheckForUpdates
            if self.checkUpdates.isChecked() == True:
                StartUpCheckForUpdates = "1"
            else:
                StartUpCheckForUpdates = "0"
            return StartUpCheckForUpdates

        if Option.StartUpStayOnTop == "1":
            self.checkStayOnTop.setChecked(True)

        def CheckStartUpStayOnTop():
            global StartUpStayOnTop
            if self.checkStayOnTop.isChecked() == True:
                StartUpStayOnTop = "1"
            else:
                StartUpStayOnTop = "0"
            return StartUpStayOnTop
        
        if Option.DoNotMoveSwitchVertically == "1":
            self.CheckDoNotMoveSwitchVertically.setChecked(True)
        
        def CheckDoNotMoveSwitchVertically():
            global _DoNotMoveSwitchVertically
            if self.CheckDoNotMoveSwitchVertically.isChecked() == True:
                _DoNotMoveSwitchVertically = "1"
            else:
                _DoNotMoveSwitchVertically = "0"
            return _DoNotMoveSwitchVertically
        
        if Option.EyeBordersWarning == "1":
            self.CheckEyeBordersWarning.setChecked(True)
        
        def CheckEyeBordersWarning():
            global _EyeBordersWarning
            if self.CheckEyeBordersWarning.isChecked() == True:
                _EyeBordersWarning = "1"
            else:
                _EyeBordersWarning = "0"
            return _EyeBordersWarning
        
        self.tabWidget.addTab(self.TabGeneral, "")
        
        self.TabAppearance = QtWidgets.QWidget()
        self.TabAppearance.setObjectName("TabAppearance")
        
        self.groupEyeBG = QtWidgets.QGroupBox(self.TabAppearance)
        self.groupEyeBG.setGeometry(QtCore.QRect(10, 0, 506, 148))
        self.groupEyeBG.setObjectName("groupEyeBG")
        
        self.CheckTextureBorder = QtWidgets.QCheckBox(self.groupEyeBG)
        self.CheckTextureBorder.setGeometry(QtCore.QRect(10, 20, 501, 17))
        self.CheckTextureBorder.setObjectName("CheckTextureBorders")

        global BG_OptionMode
        BG_OptionMode = Option.BG_Mode

        global BG_OptionColor
        BG_OptionColor = Option.BG_Color

        global BG_OptionCheckerboard
        BG_OptionCheckerboard = Option.BG_Checkerboard

        global BG_OptionGradient1
        BG_OptionGradient1 = Option.BG_Gradient1

        global BG_OptionGradient2
        BG_OptionGradient2 = Option.BG_Gradient2

        self.BG_ButtonDefault = QtWidgets.QPushButton(self.groupEyeBG)
        self.BG_ButtonDefault.setObjectName("BG_ButtonDefault")
        self.BG_ButtonDefault.setGeometry(10, 65, 48, 48)
        self.BG_ButtonDefault.setCheckable(True)
        self.BG_ButtonDefault.toggled.connect(lambda: self.BG_CheckUncheck("default"))

        self.BG_ButtonCheckerboard = QtWidgets.QPushButton(self.groupEyeBG)
        self.BG_ButtonCheckerboard.setObjectName("BG_ButtonCheckerboard")
        self.BG_ButtonCheckerboard.setGeometry(self.BG_ButtonDefault.x() + 52, self.BG_ButtonDefault.y(), 48, 48)
        BG_CheckerboardPixmap = QPixmap(f"resources/img/TextureBackground{Option.BG_Checkerboard}")
        BG_CheckerboardPixmap = BG_CheckerboardPixmap.scaled(32, 32, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        self.BG_ButtonCheckerboard.setIcon(QtGui.QIcon(BG_CheckerboardPixmap))
        self.BG_ButtonCheckerboard.setIconSize(QSize(32, 32))
        self.BG_ButtonCheckerboard.setCheckable(True)
        self.BG_ButtonCheckerboard.toggled.connect(lambda: self.BG_CheckUncheck("checkerboard"))

        self.BG_MenuCheckerboard = QtWidgets.QMenu()
        self.BG_Checkerboard1 = QtWidgets.QAction()
        self.BG_Checkerboard1.setText("1")
        self.BG_Checkerboard1.setIcon(QIcon("resources/img/TextureBackground1.png"))
        self.BG_Checkerboard1.triggered.connect(lambda: BG_SetCheckerboard(self.BG_Checkerboard1.text()))
        self.BG_Checkerboard2 = QtWidgets.QAction()
        self.BG_Checkerboard2.setText("2")
        self.BG_Checkerboard2.setIcon(QIcon("resources/img/TextureBackground2.png"))
        self.BG_Checkerboard2.triggered.connect(lambda: BG_SetCheckerboard(self.BG_Checkerboard2.text()))
        self.BG_Checkerboard3 = QtWidgets.QAction()
        self.BG_Checkerboard3.setText("3")
        self.BG_Checkerboard3.setIcon(QIcon("resources/img/TextureBackground3.png"))
        self.BG_Checkerboard3.triggered.connect(lambda: BG_SetCheckerboard(self.BG_Checkerboard3.text()))
        self.BG_MenuCheckerboard.addAction(self.BG_Checkerboard1)
        self.BG_MenuCheckerboard.addAction(self.BG_Checkerboard2)
        self.BG_MenuCheckerboard.addAction(self.BG_Checkerboard3)

        self.BG_ButtonColor = QtWidgets.QPushButton(self.groupEyeBG)
        self.BG_ButtonColor.setObjectName("BG_ButtonColor")
        self.BG_ButtonColor.setGeometry(self.BG_ButtonCheckerboard.x() + 52, self.BG_ButtonDefault.y(), 48, 48)
        BG_ColorPixmap = QPixmap(32, 32)
        BG_ColorPixmap.fill(QtGui.QColor(Option.BG_Color))
        self.BG_ButtonColor.setIcon(QIcon(BG_ColorPixmap))
        self.BG_ButtonColor.setIconSize(QSize(32, 32))
        self.BG_ButtonColor.setCheckable(True)
        self.BG_ButtonColor.toggled.connect(lambda: self.BG_CheckUncheck("color"))

        self.BG_ButtonGradient = QtWidgets.QPushButton(self.groupEyeBG)
        self.BG_ButtonGradient.setObjectName("BG_ButtonGradient")
        self.BG_ButtonGradient.setGeometry(self.BG_ButtonColor.x() + 52, self.BG_ButtonDefault.y(), 48, 48)
        BG_GradientPixmap = QPixmap(32, 32)
        BG_GradientPainter = QtGui.QPainter(BG_GradientPixmap)
        BG_Gradient = QtGui.QLinearGradient(0, 0, BG_GradientPixmap.width(), 0)
        BG_Gradient.setColorAt(0, QColor(Option.BG_Gradient1))
        BG_Gradient.setColorAt(1, QColor(Option.BG_Gradient2))
        BG_GradientPainter.fillRect(BG_GradientPixmap.rect(), BG_Gradient)
        BG_GradientPainter.end()
        self.BG_ButtonGradient.setIcon(QIcon(BG_GradientPixmap))
        self.BG_ButtonGradient.setIconSize(QSize(32, 32))
        self.BG_ButtonGradient.setCheckable(True)
        self.BG_ButtonGradient.toggled.connect(lambda: self.BG_CheckUncheck("gradient"))

        self.BG_ButtonConfigure = QtWidgets.QPushButton(self.groupEyeBG)
        self.BG_ButtonConfigure.setObjectName("BG_ButtonConfigure")
        self.BG_ButtonConfigure.setGeometry(self.BG_ButtonDefault.x(), self.BG_ButtonDefault.y() + 52, 204, 23)
        self.BG_ButtonConfigure.clicked.connect(lambda: BG_Configure())

        self.BG_ButtonReset = QtWidgets.QPushButton(self.groupEyeBG)
        self.BG_ButtonReset.setObjectName("BG_ButtonReset")
        self.BG_ButtonReset.setGeometry(self.BG_ButtonDefault.x() + 208, self.BG_ButtonDefault.y() + 52, 100, 23)
        self.BG_ButtonReset.clicked.connect(lambda: BG_Reset())

        self.BG_Label = QtWidgets.QLabel(self.groupEyeBG)
        self.BG_Label.setObjectName("BG_Label")
        self.BG_Label.setGeometry(self.BG_ButtonDefault.x(), self.BG_ButtonDefault.y() - 24, 300, 23)

        if BG_OptionMode == "default":
            self.BG_ButtonDefault.setChecked(True)
            self.BG_ButtonCheckerboard.setChecked(False)
            self.BG_ButtonColor.setChecked(False)
            self.BG_ButtonGradient.setChecked(False)
            self.BG_ButtonConfigure.setEnabled(False)
            self.BG_ButtonConfigure.setMenu(None)
        elif BG_OptionMode == "checkerboard":
            self.BG_ButtonDefault.setChecked(False)
            self.BG_ButtonCheckerboard.setChecked(True)
            self.BG_ButtonColor.setChecked(False)
            self.BG_ButtonGradient.setChecked(False)
            self.BG_ButtonConfigure.setEnabled(True)
            self.BG_ButtonConfigure.setMenu(self.BG_MenuCheckerboard)
        elif BG_OptionMode == "color":
            self.BG_ButtonDefault.setChecked(False)
            self.BG_ButtonCheckerboard.setChecked(False)
            self.BG_ButtonColor.setChecked(True)
            self.BG_ButtonGradient.setChecked(False)
            self.BG_ButtonConfigure.setEnabled(True)
            self.BG_ButtonConfigure.setMenu(None)
        elif BG_OptionMode == "gradient":
            self.BG_ButtonDefault.setChecked(False)
            self.BG_ButtonCheckerboard.setChecked(False)
            self.BG_ButtonColor.setChecked(False)
            self.BG_ButtonGradient.setChecked(True)
            self.BG_ButtonConfigure.setEnabled(True)
            self.BG_ButtonConfigure.setMenu(None)
        else:
            self.BG_ButtonDefault.setChecked(True)
            self.BG_ButtonCheckerboard.setChecked(False)
            self.BG_ButtonColor.setChecked(False)
            self.BG_ButtonGradient.setChecked(False)
            self.BG_ButtonConfigure.setEnabled(False)
            self.BG_ButtonConfigure.setMenu(None)

        self.signal_blocked = False

        def BG_Reset():
            if self.signal_blocked:
                return

            self.signal_blocked = True

            global BG_OptionMode
            global BG_OptionColor
            global BG_OptionCheckerboard
            global BG_OptionGradient1
            global BG_OptionGradient2
            
            self.BG_CheckUncheck("color")

            self.BG_ButtonDefault.setChecked(False)
            self.BG_ButtonCheckerboard.setChecked(False)
            self.BG_ButtonColor.setChecked(True)
            self.BG_ButtonGradient.setChecked(False)

            BG_OptionMode = "color"
            BG_OptionColor = "#AAAAAA"
            BG_OptionCheckerboard = "1"
            BG_OptionGradient1 = "#7F603C"
            BG_OptionGradient2 = "#FEC179"

            BG_ColorPixmap = QPixmap(32, 32)
            BG_ColorPixmap.fill(QtGui.QColor(BG_OptionColor))
            self.BG_ButtonColor.setIcon(QIcon(BG_ColorPixmap))
            self.BG_ButtonColor.setIconSize(QSize(32, 32))

            BG_CheckerboardPixmap = QPixmap(f"resources/img/TextureBackground{BG_OptionCheckerboard}.png")
            BG_CheckerboardPixmap = BG_CheckerboardPixmap.scaled(32, 32, Qt.IgnoreAspectRatio, Qt.FastTransformation)
            self.BG_ButtonCheckerboard.setIcon(QtGui.QIcon(BG_CheckerboardPixmap))
            self.BG_ButtonCheckerboard.setIconSize(QSize(32, 32))

            BG_GradientPixmap = QPixmap(32, 32)
            BG_GradientPainter = QtGui.QPainter(BG_GradientPixmap)
            BG_Gradient = QtGui.QLinearGradient(0, 0, BG_GradientPixmap.width(), 0)
            BG_Gradient.setColorAt(0, QColor(BG_OptionGradient1))
            BG_Gradient.setColorAt(1, QColor(BG_OptionGradient2))
            BG_GradientPainter.fillRect(BG_GradientPixmap.rect(), BG_Gradient)
            BG_GradientPainter.end()
            self.BG_ButtonGradient.setIcon(QIcon(BG_GradientPixmap))
            self.BG_ButtonGradient.setIconSize(QSize(32, 32))

            self.signal_blocked = False

        def BG_SetCheckerboard(TextureNumber):
            global BG_OptionCheckerboard

            if self.signal_blocked:
                return

            self.signal_blocked = True

            BG_CheckerboardPixmap = QPixmap(f"resources/img/TextureBackground{TextureNumber}.png")
            BG_CheckerboardPixmap = BG_CheckerboardPixmap.scaled(32, 32, Qt.IgnoreAspectRatio, Qt.FastTransformation)
            self.BG_ButtonCheckerboard.setIcon(QtGui.QIcon(BG_CheckerboardPixmap))
            self.BG_ButtonCheckerboard.setIconSize(QSize(32, 32))
            BG_OptionCheckerboard = TextureNumber

            self.signal_blocked = False

        def BG_ShowContextMenu(Mode):
            if self.signal_blocked:
                return

            self.signal_blocked = True

            if Mode == "checkerboard":
                self.BG_MenuCheckerboard.exec(self.BG_ButtonConfigure.mapToGlobal(QtCore.QPoint(0, 0)))

            self.signal_blocked = False

        def BG_Configure():
            if self.signal_blocked:
                return

            self.signal_blocked = True

            if self.BG_ButtonDefault.isChecked() == True:
                pass
            
            elif self.BG_ButtonCheckerboard.isChecked() == True:
                pass
                #self.BG_ButtonConfigure.showMenu(self.BG_MenuCheckerboard)
                #self.BG_ButtonConfigure.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
                #self.BG_ButtonConfigure.customContextMenuRequested.connect(lambda: BG_ShowContextMenu("checkerboard"))

            elif self.BG_ButtonColor.isChecked() == True:
                global BG_OptionColor
                BG_NewColor = QtWidgets.QColorDialog.getColor(initial = QtGui.QColor(Option.BG_Color))
                if QtGui.QColor(BG_NewColor).isValid() == False:
                    BG_NewColor = Option.BG_Color
                BG_ColorPixmap = QPixmap(32, 32)
                BG_ColorPixmap.fill(QtGui.QColor(BG_NewColor)) #QtGui.QColor(Option.BG_Color)
                self.BG_ButtonColor.setIcon(QIcon(BG_ColorPixmap)) #QIcon(BG_ColorPixmap)
                self.BG_ButtonColor.setIconSize(QSize(32, 32))
                if QtGui.QColor(BG_NewColor).isValid() == True:
                    try:
                        BG_OptionColor = BG_NewColor.name(QColor.HexRgb).upper()
                    except:
                        pass

            elif self.BG_ButtonGradient.isChecked() == True:
                global BG_OptionGradient1
                global BG_OptionGradient2

                BG_NewGradient1 = QtWidgets.QColorDialog.getColor(initial = QtGui.QColor(Option.BG_Gradient1))
                if QtGui.QColor(BG_NewGradient1).isValid() == False:
                    BG_NewGradient1 = Option.BG_Gradient1
                BG_NewGradient2 = QtWidgets.QColorDialog.getColor(initial = QtGui.QColor(Option.BG_Gradient2))
                if QtGui.QColor(BG_NewGradient2).isValid() == False:
                    BG_NewGradient2 = Option.BG_Gradient2
                BG_GradientPixmap = QPixmap(32, 32)
                BG_GradientPainter = QtGui.QPainter(BG_GradientPixmap)
                BG_Gradient = QtGui.QLinearGradient(0, 0, BG_GradientPixmap.width(), 0)
                BG_Gradient.setColorAt(0, QColor(BG_NewGradient1))
                BG_Gradient.setColorAt(1, QColor(BG_NewGradient2))
                BG_GradientPainter.fillRect(BG_GradientPixmap.rect(), BG_Gradient)
                BG_GradientPainter.end()
                self.BG_ButtonGradient.setIcon(QIcon(BG_GradientPixmap))
                self.BG_ButtonGradient.setIconSize(QSize(32, 32))
                if QtGui.QColor(BG_NewGradient1).isValid() == True:
                    try:
                        BG_OptionGradient1 = BG_NewGradient1.name(QColor.HexRgb).upper()
                    except:
                        pass
                if QtGui.QColor(BG_NewGradient2).isValid() == True:
                    try:
                        BG_OptionGradient2 = BG_NewGradient2.name(QColor.HexRgb).upper()
                    except:
                        pass

            else:
                pass

            self.signal_blocked = False
        
        self.groupEyeList = QtWidgets.QGroupBox(self.TabAppearance)
        self.groupEyeList.setGeometry(QtCore.QRect(10, 148, 506, 168))
        self.groupEyeList.setObjectName("groupEyeList")
        
        self.CheckEyeListIcons = QtWidgets.QCheckBox(self.groupEyeList)
        self.CheckEyeListIcons.setGeometry(QtCore.QRect(10, 20, 501, 17))
        self.CheckEyeListIcons.setObjectName("CheckEyeListIcons")
        self.CheckEyeListIcons.stateChanged.connect(self.DemoSetIcons)
        
        self.CheckEyeListIconBG = QtWidgets.QCheckBox(self.groupEyeList)
        self.CheckEyeListIconBG.setGeometry(QtCore.QRect(10, 40, 501, 17))
        self.CheckEyeListIconBG.setObjectName("CheckEyeListIconBG")
        self.CheckEyeListIconBG.stateChanged.connect(self.DemoSetIcons)
        
        self.SpinEyeListRowHeight = QtWidgets.QSpinBox(self.groupEyeList)
        self.SpinEyeListRowHeight.setGeometry(QtCore.QRect(10, 128, 50, 30))
        self.SpinEyeListRowHeight.setObjectName("SpinEyeListRowHeight")
        self.SpinEyeListRowHeight.setMinimum(-9)
        self.SpinEyeListRowHeight.setMaximum(999)
        self.SpinEyeListRowHeight.textChanged.connect(self.DemoSetRowHeight)
        
        self.DemoSetIcons
        
        self.LabelEyeListWarning = QtWidgets.QLabel(self.groupEyeList)
        self.LabelEyeListWarning.setObjectName("LabelEyeListWarning")
        self.LabelEyeListWarning.setGeometry(QtCore.QRect(10, 60, 288, 60))
        
        self.LabelEyeListDemo = QtWidgets.QLabel(self.groupEyeList)
        self.LabelEyeListDemo.setObjectName("LabelEyeListDemo")
        self.LabelEyeListDemo.setGeometry(QtCore.QRect(308, 10, 288, 25))
        
        self.LabelRowHeight = QtWidgets.QLabel(self.groupEyeList)
        self.LabelRowHeight.setObjectName("LabelRowHeight")
        self.LabelRowHeight.setGeometry(QtCore.QRect(65, 128, 208, 30))
        
        self.EyeListDemo = QtWidgets.QTreeWidget(self.groupEyeList)
        self.EyeListDemo.setGeometry(QtCore.QRect(308, 40, 188, 118))
        for i in range(1, self.EyeListDemo.model().columnCount()):
            self.EyeListDemo.header().hideSection(i)
        self.EyeListDemo.header().setStretchLastSection(False)
        self.EyeListDemo.header().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.EyeListDemo.setHeaderHidden(True)
        fontNine = QtGui.QFont()
        fontNine.setPointSize(9)
        self.EyeListDemo.setFont(fontNine)
        
        self.DemoItem1 = QtWidgets.QTreeWidgetItem(self.EyeListDemo)
        self.DemoItem1.setText(0, QtCore.QCoreApplication.translate("MainWindow", u"Angry", None))
        self.DemoItem2 = QtWidgets.QTreeWidgetItem(self.DemoItem1)
        self.DemoItem2.setText(0, QtCore.QCoreApplication.translate("MainWindow", u"Looking Left", None))
        self.DemoItem3 = QtWidgets.QTreeWidgetItem(self.DemoItem1)
        self.DemoItem3.setText(0, QtCore.QCoreApplication.translate("MainWindow", u"Looking Right", None))
        self.DemoItem4 = QtWidgets.QTreeWidgetItem(self.EyeListDemo)
        self.DemoItem4.setText(0, QtCore.QCoreApplication.translate("MainWindow", u"Derp", None))
        self.DemoItem5 = QtWidgets.QTreeWidgetItem(self.EyeListDemo)
        self.DemoItem5.setText(0, QtCore.QCoreApplication.translate("MainWindow", u"Happy", None))
        self.DemoItem6 = QtWidgets.QTreeWidgetItem(self.EyeListDemo)
        self.DemoItem6.setText(0, QtCore.QCoreApplication.translate("MainWindow", u"Sad", None))
        self.DemoItem7 = QtWidgets.QTreeWidgetItem(self.EyeListDemo)
        self.DemoItem7.setText(0, QtCore.QCoreApplication.translate("MainWindow", u"Surprised or Scared", None))
        self.DemoItem8 = QtWidgets.QTreeWidgetItem(self.DemoItem7)
        self.DemoItem8.setText(0, QtCore.QCoreApplication.translate("MainWindow", u"Looking Left", None))
        self.DemoItem9 = QtWidgets.QTreeWidgetItem(self.DemoItem7)
        self.DemoItem9.setText(0, QtCore.QCoreApplication.translate("MainWindow", u"Looking Right", None))
        
        def CheckTextureBorder():
            global _TextureBorder
            if self.CheckTextureBorder.isChecked() == True:
                _TextureBorder = "1"
            else:
                _TextureBorder = "0"
            return _TextureBorder
        
        if Option.TextureBorder == "1":
            self.CheckTextureBorder.setChecked(True)
            
            
        
        def CheckEyeListIcons():
            global _EyeListIcons
            if self.CheckEyeListIcons.isChecked() == True:
                _EyeListIcons = "1"
            else:
                _EyeListIcons = "0"
            return _EyeListIcons
        
        if Option.EyeListIcons == "1":
            self.CheckEyeListIcons.setChecked(True)
            
            
        
        def CheckEyeListIconBG():
            global _EyeListIconBG
            if self.CheckEyeListIconBG.isChecked() == True:
                _EyeListIconBG = "1"
            else:
                _EyeListIconBG = "0"
            return _EyeListIconBG
        
        if Option.EyeListIconBG == "1":
            self.CheckEyeListIconBG.setChecked(True)
            
            
        
        def SpinEyeListRowHeight():
            global _EyeListRowHeight
            _EyeListRowHeight = str(self.SpinEyeListRowHeight.value())
            return _EyeListRowHeight
        
        self.SpinEyeListRowHeight.setValue(int(Option.EyeListRowHeight))
        
        
        
        self.tabWidget.addTab(self.TabAppearance, "")
        
        self.TabTextures = QtWidgets.QWidget()
        self.TabTextures.setObjectName("TabTextures")
        
        self.lineHiResSM64 = QtWidgets.QLineEdit(self.TabTextures)
        self.lineHiResSM64.setGeometry(QtCore.QRect(30, 30, 486, 20))
        self.lineHiResSM64.setObjectName("lineHiResSM64")
        self.lineHiResSM64.setText(str(Option.HiResDir))
        self.labelHiResSM64 = QtWidgets.QLabel(self.TabTextures)
        self.labelHiResSM64.setGeometry(QtCore.QRect(10, 10, 201, 16))
        self.labelHiResSM64.setObjectName("labelHiResSM64")
        
        self.groupSM64 = QtWidgets.QGroupBox(self.TabTextures)
        self.groupSM64.setGeometry(QtCore.QRect(10, 60, 251, 311))
        self.groupSM64.setObjectName("groupSM64")
        
        self.labelEyesOpen = QtWidgets.QLabel(self.groupSM64)
        self.labelEyesOpen.setGeometry(QtCore.QRect(10, 20, 231, 16))
        self.labelEyesOpen.setObjectName("labelEyesOpen")
        
        self.labelEyesHalfopen = QtWidgets.QLabel(self.groupSM64)
        self.labelEyesHalfopen.setGeometry(QtCore.QRect(10, 60, 231, 16))
        self.labelEyesHalfopen.setObjectName("labelEyesHalfopen")
        
        self.labelEyesClosed = QtWidgets.QLabel(self.groupSM64)
        self.labelEyesClosed.setGeometry(QtCore.QRect(10, 100, 231, 16))
        self.labelEyesClosed.setObjectName("labelEyesClosed")
        
        self.labelCap = QtWidgets.QLabel(self.groupSM64)
        self.labelCap.setGeometry(QtCore.QRect(10, 140, 231, 16))
        self.labelCap.setObjectName("labelCap")
        
        self.labelSidehair = QtWidgets.QLabel(self.groupSM64)
        self.labelSidehair.setGeometry(QtCore.QRect(10, 180, 231, 16))
        self.labelSidehair.setObjectName("labelSidehair")
        
        self.labelMustache = QtWidgets.QLabel(self.groupSM64)
        self.labelMustache.setGeometry(QtCore.QRect(10, 220, 231, 16))
        self.labelMustache.setObjectName("labelMustache")
        
        self.labelButton = QtWidgets.QLabel(self.groupSM64)
        self.labelButton.setGeometry(QtCore.QRect(10, 260, 231, 16))
        self.labelButton.setObjectName("labelButton")
        
        self.lineEyesOpen = QtWidgets.QLineEdit(self.groupSM64)
        self.lineEyesOpen.setGeometry(QtCore.QRect(10, 40, 231, 20))
        self.lineEyesOpen.setObjectName("lineEyesOpen")
        self.lineEyesOpen.setText(str(Option.Eyes1))
        
        self.lineEyesHalfopen = QtWidgets.QLineEdit(self.groupSM64)
        self.lineEyesHalfopen.setGeometry(QtCore.QRect(10, 80, 231, 20))
        self.lineEyesHalfopen.setObjectName("lineEyesHalfopen")
        self.lineEyesHalfopen.setText(str(Option.Eyes2))
        
        self.lineEyesClosed = QtWidgets.QLineEdit(self.groupSM64)
        self.lineEyesClosed.setGeometry(QtCore.QRect(10, 120, 231, 20))
        self.lineEyesClosed.setObjectName("lineEyesClosed")
        self.lineEyesClosed.setText(str(Option.Eyes3))
        
        self.lineCap = QtWidgets.QLineEdit(self.groupSM64)
        self.lineCap.setGeometry(QtCore.QRect(10, 160, 231, 20))
        self.lineCap.setObjectName("lineCap")
        self.lineCap.setText(str(Option.Cap))
        
        self.lineSidehair = QtWidgets.QLineEdit(self.groupSM64)
        self.lineSidehair.setGeometry(QtCore.QRect(10, 200, 231, 20))
        self.lineSidehair.setObjectName("lineSidehair")
        self.lineSidehair.setText(str(Option.Hair))
        
        self.lineMustache = QtWidgets.QLineEdit(self.groupSM64)
        self.lineMustache.setGeometry(QtCore.QRect(10, 240, 231, 20))
        self.lineMustache.setObjectName("lineMustache")
        self.lineMustache.setText(str(Option.Mustache))
        
        self.lineButton = QtWidgets.QLineEdit(self.groupSM64)
        self.lineButton.setGeometry(QtCore.QRect(10, 280, 231, 20))
        self.lineButton.setObjectName("lineButton")
        self.lineButton.setText(str(Option.Button))
        
        self.groupNames = QtWidgets.QGroupBox(self.TabTextures)
        self.groupNames.setGeometry(QtCore.QRect(265, 60, 251, 371))
        self.groupNames.setObjectName("groupNames")
        
        self.labelSM64Name = QtWidgets.QLabel(self.groupNames)
        self.labelSM64Name.setGeometry(QtCore.QRect(10, 20, 231, 16))
        self.labelSM64Name.setObjectName("labelSM64Name")
        
        self.lineSM64Name = QtWidgets.QLineEdit(self.groupNames)
        self.lineSM64Name.setGeometry(QtCore.QRect(10, 40, 231, 20))
        self.lineSM64Name.setObjectName("SM64Name")
        self.lineSM64Name.setText(str(Option.SM64Name))
        
        self.labelAddNames = QtWidgets.QLabel(self.groupNames)
        self.labelAddNames.setGeometry(QtCore.QRect(10, 60, 231, 16))
        self.labelAddNames.setObjectName("labelAddNames")
        
        self.TextAddNames = QtWidgets.QTextEdit(self.groupNames)
        self.TextAddNames.setGeometry(QtCore.QRect(10, 80, 231, 280))
        self.TextAddNames.setObjectName("TextAddNames")
        self.TextAddNames.setText(str(Option.AddNames))

        self.ToolTipPath = QtWidgets.QLabel(self.TabTextures)
        self.ToolTipPath.setGeometry(QtCore.QRect(10, 32, 16, 16))
        self.ToolTipPath.setObjectName("ToolTipPath")
        self.ToolTipPath.setPixmap(QPixmap("resources/img/ToolTip.png"))
        self.ToolTipPath.setScaledContents(True)

        self.ToolTipMainTextureNames = QtWidgets.QLabel(self.groupSM64)
        self.ToolTipMainTextureNames.setGeometry(QtCore.QRect(217, 13, 24, 24))
        self.ToolTipMainTextureNames.setObjectName("ToolTipMainTextureNames")
        self.ToolTipMainTextureNames.setPixmap(QPixmap("resources/img/ToolTip.png"))
        self.ToolTipMainTextureNames.setScaledContents(True)

        self.ToolTipGameNames = QtWidgets.QLabel(self.groupNames)
        self.ToolTipGameNames.setGeometry(QtCore.QRect(217, 13, 24, 24))
        self.ToolTipGameNames.setObjectName("ToolTipGameNames")
        self.ToolTipGameNames.setPixmap(QPixmap("resources/img/ToolTip.png"))
        self.ToolTipGameNames.setScaledContents(True)
        
        self.tabWidget.addTab(self.TabTextures, "")

        def CloseSettings():
            SettingsWindow.close()
        
        self.pushClose = QtWidgets.QPushButton(SettingsWindow)
        self.pushClose.setGeometry(QtCore.QRect(460, 490, 75, 23))
        self.pushClose.setObjectName("pushClose")
        self.pushClose.clicked.connect(CloseSettings)

        def CollectLineText():
            global CollectedLineHiResSM64, CollectedLineSM64Name, CollectedLineAddNames, CollectedLineEyesOpen, CollectedLineEyesHalfopen, CollectedLineEyesClosed, CollectedLineCap, CollectedLineSidehair, CollectedLineMustache, CollectedLineButton
            
            CollectedLineHiResSM64 = str(self.lineHiResSM64.text())
            CollectedLineSM64Name = str(self.lineSM64Name.text())
            CollectedLineAddNames = str(self.TextAddNames.toPlainText())
            
            CollectedLineEyesOpen = str(self.lineEyesOpen.text())
            CollectedLineEyesHalfopen = str(self.lineEyesHalfopen.text())
            CollectedLineEyesClosed = str(self.lineEyesClosed.text())
            CollectedLineCap = str(self.lineCap.text())
            CollectedLineSidehair = str(self.lineSidehair.text())
            CollectedLineMustache = str(self.lineMustache.text())
            CollectedLineButton = str(self.lineButton.text())

            return CollectedLineHiResSM64, CollectedLineSM64Name, CollectedLineAddNames, CollectedLineEyesOpen, CollectedLineEyesHalfopen, CollectedLineEyesClosed, CollectedLineCap, CollectedLineSidehair, CollectedLineMustache, CollectedLineButton

        
        def Apply():
            global BG_OptionMode
            if os.path.exists("config.ini") is True:
                pass
            else:
                CreateConfig()
                
            CollectLineText()
            CheckLanguage()
            CheckStartUpCheckForUpdates()
            CheckStartUpStayOnTop()
            CheckDoNotMoveSwitchVertically()
            CheckEyeBordersWarning()
            CheckTextureBorder()
            CheckEyeListIconBG()
            CheckEyeListIcons()
            SpinEyeListRowHeight()
            Config = configparser.ConfigParser()
            Config.read("config.ini", encoding = "utf-8")

            Config.set("PATHS", "HiResDir", CollectedLineHiResSM64)
            Config.set("PATHS", "SM64Name", CollectedLineSM64Name)
            Config.set("PATHS", "AddNames", CollectedLineAddNames)
            
            Config.set("PATHS", "Eyes1", CollectedLineEyesOpen)
            Config.set("PATHS", "Eyes2", CollectedLineEyesHalfopen)
            Config.set("PATHS", "Eyes3", CollectedLineEyesClosed)
            Config.set("PATHS", "Cap", CollectedLineCap)
            Config.set("PATHS", "Hair", CollectedLineSidehair)
            Config.set("PATHS", "Mustache", CollectedLineMustache)
            Config.set("PATHS", "Button", CollectedLineButton)
            
            Config.set("OPTIONS", "Language", ChosenLanguage)
            Config.set("OPTIONS", "StartUpCheckForUpdates", StartUpCheckForUpdates)
            Config.set("OPTIONS", "StartUpStayOnTop", StartUpStayOnTop)
            Config.set("OPTIONS", "DoNotMoveSwitchVertically", _DoNotMoveSwitchVertically)
            Config.set("OPTIONS", "EyeBordersWarning", _EyeBordersWarning)
            Config.set("OPTIONS", "TextureBorder", _TextureBorder)
            Config.set("OPTIONS", "BG_Mode", BG_OptionMode)
            Config.set("OPTIONS", "BG_Color", BG_OptionColor)
            Config.set("OPTIONS", "BG_Checkerboard", BG_OptionCheckerboard)
            Config.set("OPTIONS", "BG_Gradient1", BG_OptionGradient1)
            Config.set("OPTIONS", "BG_Gradient2", BG_OptionGradient2)
            Config.set("OPTIONS", "EyeListIcons", _EyeListIcons)
            Config.set("OPTIONS", "EyeListIconBG", _EyeListIconBG)
            Config.set("OPTIONS", "EyeListRowHeight", _EyeListRowHeight)
            
            with open("config.ini", "w") as ConfigFile:
                Config.write(ConfigFile)

            LoadConfig()

            Option.TextureBorder = _TextureBorder
            Option.BG_Mode = BG_OptionMode
            Option.BG_Color = BG_OptionColor
            Option.BG_Checkerboard = BG_OptionCheckerboard
            Option.BG_Gradient1 = BG_OptionGradient1
            Option.BG_Gradient2 = BG_OptionGradient2
            Option.EyeListIcons = _EyeListIcons
            Option.EyeListIconBG = _EyeListIconBG
            Option.EyeListRowHeight = _EyeListRowHeight

            MainWindow.RefreshEyeList()
        
        self.pushApply = QtWidgets.QPushButton(SettingsWindow)
        self.pushApply.setGeometry(QtCore.QRect(370, 490, 85, 23))
        self.pushApply.setObjectName("pushApply")
        self.pushApply.clicked.connect(Apply)

        def ApplyClose():
            Apply()
            SettingsWindow.close()
        
        self.pushApplyClose = QtWidgets.QPushButton(SettingsWindow)
        self.pushApplyClose.setGeometry(QtCore.QRect(210, 490, 155, 23))
        self.pushApplyClose.setObjectName("pushApplyClose")
        self.pushApplyClose.clicked.connect(ApplyClose)

        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SettingsWindow)

        self.retranslateUiEnglish(SettingsWindow)
        if Language.Properties_InnerName != "English":
            self.retranslateUiOther(SettingsWindow)
            
        self.checkUpdates.adjustSize()
        self.checkStayOnTop.adjustSize()
    
    def DemoSetIcons(self):
        DemoPixmapSet = ["resources/img/Demo/DemoAngry.png", "resources/img/Demo/DemoAngryLeft.png", "resources/img/Demo/DemoAngryRight.png", "resources/img/Demo/DemoDerp.png", "resources/img/Demo/DemoHappy.png", "resources/img/Demo/DemoSad.png", "resources/img/Demo/DemoSurprisedScared.png", "resources/img/Demo/DemoSurprisedScaredLeft.png", "resources/img/Demo/DemoSurprisedScaredRight.png"]
        if self.CheckEyeListIcons.isChecked() == True:
            if self.CheckEyeListIconBG.isChecked() == True:
                DemoPixmapSetBG = []
                for i in DemoPixmapSet:
                    ColorDemoIcon = QtGui.QPixmap(QPixmap(i).size())
                    ColorDemoIcon.fill(QtGui.QColor(Option.BG_Color))
                    DemoIconPainter = QtGui.QPainter(ColorDemoIcon)
                    DemoIconPainter.drawPixmap(0, 0, QPixmap(i))
                    DemoIconPainter.end()
                    DemoPixmapSetBG.append(ColorDemoIcon)
                self.DemoItem1.setIcon(0, QIcon(DemoPixmapSetBG[0]))
                self.DemoItem2.setIcon(0, QIcon(DemoPixmapSetBG[1]))
                self.DemoItem3.setIcon(0, QIcon(DemoPixmapSetBG[2]))
                self.DemoItem4.setIcon(0, QIcon(DemoPixmapSetBG[3]))
                self.DemoItem5.setIcon(0, QIcon(DemoPixmapSetBG[4]))
                self.DemoItem6.setIcon(0, QIcon(DemoPixmapSetBG[5]))
                self.DemoItem7.setIcon(0, QIcon(DemoPixmapSetBG[6]))
                self.DemoItem8.setIcon(0, QIcon(DemoPixmapSetBG[7]))
                self.DemoItem9.setIcon(0, QIcon(DemoPixmapSetBG[8]))
            else:
                self.DemoItem1.setIcon(0, QIcon(DemoPixmapSet[0]))
                self.DemoItem2.setIcon(0, QIcon(DemoPixmapSet[1]))
                self.DemoItem3.setIcon(0, QIcon(DemoPixmapSet[2]))
                self.DemoItem4.setIcon(0, QIcon(DemoPixmapSet[3]))
                self.DemoItem5.setIcon(0, QIcon(DemoPixmapSet[4]))
                self.DemoItem6.setIcon(0, QIcon(DemoPixmapSet[5]))
                self.DemoItem7.setIcon(0, QIcon(DemoPixmapSet[6]))
                self.DemoItem8.setIcon(0, QIcon(DemoPixmapSet[7]))
                self.DemoItem9.setIcon(0, QIcon(DemoPixmapSet[8]))
        else:
            self.DemoItem1.setIcon(0, QIcon())
            self.DemoItem2.setIcon(0, QIcon())
            self.DemoItem3.setIcon(0, QIcon())
            self.DemoItem4.setIcon(0, QIcon())
            self.DemoItem5.setIcon(0, QIcon())
            self.DemoItem6.setIcon(0, QIcon())
            self.DemoItem7.setIcon(0, QIcon())
            self.DemoItem8.setIcon(0, QIcon())
            self.DemoItem9.setIcon(0, QIcon())
            
    def DemoSetRowHeight(self):
        self.EyeListDemo.setStyleSheet("QTreeView::item { padding: "+str(self.SpinEyeListRowHeight.value())+"px }")
    
    def BG_CheckUncheck(self, Mode):
        global BG_OptionMode
        try:
            if self.signal_blocked:
                return

            self.signal_blocked = True

        except:
            pass

        if Mode == "default":
            self.BG_ButtonDefault.setChecked(True)
            self.BG_ButtonCheckerboard.setChecked(False)
            self.BG_ButtonColor.setChecked(False)
            self.BG_ButtonGradient.setChecked(False)
            self.BG_ButtonConfigure.setEnabled(False)
            self.BG_ButtonConfigure.setMenu(None)
            BG_OptionMode = Mode
        elif Mode == "checkerboard":
            self.BG_ButtonDefault.setChecked(False)
            self.BG_ButtonCheckerboard.setChecked(True)
            self.BG_ButtonColor.setChecked(False)
            self.BG_ButtonGradient.setChecked(False)
            self.BG_ButtonConfigure.setEnabled(True)
            self.BG_ButtonConfigure.setMenu(self.BG_MenuCheckerboard)
            BG_OptionMode = Mode
        elif Mode == "color":
            self.BG_ButtonDefault.setChecked(False)
            self.BG_ButtonCheckerboard.setChecked(False)
            self.BG_ButtonColor.setChecked(True)
            self.BG_ButtonGradient.setChecked(False)
            self.BG_ButtonConfigure.setEnabled(True)
            self.BG_ButtonConfigure.setMenu(None)
            BG_OptionMode = Mode
        elif Mode == "gradient":
            self.BG_ButtonDefault.setChecked(False)
            self.BG_ButtonCheckerboard.setChecked(False)
            self.BG_ButtonColor.setChecked(False)
            self.BG_ButtonGradient.setChecked(True)
            self.BG_ButtonConfigure.setEnabled(True)
            self.BG_ButtonConfigure.setMenu(None)
            BG_OptionMode = Mode
        else:
            self.BG_ButtonDefault.setChecked(True)
            self.BG_ButtonCheckerboard.setChecked(False)
            self.BG_ButtonColor.setChecked(False)
            self.BG_ButtonGradient.setChecked(False)
            self.BG_ButtonConfigure.setEnabled(False)
            self.BG_ButtonConfigure.setMenu(None)
            BG_OptionMode = "default"

        try:
            self.signal_blocked = False
        except:
            pass
        
        return BG_OptionMode

    def retranslateUiEnglish(self, SettingsWindow):
        _translate = QtCore.QCoreApplication.translate
        SettingsWindow.setWindowTitle(_translate("SettingsWindow", "Settings"))
        self.groupLanguage.setTitle(_translate("SettingsWindow", "Language"))
        self.labelLanguageRestart.setText(_translate("SettingsWindow", "(requires restarting katarakta to fully work)"))
        self.groupUpdates.setTitle(_translate("SettingsWindow", "Updates"))
        self.checkUpdates.setText(_translate("SettingsWindow", "Check for updates on startup"))
        self.labelUpdates.setText(_translate("SettingsWindow", "Keep this checked to get notified about any new updates to\nkatarakta on startup.\n"
"\n"
"If you discover an issue, then, before reporting it, make sure you are on the latest version."))
        self.groupMisc.setTitle(_translate("SettingsWindow", "Miscellaneous"))
        self.checkStayOnTop.setText(_translate("SettingsWindow", "Enable Stay on Top on startup"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TabGeneral), _translate("SettingsWindow", "General"))
        self.labelHiResSM64.setText(_translate("SettingsWindow", "Hi-res folder:"))
        self.groupSM64.setTitle(_translate("SettingsWindow", "Main textures"))
        self.labelEyesOpen.setText(_translate("SettingsWindow", "Eyes open:"))
        self.labelEyesHalfopen.setText(_translate("SettingsWindow", "Eyes half-open:"))
        self.labelEyesClosed.setText(_translate("SettingsWindow", "Eyes closed:"))
        self.labelCap.setText(_translate("SettingsWindow", "Cap:"))
        self.labelSidehair.setText(_translate("SettingsWindow", "Sidehair:"))
        self.labelMustache.setText(_translate("SettingsWindow", "Mustache:"))
        self.labelButton.setText(_translate("SettingsWindow", "Button:"))
        self.groupNames.setTitle(_translate("SettingsWindow", "Games' names"))
        self.labelSM64Name.setText(_translate("SettingsWindow", "Super Mario 64:"))
        self.labelAddNames.setText(_translate("SettingsWindow", "Other games:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TabTextures), _translate("SettingsWindow", "Textures"))
        self.pushClose.setText(_translate("SettingsWindow", "Close"))
        self.pushApply.setText(_translate("SettingsWindow", "Apply"))
        self.pushApplyClose.setText(_translate("SettingsWindow", "Apply and Close"))
        self.CheckDoNotMoveSwitchVertically.setText(_translate("SettingsWindow", "Do not move the Switch button vertically on resize"))
        self.CheckEyeBordersWarning.setText(_translate("SettingsWindow", "Do not warn me when I remove borders from currently chosen textures"))
        self.BG_ButtonConfigure.setText(_translate("SettingsWindow", "Configure"))
        self.BG_ButtonReset.setText(_translate("SettingsWindow", "Reset"))
        self.BG_Label.setText(_translate("SettingsWindow", "Change texture display's background:"))
        self.CheckTextureBorder.setText(_translate("SettingsWindow", "Add borders around textures"))
        global SW_AIToolTip
        SW_AIToolTip = "This translation was mostly or fully done using machine<br>translation and/or artificial intelligence, so there may be inaccuracies."
        self.Delegate.SetToolTip()
        self.ToolTipPath.setToolTip("This is the path with the folders inside of which you put the \"hi-res\" textures that a graphics plugin can load over a game's original textures (the texture pack function).<br>This path usually looks something like the following:<br><br>[path to your emulator]/Plugin/GFX/hires_texture/<br>or<br>[path to your emulator]/Plugin/hires_texture/<br>(you can create the \"hires_texture\" folder if you don't have it.)<br><br>You need to have a \"/\" (without quotes, obviously. \"\\\" also works for Windows) in the end for katarakta to use the path correctly.<br><img src = \"resources/img/ToolTipPath.png\"><br><br>IMPORTANT! Graphics plugins' texture pack features may not work if your emulator is installed in the Program Files folder!")
        self.ToolTipMainTextureNames.setToolTip("The textures you will be changing the most are going to probably be the eyes, the cap, the sidehair, the mustache and the button. The names for this kind of textures is the bunch of seemingly random symbols that go after the game's name, starting with and including the \"#\" as shown in the example below.<br><img src = \"resources/img/ToolTipMainTextureNames.png\"><br>Though, the names for these seven textures are already included and it's extremely unlikely that you would ever have to change them.")
        self.ToolTipGameNames.setToolTip("What I call a \"game's name\" is a name which—to my knowledge—is used for referring to a specific game and is contained inside the game's ROM. These \"games' names\" are also used by the \"hi-res\" textures and hence by katarakta. If the main ROM you are using is a normal Super Mario 64 ROM, then Super Mario 64's name is probably \"SUPER MARIO 64\" for you, which is already included (keep in mind that it's case-sensitive, which means that \"Super Mario 64\" is incorrect and \"SUPER MARIO 64\" is correct). Places where a game's name can be found include but are not limited to:<br>• The emulator's \"save\" folder, specifically the .eep files inside.<br>• The folder where a game's textures are dumped when dumping textures with a graphics plugin.<br>BUT! The name your emulator can show as its window title can sometimes be incorrect, so do not rely on that.<br><img src = \"resources/img/ToolTipGameNameSmaller.png\"><br>You can add names for other games if you are planning to change textures there too (separated by semicolons (\";\") without spaces before or after the semicolons).<br>After adding any other games, you can choose which other game to apply a texture to using the button with an arrow facing down on it next to the Apply button:<br><img src = \"resources/img/ToolTipApplyDropdown.png\">")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TabAppearance), _translate("SettingsWindow", "Appearance"))
        self.groupEyeBG.setTitle("Texture Preview Background")
        self.groupEyeList.setTitle("Texture List")
        self.CheckEyeListIcons.setText("Texture icons")
        self.CheckEyeListIconBG.setText("Use the plain color as icons' background")
        self.LabelEyeListWarning.setText("Warning: the two options above can increase loading\ntimes for the texture list, especially when you have a\nlot of textures.")
        self.LabelEyeListDemo.setText("Preview:")
        self.LabelRowHeight.setText("Row height")

    def retranslateUiOther(self, SettingsWindow):
        _translate = QtCore.QCoreApplication.translate
        SettingsWindow.setWindowTitle(_translate("SettingsWindow", Language.SW_Title))
        setTextList = [
                    [self.labelLanguageRestart, Language.SW_labelLanguageRestart],
                    [self.checkUpdates, Language.SW_checkUpdates],
                    [self.labelUpdates, Language.SW_labelUpdates],
                    [self.checkStayOnTop, Language.SW_checkStayOnTop],
                    [self.labelHiResSM64, Language.SW_labelHiResSM64],
                    [self.labelEyesOpen, Language.SW_labelEyesOpen],
                    [self.labelEyesHalfopen, Language.SW_labelEyesHalfopen],
                    [self.labelEyesClosed, Language.SW_labelEyesClosed],
                    [self.labelCap, Language.SW_labelCap],
                    [self.labelSidehair, Language.SW_labelSidehair],
                    [self.labelMustache, Language.SW_labelMustache],
                    [self.labelButton, Language.SW_labelButton],
                    [self.labelSM64Name, Language.SW_labelSM64Name],
                    [self.labelAddNames, Language.SW_labelAddNames],
                    [self.pushClose, Language.SW_pushClose],
                    [self.pushApply, Language.SW_pushApply],
                    [self.pushApplyClose, Language.SW_pushApplyClose],
                    [self.CheckDoNotMoveSwitchVertically, Language.SW_CheckDoNotMoveSwitchVertically],
                    [self.CheckEyeBordersWarning, Language.SW_CheckEyeBordersWarning],
                    [self.BG_ButtonConfigure, Language.SW_BG_ButtonConfigure],
                    [self.BG_ButtonReset, Language.SW_BG_ButtonReset],
                    [self.BG_Label, Language.SW_BG_Label],
                    [self.CheckTextureBorder, Language.SW_CheckTextureBorder],
                    [self.CheckEyeListIcons, Language.SW_CheckEyeListIcons],
                    [self.CheckEyeListIconBG, Language.SW_CheckEyeListIconBG],
                    [self.LabelEyeListWarning, Language.SW_LabelEyeListWarning],
                    [self.LabelEyeListDemo, Language.SW_LabelEyeListDemo],
                    [self.LabelRowHeight, Language.SW_LabelRowHeight]
                    ]
        setTitleList = [
                    [self.groupLanguage, Language.SW_groupLanguage],
                    [self.groupUpdates, Language.SW_groupUpdates],
                    [self.groupMisc, Language.SW_groupMisc],
                    [self.groupSM64, Language.SW_groupSM64],
                    [self.groupNames, Language.SW_groupNames],
                    [self.groupEyeBG, Language.SW_groupEyeBG],
                    [self.groupEyeList, Language.SW_groupEyeList]
                    ]
        setTabTextList = [
                    [self.tabWidget, Language.SW_TabGeneral, self.TabGeneral],
                    [self.tabWidget, Language.SW_TabTextures, self.TabTextures],
                    [self.tabWidget, Language.SW_TabAppearance, self.TabAppearance]
                    ]
        
        #.setTabText(self.tabWidget.indexOf(), _translate("SettingsWindow", ))
        
        for i in setTextList:
            if (i[1] != "") and (i[1] != None):
                i[0].setText(_translate("SettingsWindow", i[1]))
        for i in setTitleList:
            if (i[1] != "") and (i[1] != None):
                i[0].setTitle(_translate("SettingsWindow", i[1]))
        for i in setTabTextList:
            if (i[1] != "") and (i[1] != None):
                i[0].setTabText(self.tabWidget.indexOf(i[2]), _translate("SettingsWindow", i[1]))
        
        self.ToolTipPath.setToolTip(str(Language.SW_ToolTipPath1) + "<br><img src = \"resources/img/ToolTipPath.png\">")
        self.ToolTipMainTextureNames.setToolTip(str(Language.SW_ToolTipMainTextureNames1) + "<br><img src = \"resources/img/ToolTipMainTextureNames.png\"><br>" + str(Language.SW_ToolTipMainTextureNames2))
        self.ToolTipGameNames.setToolTip(str(Language.SW_ToolTipGameNames1) + "<br><img src = \"resources/img/ToolTipGameNameSmaller.png\"><br>" + str(Language.SW_ToolTipGameNames2) + "<br><img src = \"resources/img/ToolTipApplyDropdown.png\">")

        global SW_AIToolTip
        SW_AIToolTip = Language.SW_AI
        self.Delegate.SetToolTip()

class Ui_ccconvWindow(QWidget):
    def setupUi(self, ccconvWindow):
        ccconvWindow.setObjectName("ccconvWindow")
        ccconvWindow.resize(400, 286)
        ccconvWindow.setFixedSize(ccconvWindow.size())
        ccconvWindow.setStyleSheet("font-size: 11px")
            
        font = QtGui.QFont()
        font.setPointSize(10)
        fontsmaller = QtGui.QFont()
        fontsmaller.setPointSize(8)
        #.setFont(fontsmaller)

        self.ccconvCentral = QtWidgets.QWidget(ccconvWindow)
        self.ccconvCentral.setObjectName("ccconvCentral")
        self.ccconvCentral.setFont(fontsmaller)
        self.InputCC = QtWidgets.QTextEdit(self.ccconvCentral)
        self.InputCC.setGeometry(QtCore.QRect(10, 10, 150, 150))
        self.InputCC.setReadOnly(False)
        self.InputCC.setObjectName("InputCC")
        self.OutputCC = QtWidgets.QTextEdit(self.ccconvCentral)
        self.OutputCC.setGeometry(QtCore.QRect(240, 10, 150, 150))
        self.OutputCC.setReadOnly(True)
        self.OutputCC.setObjectName("OutputCC")
        self.ButtonConvert = QtWidgets.QPushButton(self.ccconvCentral)
        self.ButtonConvert.setGeometry(QtCore.QRect(9, 235, 382, 42))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ButtonConvert.setFont(font)
        self.ButtonConvert.setStyleSheet("font-size: 24px")
        self.ButtonConvert.setObjectName("ButtonConvert")
        self.ArrowLabel = QtWidgets.QLabel(self.ccconvCentral)
        self.ArrowLabel.setGeometry(QtCore.QRect(170, 10, 60, 150))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.ArrowLabel.setFont(font)
        self.ArrowLabel.setStyleSheet("font-size: 31px")
        self.ArrowLabel.setObjectName("ArrowLabel")
        self.InputCombo = QtWidgets.QComboBox(self.ccconvCentral)
        self.InputCombo.setGeometry(QtCore.QRect(10, 164, 150, 20))
        self.InputCombo.setObjectName("InputCombo")
        self.InputCombo.addItem("")
        self.InputCombo.addItem("")
        self.InputCombo.addItem("")
        self.InputCombo.addItem("")
        self.OutputCombo = QtWidgets.QComboBox(self.ccconvCentral)
        self.OutputCombo.setGeometry(QtCore.QRect(240, 164, 150, 20))
        self.OutputCombo.setObjectName("OutputCombo")
        self.OutputCombo.addItem("")
        self.OutputCombo.addItem("")
        self.OutputCombo.addItem("")
        self.OutputCombo.addItem("")
        self.ButtonPaste = QtWidgets.QPushButton(self.ccconvCentral)
        self.ButtonPaste.setGeometry(QtCore.QRect(9, 187, 152, 22))
        self.ButtonPaste.setObjectName("ButtonPaste")
        self.ButtonCopy = QtWidgets.QPushButton(self.ccconvCentral)
        self.ButtonCopy.setGeometry(QtCore.QRect(239, 187, 152, 22))
        self.ButtonCopy.setObjectName("ButtonCopy")
        self.ButtonExport = QtWidgets.QPushButton(self.ccconvCentral)
        self.ButtonExport.setGeometry(QtCore.QRect(239, 211, 152, 22))
        self.ButtonExport.setObjectName("ButtonExport")
        self.ButtonImport = QtWidgets.QPushButton(self.ccconvCentral)
        self.ButtonImport.setGeometry(QtCore.QRect(9, 211, 152, 22))
        self.ButtonImport.setObjectName("ButtonImport")
        ccconvWindow.setCentralWidget(self.ccconvCentral)
        
        self.InputCombo.setItemIcon(0, QIcon("resources/img/region/RegionNTSC-J.png"))
        self.InputCombo.setItemIcon(1, QIcon("resources/img/region/RegionNTSC-U.png"))
        self.InputCombo.setItemIcon(2, QIcon("resources/img/region/RegionPAL.png"))
        self.InputCombo.setItemIcon(3, QIcon("resources/img/region/RegionShindou.png"))
        
        self.OutputCombo.setItemIcon(0, QIcon("resources/img/region/RegionNTSC-J.png"))
        self.OutputCombo.setItemIcon(1, QIcon("resources/img/region/RegionNTSC-U.png"))
        self.OutputCombo.setItemIcon(2, QIcon("resources/img/region/RegionPAL.png"))
        self.OutputCombo.setItemIcon(3, QIcon("resources/img/region/RegionShindou.png"))
        
        #if DarkMode == 1:
        ccconvWindow.setWindowIcon(QtGui.QIcon("resources/img/ccconv.png"))
        #else:
        #    msgbox.setWindowIcon(QIcon("resources/img/DarkMode/EyeBordersCurrent.png"))

        self.ButtonConvert.clicked.connect(self.CcConvert)
        self.ButtonPaste.clicked.connect(self.CcPaste)
        self.ButtonCopy.clicked.connect(self.CcCopy)
        self.ButtonExport.clicked.connect(self.CcSaveAsTxt)
        self.ButtonImport.clicked.connect(self.CcOpenFromTxt)

        QtCore.QMetaObject.connectSlotsByName(ccconvWindow)
        
        self.retranslateUiEnglish(ccconvWindow)
        if Language.Properties_InnerName != "English":
            self.retranslateUiOther(ccconvWindow)

    # Addresses for each region, the "A" stands for "Addresses"
    global A_NTSCJ, A_NTSCU, A_PAL, A_SHINDOU
    A_NTSCJ = list(["8107BDC0","8107BDC2","8107BDC4","8107BDC6","8107BDC8","8107BDCA","8107BDCC","8107BDCE","8107BDD8","8107BDDA","8107BDDC","8107BDDE","8107BDE0","8107BDE2","8107BDE4","8107BDE6","8107BDF0","8107BDF2","8107BDF4","8107BDF6","8107BDF8","8107BDFA","8107BDFC","8107BDFE","8107BE08","8107BE0A","8107BE0C","8107BE0E","8107BE10","8107BE12","8107BE14","8107BE16","8107BE20","8107BE22","8107BE24","8107BE26","8107BE28","8107BE2A","8107BE2C","8107BE2E","8107BE38","8107BE3A","8107BE3C","8107BE3E","8107BE40","8107BE42","8107BE44","8107BE46"])
    A_NTSCU = list(["8107EC20","8107EC22","8107EC24","8107EC26","8107EC28","8107EC2A","8107EC2C","8107EC2E","8107EC38","8107EC3A","8107EC3C","8107EC3E","8107EC40","8107EC42","8107EC44","8107EC46","8107EC50","8107EC52","8107EC54","8107EC56","8107EC58","8107EC5A","8107EC5C","8107EC5E","8107EC68","8107EC6A","8107EC6C","8107EC6E","8107EC70","8107EC72","8107EC74","8107EC76","8107EC80","8107EC82","8107EC84","8107EC86","8107EC88","8107EC8A","8107EC8C","8107EC8E","8107EC98","8107EC9A","8107EC9C","8107EC9E","8107ECA0","8107ECA2","8107ECA4","8107ECA6"])
    A_PAL = list(["810742E0","810742E2","810742E4","810742E6","810742E8","810742EA","810742EC","810742EE","810742F8","810742FA","810742FC","810742FE","81074300","81074302","81074304","81074306","81074310","81074312","81074314","81074316","81074318","8107431A","8107431C","8107431E","81074328","8107432A","8107432C","8107432E","81074330","81074332","81074334","81074336","81074340","81074342","81074344","81074346","81074348","8107434A","8107434C","8107434E","81074358","8107435A","8107435C","8107435E","81074360","81074362","81074364","81074366"])
    A_SHINDOU = list(["8107BDC0","8107BDC2","8107BDC4","8107BDC6","8107BDC8","8107BDCA","8107BDCC","8107BDCE","8107BDD8","8107BDDA","8107BDDC","8107BDDE","8107BDE0","8107BDE2","8107BDE4","8107BDE6","8107BDF0","8107BDF2","8107BDF4","8107BDF6","8107BDF8","8107BDFA","8107BDFC","8107BDFE","8107BE08","8107BE0A","8107BE0C","8107BE0E","8107BE10","8107BE12","8107BE14","8107BE16","8107BE20","8107BE22","8107BE24","8107BE26","8107BE28","8107BE2A","8107BE2C","8107BE2E","8107BE38","8107BE3A","8107BE3C","8107BE3E","8107BE40","8107BE42","8107BE44","8107BE46"])

    def CcConvert(self, ccconvWindow):
        InputCCvar = self.InputCC.toPlainText()

        if self.InputCombo.currentText() == "NTSC-J":
            self.ChosenListInput = A_NTSCJ
        elif self.InputCombo.currentText() == "NTSC-U":
            self.ChosenListInput = A_NTSCU
        elif self.InputCombo.currentText() == "PAL":
            self.ChosenListInput = A_PAL
        else:
            self.ChosenListInput = A_SHINDOU
    
        if self.OutputCombo.currentText() == "NTSC-J":
            self.ChosenListOutput = A_NTSCJ
        elif self.OutputCombo.currentText() == "NTSC-U":
            self.ChosenListOutput = A_NTSCU
        elif self.OutputCombo.currentText() == "PAL":
            self.ChosenListOutput = A_PAL
        else:
            self.ChosenListOutput = A_SHINDOU
    
        count = 0
        for item in self.ChosenListInput:
            InputCCvar = InputCCvar.replace(
                    item,
                    self.ChosenListOutput[count]
                    )
            OutputCCvar = InputCCvar
            count += 1

        self.OutputCC.setPlainText(OutputCCvar)
        
    def CcPaste(self, ccconvWindow):
        self.InputCC.setPlainText(pyclip.paste(text = True))
        
    def CcCopy(self, ccconvWindow):
        pyclip.copy(self.OutputCC.toPlainText())

    def CcOpenFromTxt(self, ccconvWindow):
        if Option.Language == "English":
            ChooseOpenFile = QFileDialog.getOpenFileName(self, "Open File", os.getcwd(), "Text Document (*.txt)")
        else:
            ChooseOpenFile = QFileDialog.getOpenFileName(self, Language.Ccconv_ChooseOpenFile, os.getcwd(), "{} (*.txt)".format(Language.Ccconv_TxtDocument))

        try:
            with open(ChooseOpenFile[0]) as ChosenOpenFileCC:
                self.InputCC.setPlainText(ChosenOpenFileCC.read())
                ChosenOpenFileCC.close()
        except:
            pass

    def CcSaveAsTxt(self, ccconvWindow):
        if Option.Language == "English":
            ChooseSaveFile = QFileDialog.getSaveFileName(self, "Save File", os.getcwd(), "Text Document (*.txt)")
        else:
            ChooseSaveFile = QFileDialog.getSaveFileName(self, Language.Ccconv_ChooseSaveFile, os.getcwd(), "{} (*.txt)".format(Language.Ccconv_TxtDocument))
        try:
            SaveFile = open(ChooseSaveFile[0], 'w')
            SaveFile.write(self.OutputCC.toPlainText())
            SaveFile.close()
        except:
            pass

    def retranslateUiEnglish(self, ccconvWindow):
        _translate = QtCore.QCoreApplication.translate
        ccconvWindow.setWindowTitle(_translate("ccconvWindow", "Colorcode Converter (CCConv)"))
        self.InputCC.setPlaceholderText(_translate("ccconvWindow", "Insert colorcode here..."))
        self.OutputCC.setPlaceholderText(_translate("ccconvWindow", "Output will appear here."))
        self.ButtonConvert.setText(_translate("ccconvWindow", "Convert"))
        self.ArrowLabel.setText(_translate("ccconvWindow", "--->"))
        self.InputCombo.setItemText(0, _translate("ccconvWindow", "NTSC-J"))
        self.InputCombo.setItemText(1, _translate("ccconvWindow", "NTSC-U"))
        self.InputCombo.setItemText(2, _translate("ccconvWindow", "PAL"))
        self.InputCombo.setItemText(3, _translate("ccconvWindow", "Shindou"))
        self.OutputCombo.setItemText(0, _translate("ccconvWindow", "NTSC-J"))
        self.OutputCombo.setItemText(1, _translate("ccconvWindow", "NTSC-U"))
        self.OutputCombo.setItemText(2, _translate("ccconvWindow", "PAL"))
        self.OutputCombo.setItemText(3, _translate("ccconvWindow", "Shindou"))
        self.ButtonPaste.setText(_translate("ccconvWindow", "Paste from clipboard"))
        self.ButtonCopy.setText(_translate("ccconvWindow", "Copy to clipboard"))
        self.ButtonExport.setText(_translate("ccconvWindow", "Export as .txt file"))
        self.ButtonImport.setText(_translate("ccconvWindow", "Import from .txt file"))

    def retranslateUiOther(self, ccconvWindow):
        _translate = QtCore.QCoreApplication.translate
        ccconvWindow.setWindowTitle(_translate("ccconvWindow", Language.Ccconv_Title))
        self.InputCC.setPlaceholderText(_translate("ccconvWindow", Language.Ccconv_InputCC))
        self.OutputCC.setPlaceholderText(_translate("ccconvWindow", Language.Ccconv_OutputCC))
        self.ButtonConvert.setText(_translate("ccconvWindow", Language.Ccconv_ButtonConvert))
        self.ButtonPaste.setText(_translate("ccconvWindow", Language.Ccconv_ButtonPaste))
        self.ButtonCopy.setText(_translate("ccconvWindow", Language.Ccconv_ButtonCopy))
        self.ButtonExport.setText(_translate("ccconvWindow", Language.Ccconv_ButtonExport))
        self.ButtonImport.setText(_translate("ccconvWindow", Language.Ccconv_ButtonImport))
    
if __name__ == "__main__":
    app = QApplication(sys.argv)

    try:
        LoadingImageList = os.listdir('resources/loading')
        for File in LoadingImageList:
            if not(File.endswith(".png")):
                LoadingImageList.remove(File)

        LoadingImage = random.choice(LoadingImageList)
    
        Splash = QSplashScreen(QPixmap("resources/loading/{}".format(LoadingImage)))
        Splash.show()
        
    except:
        pass
    
    MainWindow = Ui_MainWindow() #QtWidgets.QMainWindow()
    MainWindow.setupUi(MainWindow)
    #ui = Ui_MainWindow()
    #ui.setupUi(MainWindow)
    MainWindow.show()
    
    try:
        Splash.finish(MainWindow)
    except:
        pass
    
    sys.exit(app.exec_())
