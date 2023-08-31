#GPL-3.0-only

import os
import configparser
import shutil
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget, QSplashScreen, QAction, QFileDialog
from PyQt5.QtGui import QPixmap, QIcon
import sys
import random
import requests
import pyclip
import locale
import ctypes

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

class Options():
    SM64Dir = ""
    AddDir = ""
    
    Eyes1 = ""
    Eyes2 = ""
    Eyes3 = ""
    
    Cap = ""
    Hair = ""
    Mustache = ""
    Button = ""
    
    AddEyes1 = ""
    AddEyes2 = ""
    AddEyes3 = ""
    
    AddCap = ""
    AddHair = ""
    AddMustache = ""
    AddButton = ""
    
    Language = ""

AppVersion = "1.4.8"
AppEdition = "Normal"

Option = Options()

Config = configparser.ConfigParser()

def CreateConfig():
    CreatedConfig = configparser.ConfigParser()
    SetLanguage = "English"
    try:
        if locale.windows_locale[ctypes.windll.kernel32.GetUserDefaultUILanguage()] == "ru" or "ru_BY" or "ru_KZ" or "ru_KG" or "ru_MD" or "ru_RU" or "ru_UA" or "be" or "be_BY":
            SetLanguage = "Russian"
        elif locale.windows_locale[ctypes.windll.kernel32.GetUserDefaultUILanguage()] == "uk" or "uk_UA":
            SetLanguage = "Ukrainian"
        elif locale.windows_locale[ctypes.windll.kernel32.GetUserDefaultUILanguage()] == "kk" or "kk_KZ":
            SetLanguage = "KazakhLatin"
        else:
            pass
    except:
        pass
    CreatedConfig["PATHS"] = {
        "sm64dir": "",
        "adddir": "",
        "eyes1": "SUPER MARIO 64#6B8D43C4#0#2_all",
        "eyes2": "SUPER MARIO 64#6B8D43C4#0#2_all",
        "eyes3": "SUPER MARIO 64#6B8D43C4#0#2_all",
        "cap": "SUPER MARIO 64#6B8D43C4#0#2_all",
        "hair": "SUPER MARIO 64#6B8D43C4#0#2_all",
        "mustache": "SUPER MARIO 64#6B8D43C4#0#2_all",
        "button": "SUPER MARIO 64#6B8D43C4#0#2_all",
        "addeyes1": "",
        "addeyes2": "",
        "addeyes3": "",
        "addcap": "",
        "addhair": "",
        "addmustache": "",
        "addbutton": ""
        }
    CreatedConfig["OPTIONS"] = {
        "language": SetLanguage,
        "startupcheckforupdates": "1",
        "startupstayontop": "0"
        }
    with open("config.ini","w") as _ConfigFile:
        CreatedConfig.write(_ConfigFile)

if os.path.exists("config.ini") is True:
    pass
else:
    CreateConfig()

def LoadConfig():
    Config.read("config.ini")
    ConfigSecond = Config["PATHS"]

    Option.SM64Dir = ConfigSecond.get("SM64Dir", Option.SM64Dir)
    Option.AddDir = ConfigSecond.get("AddDir", Option.AddDir)
    Option.Eyes1 = ConfigSecond.get("Eyes1", Option.Eyes1)
    Option.Eyes2 = ConfigSecond.get("Eyes2", Option.Eyes2)
    Option.Eyes3 = ConfigSecond.get("Eyes3", Option.Eyes3)
    Option.Cap = ConfigSecond.get("Cap", Option.Cap)
    Option.Hair = ConfigSecond.get("Hair", Option.Hair)
    Option.Mustache = ConfigSecond.get("Mustache", Option.Mustache)
    Option.Button = ConfigSecond.get("Button", Option.Button)
    Option.AddEyes1 = ConfigSecond.get("AddEyes1", Option.AddEyes1)
    Option.AddEyes2 = ConfigSecond.get("AddEyes2", Option.AddEyes2)
    Option.AddEyes3 = ConfigSecond.get("AddEyes3", Option.AddEyes3)
    Option.AddCap = ConfigSecond.get("AddCap", Option.AddCap)
    Option.AddHair = ConfigSecond.get("AddHair", Option.AddHair)
    Option.AddMustache = ConfigSecond.get("AddMustache", Option.AddMustache)
    Option.AddButton = ConfigSecond.get("AddButton", Option.AddButton)
        
    ConfigSecond = Config["OPTIONS"]
    Option.Language = ConfigSecond.get("Language", Option.Language)
    Option.StartUpCheckForUpdates = ConfigSecond.get("StartUpCheckForUpdates")
    Option.StartUpStayOnTop = ConfigSecond.get("StartUpStayOnTop")

LoadConfig()

# Find Folders in eyes\ and chmb\
EyeFolders = os.listdir("eyes\\")
CHMBFolders = os.listdir("chmb\\")
FolderName = ""

class Ui_MainWindow(object):
    def __init__(self):
        self.Mode = "Eyes"
    
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
        MainWindow.resize(518, 563)
        MainWindow.setFixedSize(MainWindow.size())
        #MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.World))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        MainWindow.setWindowIcon(QtGui.QIcon("img/Icon.png"))

        if Option.StartUpCheckForUpdates == "1":
            self.CheckUpdatesStartUp()
        
        CopyEyesErrorBoxTitle = ""
        CopyEyesErrorBoxMessage = ""

        #Found eye folders label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 101, 16))
        self.label.setObjectName("label")

        #Displaying eye textures
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(240, 10, 120, 351))
        self.groupBox.setObjectName("groupBox")
        self.SM64DisplayLabel1 = QtWidgets.QLabel(self.groupBox)
        self.SM64DisplayLabel1.setEnabled(True)
        self.SM64DisplayLabel1.setGeometry(QtCore.QRect(10, 20, 101, 101))
        self.SM64DisplayLabel1.setText("")
        self.SM64DisplayLabel1.setPixmap(QtGui.QPixmap("img/PlaceHolderEye1.png"))
        self.SM64DisplayLabel1.setScaledContents(True)
        self.SM64DisplayLabel1.setObjectName("SM64DisplayLabel1")
        self.SM64DisplayLabel2 = QtWidgets.QLabel(self.groupBox)
        self.SM64DisplayLabel2.setGeometry(QtCore.QRect(10, 130, 101, 101))
        self.SM64DisplayLabel2.setText("")
        self.SM64DisplayLabel2.setPixmap(QtGui.QPixmap("img/PlaceHolderEye2.png"))
        self.SM64DisplayLabel2.setScaledContents(True)
        self.SM64DisplayLabel2.setObjectName("SM64DisplayLabel2")
        self.SM64DisplayLabel3 = QtWidgets.QLabel(self.groupBox)
        self.SM64DisplayLabel3.setGeometry(QtCore.QRect(10, 240, 101, 101))
        self.SM64DisplayLabel3.setText("")
        self.SM64DisplayLabel3.setPixmap(QtGui.QPixmap("img/PlaceHolderEye3.png"))
        self.SM64DisplayLabel3.setScaledContents(True)
        self.SM64DisplayLabel3.setObjectName("SM64DisplayLabel3")
        self.SM64DisplayLabel4 = QtWidgets.QLabel(self.groupBox)
        self.SM64DisplayLabel4.setGeometry(QtCore.QRect(10, 350, 101, 101))
        self.SM64DisplayLabel4.setText("")
        self.SM64DisplayLabel4.setPixmap(QtGui.QPixmap("img/PlaceHolderButton.png"))
        self.SM64DisplayLabel4.setScaledContents(True)
        self.SM64DisplayLabel4.setObjectName("SM64DisplayLabel4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(380, 10, 120, 351))
        self.groupBox_2.setObjectName("groupBox_2")
        self.AddDisplayLabel1 = QtWidgets.QLabel(self.groupBox_2)
        self.AddDisplayLabel1.setGeometry(QtCore.QRect(10, 20, 101, 101))
        self.AddDisplayLabel1.setText("")
        self.AddDisplayLabel1.setPixmap(QtGui.QPixmap("img/PlaceHolderEye1.png"))
        self.AddDisplayLabel1.setScaledContents(True)
        self.AddDisplayLabel1.setObjectName("AddDisplayLabel1")
        self.AddDisplayLabel2 = QtWidgets.QLabel(self.groupBox_2)
        self.AddDisplayLabel2.setGeometry(QtCore.QRect(10, 130, 101, 101))
        self.AddDisplayLabel2.setText("")
        self.AddDisplayLabel2.setPixmap(QtGui.QPixmap("img/PlaceHolderEye2.png"))
        self.AddDisplayLabel2.setScaledContents(True)
        self.AddDisplayLabel2.setObjectName("AddDisplayLabel2")
        self.AddDisplayLabel3 = QtWidgets.QLabel(self.groupBox_2)
        self.AddDisplayLabel3.setGeometry(QtCore.QRect(10, 240, 101, 101))
        self.AddDisplayLabel3.setText("")
        self.AddDisplayLabel3.setPixmap(QtGui.QPixmap("img/PlaceHolderEye3.png"))
        self.AddDisplayLabel3.setScaledContents(True)
        self.AddDisplayLabel3.setObjectName("AddDisplayLabel3")
        self.AddDisplayLabel4 = QtWidgets.QLabel(self.groupBox_2)
        self.AddDisplayLabel4.setGeometry(QtCore.QRect(10, 350, 101, 101))
        self.AddDisplayLabel4.setText("")
        self.AddDisplayLabel4.setPixmap(QtGui.QPixmap("img/PlaceHolderButton.png"))
        self.AddDisplayLabel4.setScaledContents(True)
        self.AddDisplayLabel4.setObjectName("AddDisplayLabel4")

        MainWindow.setCentralWidget(self.centralwidget)

        #Apply buttons
        self.ApplySM64 = QtWidgets.QPushButton(self.centralwidget)
        self.ApplySM64.setGeometry(QtCore.QRect(239, 364, 71, 23))
        self.ApplySM64.setObjectName("ApplySM64")
        #self.ApplySM64.clicked.connect(lambda: self.CopyEyes("SM64Dir", self.listWidget.currentItem().text()))
        
        self.ApplyAdd = QtWidgets.QPushButton(self.centralwidget)
        self.ApplyAdd.setGeometry(QtCore.QRect(380, 364, 91, 23))
        self.ApplyAdd.setObjectName("ApplyAdd")
        #self.ApplyAdd.clicked.connect(lambda: self.CopyEyes("AddDir", self.listWidget.currentItem().text()))

        #Eyes list
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 30, 201, 481))
        self.listWidget.setObjectName("listWidget")

        self.listWidget.addItems(EyeFolders)

        self.listWidget.itemClicked.connect(lambda: self.ItemChosen())

        #Refresh eye list button
        self.Refresh = QtWidgets.QPushButton(self.centralwidget)
        self.Refresh.setGeometry(QtCore.QRect(239, 489, 91, 23))
        self.Refresh.setObjectName("RefreshButton")
        self.Refresh.clicked.connect(lambda: self.RefreshEyeList())

        #Switch to cap, hair etc. from eyes and vice versa button
        self.SwitchItemsButton = QtWidgets.QPushButton(self.centralwidget)
        self.SwitchItemsButton.setGeometry(QtCore.QRect(239, 465, 91, 23))
        self.SwitchItemsButton.setObjectName("SwitchButton")
        self.SwitchItemsButton.clicked.connect(lambda: self.SwitchItems())

        #Menu bar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 518, 21))
        self.menubar.setObjectName("menubar")
        
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        #self.menuOptions.setIcon("img/Options.png")
        #self.menuLanguage = QtWidgets.QMenu(self.menuLanguage)
        #self.menuLanguage.setObjectName("menuLanguage")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout.setIcon(QIcon("img/Icon.png"))

        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionSettings.triggered.connect(self.OpenSettingsWindow)
        self.actionSettings.setIcon(QIcon("img/Settings.png"))
        
        self.submenuHiRes = QtWidgets.QMenu(MainWindow)
        self.submenuHiRes.setObjectName("actionHiRes")
        self.submenuHiRes.setIcon(QIcon("img/HiResMain.png"))
        self.HiResClearSM64 = self.submenuHiRes.addAction(QIcon("img/HiResClear.png"), "ClearSM64")
        self.HiResClearSM64.triggered.connect(self.ClearSM64)
        self.HiResClearAdd = self.submenuHiRes.addAction(QIcon("img/HiResClearAdd.png"), "ClearAdd")
        self.HiResClearAdd.triggered.connect(self.ClearAdd)
        self.HiResOpenSM64 = self.submenuHiRes.addAction(QIcon("img/HiResOpen.png"), "OpenSM64")
        self.HiResOpenSM64.triggered.connect(self.OpenSM64)
        self.HiResOpenAdd = self.submenuHiRes.addAction(QIcon("img/HiResOpenAdd.png"), "OpenAdd")
        self.HiResOpenAdd.triggered.connect(self.OpenAdd)
        self.actionOpenKataraktaFolder = QtWidgets.QAction(MainWindow)
        self.actionOpenKataraktaFolder.setObjectName("actionOpenKataraktaFolder")
        self.actionOpenKataraktaFolder.triggered.connect(self.OpenKataraktaFolder)
        self.actionOpenKataraktaFolder.setIcon(QIcon("img/OpenKataraktaFolder.png"))
        self.actionOpenCcconv = QtWidgets.QAction(MainWindow)
        self.actionOpenCcconv.setObjectName("actionOpenCcconv")
        self.actionOpenCcconv.triggered.connect(self.OpenCcconv)
        self.actionOpenCcconv.setIcon(QIcon("img/ccconv.png"))
        self.actionStayOnTop = QtWidgets.QAction(MainWindow)
        self.actionStayOnTop.setObjectName("actionStayOnTop")
        self.actionStayOnTop.setCheckable(True)
        self.actionStayOnTop.triggered.connect(self.StayOnTop)
        self.actionStayOnTop.setIcon(QIcon("img/StayOnTop.png"))

        if Option.StartUpStayOnTop == "1":
            self.actionStayOnTop.setChecked(True)
            self.StayOnTop()
        
        #self.HiResViewSM64 = self.submenuHiRes.addAction("ViewSM64")
        #self.HiResViewSM64.triggered.connect(self.ViewSM64)
        #self.HiResViewAdd = self.submenuHiRes.addAction("ViewAdd")
        #self.HiResViewAdd.triggered.connect(self.ViewAdd)
        
        #self.actionEnglish = QtWidgets.QAction(MainWindow)
        #self.actionEnglish.setObjectName("actionEnglish")
        #self.menuLanguage.addAction(self.actionEnglish)
        #self.actionUkrainian = QtWidgets.QAction(MainWindow)
        #self.actionUkrainian.setObjectName("actionUkrainian")
        #self.menuLanguage.addAction(self.actionUkrainian)
        #self.actionRussian = QtWidgets.QAction(MainWindow)
        #self.actionRussian.setObjectName("actionRussian")
        #self.menuLanguage.addAction(self.actionRussian)
        #self.menuOptions.addAction(self.menuLanguage.menuAction())
        self.menuOptions.addMenu(self.submenuHiRes)
        self.menuOptions.addAction(self.actionOpenKataraktaFolder)
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.actionSettings)
        self.menuOptions.addAction(self.actionOpenCcconv)
        self.menuOptions.addAction(self.actionStayOnTop)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuOptions.menuAction())

        self.actionUpdate = self.menubar.addAction("actionUpdate")
        self.actionUpdate.triggered.connect(self.OpenUpdateWindow)
        
        self.menubar.addAction(self.actionUpdate)
        
        self.menubar.addAction(self.menuHelp.menuAction())

        self.actionAbout.triggered.connect(self.OpenAboutWindow)
        
        self.ApplySM64.setEnabled(False)
        self.ApplyAdd.setEnabled(False)
        
        if Option.Language == "English":
                self.retranslateUiEnglish(MainWindow)
                self.Update()

        elif Option.Language == "Ukrainian":
                self.retranslateUiUkrainian(MainWindow)
                self.Update()
        
        elif Option.Language == "Russian":
                self.retranslateUiRussian(MainWindow)
                self.Update()
        
        elif Option.Language == "KazakhCyrillic":
                self.retranslateUiKazakhCyrillic(MainWindow)
                self.Update()
        
        elif Option.Language == "KazakhLatin":
                self.retranslateUiKazakhLatin(MainWindow)
                self.Update()
        
        else:
            self.retranslateUiEnglish(MainWindow)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def Update(self):
        self.label.adjustSize()
        #self.ApplySM64.adjustSize()
        #self.ApplyAdd.adjustSize()
        #self.groupBox.adjustSize()
        #self.groupBox_2.adjustSize()
        self.menuHelp.adjustSize()
        #self.menuLanguage.adjustSize()
        #self.Refresh.adjustSize()
        #self.SwitchItemsButton.adjustSize()
        self.menuOptions.adjustSize()
    
    def RefreshEyeList(self):
        EyeFolders = os.listdir("eyes\\")
        CHMBFolders = os.listdir("chmb\\")
        self.listWidget.clear()
        if self.Mode == "Eyes":
            self.listWidget.addItems(EyeFolders)
        else:
            self.listWidget.addItems(CHMBFolders)
        self.listWidget.clearSelection()
        try:
            #self.ApplySM64.clicked.disconnect()
            #self.ApplyAdd.clicked.disconnect()
            self.ApplySM64.setEnabled(False)
            self.ApplyAdd.setEnabled(False)
            if self.Mode == "Eyes":
                self.SM64DisplayLabel1.setPixmap(QtGui.QPixmap("img\\PlaceHolderEye1.png"))
                self.SM64DisplayLabel2.setPixmap(QtGui.QPixmap("img\\PlaceHolderEye2.png"))
                self.SM64DisplayLabel3.setPixmap(QtGui.QPixmap("img\\PlaceHolderEye3.png"))
                self.AddDisplayLabel1.setPixmap(QtGui.QPixmap("img\\PlaceHolderEye1.png"))
                self.AddDisplayLabel2.setPixmap(QtGui.QPixmap("img\\PlaceHolderEye2.png"))
                self.AddDisplayLabel3.setPixmap(QtGui.QPixmap("img\\PlaceHolderEye3.png"))
            if self.Mode == "CHMB":
                self.SM64DisplayLabel1.setPixmap(QtGui.QPixmap("img\\PlaceHolderCap.png"))
                self.SM64DisplayLabel2.setPixmap(QtGui.QPixmap("img\\PlaceHolderHair.png"))
                self.SM64DisplayLabel3.setPixmap(QtGui.QPixmap("img\\PlaceHolderMustache.png"))
                self.SM64DisplayLabel4.setPixmap(QtGui.QPixmap("img\\PlaceHolderButton.png"))
                self.AddDisplayLabel1.setPixmap(QtGui.QPixmap("img\\PlaceHolderCap.png"))
                self.AddDisplayLabel2.setPixmap(QtGui.QPixmap("img\\PlaceHolderHair.png"))
                self.AddDisplayLabel3.setPixmap(QtGui.QPixmap("img\\PlaceHolderMustache.png"))
                self.AddDisplayLabel4.setPixmap(QtGui.QPixmap("img\\PlaceHolderButton.png"))
        except:
            pass

    def SwitchItems(self):
        if self.Mode == "Eyes":
            self.Mode = "CHMB"
            
            self.groupBox.setGeometry(QtCore.QRect(240, 10, 120, 452))
            self.groupBox_2.setGeometry(QtCore.QRect(380, 10, 120, 452))
            
            self.Update()

            self.SM64DisplayLabel1.setPixmap(QtGui.QPixmap("img\\PlaceHolderCap.png"))
            self.SM64DisplayLabel2.setPixmap(QtGui.QPixmap("img\\PlaceHolderHair.png"))
            self.SM64DisplayLabel3.setPixmap(QtGui.QPixmap("img\\PlaceHolderMustache.png"))
            self.SM64DisplayLabel4.setPixmap(QtGui.QPixmap("img\\PlaceHolderButton.png"))

            self.AddDisplayLabel1.setPixmap(QtGui.QPixmap("img\\PlaceHolderCap.png"))
            self.AddDisplayLabel2.setPixmap(QtGui.QPixmap("img\\PlaceHolderHair.png"))
            self.AddDisplayLabel3.setPixmap(QtGui.QPixmap("img\\PlaceHolderMustache.png"))
            self.AddDisplayLabel4.setPixmap(QtGui.QPixmap("img\\PlaceHolderButton.png"))
            
        else:
            self.Mode = "Eyes"
            
            self.groupBox.setGeometry(QtCore.QRect(240, 10, 120, 351))
            self.groupBox_2.setGeometry(QtCore.QRect(380, 10, 120, 351))

            self.Update()

            self.SM64DisplayLabel1.setPixmap(QtGui.QPixmap("img\\PlaceHolderEye1.png"))
            self.SM64DisplayLabel2.setPixmap(QtGui.QPixmap("img\\PlaceHolderEye2.png"))
            self.SM64DisplayLabel3.setPixmap(QtGui.QPixmap("img\\PlaceHolderEye3.png"))

            self.AddDisplayLabel1.setPixmap(QtGui.QPixmap("img\\PlaceHolderEye1.png"))
            self.AddDisplayLabel2.setPixmap(QtGui.QPixmap("img\\PlaceHolderEye2.png"))
            self.AddDisplayLabel3.setPixmap(QtGui.QPixmap("img\\PlaceHolderEye3.png"))
        self.RefreshEyeList()
        
        if Option.Language == "English":
                self.retranslateUiEnglish(MainWindow)
                self.Update()

        elif Option.Language == "Ukrainian":
                self.retranslateUiUkrainian(MainWindow)
                self.Update()
        
        elif Option.Language == "Russian":
                self.retranslateUiRussian(MainWindow)
                self.Update()
        
        elif Option.Language == "KazakhCyrillic":
                self.retranslateUiKazakhCyrillic(MainWindow)
                self.Update()
        
        elif Option.Language == "KazakhLatin":
                self.retranslateUiKazakhLatin(MainWindow)
                self.Update()
        
        else:
            self.retranslateUiEnglish(MainWindow)

        
        """


        I sincerely apologize for all the mess you are about to see below, I tried to optimize some of it, but to no avail :(


        """
        

    def OnSelectionChanged(self, FolderName):
        CheckSM64 = 0
        CheckAdd = 0
        if self.Mode == "Eyes":
            
            if os.path.exists("eyes\\{}\\{}.png".format(FolderName, Option.Eyes1)):
                self.SM64DisplayLabel1.setPixmap(QtGui.QPixmap("eyes\\{}\\{}.png".format(FolderName, Option.Eyes1)))
                CheckSM64 += 1
            else:
                self.SM64DisplayLabel1.setPixmap(QtGui.QPixmap("img\\PlaceHolderEye1.png"))
            
            if os.path.exists("eyes\\{}\\{}.png".format(FolderName, Option.Eyes2)):
                self.SM64DisplayLabel2.setPixmap(QtGui.QPixmap("eyes\\{}\\{}.png".format(FolderName, Option.Eyes2)))
                CheckSM64 += 1
            else:
                self.SM64DisplayLabel2.setPixmap(QtGui.QPixmap("img\\PlaceHolderEye2.png"))
                
            if os.path.exists("eyes\\{}\\{}.png".format(FolderName, Option.Eyes3)):
                self.SM64DisplayLabel3.setPixmap(QtGui.QPixmap("eyes\\{}\\{}.png".format(FolderName, Option.Eyes3)))
                CheckSM64 += 1
            else:
                self.SM64DisplayLabel3.setPixmap(QtGui.QPixmap("img\\PlaceHolderEye3.png"))
                
            
            if os.path.exists("eyes\\{}\\{}.png".format(FolderName, Option.AddEyes1)):
                self.AddDisplayLabel1.setPixmap(QtGui.QPixmap("eyes\\{}\\{}.png".format(FolderName, Option.AddEyes1)))
                CheckAdd += 1
            else:
                self.AddDisplayLabel1.setPixmap(QtGui.QPixmap("img\\PlaceHolderEye1.png"))
            
            if os.path.exists("eyes\\{}\\{}.png".format(FolderName, Option.AddEyes2)):
                self.AddDisplayLabel2.setPixmap(QtGui.QPixmap("eyes\\{}\\{}.png".format(FolderName, Option.AddEyes2)))
                CheckAdd += 1
            else:
                self.AddDisplayLabel2.setPixmap(QtGui.QPixmap("img\\PlaceHolderEye2.png"))
                
            if os.path.exists("eyes\\{}\\{}.png".format(FolderName, Option.AddEyes3)):
                self.AddDisplayLabel3.setPixmap(QtGui.QPixmap("eyes\\{}\\{}.png".format(FolderName, Option.AddEyes3)))
                CheckAdd += 1
            else:
                self.AddDisplayLabel3.setPixmap(QtGui.QPixmap("img\\PlaceHolderEye3.png"))
        
        else:
            if os.path.exists("chmb\\{}\\{}.png".format(FolderName, Option.Cap)):
                self.SM64DisplayLabel1.setPixmap(QtGui.QPixmap("chmb\\{}\\{}.png".format(FolderName, Option.Cap)))
                CheckSM64 += 1
            else:
                self.SM64DisplayLabel1.setPixmap(QtGui.QPixmap("img\\PlaceHolderCap.png"))
            
            if os.path.exists("chmb\\{}\\{}.png".format(FolderName, Option.Hair)):
                self.SM64DisplayLabel2.setPixmap(QtGui.QPixmap("chmb\\{}\\{}.png".format(FolderName, Option.Hair)))
                CheckSM64 += 1
            else:
                self.SM64DisplayLabel2.setPixmap(QtGui.QPixmap("img\\PlaceHolderHair.png"))
            
            if os.path.exists("chmb\\{}\\{}.png".format(FolderName, Option.Mustache)):
                self.SM64DisplayLabel3.setPixmap(QtGui.QPixmap("chmb\\{}\\{}.png".format(FolderName, Option.Mustache)))
                CheckSM64 += 1
            else:
                self.SM64DisplayLabel3.setPixmap(QtGui.QPixmap("img\\PlaceHolderMustache.png"))
            
            if os.path.exists("chmb\\{}\\{}.png".format(FolderName, Option.Button)):
                self.SM64DisplayLabel4.setPixmap(QtGui.QPixmap("chmb\\{}\\{}.png".format(FolderName, Option.Button)))
                CheckSM64 += 1
            else:
                self.SM64DisplayLabel4.setPixmap(QtGui.QPixmap("img\\PlaceHolderButton.png"))
                
                
            if os.path.exists("chmb\\{}\\{}.png".format(FolderName, Option.AddCap)):
                self.AddDisplayLabel1.setPixmap(QtGui.QPixmap("chmb\\{}\\{}.png".format(FolderName, Option.AddCap)))
                CheckAdd += 1
            else:
                self.AddDisplayLabel1.setPixmap(QtGui.QPixmap("img\\PlaceHolderCap.png"))
            
            if os.path.exists("chmb\\{}\\{}.png".format(FolderName, Option.AddHair)):
                self.AddDisplayLabel2.setPixmap(QtGui.QPixmap("chmb\\{}\\{}.png".format(FolderName, Option.AddHair)))
                CheckAdd += 1
            else:
                self.AddDisplayLabel2.setPixmap(QtGui.QPixmap("img\\PlaceHolderHair.png"))
            
            if os.path.exists("chmb\\{}\\{}.png".format(FolderName, Option.AddMustache)):
                self.AddDisplayLabel3.setPixmap(QtGui.QPixmap("chmb\\{}\\{}.png".format(FolderName, Option.AddMustache)))
                CheckAdd += 1
            else:
                self.AddDisplayLabel3.setPixmap(QtGui.QPixmap("img\\PlaceHolderMustache.png"))
            
            if os.path.exists("chmb\\{}\\{}.png".format(FolderName, Option.AddButton)):
                self.AddDisplayLabel4.setPixmap(QtGui.QPixmap("chmb\\{}\\{}.png".format(FolderName, Option.AddButton)))
                CheckAdd += 1
            else:
                self.AddDisplayLabel4.setPixmap(QtGui.QPixmap("img\\PlaceHolderButton.png"))
                
        if CheckSM64 > 0:
            self.ApplySM64.setEnabled(True)
        else:
            self.ApplySM64.setEnabled(False)
        if CheckAdd > 0:
            self.ApplyAdd.setEnabled(True)
        else:
            self.ApplyAdd.setEnabled(False)
            

    def CopyEyes(self, Type, FolderName):
        if self.Mode == "Eyes":
            if Type == "SM64Dir":
                Path = Option.SM64Dir
                try:
                    shutil.copyfile("eyes\\{}\\{}.png".format(FolderName, Option.Eyes1), "{}{}.png".format(Path, Option.Eyes1))
                except:
                    pass
                try:
                    shutil.copyfile("eyes\\{}\\{}.png".format(FolderName, Option.Eyes2), "{}{}.png".format(Path, Option.Eyes2))
                except:
                    pass
                try:
                    shutil.copyfile("eyes\\{}\\{}.png".format(FolderName, Option.Eyes3), "{}{}.png".format(Path, Option.Eyes3))
                except:
                    pass
            if Type == "AddDir":
                Path = Option.AddDir
                try:
                    shutil.copyfile("eyes\\{}\\{}.png".format(FolderName, Option.AddEyes1), "{}{}.png".format(Path, Option.AddEyes1))
                except:
                    pass
                try:
                    shutil.copyfile("eyes\\{}\\{}.png".format(FolderName, Option.AddEyes2), "{}{}.png".format(Path, Option.AddEyes2))
                except:
                    pass
                try:
                    shutil.copyfile("eyes\\{}\\{}.png".format(FolderName, Option.AddEyes3), "{}{}.png".format(Path, Option.AddEyes3))
                except:
                    pass

        else:
            if Type == "SM64Dir":
                Path = Option.SM64Dir
                try:
                    shutil.copyfile("chmb\\{}\\{}.png".format(FolderName, Option.Cap), "{}{}.png".format(Path, Option.Cap))
                except:
                    pass
                try:
                    shutil.copyfile("chmb\\{}\\{}.png".format(FolderName, Option.Hair), "{}{}.png".format(Path, Option.Hair))
                except:
                    pass
                try:
                    shutil.copyfile("chmb\\{}\\{}.png".format(FolderName, Option.Mustache), "{}{}.png".format(Path, Option.Mustache))
                except:
                    pass
                try:
                    shutil.copyfile("chmb\\{}\\{}.png".format(FolderName, Option.Button), "{}{}.png".format(Path, Option.Button))
                except:
                    pass
                
            if Type == "AddDir":
                Path = Option.AddDir
                try:
                    shutil.copyfile("chmb\\{}\\{}.png".format(FolderName, Option.AddCap), "{}{}.png".format(Path, Option.AddCap))
                except:
                    pass
                try:
                    shutil.copyfile("chmb\\{}\\{}.png".format(FolderName, Option.AddHair), "{}{}.png".format(Path, Option.AddHair))
                except:
                    pass
                try:
                    shutil.copyfile("chmb\\{}\\{}.png".format(FolderName, Option.AddMustache), "{}{}.png".format(Path, Option.AddMustache))
                except:
                    pass
                try:
                    shutil.copyfile("chmb\\{}\\{}.png".format(FolderName, Option.AddButton), "{}{}.png".format(Path, Option.AddButton))
                except:
                    pass

    def ItemChosen(self):
        self.ApplySM64.clicked.connect(lambda: self.CopyEyes("SM64Dir", self.listWidget.currentItem().text()))
        self.ApplyAdd.clicked.connect(lambda: self.CopyEyes("AddDir", self.listWidget.currentItem().text()))
        self.OnSelectionChanged(self.listWidget.currentItem().text())

    def OpenSM64(self):
        os.startfile(Option.SM64Dir)

    def OpenAdd(self):
        os.startfile(Option.AddDir)

    def OpenKataraktaFolder(self):
        os.startfile(os.getcwd())

    def ClearSM64(self):
        try:
            os.remove("{}{}.png".format(Option.SM64Dir, Option.Eyes1))
        except:
            pass
        try:
            os.remove("{}{}.png".format(Option.SM64Dir, Option.Eyes2))
        except:
            pass
        try:
            os.remove("{}{}.png".format(Option.SM64Dir, Option.Eyes3))
        except:
            pass
        try:
            os.remove("{}{}.png".format(Option.SM64Dir, Option.Cap))
        except:
            pass
        try:
            os.remove("{}{}.png".format(Option.SM64Dir, Option.Hair))
        except:
            pass
        try:
            os.remove("{}{}.png".format(Option.SM64Dir, Option.Mustache))
        except:
            pass
        try:
            os.remove("{}{}.png".format(Option.SM64Dir, Option.Button))
        except:
            pass
        
    def ClearAdd(self):
        try:
            os.remove("{}{}.png".format(Option.AddDir, Option.AddEyes1))
        except:
            pass
        try:
            os.remove("{}{}.png".format(Option.AddDir, Option.AddEyes2))
        except:
            pass
        try:
            os.remove("{}{}.png".format(Option.AddDir, Option.AddEyes3))
        except:
            pass
        try:
            os.remove("{}{}.png".format(Option.AddDir, Option.AddCap))
        except:
            pass
        try:
            os.remove("{}{}.png".format(Option.AddDir, Option.AddHair))
        except:
            pass
        try:
            os.remove("{}{}.png".format(Option.AddDir, Option.AddMustache))
        except:
            pass
        try:
            os.remove("{}{}.png".format(Option.AddDir, Option.AddButton))
        except:
            pass

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
        self.label.setText(_translate("MainWindow", "Found folders"))
        self.ApplySM64.setText(_translate("MainWindow", "Apply SM64"))
        self.ApplyAdd.setText(_translate("MainWindow", "Apply Additional"))
        self.groupBox.setTitle(_translate("MainWindow", "SM64"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Additional"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        #self.menuLanguage.setTitle(_translate("MainWindow", "Language"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        #self.actionEnglish.setText(_translate("MainWindow", "English"))
        #self.actionUkrainian.setText(_translate("MainWindow", "Українська"))
        #self.actionRussian.setText(_translate("MainWindow", "Русский"))
        if self.Mode == "Eyes":
            self.ApplySM64.setGeometry(QtCore.QRect(239, 364, 122, 23))
            self.ApplyAdd.setGeometry(QtCore.QRect(379, 364, 122, 23))
        else:
            self.ApplySM64.setGeometry(QtCore.QRect(331, 465, 170, 23))
            self.ApplyAdd.setGeometry(QtCore.QRect(331, 489, 170, 23))
        self.Refresh.setText(_translate("MainWindow", "Refresh"))
        self.SwitchItemsButton.setText(_translate("MainWindow", "Switch"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.submenuHiRes.setTitle(_translate("MainWindow", "Hi-res folders"))
        self.HiResClearSM64.setText(_translate("MainWindow", "Clear SM64"))
        self.HiResClearAdd.setText(_translate("MainWindow", "Clear Additional"))
        self.HiResOpenSM64.setText(_translate("MainWindow", "Open SM64"))
        self.HiResOpenAdd.setText(_translate("MainWindow", "Open Additional"))
        self.actionOpenKataraktaFolder.setText(_translate("MainWindow", "Open katarakta folder"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionOpenCcconv.setText(_translate("MainWindow", "Colorcode Converter"))
        self.actionStayOnTop.setText(_translate("MainWindow", "Stay on Top"))
        self.actionUpdate.setText(_translate("MainWindow", "Check for Updates"))

    def retranslateUiUkrainian(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "katarakta {} ({})".format(AppVersion, AppEdition)))
        self.label.setText(_translate("MainWindow", "Знайдені папки"))
        self.ApplySM64.setText(_translate("MainWindow", "Застосувати SM64"))
        self.ApplyAdd.setText(_translate("MainWindow", "Застосувати додаткове"))
        self.groupBox.setTitle(_translate("MainWindow", "SM64"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Додаткове"))
        self.menuHelp.setTitle(_translate("MainWindow", "Допомога"))
        #self.menuLanguage.setTitle(_translate("MainWindow", "Мова"))
        self.actionAbout.setText(_translate("MainWindow", "Про програму"))
        #self.actionEnglish.setText(_translate("MainWindow", "English"))
        #self.actionUkrainian.setText(_translate("MainWindow", "Українська"))
        #self.actionRussian.setText(_translate("MainWindow", "Русский"))
        if self.Mode == "Eyes":
            self.ApplySM64.setGeometry(QtCore.QRect(239, 364, 122, 23))
            self.ApplyAdd.setGeometry(QtCore.QRect(362, 364, 139, 23))
        else:
            self.ApplySM64.setGeometry(QtCore.QRect(331, 465, 170, 23))
            self.ApplyAdd.setGeometry(QtCore.QRect(331, 489, 170, 23))
        self.Refresh.setText(_translate("MainWindow", "Оновити"))
        self.SwitchItemsButton.setText(_translate("MainWindow", "Перемкнути"))
        self.menuOptions.setTitle(_translate("MainWindow", "Опції"))
        self.submenuHiRes.setTitle(_translate("MainWindow", "Hi-res папки"))
        self.HiResClearSM64.setText(_translate("MainWindow", "Очистити SM64"))
        self.HiResClearAdd.setText(_translate("MainWindow", "Очистити додаткове"))
        self.HiResOpenSM64.setText(_translate("MainWindow", "Відкрити папку SM64"))
        self.HiResOpenAdd.setText(_translate("MainWindow", "Відкрити додаткову папку"))
        self.actionOpenKataraktaFolder.setText(_translate("MainWindow", "Відкрити папку katarakta"))
        #self.HiResViewSM64.setText(_translate("MainWindow", "Переглянути папку SM64"))
        #self.HiResViewAdd.setText(_translate("MainWindow", "Переглянути додаткову папку"))
        self.actionSettings.setText(_translate("MainWindow", "Налаштування"))
        self.actionOpenCcconv.setText(_translate("MainWindow", "Конвертер колірних кодів"))
        self.actionStayOnTop.setText(_translate("MainWindow", "Завжди зверху"))
        self.actionUpdate.setText(_translate("MainWindow", "Перевірка на оновлення"))

    def retranslateUiRussian(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "katarakta {} ({})".format(AppVersion, AppEdition)))
        self.label.setText(_translate("MainWindow", "Найденные папки"))
        self.ApplySM64.setText(_translate("MainWindow", "Применить SM64"))
        self.ApplyAdd.setText(_translate("MainWindow", "Применить дополнительное"))
        self.groupBox.setTitle(_translate("MainWindow", "SM64"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Дополнительное"))
        self.menuHelp.setTitle(_translate("MainWindow", "Помощь"))
        #self.menuLanguage.setTitle(_translate("MainWindow", "Язык"))
        self.actionAbout.setText(_translate("MainWindow", "О программе"))
        #self.actionEnglish.setText(_translate("MainWindow", "English"))
        #self.actionUkrainian.setText(_translate("MainWindow", "Українська"))
        #self.actionRussian.setText(_translate("MainWindow", "Русский"))
        if self.Mode == "Eyes":
            self.ApplySM64.setGeometry(QtCore.QRect(239, 364, 102, 23))
            self.ApplyAdd.setGeometry(QtCore.QRect(342, 364, 159, 23))
        else:
            self.ApplySM64.setGeometry(QtCore.QRect(331, 465, 170, 23))
            self.ApplyAdd.setGeometry(QtCore.QRect(331, 489, 170, 23))
        self.Refresh.setText(_translate("MainWindow", "Обновить"))
        self.SwitchItemsButton.setText(_translate("MainWindow", "Переключить"))
        self.menuOptions.setTitle(_translate("MainWindow", "Опции"))
        self.submenuHiRes.setTitle(_translate("MainWindow", "Hi-res папки"))
        self.HiResClearSM64.setText(_translate("MainWindow", "Очистить SM64"))
        self.HiResClearAdd.setText(_translate("MainWindow", "Очистить дополнительное"))
        self.HiResOpenSM64.setText(_translate("MainWindow", "Открыть папку SM64"))
        self.HiResOpenAdd.setText(_translate("MainWindow", "Открыть дополнительную папку"))
        self.actionOpenKataraktaFolder.setText(_translate("MainWindow", "Открыть папку katarakta"))
        self.actionSettings.setText(_translate("MainWindow", "Настройки"))
        self.actionOpenCcconv.setText(_translate("MainWindow", "Конвертер цветовых кодов"))
        self.actionStayOnTop.setText(_translate("MainWindow", "Всегда сверху"))
        self.actionUpdate.setText(_translate("MainWindow", "Проверка на обновления"))

    def retranslateUiKazakhCyrillic(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "katarakta {} ({})".format(AppVersion, AppEdition)))
        self.label.setText(_translate("MainWindow", "Табылған қалталар"))
        self.ApplySM64.setText(_translate("MainWindow", "SM64 қолдаңуга"))
        self.ApplyAdd.setText(_translate("MainWindow", "Қосымша қолдану"))
        self.groupBox.setTitle(_translate("MainWindow", "SM64"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Қосымша"))
        self.menuHelp.setTitle(_translate("MainWindow", "Көмек"))
        #self.menuLanguage.setTitle(_translate("MainWindow", "Язык"))
        self.actionAbout.setText(_translate("MainWindow", "Бағдаларлама туралы"))
        #self.actionEnglish.setText(_translate("MainWindow", "English"))
        #self.actionUkrainian.setText(_translate("MainWindow", "Українська"))
        #self.actionRussian.setText(_translate("MainWindow", "Русский"))
        if self.Mode == "Eyes":
            self.ApplySM64.setGeometry(QtCore.QRect(239, 364, 122, 23))
            self.ApplyAdd.setGeometry(QtCore.QRect(379, 364, 122, 23))
        else:
            self.ApplySM64.setGeometry(QtCore.QRect(331, 465, 170, 23))
            self.ApplyAdd.setGeometry(QtCore.QRect(331, 489, 170, 23))
        self.Refresh.setText(_translate("MainWindow", "Жаңарту"))
        self.SwitchItemsButton.setText(_translate("MainWindow", "Аустыру"))
        self.menuOptions.setTitle(_translate("MainWindow", "Опциялар"))
        self.submenuHiRes.setTitle(_translate("MainWindow", "Hi-res қалталар"))
        self.HiResClearSM64.setText(_translate("MainWindow", "SM64 тазарту"))
        self.HiResClearAdd.setText(_translate("MainWindow", "Қосымшаны тазарту"))
        self.HiResOpenSM64.setText(_translate("MainWindow", "SM64 қалта ашығу"))
        self.HiResOpenAdd.setText(_translate("MainWindow", "Қосымша қалта ашығу"))
        self.actionOpenKataraktaFolder.setText(_translate("MainWindow", "Katarakta қалтаны ашыңыз"))
        self.actionSettings.setText(_translate("MainWindow", "Параметрлер"))
        self.actionOpenCcconv.setText(_translate("MainWindow", "Түс кодын түрлендіргіш"))
        self.actionStayOnTop.setText(_translate("MainWindow", "Әрқашан биікте"))
        self.actionUpdate.setText(_translate("MainWindow", "Жаңартуларды тексеріңіз"))

    def retranslateUiKazakhLatin(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "katarakta {} ({})".format(AppVersion, AppEdition)))
        self.label.setText(_translate("MainWindow", "Tabylğan qaltalar"))
        self.ApplySM64.setText(_translate("MainWindow", "SM64 qoldañuga"))
        self.ApplyAdd.setText(_translate("MainWindow", "Qosymşa qoldanu"))
        self.groupBox.setTitle(_translate("MainWindow", "SM64"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Qosymşa"))
        self.menuHelp.setTitle(_translate("MainWindow", "Kömek"))
        #self.menuLanguage.setTitle(_translate("MainWindow", "Язык"))
        self.actionAbout.setText(_translate("MainWindow", "Bağdalarlama turaly"))
        #self.actionEnglish.setText(_translate("MainWindow", "English"))
        #self.actionUkrainian.setText(_translate("MainWindow", "Українська"))
        #self.actionRussian.setText(_translate("MainWindow", "Русский"))
        if self.Mode == "Eyes":
            self.ApplySM64.setGeometry(QtCore.QRect(239, 364, 122, 23))
            self.ApplyAdd.setGeometry(QtCore.QRect(379, 364, 122, 23))
        else:
            self.ApplySM64.setGeometry(QtCore.QRect(331, 465, 170, 23))
            self.ApplyAdd.setGeometry(QtCore.QRect(331, 489, 170, 23))
        self.Refresh.setText(_translate("MainWindow", "Jañartu"))
        self.SwitchItemsButton.setText(_translate("MainWindow", "Austyru"))
        self.menuOptions.setTitle(_translate("MainWindow", "Opsialar"))
        self.submenuHiRes.setTitle(_translate("MainWindow", "Hi-res qaltalar"))
        self.HiResClearSM64.setText(_translate("MainWindow", "SM64 tazartu"))
        self.HiResClearAdd.setText(_translate("MainWindow", "Qosymşany tazartu"))
        self.HiResOpenSM64.setText(_translate("MainWindow", "SM64 qalta aşyğu"))
        self.HiResOpenAdd.setText(_translate("MainWindow", "Qosymşa qalta aşyğu"))
        self.actionOpenKataraktaFolder.setText(_translate("MainWindow", "Katarakta qaltany aşyñyz"))
        self.actionSettings.setText(_translate("MainWindow", "Parametrler"))
        self.actionOpenCcconv.setText(_translate("MainWindow", "Tüs kodyn türlendırgış"))
        self.actionStayOnTop.setText(_translate("MainWindow", "Ärqaşan biıkte"))
        self.actionUpdate.setText(_translate("MainWindow", "Jañartulardy tekserıñız"))

class Ui_AboutWindow(object):
    def setupUi(self, AboutWindow):
        AboutWindow.setObjectName("About katarakta")
        AboutWindow.resize(520, 336)
        AboutWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.World))
        AboutWindow.setWindowFlags(AboutWindow.windowFlags() | Qt.WindowStaysOnTopHint)
        self.LabelName = QtWidgets.QLabel(AboutWindow)
        self.LabelName.setGeometry(QtCore.QRect(240, 20, 271, 71))
        self.LabelName.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setItalic(False)
        self.LabelName.setFont(font)
        self.LabelName.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.World))
        self.LabelName.setScaledContents(False)
        self.LabelName.setObjectName("LabelName")
        self.LabelVersion = QtWidgets.QLabel(AboutWindow)
        self.LabelVersion.setGeometry(QtCore.QRect(240, 90, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.LabelVersion.setFont(font)
        self.LabelVersion.setObjectName("LabelVersion")
        self.LabelAuthor = QtWidgets.QLabel(AboutWindow)
        self.LabelAuthor.setGeometry(QtCore.QRect(20, 230, 481, 16))
        self.LabelAuthor.setObjectName("LabelAuthor")
        self.LabelAuthor.setOpenExternalLinks(True)
        self.LabelIcon = QtWidgets.QLabel(AboutWindow)
        self.LabelIcon.setGeometry(QtCore.QRect(20, 20, 201, 201))
        self.LabelIcon.setText("")
        self.LabelIcon.setPixmap(QtGui.QPixmap("img\\768icon.png"))
        self.LabelIcon.setScaledContents(True)
        self.LabelIcon.setObjectName("LabelIcon")
        self.LabelAddInfo = QtWidgets.QLabel(AboutWindow)
        self.LabelAddInfo.setGeometry(QtCore.QRect(240, 145, 481, 16))
        self.LabelAddInfo.setObjectName("AddInfo")
        self.LabelAddInfo.setOpenExternalLinks(True)
        AboutWindow.setFixedSize(AboutWindow.size())
        
        AboutWindow.setWindowIcon(QtGui.QIcon("img\\Icon.png"))

        if Option.Language == "English":
            self.retranslateUiEnglish(AboutWindow)
            self.Update()

        elif Option.Language == "Ukrainian":
            self.retranslateUiUkrainian(AboutWindow)
            self.Update()
        
        elif Option.Language == "Russian":
            self.retranslateUiRussian(AboutWindow)
            self.Update()
        
        elif Option.Language == "KazakhCyrillic":
            self.retranslateUiKazakhCyrillic(AboutWindow)
            self.Update()
        
        elif Option.Language == "KazakhLatin":
            self.retranslateUiKazakhLatin(AboutWindow)
            self.Update()
        
        else:
            self.retranslateUiEnglish(MainWindow)
        
        QtCore.QMetaObject.connectSlotsByName(AboutWindow)
        
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
        self.LabelAuthor.setText(_translate("AboutWindow", "By DanilAstroid (<a href = 'https://github.com/vazhka-dolya/'>GitHub</a>).<br><br>Thanks to these people for testing katarakta:<br>@Blender_Blenderovych (<a href = 'https://www.youtube.com/channel/UCGxro_VNeDQBY9k8_jitMCw'>YouTube</a>)<br>@SDRM45 (<a href = 'https://www.youtube.com/channel/UC-3gc0FmQA2_Z2-MIS5sZNQ'>YouTube</a>)<br><br>Kazakh translation by @rmsm6418 (<a href = 'https://www.youtube.com/channel/UCH8LNphoKyKREMgS2ZVU1Ng'>YouTube</a>)"))
        self.LabelAddInfo.setText(_translate("AboutWindow", "This project uses the GNU General Public License v3.0<br><br><a href = 'https://github.com/vazhka-dolya/katarakta/issues/'>Report issues</a>"))

    def retranslateUiUkrainian(self, AboutWindow):
        _translate = QtCore.QCoreApplication.translate
        AboutWindow.setWindowTitle(_translate("AboutWindow", "Про katarakta"))
        self.LabelName.setText(_translate("AboutWindow", "katarakta"))
        self.LabelVersion.setText(_translate("AboutWindow", "Версія: {}\nРедакція: {}".format(AppVersion, AppEdition)))
        self.LabelAuthor.setText(_translate("AboutWindow", "Від DanilAstroid (<a href = 'https://github.com/vazhka-dolya/'>GitHub</a>).<br><br>Висловлюється подяка цим людям за тестування katarakta:<br>@Blender_Blenderovych (<a href = 'https://www.youtube.com/channel/UCGxro_VNeDQBY9k8_jitMCw'>YouTube</a>)<br>@SDRM45 (<a href = 'https://www.youtube.com/channel/UC-3gc0FmQA2_Z2-MIS5sZNQ'>YouTube</a>)<br><br>Казахський переклад від @rmsm6418 (<a href = 'https://www.youtube.com/channel/UCH8LNphoKyKREMgS2ZVU1Ng'>YouTube</a>)"))
        self.LabelAddInfo.setText(_translate("AboutWindow", "Цей проект використовує ліцензію<br>GNU General Public License v3.0<br><a href = 'https://github.com/vazhka-dolya/katarakta/issues/'>Повідомити про проблему</a>"))
    
    def retranslateUiRussian(self, AboutWindow):
        _translate = QtCore.QCoreApplication.translate
        AboutWindow.setWindowTitle(_translate("AboutWindow", "О katarakta"))
        self.LabelName.setText(_translate("AboutWindow", "katarakta"))
        self.LabelVersion.setText(_translate("AboutWindow", "Версия: {}\nРедакция: {}".format(AppVersion, AppEdition)))
        self.LabelAuthor.setText(_translate("AboutWindow", "От DanilAstroid (<a href = 'https://github.com/vazhka-dolya/'>GitHub</a>).<br><br>Выражается благодарность этим людям за тестирование katarakta:<br>@Blender_Blenderovych (<a href = 'https://www.youtube.com/channel/UCGxro_VNeDQBY9k8_jitMCw'>YouTube</a>)<br>@SDRM45 (<a href = 'https://www.youtube.com/channel/UC-3gc0FmQA2_Z2-MIS5sZNQ'>YouTube</a>)<br><br>Казахский перевод от @rmsm6418 (<a href = 'https://www.youtube.com/channel/UCH8LNphoKyKREMgS2ZVU1Ng'>YouTube</a>)"))
        self.LabelAddInfo.setText(_translate("AboutWindow", "Этот проект использует лицензию<br>GNU General Public License v3.0<br><a href = 'https://github.com/vazhka-dolya/katarakta/issues/'>Сообщить о проблеме</a>"))
    
    def retranslateUiKazakhCyrillic(self, AboutWindow):
        _translate = QtCore.QCoreApplication.translate
        AboutWindow.setWindowTitle(_translate("AboutWindow", "katarakta туралы"))
        self.LabelName.setText(_translate("AboutWindow", "katarakta"))
        self.LabelVersion.setText(_translate("AboutWindow", "Нұсқа: {}\nРедакциялық: {}".format(AppVersion, AppEdition)))
        self.LabelAuthor.setText(_translate("AboutWindow", "Авторы DanilAstroid (<a href = 'https://github.com/vazhka-dolya/'>GitHub</a>).<br><br>katarakta сынағандары үшін осы адамдарға рахмет:<br>@Blender_Blenderovych (<a href = 'https://www.youtube.com/channel/UCGxro_VNeDQBY9k8_jitMCw'>YouTube</a>)<br>@SDRM45 (<a href = 'https://www.youtube.com/channel/UC-3gc0FmQA2_Z2-MIS5sZNQ'>YouTube</a>)<br><br>@rmsm6418 бойынша қазақша аударма (<a href = 'https://www.youtube.com/channel/UCH8LNphoKyKREMgS2ZVU1Ng'>YouTube</a>)"))
        self.LabelAddInfo.setText(_translate("AboutWindow", "Бұл жоба GNU General Public License v3.0<br>нұсқанын пайдаланады<br><a href = 'https://github.com/vazhka-dolya/katarakta/issues/'>Мәселе туралы хабарлау</a>"))
    
    def retranslateUiKazakhLatin(self, AboutWindow):
        _translate = QtCore.QCoreApplication.translate
        AboutWindow.setWindowTitle(_translate("AboutWindow", "katarakta turaly"))
        self.LabelName.setText(_translate("AboutWindow", "katarakta"))
        self.LabelVersion.setText(_translate("AboutWindow", "Nūsqa: {}\nRedaksialyq: {}".format(AppVersion, AppEdition)))
        self.LabelAuthor.setText(_translate("AboutWindow", "Avtory DanilAstroid (<a href = 'https://github.com/vazhka-dolya/'>GitHub</a>).<br><br>katarakta synağandary üşın osy adamdarğa rahmet:<br>@Blender_Blenderovych (<a href = 'https://www.youtube.com/channel/UCGxro_VNeDQBY9k8_jitMCw'>YouTube</a>)<br>@SDRM45 (<a href = 'https://www.youtube.com/channel/UC-3gc0FmQA2_Z2-MIS5sZNQ'>YouTube</a>)<br><br>@rmsm6418 boiynşa qazaqşa audarma (<a href = 'https://www.youtube.com/channel/UCH8LNphoKyKREMgS2ZVU1Ng'>YouTube</a>)"))
        self.LabelAddInfo.setText(_translate("AboutWindow", "Būl joba GNU General Public License v3.0<br>nūsqanyn paidalanady<br><a href = 'https://github.com/vazhka-dolya/katarakta/issues/'>Mäsele turaly habarlau</a>"))
        
        AboutWindow.show()

class Ui_UpdateWindow(object):
    def setupUi(self, UpdateWindow):
        if not UpdateWindow.objectName():
            UpdateWindow.setObjectName("UpdateWindow")
        UpdateWindow.resize(480, 336)
        UpdateWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.World))
        self.UpdateCheckLabel = QtWidgets.QLabel(UpdateWindow)
        self.UpdateCheckLabel.setObjectName("UpdateCheckLabel")
        self.UpdateCheckLabel.setGeometry(QtCore.QRect(90, 10, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.UpdateCheckLabel.setFont(font)
        self.YourVersionLabel = QtWidgets.QLabel(UpdateWindow)
        self.YourVersionLabel.setObjectName("YourVersionLabel")
        self.YourVersionLabel.setGeometry(QtCore.QRect(10, 70, 131, 21))
        font1 = QtGui.QFont()
        font1.setPointSize(12)
        self.YourVersionLabel.setFont(font1)
        self.LatestVersionLabel = QtWidgets.QLabel(UpdateWindow)
        self.LatestVersionLabel.setObjectName("LatestVersionLabel")
        self.LatestVersionLabel.setGeometry(QtCore.QRect(10, 95, 201, 61))
        self.LatestVersionLabel.setFont(font1)
        self.IconLabel = QtWidgets.QLabel(UpdateWindow)
        self.IconLabel.setObjectName("IconLabel")
        self.IconLabel.setGeometry(QtCore.QRect(10, 0, 71, 71))
        self.IconLabel.setPixmap(QPixmap("img/update256.png"))
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
        self.textBrowserDescription = QtWidgets.QLabel(UpdateWindow)
        self.textBrowserDescription.setObjectName("textBrowserDescription")
        self.textBrowserDescription.setGeometry(QtCore.QRect(10, 115, 460, 22))
        UpdateWindow.setFixedSize(UpdateWindow.size())

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

        if Option.Language == "English":
            self.retranslateUiEnglish(UpdateWindow)
            self.Update()

        elif Option.Language == "Ukrainian":
            self.retranslateUiUkrainian(UpdateWindow)
            self.Update()
        
        elif Option.Language == "Russian":
            self.retranslateUiRussian(UpdateWindow)
            self.Update()
        
        elif Option.Language == "KazakhCyrillic":
            self.retranslateUiKazakhCyrillic(UpdateWindow)
            self.Update()
        
        elif Option.Language == "KazakhLatin":
            self.retranslateUiKazakhLatin(UpdateWindow)
            self.Update()
        
        else:
            self.retranslateUiEnglish(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(UpdateWindow)
        
        try:
            UpdateWindow.setWindowIcon(QtGui.QIcon("img\\update64.png"))
        except:
            pass

        if Option.Language == "English":
            _translate = QtCore.QCoreApplication.translate
            self.retranslateUiEnglish(UpdateWindow)
            UpdateWindow.setWindowTitle(_translate("UpdateWindow", "Update Checker"))
            self.UpdateCheckLabel.setText("Update Checker")
            self.YourVersionLabel.setText("Your version: katarakta {}".format(str(AppVersion)))
            self.LatestVersionLabel.setText("Latest version on Github: {}".format(str(LatestVersion)))
            if IsLatestVersion == True:
                self.StatusLabel.setText("You have the latest version! <a href = 'https://github.com/vazhka-dolya/katarakta/releases'>All releases on GitHub</a>")
            elif IsLatestVersion == False:
                self.StatusLabel.setText("You have an outdated version! <a href = 'https://github.com/vazhka-dolya/katarakta/releases/latest'>Download latest release on GitHub</a>")
            else:
                self.StatusLabe.setText("Could not check for the latest version. <a href = 'https://github.com/vazhka-dolya/katarakta/releases>All releases on GitHub</a>")
            self.textBrowserDescription.setText("Update's changelog:")
            self.Update()

        elif Option.Language == "Ukrainian":
            _translate = QtCore.QCoreApplication.translate
            self.retranslateUiUkrainian(UpdateWindow)
            UpdateWindow.setWindowTitle(_translate("UpdateWindow", "Перевірка на оновлення"))
            self.UpdateCheckLabel.setText("Перевірка на оновлення")
            self.YourVersionLabel.setText("Ваша версія: katarakta {}".format(str(AppVersion)))
            self.LatestVersionLabel.setText("Остання версія на GitHub: {}".format(str(LatestVersion)))
            if IsLatestVersion == True:
                self.StatusLabel.setText("У Вас остання версія! <a href = 'https://github.com/vazhka-dolya/katarakta/releases'>Усі випуски на GitHub</a>")
            elif IsLatestVersion == False:
                self.StatusLabel.setText("У Вас застаріла версія! <a href = 'https://github.com/vazhka-dolya/katarakta/releases/latest'>Завантажити останню версію на GitHub</a>")
            else:
                self.StatusLabe.setText("Неможливо перевірити версію. <a href = 'https://github.com/vazhka-dolya/katarakta/releases'>Усі випуски на GitHub</a>")
            self.textBrowserDescription.setText("Список змін оновлення:")
            self.Update()
        
        elif Option.Language == "Russian":
            _translate = QtCore.QCoreApplication.translate
            self.retranslateUiRussian(UpdateWindow)
            UpdateWindow.setWindowTitle(_translate("UpdateWindow", "Проверка на обновления"))
            self.UpdateCheckLabel.setText("Проверка на обновления")
            self.YourVersionLabel.setText("Ваша версия: katarakta {}".format(str(AppVersion)))
            self.LatestVersionLabel.setText("Последняя версия на GitHub: {}".format(str(LatestVersion)))
            if IsLatestVersion == True:
                self.StatusLabel.setText("У Вас последняя версия! <a href = 'https://github.com/vazhka-dolya/katarakta/releases'>Все выпуски на GitHub</a>")
            elif IsLatestVersion == False:
                self.StatusLabel.setText("У Вас устаревшая версия! <a href = 'https://github.com/vazhka-dolya/katarakta/releases/latest'>Скачать последнюю версию на GitHub</a>")
            else:
                self.StatusLabe.setText("Невозможно проверить версию. <a href = 'https://github.com/vazhka-dolya/katarakta/releases'>Все выпуски на GitHub</a>")
            self.textBrowserDescription.setText("Список изменений:")
    
            self.Update()
        
        elif Option.Language == "KazakhCyrillic":
            _translate = QtCore.QCoreApplication.translate
            self.retranslateUiKazakhCyrillic(UpdateWindow)
            UpdateWindow.setWindowTitle(_translate("UpdateWindow", "Жаңартуларды тексеруге"))
            self.UpdateCheckLabel.setText("Жаңартуларды тексеруге")
            self.YourVersionLabel.setText("Сіздің нұсқаңыз: katarakta {}".format(str(AppVersion)))
            self.LatestVersionLabel.setText("GitHub сайтындағы соңғы нұсқасы: {}".format(str(LatestVersion)))
            if IsLatestVersion == True:
                self.StatusLabel.setText("Сізде соңғы нұсқа бар! <a href = 'https://github.com/vazhka-dolya/katarakta/releases'>GitHub сайтындағы барлық шығарылымдар</a>")
            elif IsLatestVersion == False:
                self.StatusLabel.setText("Сізде ескірген нұсқа бар! <a href = 'https://github.com/vazhka-dolya/katarakta/releases/latest'>GitHub сайтында соңғы нұсқаны жазу</a>")
            else:
                self.StatusLabe.setText("Нұсқаны тексеру мүмкін емес. <a href = 'https://github.com/vazhka-dolya/katarakta/releases'>GitHub сайтындағы барлық шығарылымдар</a>")
            self.textBrowserDescription.setText("Өзгерістер тізімі:")
    
            self.Update()
        
        elif Option.Language == "KazakhLatin":
            _translate = QtCore.QCoreApplication.translate
            self.retranslateUiKazakhLatin(UpdateWindow)
            UpdateWindow.setWindowTitle(_translate("UpdateWindow", "Özgerıster tızımı"))
            self.UpdateCheckLabel.setText("Özgerıster tızımı")
            self.YourVersionLabel.setText("Sızdıñ nūsqañyz: katarakta {}".format(str(AppVersion)))
            self.LatestVersionLabel.setText("GitHub saityndağy soñğy nūsqasy: {}".format(str(LatestVersion)))
            if IsLatestVersion == True:
                self.StatusLabel.setText("Sızde soñğy nūsqa bar! <a href = 'https://github.com/vazhka-dolya/katarakta/releases'>GitHub saityndağy barlyq şyğarylymdar</a>")
            elif IsLatestVersion == False:
                self.StatusLabel.setText("Sızde eskırgen nūsqa bar! <a href = 'https://github.com/vazhka-dolya/katarakta/releases/latest'>GitHub saitynda soñğy nūsqany jazu</a>")
            else:
                self.StatusLabe.setText("Nūsqany tekseru mümkın emes. <a href = 'https://github.com/vazhka-dolya/katarakta/releases'>GitHub saityndağy barlyq şyğarylymdar</a>")
            self.textBrowserDescription.setText("Özgerıster tızımı:")
    
            self.Update()
        
        else:
            self.retranslateUiEnglish(MainWindow)
        
        QtCore.QMetaObject.connectSlotsByName(UpdateWindow)
        
        UpdateWindow.setWindowFlags(UpdateWindow.windowFlags() | Qt.WindowStaysOnTopHint)
        UpdateWindow.show()
        
    def Update(self):
        self.UpdateCheckLabel.adjustSize()
        self.YourVersionLabel.adjustSize()
        self.LatestVersionLabel.adjustSize()
        self.StatusLabel.adjustSize()
    
    def retranslateUiEnglish(self, AboutWindow):
        _translate = QtCore.QCoreApplication.translate
        AboutWindow.setWindowTitle(_translate("UpdateWindow", "Update check"))
        
    def retranslateUiUkrainian(self, AboutWindow):
        _translate = QtCore.QCoreApplication.translate
        AboutWindow.setWindowTitle(_translate("UpdateWindow", "Перевірка на оновлення"))
        
    def retranslateUiRussian(self, AboutWindow):
        _translate = QtCore.QCoreApplication.translate
        AboutWindow.setWindowTitle(_translate("UpdateWindow", "Проверка на обновления"))
        
    def retranslateUiKazakhCyrillic(self, AboutWindow):
        _translate = QtCore.QCoreApplication.translate
        AboutWindow.setWindowTitle(_translate("UpdateWindow", "Жаңартуларды тексеруге"))
        
    def retranslateUiKazakhLatin(self, AboutWindow):
        _translate = QtCore.QCoreApplication.translate
        AboutWindow.setWindowTitle(_translate("UpdateWindow", "Özgerıster tızımı"))
    
class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        SettingsWindow.resize(550, 505)
        SettingsWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.World))
        SettingsWindow.setFixedSize(SettingsWindow.size())
        SettingsWindow.setWindowIcon(QtGui.QIcon("img\\Settings.png"))
        SettingsWindow.setWindowFlags(SettingsWindow.windowFlags() | Qt.WindowStaysOnTopHint)
            
        self.tabWidget = QtWidgets.QTabWidget(SettingsWindow)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 531, 461))
        self.tabWidget.setObjectName("tabWidget")
        self.TabGeneral = QtWidgets.QWidget()
        self.TabGeneral.setObjectName("TabGeneral")
        self.groupLanguage = QtWidgets.QGroupBox(self.TabGeneral)
        self.groupLanguage.setGeometry(QtCore.QRect(10, 0, 506, 91))
        self.groupLanguage.setObjectName("groupLanguage")
        font = QtGui.QFont()
        font.setPointSize(10)
        
        self.labelLanguage = QtWidgets.QLabel(self.groupLanguage)
        self.labelLanguage.setGeometry(QtCore.QRect(50, 20, 360, 31))
        self.labelLanguage.setFont(font)
        self.labelLanguage.setObjectName("labelLanguage")
        
        self.labelLanguageRestart = QtWidgets.QLabel(self.groupLanguage)
        self.labelLanguageRestart.setGeometry(QtCore.QRect(256, 48, 290, 44))
        self.labelLanguageRestart.setObjectName("labelLanguageRestart")
        
        self.comboLanguage = QtWidgets.QComboBox(self.groupLanguage)
        self.comboLanguage.setGeometry(QtCore.QRect(10, 60, 241, 22))
        self.comboLanguage.setObjectName("comboLanguage")
        
        self.comboLanguage.addItem("")
        self.comboLanguage.addItem("")
        self.comboLanguage.addItem("")
        self.comboLanguage.addItem("")
        self.comboLanguage.addItem("")
        
        _translate = QtCore.QCoreApplication.translate
        
        self.comboLanguage.setItemText(0, _translate("SettingsWindow", "English (United States)"))
        self.comboLanguage.setItemIcon(0, QIcon("img/LangEnglishUS.png"))
        self.comboLanguage.setItemText(1, _translate("SettingsWindow", "Українська (Україна)"))
        self.comboLanguage.setItemIcon(1, QIcon("img/LangUkrainian.png"))
        self.comboLanguage.setItemText(2, _translate("SettingsWindow", "Русский (Россия)"))
        self.comboLanguage.setItemIcon(2, QIcon("img/LangRussian.png"))
        self.comboLanguage.setItemText(3, _translate("SettingsWindow", "Қазақша (Қазақстан | Кириллица)"))
        self.comboLanguage.setItemIcon(3, QIcon("img/LangKazakhCyrillic.png"))
        self.comboLanguage.setItemText(4, _translate("SettingsWindow", "Qazaqşa (Qazaqstan | Latyn)"))
        self.comboLanguage.setItemIcon(4, QIcon("img/LangKazakhLatin.png"))
        
        self.labelFlagBackground = QtWidgets.QLabel(self.groupLanguage)
        self.labelFlagBackground.setGeometry(QtCore.QRect(7, 17, 37, 37))
        self.labelFlagBackground.setText("")
        self.labelFlagBackground.setScaledContents(True)
        self.labelFlagBackground.setObjectName("labelFlagBackground")
        self.labelFlagBackground.setPixmap(QtGui.QPixmap("img/FlagBackground.png"))
        
        self.labelLanguageFlag = QtWidgets.QLabel(self.groupLanguage)
        self.labelLanguageFlag.setGeometry(QtCore.QRect(10, 20, 31, 31))
        self.labelLanguageFlag.setText("")
        self.labelLanguageFlag.setScaledContents(True)
        self.labelLanguageFlag.setObjectName("labelLanguageFlag")

        if Option.Language == "English":
            self.comboLanguage.setCurrentIndex(0)
        elif Option.Language == "Ukrainian":
            self.comboLanguage.setCurrentIndex(1)
        elif Option.Language == "Russian":
            self.comboLanguage.setCurrentIndex(2)
        elif Option.Language == "KazakhCyrillic":
            self.comboLanguage.setCurrentIndex(3)
        elif Option.Language == "KazakhLatin":
            self.comboLanguage.setCurrentIndex(4)
        else:
            self.comboLanguage.setCurrentIndex(-1)

        def CheckLanguage():
            global ChosenLanguage
            if self.comboLanguage.currentIndex() == 0:
                self.labelLanguageFlag.setPixmap(QtGui.QPixmap("img/LangEnglishUS.png"))
                self.labelLanguage.setText(_translate("SettingsWindow", "English (United States)"))
                ChosenLanguage = "English"
            elif self.comboLanguage.currentIndex() == 1:
                self.labelLanguageFlag.setPixmap(QtGui.QPixmap("img/LangUkrainian.png"))
                self.labelLanguage.setText(_translate("SettingsWindow", "Українська (Україна)"))
                ChosenLanguage = "Ukrainian"
            elif self.comboLanguage.currentIndex() == 2:
                self.labelLanguageFlag.setPixmap(QtGui.QPixmap("img/LangRussian.png"))
                self.labelLanguage.setText(_translate("SettingsWindow", "Русский (Россия)"))
                ChosenLanguage = "Russian"
            elif self.comboLanguage.currentIndex() == 3:
                self.labelLanguageFlag.setPixmap(QtGui.QPixmap("img/LangKazakhCyrillic.png"))
                self.labelLanguage.setText(_translate("SettingsWindow", "Қазақша (Қазақстан | Кириллица)"))
                ChosenLanguage = "KazakhCyrillic"
            elif self.comboLanguage.currentIndex() == 4:
                self.labelLanguageFlag.setPixmap(QtGui.QPixmap("img/LangKazakhLatin.png"))
                self.labelLanguage.setText(_translate("SettingsWindow", "Qazaqşa (Qazaqstan | Latyn)"))
                ChosenLanguage = "KazakhLatin"
            else:
                self.labelLanguageFlag.setPixmap(QtGui.QPixmap("img/LangUnknown.png"))
                self.labelLanguage.setText(_translate("SettingsWindow", "Not detected, using English (United States)"))
                ChosenLanguage = "English"
            return ChosenLanguage

        CheckLanguage()
        self.comboLanguage.currentIndexChanged.connect(CheckLanguage)
        
        self.groupUpdates = QtWidgets.QGroupBox(self.TabGeneral)
        self.groupUpdates.setGeometry(QtCore.QRect(10, 90, 506, 101))
        self.groupUpdates.setObjectName("groupBox")
        self.checkUpdates = QtWidgets.QCheckBox(self.groupUpdates)
        self.checkUpdates.setGeometry(QtCore.QRect(10, 20, 501, 17))
        self.checkUpdates.setObjectName("checkBox")
        self.labelUpdates = QtWidgets.QLabel(self.groupUpdates)
        self.labelUpdates.setGeometry(QtCore.QRect(10, 40, 501, 51))
        self.labelUpdates.setObjectName("labelUpdates")
        
        self.groupMisc = QtWidgets.QGroupBox(self.TabGeneral)
        self.groupMisc.setGeometry(QtCore.QRect(10, 190, 506, 241))
        self.groupMisc.setObjectName("groupMisc")
        self.checkStayOnTop = QtWidgets.QCheckBox(self.groupMisc)
        self.checkStayOnTop.setGeometry(QtCore.QRect(10, 20, 501, 17))
        self.checkStayOnTop.setObjectName("checkStayOnTop")

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
        
        self.tabWidget.addTab(self.TabGeneral, "")
        self.TabTextures = QtWidgets.QWidget()
        self.TabTextures.setObjectName("TabTextures")
        self.groupPaths = QtWidgets.QGroupBox(self.TabTextures)
        self.groupPaths.setGeometry(QtCore.QRect(10, 0, 506, 121))
        self.groupPaths.setObjectName("groupPaths")
        
        self.lineHiResSM64 = QtWidgets.QLineEdit(self.groupPaths)
        self.lineHiResSM64.setGeometry(QtCore.QRect(10, 40, 486, 20))
        self.lineHiResSM64.setObjectName("lineHiResSM64")
        self.lineHiResSM64.setText(str(Option.SM64Dir))
        self.labelHiResSM64 = QtWidgets.QLabel(self.groupPaths)
        self.labelHiResSM64.setGeometry(QtCore.QRect(10, 20, 141, 16))
        self.labelHiResSM64.setObjectName("labelHiResSM64")
        
        self.labelHiResAdd = QtWidgets.QLabel(self.groupPaths)
        self.labelHiResAdd.setGeometry(QtCore.QRect(10, 70, 161, 16))
        self.labelHiResAdd.setObjectName("labelHiResAdd")
        self.lineHiResAdd = QtWidgets.QLineEdit(self.groupPaths)
        self.lineHiResAdd.setGeometry(QtCore.QRect(10, 90, 486, 20))
        self.lineHiResAdd.setObjectName("lineHiResAdd")
        self.lineHiResAdd.setText(str(Option.AddDir))
        
        self.groupSM64 = QtWidgets.QGroupBox(self.TabTextures)
        self.groupSM64.setGeometry(QtCore.QRect(10, 120, 251, 311))
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
        
        self.groupAdd = QtWidgets.QGroupBox(self.TabTextures)
        self.groupAdd.setGeometry(QtCore.QRect(265, 120, 251, 311))
        self.groupAdd.setObjectName("groupAdd")
        
        self.labelEyesOpenAdd = QtWidgets.QLabel(self.groupAdd)
        self.labelEyesOpenAdd.setGeometry(QtCore.QRect(10, 20, 221, 16))
        self.labelEyesOpenAdd.setObjectName("labelEyesOpenAdd")
        
        self.labelEyesHalfopenAdd = QtWidgets.QLabel(self.groupAdd)
        self.labelEyesHalfopenAdd.setGeometry(QtCore.QRect(10, 60, 221, 16))
        self.labelEyesHalfopenAdd.setObjectName("labelEyesHalfopenAdd")
        
        self.labelCapAdd = QtWidgets.QLabel(self.groupAdd)
        self.labelCapAdd.setGeometry(QtCore.QRect(10, 140, 231, 16))
        self.labelCapAdd.setObjectName("labelCapAdd")
        
        self.labelEyesClosedAdd = QtWidgets.QLabel(self.groupAdd)
        self.labelEyesClosedAdd.setGeometry(QtCore.QRect(10, 100, 231, 16))
        self.labelEyesClosedAdd.setObjectName("labelEyesClosedAdd")
        
        self.labelButtonAdd = QtWidgets.QLabel(self.groupAdd)
        self.labelButtonAdd.setGeometry(QtCore.QRect(10, 260, 231, 16))
        self.labelButtonAdd.setObjectName("labelButtonAdd")
        
        self.labelMustacheAdd = QtWidgets.QLabel(self.groupAdd)
        self.labelMustacheAdd.setGeometry(QtCore.QRect(10, 220, 231, 16))
        self.labelMustacheAdd.setObjectName("labelMustacheAdd")
        
        self.labelSidehairAdd = QtWidgets.QLabel(self.groupAdd)
        self.labelSidehairAdd.setGeometry(QtCore.QRect(10, 180, 231, 16))
        self.labelSidehairAdd.setObjectName("labelSidehairAdd")
        
        self.lineSidehairAdd = QtWidgets.QLineEdit(self.groupAdd)
        self.lineSidehairAdd.setGeometry(QtCore.QRect(10, 200, 231, 20))
        self.lineSidehairAdd.setObjectName("lineSidehairAdd")
        self.lineSidehairAdd.setText(str(Option.AddHair))
        
        self.lineOpenAdd = QtWidgets.QLineEdit(self.groupAdd)
        self.lineOpenAdd.setGeometry(QtCore.QRect(10, 40, 231, 20))
        self.lineOpenAdd.setObjectName("lineOpenAdd")
        self.lineOpenAdd.setText(str(Option.AddEyes1))
        
        self.lineHalfopenAdd = QtWidgets.QLineEdit(self.groupAdd)
        self.lineHalfopenAdd.setGeometry(QtCore.QRect(10, 80, 231, 20))
        self.lineHalfopenAdd.setObjectName("lineHalfopenAdd")
        self.lineHalfopenAdd.setText(str(Option.AddEyes2))
        
        self.lineCapAdd = QtWidgets.QLineEdit(self.groupAdd)
        self.lineCapAdd.setGeometry(QtCore.QRect(10, 160, 231, 20))
        self.lineCapAdd.setObjectName("lineCapAdd")
        self.lineCapAdd.setText(str(Option.AddCap))
        
        self.lineClosedAdd = QtWidgets.QLineEdit(self.groupAdd)
        self.lineClosedAdd.setGeometry(QtCore.QRect(10, 120, 231, 20))
        self.lineClosedAdd.setObjectName("lineClosedAdd")
        self.lineClosedAdd.setText(str(Option.AddEyes3))
        
        self.lineButtonAdd = QtWidgets.QLineEdit(self.groupAdd)
        self.lineButtonAdd.setGeometry(QtCore.QRect(10, 280, 231, 20))
        self.lineButtonAdd.setObjectName("lineButtonAdd")
        self.lineButtonAdd.setText(str(Option.AddButton))
        
        self.lineMustacheAdd = QtWidgets.QLineEdit(self.groupAdd)
        self.lineMustacheAdd.setGeometry(QtCore.QRect(10, 240, 231, 20))
        self.lineMustacheAdd.setObjectName("lineMustacheAdd")
        self.lineMustacheAdd.setText(str(Option.AddMustache))
        
        self.tabWidget.addTab(self.TabTextures, "")

        def CloseSettings():
            SettingsWindow.close()
        
        self.pushClose = QtWidgets.QPushButton(SettingsWindow)
        self.pushClose.setGeometry(QtCore.QRect(460, 475, 75, 23))
        self.pushClose.setObjectName("pushClose")
        self.pushClose.clicked.connect(CloseSettings)

        def CollectLineText():
            global CollectedLineHiResSM64, CollectedLineHiResAdd, CollectedLineEyesOpen, CollectedLineEyesHalfopen, CollectedLineEyesClosed, CollectedLineCap, CollectedLineSidehair, CollectedLineMustache, CollectedLineButton, CollectedLineEyesOpenAdd, CollectedLineEyesHalfopenAdd, CollectedLineEyesClosedAdd, CollectedLineCapAdd, CollectedLineSidehairAdd, CollectedLineMustacheAdd, CollectedLineButtonAdd
            
            CollectedLineHiResSM64 = str(self.lineHiResSM64.text())
            CollectedLineHiResAdd = str(self.lineHiResAdd.text())
            
            CollectedLineEyesOpen = str(self.lineEyesOpen.text())
            CollectedLineEyesHalfopen = str(self.lineEyesHalfopen.text())
            CollectedLineEyesClosed = str(self.lineEyesClosed.text())
            CollectedLineCap = str(self.lineCap.text())
            CollectedLineSidehair = str(self.lineSidehair.text())
            CollectedLineMustache = str(self.lineMustache.text())
            CollectedLineButton = str(self.lineButton.text())
            
            CollectedLineEyesOpenAdd = str(self.lineOpenAdd.text())
            CollectedLineEyesHalfopenAdd = str(self.lineHalfopenAdd.text())
            CollectedLineEyesClosedAdd = str(self.lineClosedAdd.text())
            CollectedLineCapAdd = str(self.lineCapAdd.text())
            CollectedLineSidehairAdd = str(self.lineSidehairAdd.text())
            CollectedLineMustacheAdd = str(self.lineMustacheAdd.text())
            CollectedLineButtonAdd = str(self.lineButtonAdd.text())

            return CollectedLineHiResSM64, CollectedLineHiResAdd, CollectedLineEyesOpen, CollectedLineEyesHalfopen, CollectedLineEyesClosed, CollectedLineCap, CollectedLineSidehair, CollectedLineMustache, CollectedLineButton, CollectedLineEyesOpenAdd, CollectedLineEyesHalfopenAdd, CollectedLineEyesClosedAdd, CollectedLineCapAdd, CollectedLineSidehairAdd, CollectedLineMustacheAdd, CollectedLineButtonAdd

        
        def Apply():
            if os.path.exists("config.ini") is True:
                pass
            else:
                CreateConfig()
                
            CollectLineText()
            CheckLanguage()
            CheckStartUpCheckForUpdates()
            CheckStartUpStayOnTop()
            Config = configparser.ConfigParser()
            Config.read("config.ini")

            Config.set("PATHS", "SM64Dir", CollectedLineHiResSM64)
            Config.set("PATHS", "AddDir", CollectedLineHiResAdd)
            
            Config.set("PATHS", "Eyes1", CollectedLineEyesOpen)
            Config.set("PATHS", "Eyes2", CollectedLineEyesHalfopen)
            Config.set("PATHS", "Eyes3", CollectedLineEyesClosed)
            Config.set("PATHS", "Cap", CollectedLineCap)
            Config.set("PATHS", "Hair", CollectedLineSidehair)
            Config.set("PATHS", "Mustache", CollectedLineMustache)
            Config.set("PATHS", "Button", CollectedLineButton)
            
            Config.set("PATHS", "AddEyes1", CollectedLineEyesOpenAdd)
            Config.set("PATHS", "AddEyes2", CollectedLineEyesHalfopenAdd)
            Config.set("PATHS", "AddEyes3", CollectedLineEyesClosedAdd)
            Config.set("PATHS", "AddCap", CollectedLineCapAdd)
            Config.set("PATHS", "AddHair", CollectedLineSidehairAdd)
            Config.set("PATHS", "AddMustache", CollectedLineMustacheAdd)
            Config.set("PATHS", "AddButton", CollectedLineButtonAdd)
            
            Config.set("OPTIONS", "Language", ChosenLanguage)
            Config.set("OPTIONS", "StartUpCheckForUpdates", StartUpCheckForUpdates)
            Config.set("OPTIONS", "StartUpStayOnTop", StartUpStayOnTop)
            
            with open("config.ini", "w") as ConfigFile:
                Config.write(ConfigFile)

            LoadConfig()
        
        self.pushApply = QtWidgets.QPushButton(SettingsWindow)
        self.pushApply.setGeometry(QtCore.QRect(380, 475, 75, 23))
        self.pushApply.setObjectName("pushApply")
        self.pushApply.clicked.connect(Apply)

        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SettingsWindow)

        if Option.Language == "English":
            self.retranslateUiEnglish(SettingsWindow)

        elif Option.Language == "Ukrainian":
            self.retranslateUiUkrainian(SettingsWindow)
        
        elif Option.Language == "Russian":
            self.retranslateUiRussian(SettingsWindow)
        
        elif Option.Language == "KazakhCyrillic":
            self.retranslateUiKazakhCyrillic(SettingsWindow)
        
        elif Option.Language == "KazakhLatin":
            self.retranslateUiKazakhLatin(SettingsWindow)
        
        else:
            self.retranslateUiEnglish(SettingsWindow)

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
        self.groupPaths.setTitle(_translate("SettingsWindow", "Paths"))
        self.labelHiResSM64.setText(_translate("SettingsWindow", "SM64 hi-res folder:"))
        self.labelHiResAdd.setText(_translate("SettingsWindow", "Additional hi-res folder:"))
        self.groupSM64.setTitle(_translate("SettingsWindow", "SM64 Textures"))
        self.labelEyesOpen.setText(_translate("SettingsWindow", "Eyes open:"))
        self.labelEyesHalfopen.setText(_translate("SettingsWindow", "Eyes half-open:"))
        self.labelEyesClosed.setText(_translate("SettingsWindow", "Eyes closed:"))
        self.labelCap.setText(_translate("SettingsWindow", "Cap:"))
        self.labelSidehair.setText(_translate("SettingsWindow", "Sidehair:"))
        self.labelMustache.setText(_translate("SettingsWindow", "Mustache:"))
        self.labelButton.setText(_translate("SettingsWindow", "Button:"))
        self.groupAdd.setTitle(_translate("SettingsWindow", "Additional Textures"))
        self.labelEyesOpenAdd.setText(_translate("SettingsWindow", "Eyes open:"))
        self.labelEyesHalfopenAdd.setText(_translate("SettingsWindow", "Eyes half-open:"))
        self.labelCapAdd.setText(_translate("SettingsWindow", "Cap:"))
        self.labelEyesClosedAdd.setText(_translate("SettingsWindow", "Eyes closed:"))
        self.labelButtonAdd.setText(_translate("SettingsWindow", "Button:"))
        self.labelMustacheAdd.setText(_translate("SettingsWindow", "Mustache:"))
        self.labelSidehairAdd.setText(_translate("SettingsWindow", "Sidehair:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TabTextures), _translate("SettingsWindow", "Textures"))
        self.pushClose.setText(_translate("SettingsWindow", "Close"))
        self.pushApply.setText(_translate("SettingsWindow", "Apply"))

    def retranslateUiUkrainian(self, SettingsWindow):
        _translate = QtCore.QCoreApplication.translate
        SettingsWindow.setWindowTitle(_translate("SettingsWindow", "Налаштування"))
        self.groupLanguage.setTitle(_translate("SettingsWindow", "Мова"))
        self.labelLanguageRestart.setText(_translate("SettingsWindow", "(необхідний перезапуск katarakta щоб зміни\nповністю набули чинності)"))
        self.groupUpdates.setTitle(_translate("SettingsWindow", "Оновлення"))
        self.checkUpdates.setText(_translate("SettingsWindow", "Перевіряти на оновлення при запуску"))
        self.labelUpdates.setText(_translate("SettingsWindow", "Залиште це увімкненим щоб отримувати повідомлення про нові версії. Якщо Ви знайдете\nпроблему, то перед тим, як повідомляти про неї, переконайтесь, що у Вас остання версія."))
        self.groupMisc.setTitle(_translate("SettingsWindow", "Інше"))
        self.checkStayOnTop.setText(_translate("SettingsWindow", "Завжди зверху при запуску"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TabGeneral), _translate("SettingsWindow", "Основне"))
        self.groupPaths.setTitle(_translate("SettingsWindow", "Шляхи"))
        self.labelHiResSM64.setText(_translate("SettingsWindow", "Hi-res папка СМ64:"))
        self.labelHiResAdd.setText(_translate("SettingsWindow", "Додаткова hi-res папка:"))
        self.groupSM64.setTitle(_translate("SettingsWindow", "Текстури СМ64"))
        self.labelEyesOpen.setText(_translate("SettingsWindow", "Розплючені очі:"))
        self.labelEyesHalfopen.setText(_translate("SettingsWindow", "Напіврозплючені очі:"))
        self.labelEyesClosed.setText(_translate("SettingsWindow", "Заплющені очі:"))
        self.labelCap.setText(_translate("SettingsWindow", "Шапка:"))
        self.labelSidehair.setText(_translate("SettingsWindow", "Бочне волосся:"))
        self.labelMustache.setText(_translate("SettingsWindow", "Вуса:"))
        self.labelButton.setText(_translate("SettingsWindow", "Кнопка:"))
        self.groupAdd.setTitle(_translate("SettingsWindow", "Додаткові текстури:"))
        self.labelEyesOpenAdd.setText(_translate("SettingsWindow", "Розплючені очі:"))
        self.labelEyesHalfopenAdd.setText(_translate("SettingsWindow", "Напіврозплючені очі:"))
        self.labelCapAdd.setText(_translate("SettingsWindow", "Шапка:"))
        self.labelEyesClosedAdd.setText(_translate("SettingsWindow", "Заплющені очі:"))
        self.labelButtonAdd.setText(_translate("SettingsWindow", "Кнопка:"))
        self.labelMustacheAdd.setText(_translate("SettingsWindow", "Вуса:"))
        self.labelSidehairAdd.setText(_translate("SettingsWindow", "Бочне волосся:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TabTextures), _translate("SettingsWindow", "Текстури"))
        self.pushClose.setText(_translate("SettingsWindow", "Закрити"))
        self.pushApply.setText(_translate("SettingsWindow", "Застосувати"))

    def retranslateUiRussian(self, SettingsWindow):
        _translate = QtCore.QCoreApplication.translate
        SettingsWindow.setWindowTitle(_translate("SettingsWindow", "Настройки"))
        self.groupLanguage.setTitle(_translate("SettingsWindow", "Язык"))
        self.labelLanguageRestart.setText(_translate("SettingsWindow", "(необходимо перезапустить katarakta чтобы\nизменения полностью вошли в силу)"))
        self.groupUpdates.setTitle(_translate("SettingsWindow", "Обновления"))
        self.checkUpdates.setText(_translate("SettingsWindow", "Проверять на обновления при запуске"))
        self.labelUpdates.setText(_translate("SettingsWindow", "Оставьте это включённым чтобы получать уведомления о новых обновлениях. Если Вы нашли\nпроблему, то перед тем, как о ней сообщить, убедитесь, что у Вас последняя версия."))
        self.groupMisc.setTitle(_translate("SettingsWindow", "Другое"))
        self.checkStayOnTop.setText(_translate("SettingsWindow", "Всегда сверху при запуске"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TabGeneral), _translate("SettingsWindow", "Основное"))
        self.groupPaths.setTitle(_translate("SettingsWindow", "Пути"))
        self.labelHiResSM64.setText(_translate("SettingsWindow", "Hi-res папка СМ64:"))
        self.labelHiResAdd.setText(_translate("SettingsWindow", "Дополнительная hi-res папка:"))
        self.groupSM64.setTitle(_translate("SettingsWindow", "Текстуры SM64"))
        self.labelEyesOpen.setText(_translate("SettingsWindow", "Открытые глаза:"))
        self.labelEyesHalfopen.setText(_translate("SettingsWindow", "Наполовину открытые глаза:"))
        self.labelEyesClosed.setText(_translate("SettingsWindow", "Закрытые глаза:"))
        self.labelCap.setText(_translate("SettingsWindow", "Кепка:"))
        self.labelSidehair.setText(_translate("SettingsWindow", "Боковые волосы:"))
        self.labelMustache.setText(_translate("SettingsWindow", "Усы:"))
        self.labelButton.setText(_translate("SettingsWindow", "Кнопка:"))
        self.groupAdd.setTitle(_translate("SettingsWindow", "Дополнительные текстуры"))
        self.labelEyesOpenAdd.setText(_translate("SettingsWindow", "Открытые глаза:"))
        self.labelEyesHalfopenAdd.setText(_translate("SettingsWindow", "Наполовину открытые глаза:"))
        self.labelCapAdd.setText(_translate("SettingsWindow", "Кепка:"))
        self.labelEyesClosedAdd.setText(_translate("SettingsWindow", "Закрытые глаза:"))
        self.labelButtonAdd.setText(_translate("SettingsWindow", "Кнопка:"))
        self.labelMustacheAdd.setText(_translate("SettingsWindow", "Усы:"))
        self.labelSidehairAdd.setText(_translate("SettingsWindow", "Боковые волосы:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TabTextures), _translate("SettingsWindow", "Текстуры"))
        self.pushClose.setText(_translate("SettingsWindow", "Закрыть"))
        self.pushApply.setText(_translate("SettingsWindow", "Применить"))

    def retranslateUiKazakhCyrillic(self, SettingsWindow):
        _translate = QtCore.QCoreApplication.translate
        SettingsWindow.setWindowTitle(_translate("SettingsWindow", "Параметлер"))
        self.groupLanguage.setTitle(_translate("SettingsWindow", "Тіл"))
        self.labelLanguageRestart.setText(_translate("SettingsWindow", "(Өзгерістер толығымен күшіне енуі үшін\nkatarakta қайта бастау керек)"))
        self.groupUpdates.setTitle(_translate("SettingsWindow", "Жаңартулар"))
        self.checkUpdates.setText(_translate("SettingsWindow", "Іске қосу кезінде жаңартуларды тексеруге"))
        self.labelUpdates.setText(_translate("SettingsWindow", "Жаңа жаңартулар туралы хабардар болу үшін оны қосулы қалдырыңыз. Мәселе тапсаңыз, ол\nтуралы хабарлаудан бұрын соңғы нұсқасы бар екеніне көз жеткізіңіз."))
        self.groupMisc.setTitle(_translate("SettingsWindow", "Басқа"))
        self.checkStayOnTop.setText(_translate("SettingsWindow", "Іске қосу кезінде әрқашан биікте"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TabGeneral), _translate("SettingsWindow", "Негізгі"))
        self.groupPaths.setTitle(_translate("SettingsWindow", "Қалталар"))
        self.labelHiResSM64.setText(_translate("SettingsWindow", "Hi-res SM64 қалтасы:"))
        self.labelHiResAdd.setText(_translate("SettingsWindow", "Қосымша hi-res қалта:"))
        self.groupSM64.setTitle(_translate("SettingsWindow", "SM64 Текстурлар"))
        self.labelEyesOpen.setText(_translate("SettingsWindow", "Ашық көздер:"))
        self.labelEyesHalfopen.setText(_translate("SettingsWindow", "Жартылай ашық көздер:"))
        self.labelEyesClosed.setText(_translate("SettingsWindow", "Жабық көздер:"))
        self.labelCap.setText(_translate("SettingsWindow", "Қақпақ:"))
        self.labelSidehair.setText(_translate("SettingsWindow", "Бүйірлік шаш:"))
        self.labelMustache.setText(_translate("SettingsWindow", "Мұрттар:"))
        self.labelButton.setText(_translate("SettingsWindow", "Түйме:"))
        self.groupAdd.setTitle(_translate("SettingsWindow", "Қосымша текстуралар"))
        self.labelEyesOpenAdd.setText(_translate("SettingsWindow", "Ашық көздер:"))
        self.labelEyesHalfopenAdd.setText(_translate("SettingsWindow", "Жартылай ашық көздер:"))
        self.labelCapAdd.setText(_translate("SettingsWindow", "Қақпақ:"))
        self.labelEyesClosedAdd.setText(_translate("SettingsWindow", "Жабық көздер:"))
        self.labelButtonAdd.setText(_translate("SettingsWindow", "Түйме:"))
        self.labelMustacheAdd.setText(_translate("SettingsWindow", "Мұрттар:"))
        self.labelSidehairAdd.setText(_translate("SettingsWindow", "Бүйірлік шаш:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TabTextures), _translate("SettingsWindow", "Текстуралар"))
        self.pushClose.setText(_translate("SettingsWindow", "Жабу"))
        self.pushApply.setText(_translate("SettingsWindow", "Қолдану"))

    def retranslateUiKazakhLatin(self, SettingsWindow):
        _translate = QtCore.QCoreApplication.translate
        SettingsWindow.setWindowTitle(_translate("SettingsWindow", "Parametler"))
        self.groupLanguage.setTitle(_translate("SettingsWindow", "Tıl"))
        self.labelLanguageRestart.setText(_translate("SettingsWindow", "(Özgerıster tolyğymen küşıne enuı üşın\nkatarakta qaita bastau kerek)"))
        self.groupUpdates.setTitle(_translate("SettingsWindow", "Jañartular"))
        self.checkUpdates.setText(_translate("SettingsWindow", "Iske qosu kezınde jañartulardy tekseruge"))
        self.labelUpdates.setText(_translate("SettingsWindow", "Jaña jañartular turaly habardar bolu üşın ony qosuly qaldyryñyz. Mäsele tapsañyz, ol\nturaly habarlaudan būryn soñğy nūsqasy bar ekenıne köz jetkızıñız."))
        self.groupMisc.setTitle(_translate("SettingsWindow", "Basqa"))
        self.checkStayOnTop.setText(_translate("SettingsWindow", "Iske qosu kezınde ärqaşan biıkte"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TabGeneral), _translate("SettingsWindow", "Negızgı"))
        self.groupPaths.setTitle(_translate("SettingsWindow", "Qaltalar"))
        self.labelHiResSM64.setText(_translate("SettingsWindow", "Hi-res SM64 qaltasy:"))
        self.labelHiResAdd.setText(_translate("SettingsWindow", "Qosymşa hi-res qalta:"))
        self.groupSM64.setTitle(_translate("SettingsWindow", "SM64 Teksturlar"))
        self.labelEyesOpen.setText(_translate("SettingsWindow", "Aşyq közder:"))
        self.labelEyesHalfopen.setText(_translate("SettingsWindow", "Jartylai aşyq közder:"))
        self.labelEyesClosed.setText(_translate("SettingsWindow", "Jabyq közder:"))
        self.labelCap.setText(_translate("SettingsWindow", "Qaqpaq:"))
        self.labelSidehair.setText(_translate("SettingsWindow", "Büiırlık şaş:"))
        self.labelMustache.setText(_translate("SettingsWindow", "Mūrttar:"))
        self.labelButton.setText(_translate("SettingsWindow", "Tüime:"))
        self.groupAdd.setTitle(_translate("SettingsWindow", "Qosymşa teksturalar"))
        self.labelEyesOpenAdd.setText(_translate("SettingsWindow", "Aşyq közder:"))
        self.labelEyesHalfopenAdd.setText(_translate("SettingsWindow", "Jartylai aşyq közder:"))
        self.labelCapAdd.setText(_translate("SettingsWindow", "Qaqpaq:"))
        self.labelEyesClosedAdd.setText(_translate("SettingsWindow", "Jabyq közder:"))
        self.labelButtonAdd.setText(_translate("SettingsWindow", "Tüime:"))
        self.labelMustacheAdd.setText(_translate("SettingsWindow", "Mūrttar:"))
        self.labelSidehairAdd.setText(_translate("SettingsWindow", "Büiırlık şaş:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TabTextures), _translate("SettingsWindow", "Teksturalar"))
        self.pushClose.setText(_translate("SettingsWindow", "Jabu"))
        self.pushApply.setText(_translate("SettingsWindow", "Qoldanu"))
        
        SettingsWindow.show()

class Ui_ccconvWindow(QWidget):
    def setupUi(self, ccconvWindow):
        ccconvWindow.setObjectName("ccconvWindow")
        ccconvWindow.resize(400, 286)
        ccconvWindow.setFixedSize(ccconvWindow.size())
        ccconvWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.World))
        self.ccconvCentral = QtWidgets.QWidget(ccconvWindow)
        self.ccconvCentral.setObjectName("ccconvCentral")
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
        self.ButtonConvert.setObjectName("ButtonConvert")
        self.ArrowLabel = QtWidgets.QLabel(self.ccconvCentral)
        self.ArrowLabel.setGeometry(QtCore.QRect(170, 10, 60, 150))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.ArrowLabel.setFont(font)
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
        
        ccconvWindow.setWindowIcon(QtGui.QIcon("img/ccconv.png"))

        self.ButtonConvert.clicked.connect(self.CcConvert)
        self.ButtonPaste.clicked.connect(self.CcPaste)
        self.ButtonCopy.clicked.connect(self.CcCopy)
        self.ButtonExport.clicked.connect(self.CcSaveAsTxt)
        self.ButtonImport.clicked.connect(self.CcOpenFromTxt)

        QtCore.QMetaObject.connectSlotsByName(ccconvWindow)

        if Option.Language == "English":
            self.retranslateUiEnglish(ccconvWindow)

        elif Option.Language == "Ukrainian":
            self.retranslateUiUkrainian(ccconvWindow)
        
        elif Option.Language == "Russian":
            self.retranslateUiRussian(ccconvWindow)
        
        elif Option.Language == "KazakhCyrillic":
            self.retranslateUiKazakhCyrillic(ccconvWindow)
        
        elif Option.Language == "KazakhLatin":
            self.retranslateUiKazakhLatin(ccconvWindow)
        
        else:
            self.retranslateUiEnglish(ccconvWindow)

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
            ChooseOpenFile = QFileDialog.getOpenFileName(self, "Open file", os.getcwd(), "Text Document (*.txt)")

        elif Option.Language == "Ukrainian":
            ChooseOpenFile = QFileDialog.getOpenFileName(self, "Виберіть файл", os.getcwd(), "Текстовий документ (*.txt)")
        
        elif Option.Language == "Russian":
            ChooseOpenFile = QFileDialog.getOpenFileName(self, "Выберить файл", os.getcwd(), "Текстовый документ (*.txt)")

        elif Option.Language == "KazakhCyrillic":
            ChooseOpenFile = QFileDialog.getOpenFileName(self, "Файлды таңдаңыз", os.getcwd(), "Мәтіндік құжат (*.txt)")

        elif Option.Language == "KazakhLatin":
            ChooseOpenFile = QFileDialog.getOpenFileName(self, "Faildy tañdañyz", os.getcwd(), "Mätındık qūjat (*.txt)")
            
        else:
            ChooseOpenFile = QFileDialog.getOpenFileName(self, "Open file", os.getcwd(), "Text Document (*.txt)")

        try:
            with open(ChooseOpenFile[0]) as ChosenOpenFileCC:
                self.InputCC.setPlainText(ChosenOpenFileCC.read())
                ChosenOpenFileCC.close()
        except:
            pass

    def CcSaveAsTxt(self, ccconvWindow):
        if Option.Language == "English":
            ChooseSaveFile = QFileDialog.getSaveFileName(self, "Save file", os.getcwd(), "Text Document (*.txt)")

        elif Option.Language == "Ukrainian":
            ChooseSaveFile = QFileDialog.getSaveFileName(self, "Збереження файла", os.getcwd(), "Текстовий документ (*.txt)")
        
        elif Option.Language == "Russian":
            ChooseSaveFile = QFileDialog.getSaveFileName(self, "Сохранение файла", os.getcwd(), "Текстовый документ (*.txt)")

        elif Option.Language == "KazakhCyrillic":
            ChooseSaveFile = QFileDialog.getSaveFileName(self, "Файлды сақтау", os.getcwd(), "Мәтіндік құжат (*.txt)")

        elif Option.Language == "KazakhLatin":
            ChooseSaveFile = QFileDialog.getSaveFileName(self, "Faildy saqtau", os.getcwd(), "Mätındık qūjat (*.txt)")
            
        else:
            ChooseSaveFile = QFileDialog.getSaveFileName(self, "Save file", os.getcwd(), "Text Document (*.txt)")
        try:
            SaveFile = open(ChooseSaveFile[0], 'w')
            SaveFile.write(self.OutputCC.toPlainText())
            SaveFile.close()
        except:
            pass

    def retranslateUiEnglish(self, ccconvWindow):
        _translate = QtCore.QCoreApplication.translate
        ccconvWindow.setWindowTitle(_translate("ccconvWindow", "Colorcode Converter"))
        #self.InputCC.setHtml(_translate("ccconvWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
#"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
#"p, li { white-space: pre-wrap; }\n"
#"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
#"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.InputCC.setPlaceholderText(_translate("ccconvWindow", "Insert colorcode here..."))
        #self.OutputCC.setHtml(_translate("ccconvWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
#"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
#"p, li { white-space: pre-wrap; }\n"
#"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
#"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.OutputCC.setPlaceholderText(_translate("ccconvWindow", "Output will appear here."))
        self.ButtonConvert.setText(_translate("ccconvWindow", "Convert"))
        self.ArrowLabel.setText(_translate("ccconvWindow", "--->"))
        self.InputCombo.setItemText(0, _translate("ccconvWindow", "NTSC-U"))
        self.InputCombo.setItemText(1, _translate("ccconvWindow", "NTSC-J"))
        self.InputCombo.setItemText(2, _translate("ccconvWindow", "PAL"))
        self.InputCombo.setItemText(3, _translate("ccconvWindow", "Shindou"))
        self.OutputCombo.setItemText(0, _translate("ccconvWindow", "NTSC-U"))
        self.OutputCombo.setItemText(1, _translate("ccconvWindow", "NTSC-J"))
        self.OutputCombo.setItemText(2, _translate("ccconvWindow", "PAL"))
        self.OutputCombo.setItemText(3, _translate("ccconvWindow", "Shindou"))
        self.ButtonPaste.setText(_translate("ccconvWindow", "Paste from clipboard"))
        self.ButtonCopy.setText(_translate("ccconvWindow", "Copy to clipboard"))
        self.ButtonExport.setText(_translate("ccconvWindow", "Export as .txt file"))
        self.ButtonImport.setText(_translate("ccconvWindow", "Import from .txt file"))

    def retranslateUiUkrainian(self, ccconvWindow):
        _translate = QtCore.QCoreApplication.translate
        ccconvWindow.setWindowTitle(_translate("ccconvWindow", "Конвертер колірних кодів"))
        self.InputCC.setHtml(_translate("ccconvWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.InputCC.setPlaceholderText(_translate("ccconvWindow", "Додайте сюди колірний код..."))
        self.OutputCC.setHtml(_translate("ccconvWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.OutputCC.setPlaceholderText(_translate("ccconvWindow", "Результат з'явиться тут."))
        self.ButtonConvert.setText(_translate("ccconvWindow", "Конвертувати"))
        self.ArrowLabel.setText(_translate("ccconvWindow", "--->"))
        self.InputCombo.setItemText(0, _translate("ccconvWindow", "NTSC-U"))
        self.InputCombo.setItemText(1, _translate("ccconvWindow", "NTSC-J"))
        self.InputCombo.setItemText(2, _translate("ccconvWindow", "PAL"))
        self.InputCombo.setItemText(3, _translate("ccconvWindow", "Shindou"))
        self.OutputCombo.setItemText(0, _translate("ccconvWindow", "NTSC-U"))
        self.OutputCombo.setItemText(1, _translate("ccconvWindow", "NTSC-J"))
        self.OutputCombo.setItemText(2, _translate("ccconvWindow", "PAL"))
        self.OutputCombo.setItemText(3, _translate("ccconvWindow", "Shindou"))
        self.ButtonPaste.setText(_translate("ccconvWindow", "Вставити з буфера обміну"))
        self.ButtonCopy.setText(_translate("ccconvWindow", "Копіювати"))
        self.ButtonExport.setText(_translate("ccconvWindow", "Експортувати як .txt файл"))
        self.ButtonImport.setText(_translate("ccconvWindow", "Імпортувати з .txt файлу"))

    def retranslateUiRussian(self, ccconvWindow):
        _translate = QtCore.QCoreApplication.translate
        ccconvWindow.setWindowTitle(_translate("ccconvWindow", "Конвертер цветовых кодов"))
        self.InputCC.setHtml(_translate("ccconvWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.InputCC.setPlaceholderText(_translate("ccconvWindow", "Вставьте сюда цветовой код..."))
        self.OutputCC.setHtml(_translate("ccconvWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.OutputCC.setPlaceholderText(_translate("ccconvWindow", "Результат появится здесь."))
        self.ButtonConvert.setText(_translate("ccconvWindow", "Конвертировать"))
        self.ArrowLabel.setText(_translate("ccconvWindow", "--->"))
        self.InputCombo.setItemText(0, _translate("ccconvWindow", "NTSC-U"))
        self.InputCombo.setItemText(1, _translate("ccconvWindow", "NTSC-J"))
        self.InputCombo.setItemText(2, _translate("ccconvWindow", "PAL"))
        self.InputCombo.setItemText(3, _translate("ccconvWindow", "Shindou"))
        self.OutputCombo.setItemText(0, _translate("ccconvWindow", "NTSC-U"))
        self.OutputCombo.setItemText(1, _translate("ccconvWindow", "NTSC-J"))
        self.OutputCombo.setItemText(2, _translate("ccconvWindow", "PAL"))
        self.OutputCombo.setItemText(3, _translate("ccconvWindow", "Shindou"))
        self.ButtonPaste.setText(_translate("ccconvWindow", "Вставить из буфера обмена"))
        self.ButtonCopy.setText(_translate("ccconvWindow", "Копировать"))
        self.ButtonExport.setText(_translate("ccconvWindow", "Экспортировать как .txt"))
        self.ButtonImport.setText(_translate("ccconvWindow", "Импортировать из .txt"))

    def retranslateUiKazakhCyrillic(self, ccconvWindow):
        _translate = QtCore.QCoreApplication.translate
        ccconvWindow.setWindowTitle(_translate("ccconvWindow", "Түс кодын түрлендіргіш"))
        self.InputCC.setHtml(_translate("ccconvWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.InputCC.setPlaceholderText(_translate("ccconvWindow", "Түс кодын осы жерге қойыңыз..."))
        self.OutputCC.setHtml(_translate("ccconvWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.OutputCC.setPlaceholderText(_translate("ccconvWindow", "Нәтиже осы жерде пайда болады."))
        self.ButtonConvert.setText(_translate("ccconvWindow", "Түрлендіру"))
        self.ArrowLabel.setText(_translate("ccconvWindow", "--->"))
        self.InputCombo.setItemText(0, _translate("ccconvWindow", "NTSC-U"))
        self.InputCombo.setItemText(1, _translate("ccconvWindow", "NTSC-J"))
        self.InputCombo.setItemText(2, _translate("ccconvWindow", "PAL"))
        self.InputCombo.setItemText(3, _translate("ccconvWindow", "Shindou"))
        self.OutputCombo.setItemText(0, _translate("ccconvWindow", "NTSC-U"))
        self.OutputCombo.setItemText(1, _translate("ccconvWindow", "NTSC-J"))
        self.OutputCombo.setItemText(2, _translate("ccconvWindow", "PAL"))
        self.OutputCombo.setItemText(3, _translate("ccconvWindow", "Shindou"))
        self.ButtonPaste.setText(_translate("ccconvWindow", "Буферден қою"))
        self.ButtonCopy.setText(_translate("ccconvWindow", "Көшіру"))
        self.ButtonExport.setText(_translate("ccconvWindow", ".txt файлына экспорттау"))
        self.ButtonImport.setText(_translate("ccconvWindow", ".txt файлына импорттау"))

    def retranslateUiKazakhLatin(self, ccconvWindow):
        _translate = QtCore.QCoreApplication.translate
        ccconvWindow.setWindowTitle(_translate("ccconvWindow", "Tüs kodyn türlendırgış"))
        self.InputCC.setHtml(_translate("ccconvWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.InputCC.setPlaceholderText(_translate("ccconvWindow", "Tüs kodyn osy jerge qoiyñyz..."))
        self.OutputCC.setHtml(_translate("ccconvWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.OutputCC.setPlaceholderText(_translate("ccconvWindow", "Nätije osy jerde paida bolady."))
        self.ButtonConvert.setText(_translate("ccconvWindow", "Türlendıru"))
        self.ArrowLabel.setText(_translate("ccconvWindow", "--->"))
        self.InputCombo.setItemText(0, _translate("ccconvWindow", "NTSC-U"))
        self.InputCombo.setItemText(1, _translate("ccconvWindow", "NTSC-J"))
        self.InputCombo.setItemText(2, _translate("ccconvWindow", "PAL"))
        self.InputCombo.setItemText(3, _translate("ccconvWindow", "Shindou"))
        self.OutputCombo.setItemText(0, _translate("ccconvWindow", "NTSC-U"))
        self.OutputCombo.setItemText(1, _translate("ccconvWindow", "NTSC-J"))
        self.OutputCombo.setItemText(2, _translate("ccconvWindow", "PAL"))
        self.OutputCombo.setItemText(3, _translate("ccconvWindow", "Shindou"))
        self.ButtonPaste.setText(_translate("ccconvWindow", "Buferden qoiu"))
        self.ButtonCopy.setText(_translate("ccconvWindow", "Köşıru"))
        self.ButtonExport.setText(_translate("ccconvWindow", ".txt failyna eksporttau"))
        self.ButtonImport.setText(_translate("ccconvWindow", ".txt failyna importtau"))
        
if Option.Language == "English":
    CopyEyesErrorBoxTitle = "Error"
    CopyEyesErrorBoxMessage = "An error occured!\nMake sure that:\n- You entered the correct path in config.ini\n- You entered the correct eye texture name in config.ini\n- You have the eye textures in the folder\n- If your Project64 is on your C: drive, then either run katarakta as administrator or move Project64 elsewhere."


elif Option.Language == "Ukrainian":
    CopyEyesErrorBoxTitle = "Помилка"
    CopyEyesErrorBoxMessage = "Сталая помилка!\nПереконайтеся, що:\n- Ви ввели існуючий шлях до hi-res текстур у config.ini\n- Ви ввели правильні назви текстур очей у config.ini\n- У самій папці є текстури очей\n- Якщо Project64 знаходиться на диску C:, то запустить katarakta від імені адміністратора, або перемістить Project64 в інше місце."
    
elif Option.Language == "Russian":
    CopyEyesErrorBoxTitle = "Ошибка"
    CopyEyesErrorBoxMessage = "Произошла ошибка!\nУбедитесь, что:\n- Вы ввели существующий путь к hi-res текстурам в config.ini\n- Вы ввели правильные названия текстур глаз в config.ini\n- У вас есть сами текстуры глаз в папке\n- Если Project64 находится на диске C:, то либо запустите katarakta от имени администратора, либо переместите Project64 в другое место."
    
else:
    CopyEyesErrorBoxTitle = "Error"
    CopyEyesErrorBoxMessage = "An error occured!\nMake sure that:\n- You entered the correct path in config.ini\n- You entered the correct eye texture name in config.ini\n- You have the eye textures in the folder\n- If your Project64 is on your C: drive, then either run katarakta as administrator or move Project64 elsewhere."
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    try:
        LoadingImageList = os.listdir('loading')
        for File in LoadingImageList:
            if not(File.endswith(".png")):
                LoadingImageList.remove(File)

        LoadingImage = random.choice(LoadingImageList)
    
        Splash = QSplashScreen(QPixmap("loading\\{}".format(LoadingImage)))
        Splash.show()
        
    except:
        pass
    
    appAboutWindow = QtWidgets.QMainWindow()

    #CopyEyes error message
    CopyEyesErrorBox = QMessageBox()
    CopyEyesErrorBox.setWindowTitle(CopyEyesErrorBoxTitle)
    CopyEyesErrorBox.setText(CopyEyesErrorBoxMessage)
    CopyEyesErrorBox.setIcon(QMessageBox.Information)
    CopyEyesErrorBox.setStandardButtons(QMessageBox.Close)
    
    try:
        CopyEyesErrorBox.setWindowIcon(QtGui.QIcon("img\\256icon.png"))
    except:
        pass
    
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    try:
        Splash.finish(MainWindow)
    except:
        pass
    
    sys.exit(app.exec_())
