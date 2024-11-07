#GPL-3.0-only

import os
import configparser
import requests
import zipfile
import shutil
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt

import github_release
import psutil

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
    
Option = Options()

Config = configparser.ConfigParser()

def LoadConfig():
    if mode == "dotini":
        Config.read("config.ini")
    else:
        Config.read("config.txt")
    ConfigSecond = Config["PATHS"]
    
    if ConfigSecond.has_option("HiresDir") == True:
        Option.SM64Dir = ConfigSecond.get("HiresDir", Option.HiresDir)
        Option.AddDir = ConfigSecond.get("HiresDir", Option.HiresDir)
    else:
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

def LoadConfig():
    if mode == "dotini":
        Config.read("config.ini")
    else:
        Config.read("config.txt")
    ConfigSecond = Config["PATHS"]
    
    if Config.has_option("PATHS", "HiResDir") == True:
        Option.HiResDir = ConfigSecond.get("HiResDir")
    
        Option.SM64Name = ConfigSecond.get("SM64Name")
        Option.AddNames = ConfigSecond.get("AddNames")
    else:
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

def CreateConfig():
    CreatedConfig = configparser.ConfigParser()
    if mode == "dotini":
        Config.read("config.ini")
    else:
        Config.read("config.txt")
    if Config.has_option("PATHS", "HiResDir") == True:
        CreatedConfig["PATHS"] = {
            "hiresdir": Option.HiResDir,
            "sm64name": Option.SM64Name,
            "addnames": Option.AddNames,
            "eyes1": Option.Eyes1,
            "eyes2": Option.Eyes2,
            "eyes3": Option.Eyes3,
            "cap": Option.Cap,
            "hair": Option.Hair,
            "mustache": Option.Mustache,
            "button": Option.Button,
            "addeyes1": Option.AddEyes1,
            "addeyes2": Option.AddEyes2,
            "addeyes3": Option.AddEyes3,
            "addcap": Option.AddCap,
            "addhair": Option.AddHair,
            "addmustache": Option.AddMustache,
            "addbutton": Option.AddButton
            }
        CreatedConfig["OPTIONS"] = {
            "language": Option.Language
            }
    else:
        CreatedConfig["PATHS"] = {
            "sm64dir": Option.SM64Dir,
            "adddir": Option.AddDir,
            "eyes1": Option.Eyes1,
            "eyes2": Option.Eyes2,
            "eyes3": Option.Eyes3,
            "cap": Option.Cap,
            "hair": Option.Hair,
            "mustache": Option.Mustache,
            "button": Option.Button,
            "addeyes1": Option.AddEyes1,
            "addeyes2": Option.AddEyes2,
            "addeyes3": Option.AddEyes3,
            "addcap": Option.AddCap,
            "addhair": Option.AddHair,
            "addmustache": Option.AddMustache,
            "addbutton": Option.AddButton
            }
        CreatedConfig["OPTIONS"] = {
            "language": Option.Language
            }
    with open("migrateconfig.ini","w") as _ConfigFile:
        CreatedConfig.write(_ConfigFile)

def LoadLanguage():
    if mode == "dotini":
        Config.read("config.ini")
    else:
        Config.read("config.txt")
    LoadLanguage = configparser.ConfigParser()
    LoadLanguage = Config["OPTIONS"]
    Option.Language = LoadLanguage.get("Language", Option.Language)

global mode
if os.path.isfile("config.txt"):
    mode = "dottxt"
if os.path.isfile("config.ini"):
    mode = "dotini"
try:
    LoadLanguage()
except:
    Option.Language = "English"
    
UpdaterVersion = "rev3"

class Ui_UpdaterWindow(object):
    def setupUi(self, UpdaterWindow):
        UpdaterWindow.setObjectName("UpdaterWindow")
        UpdaterWindow.resize(451, 321)
        UpdaterWindow.setFixedSize(UpdaterWindow.size())
        self.centralwidget = QtWidgets.QWidget(UpdaterWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ButtonNormal = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonNormal.setGeometry(QtCore.QRect(10, 270, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.ButtonNormal.setFont(font)
        self.ButtonNormal.setObjectName("ButtonNormal")
        self.ButtonPy38 = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonPy38.setGeometry(QtCore.QRect(230, 270, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.ButtonPy38.setFont(font)
        self.ButtonPy38.setObjectName("ButtonPy38")
        self.LabelNormal = QtWidgets.QLabel(self.centralwidget)
        self.LabelNormal.setGeometry(QtCore.QRect(10, 240, 211, 31))
        self.LabelNormal.setObjectName("LabelNormal")
        self.LabelNormal.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelPy38 = QtWidgets.QLabel(self.centralwidget)
        self.LabelPy38.setGeometry(QtCore.QRect(230, 240, 211, 31))
        self.LabelPy38.setObjectName("LabelPy38")
        self.LabelPy38.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelVersion = QtWidgets.QLabel(self.centralwidget)
        self.LabelVersion.setGeometry(QtCore.QRect(10, 0, 431, 41))
        self.LabelVersion.setObjectName("LabelVersions")
        self.LabelVersion.setAlignment(QtCore.Qt.AlignCenter)
        self.TextBox = QtWidgets.QTextBrowser(self.centralwidget)
        self.TextBox.setGeometry(QtCore.QRect(10, 40, 431, 201))
        self.TextBox.setObjectName("plainTextEdit")
        self.TextBox.setOpenExternalLinks(True)
        UpdaterWindow.setCentralWidget(self.centralwidget)
        
        if os.path.isfile("img/UpdaterIcon.png") == True:
            UpdaterWindow.setWindowIcon(QtGui.QIcon("img/UpdaterIcon.png"))
        else:
            UpdaterWindow.setWindowIcon(QtGui.QIcon("resources/img/UpdaterIcon.png"))
    
        self.ButtonNormal.clicked.connect(self.DownloadNormal)
        self.ButtonPy38.clicked.connect(self.DownloadPy38)

        if Option.Language == "English":
            self.retranslateUiEnglish(UpdaterWindow)
            
        elif Option.Language == "Ukrainian":
            self.retranslateUiUkrainian(UpdaterWindow)
            
        elif Option.Language == "Russian":
            self.retranslateUiRussian(UpdaterWindow)
            
        elif Option.Language == "KazakhCyrillic":
            self.retranslateUiKazakhCyrillic(UpdaterWindow)
            
        elif Option.Language == "KazakhLatin":
            self.retranslateUiKazakhLatin(UpdaterWindow)

        else:
            self.retranslateUiEnglish(UpdaterWindow)
            
        QtCore.QMetaObject.connectSlotsByName(UpdaterWindow)

        try:
            global LatestResponse, LatestVersion, LatestBody
            LatestResponse = requests.get("https://api.github.com/repos/vazhka-dolya/katarakta/releases/latest")
            LatestVersion = LatestResponse.json()["name"]
            LatestBody = LatestResponse.json()["body"]
        except:
            LatestVersion = "Unknown"
            LatestBody = "Unknown"
            
        _translate = QtCore.QCoreApplication.translate

        if Option.Language == "English":
            self.LabelVersion.setText(_translate("UpdaterWindow", "Latest version on Github: {}".format(str(LatestVersion))))
            
        elif Option.Language == "Ukrainian":
            self.LabelVersion.setText(_translate("UpdaterWindow", "Остання версія на GitHub: {}".format(str(LatestVersion))))
            
        elif Option.Language == "Russian":
            self.LabelVersion.setText(_translate("UpdaterWindow", "Последняя версия на GitHub: {}".format(str(LatestVersion))))
            
        elif Option.Language == "KazakhCyrillic":
            self.LabelVersion.setText(_translate("UpdaterWindow", "GitHub сайтындағы соңғы нұсқасы: {}".format(str(LatestVersion))))
            
        elif Option.Language == "KazakhLatin":
            self.LabelVersion.setText(_translate("UpdaterWindow", "GitHub saityndağy soñğy nūsqasy: {}".format(str(LatestVersion))))

        else:
            self.LabelVersion.setText(_translate("UpdaterWindow", "Latest version on Github: {}".format(str(LatestVersion))))
        
        #try:
        self.TextBox.setMarkdown(LatestBody)
        #except:
            #pass
    
    ExceptFiles = ["updater.exe", "katarakta.exe", "config.ini"]
    ExceptDirs = ["chmb", "eyes", "updater"]

    def DownloadNormal(self, UpdaterWindow):
        for process in psutil.process_iter():
            if process.name() == "katarakta.exe":
                process.kill()
        if not os.path.exists("updater/"):
            os.makedirs("updater/")
        global mode
        if os.path.isfile("config.txt"):
            mode = "dottxt"
            LoadConfig()
            CreateConfig()
        if os.path.isfile("config.ini"):
            mode = "dotini"
            LoadConfig()
            CreateConfig()
            
        LatestResponse = requests.get("https://api.github.com/repos/vazhka-dolya/katarakta/releases/latest")
        LatestVersion = LatestResponse.json()["name"]
        StrippedVersion = LatestVersion.strip("katarakta ")
        github_release.gh_asset_download("vazhka-dolya/katarakta", "v{}".format(StrippedVersion), "katarakta-{}.zip".format(StrippedVersion))
        shutil.move("katarakta-{}.zip".format(StrippedVersion), "updater/katarakta-{}.zip".format(StrippedVersion))
        with zipfile.ZipFile("updater/katarakta-{}.zip".format(StrippedVersion), 'r') as kataraktaZip:
            kataraktaZip.extractall("updater/")
        shutil.move("updater/katarakta-{}/katarakta.exe".format(StrippedVersion), "katarakta.exe")
        try:
            shutil.rmtree("loading/")
            shutil.move("updater/katarakta-{}/loading/".format(StrippedVersion), os.getcwd())
        except:
            pass
        try:
            shutil.rmtree("img/")
            shutil.move("updater/katarakta-{}/img/".format(StrippedVersion), os.getcwd())
        except:
            pass
        if os.path.isfile("config.ini"):
            os.remove("config.ini")
        if os.path.isfile("config.txt"):
            os.remove("config.txt")
        if not os.path.exists("chmb/"):
            os.makedirs("chmb/")

    def DownloadPy38(self, UpdaterWindow):
        for process in psutil.process_iter():
            if process.name() == "katarakta.exe":
                process.kill()
        if not os.path.exists("updater/"):
            os.makedirs("updater/")
        global mode
        if os.path.isfile("config.txt"):
            mode = "dottxt"
            LoadConfig()
            CreateConfig()
        if os.path.isfile("config.ini"):
            mode = "dotini"
            LoadConfig()
            CreateConfig()
            
        LatestResponse = requests.get("https://api.github.com/repos/vazhka-dolya/katarakta/releases/latest")
        LatestVersion = LatestResponse.json()["name"]
        StrippedVersion = LatestVersion.strip("katarakta ")
        github_release.gh_asset_download("vazhka-dolya/katarakta", "v{}".format(StrippedVersion), "katarakta-{}-py38.zip".format(StrippedVersion))
        shutil.move("katarakta-{}-py38.zip".format(StrippedVersion), "updater/katarakta-{}-py38.zip".format(StrippedVersion))
        with zipfile.ZipFile("updater/katarakta-{}-py38.zip".format(StrippedVersion), 'r') as kataraktaZip:
            kataraktaZip.extractall("updater/")
        shutil.move("updater/katarakta-{}-py38/katarakta.exe".format(StrippedVersion), "katarakta.exe")
        try:
            shutil.rmtree("loading/")
            shutil.move("updater/katarakta-{}-py38/loading/".format(StrippedVersion), os.getcwd())
        except:
            pass
        try:
            shutil.rmtree("img/")
            shutil.move("updater/katarakta-{}-py38/img/".format(StrippedVersion), os.getcwd())
        except:
            pass
        if os.path.isfile("config.ini"):
            os.remove("config.ini")
        if os.path.isfile("config.txt"):
            os.remove("config.txt")
        if not os.path.exists("chmb/"):
            os.makedirs("chmb/")

    def retranslateUiEnglish(self, UpdaterWindow):
        _translate = QtCore.QCoreApplication.translate
        UpdaterWindow.setWindowTitle(_translate("UpdaterWindow", "katarakta Updater ({})".format(UpdaterVersion)))
        self.ButtonNormal.setText(_translate("UpdaterWindow", "Install update (Normal)"))
        self.ButtonPy38.setText(_translate("UpdaterWindow", "Install update (py38)"))
        self.LabelNormal.setText(_translate("UpdaterWindow", "For Windows 8.1 or newer:"))
        self.LabelPy38.setText(_translate("UpdaterWindow", "For Windows Vista/7:"))

    def retranslateUiUkrainian(self, UpdaterWindow):
        _translate = QtCore.QCoreApplication.translate
        UpdaterWindow.setWindowTitle(_translate("UpdaterWindow", "Оновлювач katarakta ({})".format(UpdaterVersion)))
        self.ButtonNormal.setText(_translate("UpdaterWindow", "Встановити (Normal)"))
        self.ButtonPy38.setText(_translate("UpdaterWindow", "Встановити (py38)"))
        self.LabelNormal.setText(_translate("UpdaterWindow", "Для Windows 8.1 чи новіше:"))
        self.LabelPy38.setText(_translate("UpdaterWindow", "Для Windows Vista/7:"))

    def retranslateUiRussian(self, UpdaterWindow):
        _translate = QtCore.QCoreApplication.translate
        UpdaterWindow.setWindowTitle(_translate("UpdaterWindow", "Средство обновления katarakta ({})".format(UpdaterVersion)))
        self.ButtonNormal.setText(_translate("UpdaterWindow", "Установить (Normal)"))
        self.ButtonPy38.setText(_translate("UpdaterWindow", "Установить (py38)"))
        self.LabelNormal.setText(_translate("UpdaterWindow", "Для Windows 8.1 или новее:"))
        self.LabelPy38.setText(_translate("UpdaterWindow", "Для Windows Vista/7:"))

    def retranslateUiKazakhCyrillic(self, UpdaterWindow):
        _translate = QtCore.QCoreApplication.translate
        UpdaterWindow.setWindowTitle(_translate("UpdaterWindow", "katarakta жаңартушысы ({})".format(UpdaterVersion)))
        self.ButtonNormal.setText(_translate("UpdaterWindow", "Орнату (Normal)"))
        self.ButtonPy38.setText(_translate("UpdaterWindow", "Орнату (py38)"))
        self.LabelNormal.setText(_translate("UpdaterWindow", "Windows 8.1 немесе одан жаңарақ:"))
        self.LabelPy38.setText(_translate("UpdaterWindow", "Windows Vista/7 үшін:"))

    def retranslateUiKazakhLatin(self, UpdaterWindow):
        _translate = QtCore.QCoreApplication.translate
        UpdaterWindow.setWindowTitle(_translate("UpdaterWindow", "katarakta jañartuşysy ({})".format(UpdaterVersion)))
        self.ButtonNormal.setText(_translate("UpdaterWindow", "Ornatu (Normal)"))
        self.ButtonPy38.setText(_translate("UpdaterWindow", "Ornatu (py38)"))
        self.LabelNormal.setText(_translate("UpdaterWindow", "Windows 8.1 nemese odan jañaraq:"))
        self.LabelPy38.setText(_translate("UpdaterWindow", "Windows Vista/7 üşın:"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UpdaterWindow = QtWidgets.QMainWindow()
    ui = Ui_UpdaterWindow()
    ui.setupUi(UpdaterWindow)
    UpdaterWindow.show()
    sys.exit(app.exec_())
