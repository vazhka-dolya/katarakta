#GPL-3.0-only

import ctypes
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
import locale
import numpy as np
from PIL import Image
from datetime import datetime
from typing import List
import traceback

from playsound import playsound
from time import sleep as timesleep
import threading

AppVersion = "Public Test 4"

if sys.version_info[:2] == (3, 11):
    AppEdition = "Normal"
elif sys.version_info[:2] == (3, 8):
    AppEdition = "py38"
else:
    AppEdition = "Unknown"

IsTestVersion = True

if IsTestVersion == True:
    kataraktaIcon = "resources/img/IconPT.png"
else:
    kataraktaIcon = "resources/img/Icon.png"

class Ui_CrashWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
    def setupUi(self, CrashWindow, ErrorMessage):
        CrashWindow.setObjectName("CrashWindow")
        CrashWindow.setFixedSize(651, 421)
        CrashWindow.setWindowIcon(QIcon(kataraktaIcon))
        CrashWindow.setStyleSheet("font-size: 11px")

        self.centralwidget = QtWidgets.QWidget(CrashWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.CrashLabelTitle = QtWidgets.QLabel(self.centralwidget)
        self.CrashLabelTitle.setGeometry(QtCore.QRect(10, 40, 311, 71))
        self.CrashLabelTitle.setStyleSheet("font-size: 22px")
        self.CrashLabelTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.CrashLabelTitle.setObjectName("CrashLabelTitle")
        self.CrashLabelDesc = QtWidgets.QLabel(self.centralwidget)
        self.CrashLabelDesc.setGeometry(QtCore.QRect(10, 100, 311, 41))
        self.CrashLabelDesc.setObjectName("CrashLabelDesc")
        self.CrashLabelHelp = QtWidgets.QLabel(self.centralwidget)
        self.CrashLabelHelp.setGeometry(QtCore.QRect(330, 10, 311, 41))
        self.CrashLabelHelp.setObjectName("CrashLabelHelp")
        self.CrashLabelReport = QtWidgets.QLabel(self.centralwidget)
        self.CrashLabelReport.setGeometry(QtCore.QRect(330, 340, 311, 41))
        self.CrashLabelReport.setObjectName("CrashLabelReport")
        
        # Uncomment to see the label's boundaries
        #self.CrashLabelReport.setStyleSheet("background-color:#7F7F7F")

        self.CrashComboLang = QtWidgets.QComboBox(self.centralwidget)
        self.CrashComboLang.setGeometry(QtCore.QRect(10, 10, 311, 21))
        self.CrashComboLang.setObjectName("CrashComboLang")
        self.CrashComboLang.addItem("")
        self.CrashComboLang.addItem("")
        self.CrashComboLang.addItem("")
        self.CrashComboLang.currentIndexChanged.connect(self.OnComboLangChanged)
        
        MonospacedFont = QtGui.QFont(QtGui.QFontDatabase.applicationFontFamilies(QtGui.QFontDatabase.addApplicationFont("resources/fonts/LiberationMono-Regular.ttf"))[0])
        MonospacedFont.setPointSize(7)
        self.CrashTextError = QtWidgets.QTextBrowser(self.centralwidget)
        self.CrashTextError.setGeometry(QtCore.QRect(10, 140, 311, 271))
        self.CrashTextError.setObjectName("CrashTextError")
        self.CrashTextError.setFont(MonospacedFont)
        self.CrashTextError.setStyleSheet("font-size: 10px")
        
        self.CrashPushLogs = QtWidgets.QPushButton(self.centralwidget)
        self.CrashPushLogs.setGeometry(QtCore.QRect(330, 60, 311, 61))
        self.CrashPushLogs.setObjectName("CrashPushLogs")
        self.CrashPushLogs.setIcon(QIcon("resources/img/CrashLogs.png"))
        self.CrashPushLogs.setIconSize(QSize(48, 48))
        self.CrashPushLogs.setStyleSheet("text-align:left")
        
        self.CrashPushConfig = QtWidgets.QPushButton(self.centralwidget)
        self.CrashPushConfig.setGeometry(QtCore.QRect(330, 130, 311, 61))
        self.CrashPushConfig.setObjectName("CrashPushConfig")
        self.CrashPushConfig.setIcon(QIcon("resources/img/CrashConfig.png"))
        self.CrashPushConfig.setIconSize(QSize(48, 48))
        self.CrashPushConfig.setStyleSheet("text-align:left")
        
        self.CrashPushLang = QtWidgets.QPushButton(self.centralwidget)
        self.CrashPushLang.setGeometry(QtCore.QRect(330, 200, 311, 61))
        self.CrashPushLang.setObjectName("CrashPushLang")
        self.CrashPushLang.setIcon(QIcon("resources/img/CrashLang.png"))
        self.CrashPushLang.setIconSize(QSize(48, 48))
        self.CrashPushLang.setStyleSheet("text-align:left")
        self.CrashPushLang.clicked.connect(self.CrashOpenLang)
        
        self.CrashPushIgnore = QtWidgets.QPushButton(self.centralwidget)
        self.CrashPushIgnore.setGeometry(QtCore.QRect(330, 270, 311, 61))
        self.CrashPushIgnore.setObjectName("CrashPushIgnore")
        self.CrashPushIgnore.setIcon(QIcon("resources/img/CrashIgnore.png"))
        self.CrashPushIgnore.setIconSize(QSize(48, 48))
        self.CrashPushIgnore.setStyleSheet("text-align:left")
        self.CrashPushIgnore.clicked.connect(self.CrashIgnoreError)
        
        self.CrashPushLogsLabel = QtWidgets.QLabel(self.centralwidget)
        self.CrashPushLogsLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.CrashPushLogsLabel.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.CrashPushLogsLabel.setGeometry(QtCore.QRect(330, 60, 300, 61))
        
        self.CrashPushConfigLabel = QtWidgets.QLabel(self.centralwidget)
        self.CrashPushConfigLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.CrashPushConfigLabel.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.CrashPushConfigLabel.setGeometry(QtCore.QRect(330, 130, 300, 61))
        
        self.CrashPushLangLabel = QtWidgets.QLabel(self.centralwidget)
        self.CrashPushLangLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.CrashPushLangLabel.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.CrashPushLangLabel.setGeometry(QtCore.QRect(330, 200, 300, 61))
        
        self.CrashPushIgnoreLabel = QtWidgets.QLabel(self.centralwidget)
        self.CrashPushIgnoreLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.CrashPushIgnoreLabel.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.CrashPushIgnoreLabel.setGeometry(QtCore.QRect(330, 270, 300, 61))

        self.CrashPushLogs.setEnabled(False)
        self.CrashPushConfig.setEnabled(False)
        self.CrashPushLogsLabel.setEnabled(False)
        self.CrashPushConfigLabel.setEnabled(False)

        self.CrashPushCloseCompletely = QtWidgets.QPushButton(self.centralwidget)
        self.CrashPushCloseCompletely.resize(160, 23)
        self.CrashPushCloseCompletely.move(CrashWindow.width() - self.CrashPushCloseCompletely.width() - 10, CrashWindow.height() - self.CrashPushCloseCompletely.height() - 10)
        self.CrashPushCloseCompletely.setObjectName("CrashPushCloseCompletely")
        self.CrashPushCloseCompletely.clicked.connect(self.CloseCompletely)

        #self.CrashPushLogsLabel.hide()
        #self.CrashPushConfigLabel.hide()
        #self.CrashPushLangLabel.hide()

        CrashWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(CrashWindow)
        QtCore.QMetaObject.connectSlotsByName(CrashWindow)
        
        self.CrashTextError.setText(ErrorMessage)
        #self.CrashTextError.setText("uhh")
    
    def CloseCompletely(self):
        sys.exit(1)
        
    def OnComboLangChanged(self, index):
        if index == 1:
            self.retranslateUiRussian(CrashWindow)
        elif index == 2:
            self.retranslateUiUkrainian(CrashWindow)
        else:
            self.retranslateUi(CrashWindow)
    
    def CrashOpenLang(self):
        os.startfile(os.getcwd() + "/resources/lang")
    
    def CrashIgnoreError(self):
        CrashWindow.close()

    def retranslateUi(self, CrashWindow):
        _translate = QtCore.QCoreApplication.translate
        CrashWindow.setWindowTitle(_translate("CrashWindow", "katarakta has crashed!"))
        self.CrashLabelTitle.setText(_translate("CrashWindow", "katarakta has crashed!"))
        self.CrashLabelDesc.setText(_translate("CrashWindow", "The program has crashed with the following error message:"))
        self.CrashPushConfig.setText(_translate("CrashWindow", ""))
        self.CrashPushLogs.setText(_translate("CrashWindow", ""))
        self.CrashLabelHelp.setText(_translate("CrashWindow", "Actions that can help you find out what the error is and\n"
"possibly fix it:"))
        self.CrashPushIgnore.setText(_translate("CrashWindow", ""))
        self.CrashLabelReport.setText(_translate("CrashWindow", "If the above didn\'t help, you may either report this issue\n"
"in the program\'s GitHub issues or my Discord server if you\n"
"speak Russian."))
        self.CrashComboLang.setItemText(0, _translate("CrashWindow", "English (United States)"))
        self.CrashComboLang.setItemText(1, _translate("CrashWindow", "Русский (Россия)"))
        self.CrashComboLang.setItemText(2, _translate("CrashWindow", "Українська (Україна)"))
        #self.CrashPushLogsLabel.setText("<span style = 'font-size:13px'>View the logs file</span><br><span style = 'font-size:10px'>The logs store information that<br>may help you identify the problem</span>")
        #self.CrashPushConfigLabel.setText("<span style = 'font-size:13px'>Manually edit the configuration file</span><br><span style = 'font-size:10px'>Your settings file may be broken<br>and katarakta is unable to load it</span>")
        self.CrashPushLogsLabel.setText("<span style = 'font-size:13px'>Coming soon!</span>")
        self.CrashPushConfigLabel.setText("<span style = 'font-size:13px'>Coming soon!</span>")
        self.CrashPushLangLabel.setText("<span style = 'font-size:13px'>Open the language folder</span><br><span style = 'font-size:10px'>If you're using a custom language, it may<br>have an error in it that causes the crash</span>")
        self.CrashPushLang.setToolTip("I know that this is kind of useless, but the icon is too funny, so I'm keeping it in.")
        self.CrashPushIgnoreLabel.setText("<span style = 'font-size:13px'>Ignore the error</span><br><span style = 'font-size:10px'>Continue using katarakta without relaunching.<br><span style = 'color:red'>Not recommended; proceed with caution</span></span>")
        self.CrashPushCloseCompletely.setText(_translate("CrashWindow", "Close completely"))

    def retranslateUiRussian(self, CrashWindow):
        _translate = QtCore.QCoreApplication.translate
        CrashWindow.setWindowTitle(_translate("CrashWindow", "katarakta вылетела!"))
        self.CrashLabelTitle.setText(_translate("CrashWindow", "katarakta вылетела!"))
        self.CrashLabelDesc.setText(_translate("CrashWindow", "Программа вылетела со следующей ошибкой:"))
        self.CrashPushConfig.setText(_translate("CrashWindow", ""))
        self.CrashPushLogs.setText(_translate("CrashWindow", ""))
        self.CrashLabelHelp.setText(_translate("CrashWindow", "Действия, которые могут Вам помочь узнать в чём именно\n"
"проблема и возможно исправить её:"))
        self.CrashPushIgnore.setText(_translate("CrashWindow", ""))
        self.CrashLabelReport.setText(_translate("CrashWindow", "Если действия выше не помогли, то Вы можете рассказать\n"
"об этой проблеме во вкладке Issues на GitHub'е или же на\n"
"моём Discord-сервере, если Вы владеете русским языком."))
        self.CrashComboLang.setItemText(0, _translate("CrashWindow", "English (United States)"))
        self.CrashComboLang.setItemText(1, _translate("CrashWindow", "Русский (Россия)"))
        self.CrashComboLang.setItemText(2, _translate("CrashWindow", "Українська (Україна)"))
        #self.CrashPushLogsLabel.setText("<span style = 'font-size:13px'>View the logs file</span><br><span style = 'font-size:10px'>The logs store information that<br>may help you identify the problem</span>")
        #self.CrashPushConfigLabel.setText("<span style = 'font-size:13px'>Manually edit the configuration file</span><br><span style = 'font-size:10px'>Your settings file may be broken<br>and katarakta is unable to load it</span>")
        self.CrashPushLogsLabel.setText("<span style = 'font-size:13px'>Появится в следующих обновлениях!</span>")
        self.CrashPushConfigLabel.setText("<span style = 'font-size:13px'>Появится в следующих обновлениях!</span>")
        self.CrashPushLangLabel.setText("<span style = 'font-size:13px'>Открыть папку с переводами</span><br><span style = 'font-size:10px'>Если Вы используете пользовательский<br>перевод, то возможно он вызывает ошибку</span>")
        self.CrashPushLang.setToolTip("Знаю, что не прям полезная функция, но мне смешно с иконки, поэтому оставлю.")
        self.CrashPushIgnoreLabel.setText("<span style = 'font-size:13px'>Проигнорировать</span><br><span style = 'font-size:10px'>Продолжить использование без перезапуска.<br><span style = 'color:red'>Не рекомендуется; будьте осторожными</span></span>")
        self.CrashPushCloseCompletely.setText(_translate("CrashWindow", "Полностью закрыть"))

    def retranslateUiUkrainian(self, CrashWindow):
        _translate = QtCore.QCoreApplication.translate
        CrashWindow.setWindowTitle(_translate("CrashWindow", "Стався збій!"))
        self.CrashLabelTitle.setText(_translate("CrashWindow", "Стався збій!"))
        self.CrashLabelDesc.setText(_translate("CrashWindow", "У програмі стався збій з наступним повідомленням:"))
        self.CrashPushConfig.setText(_translate("CrashWindow", ""))
        self.CrashPushLogs.setText(_translate("CrashWindow", ""))
        self.CrashLabelHelp.setText(_translate("CrashWindow", "Дії, які можуть Вам допомогти дізнатися в чому саме\n"
"проблема та, можливо, виправити її:"))
        self.CrashPushIgnore.setText(_translate("CrashWindow", ""))
        self.CrashLabelReport.setText(_translate("CrashWindow", "Якщо дії вище Вам не допомогли, то Ви можете розповісти\n"
"про цю проблему у вкладці Issues на GitHub'і або ж на моєму\n"
"Discord-сервері, якщо Ви спілкуєтесь російською мовою."))
        self.CrashComboLang.setItemText(0, _translate("CrashWindow", "English (United States)"))
        self.CrashComboLang.setItemText(1, _translate("CrashWindow", "Русский (Россия)"))
        self.CrashComboLang.setItemText(2, _translate("CrashWindow", "Українська (Україна)"))
        #self.CrashPushLogsLabel.setText("<span style = 'font-size:13px'>View the logs file</span><br><span style = 'font-size:10px'>The logs store information that<br>may help you identify the problem</span>")
        #self.CrashPushConfigLabel.setText("<span style = 'font-size:13px'>Manually edit the configuration file</span><br><span style = 'font-size:10px'>Your settings file may be broken<br>and katarakta is unable to load it</span>")
        self.CrashPushLogsLabel.setText("<span style = 'font-size:13px'>З'явиться в наступних оновленнях!</span>")
        self.CrashPushConfigLabel.setText("<span style = 'font-size:13px'>З'явиться в наступних оновленнях!</span>")
        self.CrashPushLangLabel.setText("<span style = 'font-size:13px'>Відкрити папку з перекладами</span><br><span style = 'font-size:10px'>Якщо Ви використовуєте користувацький<br>переклад, то мабуть він визиває збій</span>")
        self.CrashPushLang.setToolTip("Знаю, що це не дуже корисна функція, але мені з неї смішно, тому залишу.")
        self.CrashPushIgnoreLabel.setText("<span style = 'font-size:13px'>Проігнорувати</span><br><span style = 'font-size:10px'>Продовжити використання без перезапуску.<br><span style = 'color:red'>Не рекомендується; будьте обережними</span></span>")
        self.CrashPushCloseCompletely.setText(_translate("CrashWindow", "Повністю закрити"))

def HandleException(exc_type, exc_value, exc_traceback):
    global CrashWindow
    global app
    
    try:
        traceback_info = "".join(traceback.format_exception(exc_type, exc_value, exc_traceback))
        ErrorPlace = "WhileRunning"
    except:
        traceback_info = exc_value
        ErrorPlace = "WhileLaunching"
    
    print(traceback_info)
    
    try:
        if app is None:
            app = QApplication(sys.argv)
    except:
        app = QApplication(sys.argv)
    CrashWindow = Ui_CrashWindow()
    CrashWindow.setupUi(CrashWindow, traceback_info)
    CrashWindow.show()
    
    try:
        sys.exit(app.exec_())
    except:
        pass
    
sys.excepthook = HandleException

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
    TexturesRAM = []
    Display1 = ""
    Display2 = ""
    Display3 = ""
    Display4 = ""

Option = Options()

class LanguageText():
    pass

global BG_OptionMode
global AddNamesList
global ApplyDropdownConnected
ApplyDropdownConnected = False
global SW_AIToolTip
SW_AIToolTip = ""
global listWidgetXOffset, groupBoxXPos, ApplySM64XPos, ApplyDropdownXPos, SwitchItemsButtonXPos

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
        "eyelistrowheight": "0",
        "enablerammod": "1",
        "autofixbody": "1",
        "radioram": "1",
        "enableramutilities": "1",
        "enabledebugoptions": "0",
        "radiofiltering": "1",
        "checkmirrorui": "0",
        "checkmirrormenubar": "0",
        "checkmirroreyelist": "0"
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
        "eyelistrowheight": "0",
        "enablerammod": "1",
        "autofixbody": "1",
        "radioram": "1",
        "enableramutilities": "1",
        "enabledebugoptions": "0",
        "radiofiltering": "1",
        "checkmirrorui": "0",
        "checkmirrormenubar": "0",
        "checkmirroreyelist": "0"
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
    Option.EnableRAMMod = ConfigSecond.get("enablerammod")
    Option.AutoFixBody = ConfigSecond.get("autofixbody")
    Option.RadioRAM = ConfigSecond.get("radioram")
    Option.EnableRAMUtilities = ConfigSecond.get("enableramutilities")
    Option.EnableDebugOptions = ConfigSecond.get("enabledebugoptions")
    Option.RadioFiltering = ConfigSecond.get("radiofiltering")
    Option.CheckMirrorUI = ConfigSecond.get("checkmirrorui")
    Option.CheckMirrorMenubar = ConfigSecond.get("checkmirrormenubar")
    Option.CheckMirrorEyeList = ConfigSecond.get("checkmirroreyelist")

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
        Language.MW_submenuEyeStates =          ConfigLanguage.get("MW_submenuEyeStates")
        Language.MW_actionFixBlackTextures =    ConfigLanguage.get("MW_actionFixBlackTextures")
        Language.MW_submenuUtilities =          ConfigLanguage.get("MW_submenuUtilities")
        Language.MW_EyeState =                  ConfigLanguage.get("MW_EyeState")
        Language.MW_actionStateFixBody =        ConfigLanguage.get("MW_actionStateFixBody")
        Language.MW_actionDebugCrash =          ConfigLanguage.get("MW_actionDebugCrash")
        Language.MW_actionDebugCrashEffect =    ConfigLanguage.get("MW_actionDebugCrashEffect")
        
        ConfigLanguage = Config["ABOUTWINDOW"]
        Language.AW_Title =             ConfigLanguage.get("AW_Title")
        Language.AW_LabelName =         ConfigLanguage.get("AW_LabelName")
        Language.AW_LabelVersion =      ConfigLanguage.get("AW_LabelVersion")
        Language.AW_LabelEdition =      ConfigLanguage.get("AW_LabelEdition")
        Language.AW_LabelAuthor =       ConfigLanguage.get("AW_LabelAuthor")
        Language.AW_SpecialThanks =     ConfigLanguage.get("AW_SpecialThanks")
        Language.AW_SpecialThanksHelp = ConfigLanguage.get("AW_SpecialThanksHelp")
        Language.AW_LabelAddInfo =      ConfigLanguage.get("AW_LabelAddInfo")
        Language.AW_LabelReportIssue =  ConfigLanguage.get("AW_LabelReportIssue")
        Language.AW_LabelLegalNotice =  ConfigLanguage.get("AW_LabelLegalNotice")

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
        Language.SW_CheckEnableRAMMod =              ConfigLanguage.get("SW_CheckEnableRAMMod")
        Language.SW_CheckAutoFixBody =               ConfigLanguage.get("SW_CheckAutoFixBody")
        Language.SW_RadioRAMIfCannotReplace =        ConfigLanguage.get("SW_RadioRAMIfCannotReplace")
        Language.SW_RadioRAMIfNone =                 ConfigLanguage.get("SW_RadioRAMIfNone")
        Language.SW_RadioRAMOnly =                   ConfigLanguage.get("SW_RadioRAMOnly")
        Language.SW_CheckEnableRAMUtilities =        ConfigLanguage.get("SW_CheckEnableRAMUtilities")
        Language.SW_groupRAMReplace =                ConfigLanguage.get("SW_groupRAMReplace")
        Language.SW_groupRAMUtilities =              ConfigLanguage.get("SW_groupRAMUtilities")
        Language.SW_TabRAM =                         ConfigLanguage.get("SW_TabRAM")
        Language.SW_CheckEnableDebugOptions =        ConfigLanguage.get("SW_CheckEnableDebugOptions")
        Language.SW_RadioFilteringNone =             ConfigLanguage.get("SW_RadioFilteringNone")
        Language.SW_RadioFilteringBilinear =         ConfigLanguage.get("SW_RadioFilteringBilinear")
        Language.SW_RadioFilteringN64 =              ConfigLanguage.get("SW_RadioFilteringN64")
        Language.SW_CheckMirrorUI =                  ConfigLanguage.get("SW_CheckMirrorUI")
        Language.SW_CheckMirrorMenubar =             ConfigLanguage.get("SW_CheckMirrorMenubar")
        Language.SW_CheckMirrorEyeList =             ConfigLanguage.get("SW_CheckMirrorEyeList")
        
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
        
    def closeEvent(self, event):
        sys.exit(0)
    
    def RightOrLeftMode(self):
        global listWidgetXOffset, groupBoxXPos, ApplySM64XPos, ApplyDropdownXPos, SwitchItemsButtonXPos
        if Option.CheckMirrorUI == "0":
            listWidgetXOffset = 0
            groupBoxXPos = MainWindow.width() - 131
            ApplySM64XPos = MainWindow.width() - 132
            SwitchItemsButtonXPos = MainWindow.width() - 132
        else:
            listWidgetXOffset = 123
            groupBoxXPos = 18
            ApplySM64XPos = 17
            SwitchItemsButtonXPos = 17
        ApplyDropdownXPos = ApplySM64XPos + 92
    
    def RightOrLeftMenubar(self):
        if Option.CheckMirrorMenubar == "0":
            self.menubar.setLayoutDirection(Qt.LeftToRight)
        else:
            self.menubar.setLayoutDirection(Qt.RightToLeft)
    
    def RightOrLeftListWidget(self):
        if Option.CheckMirrorEyeList == "0":
            self.listWidget.setLayoutDirection(Qt.LeftToRight)
        else:
            self.listWidget.setLayoutDirection(Qt.RightToLeft)

    def resizeEventFunction(self):
        global listWidgetXOffset, groupBoxXPos, ApplySM64XPos, ApplyDropdownXPos, SwitchItemsButtonXPos
        self.RightOrLeftMode()
        self.listWidget.setGeometry(QtCore.QRect(18 + listWidgetXOffset, 16, MainWindow.width() - 159, MainWindow.height() - 67))
        self.groupBox.move(groupBoxXPos, self.groupBox.y())
        self.ApplySM64.move(ApplySM64XPos, self.ApplySM64.y())
        self.ApplyDropdown.move(ApplyDropdownXPos, self.ApplySM64.y())
        if Option.DoNotMoveSwitchVertically == "1":
            self.SwitchItemsButton.move(SwitchItemsButtonXPos, 490)
        else:
            self.SwitchItemsButton.move(SwitchItemsButtonXPos, (MainWindow.height() - 74))

    def resizeEvent(self, resizeEvent):
        self.resizeEventFunction()
    
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

    def OpenBodyStateWindow(self):
        self.BodyStateWindow = QtWidgets.QMainWindow()
        self.BodyStateWindowUi = Ui_BodyStateWindow()
        self.BodyStateWindowUi.setupUi(self.BodyStateWindow)
        self.BodyStateWindow.show()

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
        
        MainWindow.setWindowIcon(QtGui.QIcon(kataraktaIcon))

        if Option.StartUpCheckForUpdates == "1":
            if IsTestVersion is False:
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
        self.groupBox.setGeometry(QtCore.QRect(238, 10, 113, 333))
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
        self.SM64DisplayLabel2.setGeometry(QtCore.QRect(6, self.SM64DisplayLabel1.y() + 107, 101, 101))
        self.SM64DisplayLabel2.setText("")
        self.SM64DisplayLabel2.setPixmap(QtGui.QPixmap("resources/img/PlaceHolderEye2.png"))
        self.SM64DisplayLabel2.setScaledContents(True)
        self.SM64DisplayLabel2.setObjectName("SM64DisplayLabel2")
        
        self.SM64DisplayLabel3 = QtWidgets.QLabel(self.groupBox)
        #self.SM64DisplayLabel3.setGeometry(QtCore.QRect(14, 234, 101, 101))
        self.SM64DisplayLabel3.setGeometry(QtCore.QRect(6, self.SM64DisplayLabel2.y() + 107, 101, 101))
        self.SM64DisplayLabel3.setText("")
        self.SM64DisplayLabel3.setPixmap(QtGui.QPixmap("resources/img/PlaceHolderEye3.png"))
        self.SM64DisplayLabel3.setScaledContents(True)
        self.SM64DisplayLabel3.setObjectName("SM64DisplayLabel3")
        
        self.SM64DisplayLabel4 = QtWidgets.QLabel(self.groupBox)
        #self.SM64DisplayLabel4.setGeometry(QtCore.QRect(14, 341, 101, 101))
        self.SM64DisplayLabel4.setGeometry(QtCore.QRect(6, self.SM64DisplayLabel3.y() + 107, 101, 101))
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

        self.listWidget.itemSelectionChanged.connect(self.OnSelectionChanged)
        
        self.labelExplode = QtWidgets.QLabel(self)
        self.labelExplode.setObjectName("labelExplode")
        self.labelExplode.setScaledContents(True)
        self.labelExplode.setStyleSheet("background-color: rgba(255, 255, 255, 0);")

        #Switch to cap, hair etc. from eyes and vice versa button
        self.SwitchItemsButton = QtWidgets.QPushButton(self.centralwidget)
        #self.SwitchItemsButton.setGeometry(QtCore.QRect(237, 489, 130, 23))
        #self.SwitchItemsButton.setGeometry(QtCore.QRect(237, 489, 262, 23))
        self.SwitchItemsButton.setObjectName("SwitchButton")
        self.SwitchItemsButton.clicked.connect(lambda: self.SwitchItems())
        self.SwitchItemsButton.setStyleSheet("font-size: 11px")
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
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout.triggered.connect(self.OpenAboutWindow)

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
        self.actionStayOnTop = QtWidgets.QAction(MainWindow)
        self.actionStayOnTop.setObjectName("actionStayOnTop")
        self.actionStayOnTop.setCheckable(True)
        self.actionStayOnTop.triggered.connect(self.StayOnTop)
        self.submenuUtilities = QtWidgets.QMenu(MainWindow)
        self.submenuUtilities.setObjectName("submenuUtilities")
        #self.submenuUtilities.setIcon(QIcon("resources/img/fixBodyStateReset.png"))

        self.submenuEyeBorders = self.submenuUtilities.addMenu("submenuEyeBorders")
        self.submenuEyeBorders.setObjectName("submenuEyeBorders")

        self.submenuUtilities.addSeparator()

        self.submenuEyeStates = self.submenuUtilities.addMenu("submenuEyeStates")
        self.submenuEyeStates.setObjectName("submenuEyeStates")
        self.submenuEyeStates.setIcon(QIcon("resources/img/eyes2.png"))

        self.actionStateFixBody = self.submenuEyeStates.addAction("actionStateFixBody")
        self.submenuEyeStates.addSeparator()
        self.actionStateEyes0 = self.submenuEyeStates.addAction("actionStateEyes0")
        self.actionStateEyes1 = self.submenuEyeStates.addAction("actionStateEyes1")
        self.actionStateEyes2 = self.submenuEyeStates.addAction("actionStateEyes2")
        self.actionStateEyes3 = self.submenuEyeStates.addAction("actionStateEyes3")
        self.actionStateEyes4 = self.submenuEyeStates.addAction("actionStateEyes4")
        self.actionStateEyes5 = self.submenuEyeStates.addAction("actionStateEyes5")
        self.actionStateEyes6 = self.submenuEyeStates.addAction("actionStateEyes6")
        self.actionStateEyes7 = self.submenuEyeStates.addAction("actionStateEyes7")
        self.actionStateEyes8 = self.submenuEyeStates.addAction("actionStateEyes8")

        self.actionStateFixBody.setObjectName("actionStateFixBody")
        self.actionStateEyes0.setObjectName("actionStateEyes0")
        self.actionStateEyes1.setObjectName("actionStateEyes1")
        self.actionStateEyes2.setObjectName("actionStateEyes2")
        self.actionStateEyes3.setObjectName("actionStateEyes3")
        self.actionStateEyes4.setObjectName("actionStateEyes4")
        self.actionStateEyes5.setObjectName("actionStateEyes5")
        self.actionStateEyes6.setObjectName("actionStateEyes6")
        self.actionStateEyes7.setObjectName("actionStateEyes7")
        self.actionStateEyes8.setObjectName("actionStateEyes8")
        
        self.actionStateFixBody.triggered.connect(RAMFunctions.pushFixBodyFunc)
        self.actionStateEyes0.triggered.connect(lambda: RAMFunctions.pushEyesFunc(self, 0))
        self.actionStateEyes1.triggered.connect(lambda: RAMFunctions.pushEyesFunc(self, 1))
        self.actionStateEyes2.triggered.connect(lambda: RAMFunctions.pushEyesFunc(self, 2))
        self.actionStateEyes3.triggered.connect(lambda: RAMFunctions.pushEyesFunc(self, 3))
        self.actionStateEyes4.triggered.connect(lambda: RAMFunctions.pushEyesFunc(self, 4))
        self.actionStateEyes5.triggered.connect(lambda: RAMFunctions.pushEyesFunc(self, 5))
        self.actionStateEyes6.triggered.connect(lambda: RAMFunctions.pushEyesFunc(self, 6))
        self.actionStateEyes7.triggered.connect(lambda: RAMFunctions.pushEyesFunc(self, 7))
        self.actionStateEyes8.triggered.connect(lambda: RAMFunctions.pushEyesFunc(self, 8))

        self.actionFixBlackTextures = self.submenuUtilities.addAction("actionFixBlackTextures")
        self.actionFixBlackTextures.setObjectName("actionFixBlackTextures")
        self.actionFixBlackTextures.triggered.connect(self.FixBlackTexturesFunc)
        self.actionFixBlackTextures.setIcon(QIcon("resources/img/SaveStateFixer.png"))

        self.EyeBordersCurrent = self.submenuEyeBorders.addAction("Current")
        self.EyeBordersAll = self.submenuEyeBorders.addAction("All")
        self.actionRefresh = QtWidgets.QAction(self.menubar)
        self.actionRefresh.setObjectName("actionRefresh")
        self.actionRefresh.triggered.connect(self.RefreshEyeList)

        self.actionUpdate = QtWidgets.QAction(MainWindow)
        self.actionUpdate.setObjectName("actionUpdate")
        self.actionUpdate.triggered.connect(self.OpenUpdateWindow)
        if IsTestVersion is False:
            self.actionUpdate.setVisible(True)
        else:
            self.actionUpdate.setVisible(False)
        
        self.actionDebugCrash = QtWidgets.QAction(MainWindow)
        self.actionDebugCrash.triggered.connect(self.DebugCrash)
        self.actionDebugCrashEffect = QtWidgets.QAction(MainWindow)
        self.actionDebugCrashEffect.triggered.connect(self.DebugCrashEffect)

        if Option.StartUpStayOnTop == "1":
            self.actionStayOnTop.setChecked(True)
            self.StayOnTop()
        
        if Option.DarkMode == "1":
            self.actionDarkMode.setChecked(True)
        
        self.ApplySM64.setEnabled(False)
        
        self.ApplySM64.clicked.connect(lambda: self.CopyEyes("SM64Dir", (self.listWidget.selectedIndexes()[0].data(Qt.DisplayRole))))
        self.EyeBordersCurrent.triggered.connect(lambda: self.RemoveEyeBorders("Current"))
        self.EyeBordersAll.triggered.connect(lambda: self.RemoveEyeBorders("All"))
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.DarkModeSwitch()
        self.HideAdditional()
        
        self.RefreshEyeList()

    def TextureFiltering(self, path):
        if Option.RadioFiltering == "0":
            # No filtering
            qpixmap = QPixmap(path)
            qpixmap = qpixmap.scaled(self.SM64DisplayLabel1.size(), Qt.KeepAspectRatio, Qt.FastTransformation)
        if Option.RadioFiltering == "1":
            # Bilinear filtering. The one that is common in N64 emulation
            qpixmap = QPixmap(path)
        if Option.RadioFiltering == "2":
            # 3-point filtering. The one that N64 actually uses
            img = Image.open(path)
            img = img.convert('RGBA')
            upscale_factor = 2
            img = img.resize((img.width * upscale_factor, img.height * upscale_factor), Image.NEAREST)

            img_array = np.array(img)
            
            height, width, _ = img_array.shape

            right_down = img_array[1:, :-1]  # (bottom-right)
            center = img_array[:-1, 1:]  # (center)
            left_up = img_array[:-1, 1:]  # (top-left)

            # We do this two times so that
            # 1. To be more similar to N64's filtering
            # 2. To be more centered (it off-centers the image for some reason and I don't know any other way for fixing this:sob:)
            filtered_rgb = np.mean([right_down[:, :, :3], center[:, :, :3], left_up[:, :, :3]], axis=0).astype(int)
            filtered_alpha = np.mean([right_down[:, :, 3], center[:, :, 3], left_up[:, :, 3]], axis=0).astype(int)

            img_array[1:, :-1, :3] = filtered_rgb
            img_array[1:, :-1, 3] = filtered_alpha

            filtered_rgb = np.mean([right_down[:, :, :3], center[:, :, :3], left_up[:, :, :3]], axis=0).astype(int)
            filtered_alpha = np.mean([right_down[:, :, 3], center[:, :, 3], left_up[:, :, 3]], axis=0).astype(int)

            img_array[:-1, 1:, :3] = filtered_rgb
            img_array[:-1, 1:, 3] = filtered_alpha

            result_img = Image.fromarray(img_array)

            result_img_data = result_img.convert("RGBA").tobytes("raw", "RGBA")
            width, height = result_img.size
            qimage = QtGui.QImage(result_img_data, width, height, QtGui.QImage.Format_RGBA8888)

            qpixmap = QPixmap(qimage)
        return qpixmap
    
    def ShowRAMUtilities(self):
        if Option.EnableRAMUtilities == "1":
            self.submenuEyeStates.menuAction().setVisible(True)
            self.actionFixBlackTextures.setVisible(True)
        else:
            self.submenuEyeStates.menuAction().setVisible(False)
            self.actionFixBlackTextures.setVisible(False)
    
    def FixBlackTexturesFunc(self):
        Utils.find_base_address()
        for i in range(0, 1048575):
            if Utils.read_ulong(Utils.base_address + i*8) == 0xFFFFF838FC127FFF:
                Utils.write_ulong(Utils.base_address + i*8, 0xFF33FFFFFC121824)
        
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
        MainWindow.setMinimumSize(369, 551)
        MainWindow.resize(369, 551)

    def DarkModeSwitch(self):
        if os.path.exists("config.ini") is True:
            pass
        else:
            CreateConfig()
        Config = configparser.ConfigParser()
        Config.read("config.ini")
        
        self.actionAbout.setIcon(QIcon(kataraktaIcon))
        global DarkMode
        if DarkMode == 1:
            app.setStyle("Fusion")
            app.setPalette(DarkPalette)
            
            self.submenuHiRes.setIcon(QIcon("resources/img/DarkMode/HiResMain.png"))
            self.actionSettings.setIcon(QIcon("resources/img/DarkMode/Settings.png"))
            self.HiResClearSM64.setIcon(QIcon("resources/img/DarkMode/HiResClear.png"))
            self.HiResClearAdd.setIcon(QIcon("resources/img/DarkMode/HiResClearAdd.png"))
            self.HiResOpenSM64.setIcon(QIcon("resources/img/DarkMode/HiResOpen.png"))
            self.actionOpenKataraktaFolder.setIcon(QIcon("resources/img/DarkMode/OpenKataraktaFolder.png"))
            self.actionStayOnTop.setIcon(QIcon("resources/img/DarkMode/StayOnTop.png"))
            self.actionDarkMode.setIcon(QIcon("resources/img/ModeLight.png"))
            self.submenuEyeBorders.setIcon(QIcon("resources/img/DarkMode/EyeBorders.png"))
            self.EyeBordersCurrent.setIcon(QIcon("resources/img/DarkMode/EyeBordersCurrent.png"))
            self.EyeBordersAll.setIcon(QIcon("resources/img/DarkMode/EyeBordersAll.png"))
            self.actionRefresh.setIcon(QIcon("resources/img/DarkMode/Refresh.png"))
            self.submenuUtilities.setIcon(QIcon("resources/img/DarkMode/Utilities.png"))

            self.actionStateFixBody.setIcon(QIcon("resources/img/DarkMode/fixBodyStateReset.png"))
            self.actionStateEyes0.setIcon(QIcon("resources/img/DarkMode/eyes1.png"))
            self.actionStateEyes1.setIcon(QIcon("resources/img/DarkMode/eyes2.png"))
            self.actionStateEyes2.setIcon(QIcon("resources/img/DarkMode/eyes3.png"))
            self.actionStateEyes3.setIcon(QIcon("resources/img/DarkMode/eyes4.png"))
            self.actionStateEyes4.setIcon(QIcon("resources/img/DarkMode/eyes5.png"))
            self.actionStateEyes5.setIcon(QIcon("resources/img/DarkMode/eyes6.png"))
            self.actionStateEyes6.setIcon(QIcon("resources/img/DarkMode/eyes7.png"))
            self.actionStateEyes7.setIcon(QIcon("resources/img/DarkMode/eyes8.png"))
            self.actionStateEyes8.setIcon(QIcon("resources/img/DarkMode/eyes9.png"))

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
            
            self.submenuHiRes.setIcon(QIcon("resources/img/HiResMain.png"))
            self.actionSettings.setIcon(QIcon("resources/img/Settings.png"))
            self.HiResClearSM64.setIcon(QIcon("resources/img/HiResClear.png"))
            self.HiResClearAdd.setIcon(QIcon("resources/img/HiResClearAdd.png"))
            self.HiResOpenSM64.setIcon(QIcon("resources/img/HiResOpen.png"))
            self.actionOpenKataraktaFolder.setIcon(QIcon("resources/img/OpenKataraktaFolder.png"))
            self.actionStayOnTop.setIcon(QIcon("resources/img/StayOnTop.png"))
            self.actionDarkMode.setIcon(QIcon("resources/img/ModeDark.png"))
            self.submenuEyeBorders.setIcon(QIcon("resources/img/EyeBorders.png"))
            self.EyeBordersCurrent.setIcon(QIcon("resources/img/EyeBordersCurrent.png"))
            self.EyeBordersAll.setIcon(QIcon("resources/img/EyeBordersAll.png"))
            self.actionRefresh.setIcon(QIcon("resources/img/Refresh.png"))
            self.submenuUtilities.setIcon(QIcon("resources/img/Utilities.png"))

            self.actionStateFixBody.setIcon(QIcon("resources/img/fixBodyStateReset.png"))
            self.actionStateEyes0.setIcon(QIcon("resources/img/eyes1.png"))
            self.actionStateEyes1.setIcon(QIcon("resources/img/eyes2.png"))
            self.actionStateEyes2.setIcon(QIcon("resources/img/eyes3.png"))
            self.actionStateEyes3.setIcon(QIcon("resources/img/eyes4.png"))
            self.actionStateEyes4.setIcon(QIcon("resources/img/eyes5.png"))
            self.actionStateEyes5.setIcon(QIcon("resources/img/eyes6.png"))
            self.actionStateEyes6.setIcon(QIcon("resources/img/eyes7.png"))
            self.actionStateEyes7.setIcon(QIcon("resources/img/eyes8.png"))
            self.actionStateEyes8.setIcon(QIcon("resources/img/eyes9.png"))

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
        # Repeating this two times is intentional since if you do this only one time while having a ";" at the end of Option.AddNames, you'll still have a "" at the end of the list for some reason
        for i in ["", " ", None]:
            while i in AddNamesList:
                try:
                    AddNamesList.remove(i)
                except:
                    pass
        return AddNamesList
    
    def RefreshEyeList(self):
        EyeFolders = os.listdir("eyes/")
        CHMBFolders = os.listdir("chmb/")
        self.GetAddNames()
        global ApplyDropdownConnected
        
        self.menuOptions.clear()
        self.menuHelp.clear()
        self.menubar.clear()
        
        self.menuOptions.addMenu(self.submenuHiRes)
        self.menuOptions.addAction(self.actionOpenKataraktaFolder)
        self.menuOptions.addMenu(self.submenuUtilities)
        self.ShowRAMUtilities()
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.actionSettings)
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.actionStayOnTop)
        self.menuOptions.addAction(self.actionDarkMode)
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.actionRefresh)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuOptions.menuAction())
        
        if Option.EnableDebugOptions == "1":
            self.menuOptions.addSeparator()
            self.menuOptions.addAction(self.actionDebugCrash)
            self.menuOptions.addAction(self.actionDebugCrashEffect)
        
        self.EyeBordersCurrent.setEnabled(False)
        
        self.menubar.addAction(self.actionUpdate)
        
        self.menubar.addAction(self.menuHelp.menuAction())
        
        self.setStyleSheet("QTreeView::item { padding: "+Option.EyeListRowHeight+"px }")

        self.resizeEventFunction()
        self.RightOrLeftMenubar()
        self.RightOrLeftListWidget()
        
        self.retranslateUiEnglish(MainWindow)
        if Language.Properties_InnerName != "English":
            self.retranslateUiOther(MainWindow)
        self.Update()
        
        if ApplyDropdownConnected == True:
            self.ApplyDropdown.clicked.disconnect()
        self.ApplyDropdown.clicked.connect(self.ApplyDropdownContext)
        ApplyDropdownConnected = True
        if len(AddNamesList) == 0:
            self.ApplyDropdown.setEnabled(False)

        global listWidgetXOffset, groupBoxXPos, ApplySM64XPos, ApplyDropdownXPos, SwitchItemsButtonXPos
        self.RightOrLeftMode()
        if self.Mode == "Eyes":
            self.PopulateTree("eyes/")
            
            self.ApplySM64.setGeometry(QtCore.QRect(ApplySM64XPos, 346, 94, 23))
            self.ApplyDropdown.setGeometry(QtCore.QRect(ApplyDropdownXPos, self.ApplySM64.pos().y(), 23, 23))
        else:
            self.PopulateTree("chmb/")
                    
            self.ApplySM64.setGeometry(QtCore.QRect(ApplySM64XPos, 453, 94, 23))
            self.ApplyDropdown.setGeometry(QtCore.QRect(ApplyDropdownXPos, self.ApplySM64.pos().y(), 23, 23))
        self.listWidget.clearSelection()
        try:
            self.ApplySM64.setEnabled(False)
            self.ApplyDropdown.setEnabled(False)
            if self.Mode == "Eyes":
                self.SM64DisplayLabel1.setPixmap(self.TextureFiltering("resources/img/PlaceHolderEye1.png"))
                self.SM64DisplayLabel2.setPixmap(self.TextureFiltering("resources/img/PlaceHolderEye2.png"))
                self.SM64DisplayLabel3.setPixmap(self.TextureFiltering("resources/img/PlaceHolderEye3.png"))
                self.SM64DisplayLabel4.setPixmap(self.TextureFiltering())
            if self.Mode == "CHMB":
                self.SM64DisplayLabel1.setPixmap(self.TextureFiltering("resources/img/PlaceHolderCap.png"))
                self.SM64DisplayLabel2.setPixmap(self.TextureFiltering("resources/img/PlaceHolderHair.png"))
                self.SM64DisplayLabel3.setPixmap(self.TextureFiltering("resources/img/PlaceHolderMustache.png"))
                self.SM64DisplayLabel4.setPixmap(self.TextureFiltering("resources/img/PlaceHolderButton.png"))
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
            
            self.groupBox.setGeometry(QtCore.QRect(QtCore.QRect(self.groupBox.pos().x(), self.groupBox.pos().y(), 128, 440)))
            
            self.Update()
            
            self.SM64DisplayLabel1.setPixmap(self.TextureFiltering("resources/img/PlaceHolderCap.png"))
            self.SM64DisplayLabel2.setPixmap(self.TextureFiltering("resources/img/PlaceHolderHair.png"))
            self.SM64DisplayLabel3.setPixmap(self.TextureFiltering("resources/img/PlaceHolderMustache.png"))
            self.SM64DisplayLabel4.setPixmap(self.TextureFiltering("resources/img/PlaceHolderButton.png"))
            
            self.SM64DisplayLabel4.show()
            
        else:
            self.Mode = "Eyes"
            
            self.groupBox.setGeometry(QtCore.QRect(self.groupBox.pos().x(), self.groupBox.pos().y(), 128, 333))

            self.Update()

            self.SM64DisplayLabel1.setPixmap(self.TextureFiltering("resources/img/PlaceHolderEye1.png"))
            self.SM64DisplayLabel2.setPixmap(self.TextureFiltering("resources/img/PlaceHolderEye2.png"))
            self.SM64DisplayLabel3.setPixmap(self.TextureFiltering("resources/img/PlaceHolderEye3.png"))

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
                self.SM64DisplayLabel1.setPixmap(self.TextureFiltering("resources/img/PlaceHolderOther.png"))
                self.SM64DisplayLabel2.setPixmap(self.TextureFiltering("resources/img/PlaceHolderOther.png"))
                self.SM64DisplayLabel3.setPixmap(self.TextureFiltering("resources/img/PlaceHolderOther.png"))
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
                    self.SM64DisplayLabel1.setPixmap(self.TextureFiltering(f"{PathToTextures}/{OtherTextures.Display1}.png"))
                if OtherTextures.Display2 != "":
                    self.SM64DisplayLabel2.setPixmap(self.TextureFiltering(f"{PathToTextures}/{OtherTextures.Display2}.png"))
                if OtherTextures.Display3 != "":
                    self.SM64DisplayLabel3.setPixmap(self.TextureFiltering(f"{PathToTextures}/{OtherTextures.Display3}.png"))
                if OtherTextures.Display4 != "":
                    self.SM64DisplayLabel4.setPixmap(self.TextureFiltering(f"{PathToTextures}/{OtherTextures.Display4}.png"))
            else:
                self.SM64DisplayLabel1.setPixmap(self.TextureFiltering("resources/img/PlaceHolderEye1.png"))
                self.SM64DisplayLabel2.setPixmap(self.TextureFiltering("resources/img/PlaceHolderEye2.png"))
                self.SM64DisplayLabel3.setPixmap(self.TextureFiltering("resources/img/PlaceHolderEye3.png"))
                
                if os.path.exists("{}/{}.png".format(PathToTextures, Option.SM64Name + Option.Eyes1)):
                    self.SM64DisplayLabel1.setPixmap(self.TextureFiltering(f"{PathToTextures}/{Option.SM64Name + Option.Eyes1}.png"))
                    CheckSM64 += 1
                if os.path.exists("{}/{}.png".format(PathToTextures, Option.SM64Name + Option.Eyes2)):
                    self.SM64DisplayLabel2.setPixmap(self.TextureFiltering(f"{PathToTextures}/{Option.SM64Name + Option.Eyes2}.png"))
                    CheckSM64 += 1
                if os.path.exists("{}/{}.png".format(PathToTextures, Option.SM64Name + Option.Eyes3)):
                    self.SM64DisplayLabel3.setPixmap(self.TextureFiltering(f"{PathToTextures}/{Option.SM64Name + Option.Eyes3}.png"))
                    CheckSM64 += 1
        else:
            if os.path.isfile("{}/other.ini".format(PathToTextures)) == True:
                self.SM64DisplayLabel1.setPixmap(self.TextureFiltering("resources/img/PlaceHolderOther.png"))
                self.SM64DisplayLabel2.setPixmap(self.TextureFiltering("resources/img/PlaceHolderOther.png"))
                self.SM64DisplayLabel3.setPixmap(self.TextureFiltering("resources/img/PlaceHolderOther.png"))
                self.SM64DisplayLabel4.setPixmap(self.TextureFiltering("resources/img/PlaceHolderOther.png"))
                
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
                    self.SM64DisplayLabel1.setPixmap(self.TextureFiltering(f"{PathToTextures}/{OtherTextures.Display1}.png"))
                if OtherTextures.Display2 != "":
                    self.SM64DisplayLabel2.setPixmap(self.TextureFiltering(f"{PathToTextures}/{OtherTextures.Display1}.png"))
                if OtherTextures.Display3 != "":
                    self.SM64DisplayLabel3.setPixmap(self.TextureFiltering(f"{PathToTextures}/{OtherTextures.Display1}.png"))
                if OtherTextures.Display4 != "":
                    self.SM64DisplayLabel4.setPixmap(self.TextureFiltering(f"{PathToTextures}/{OtherTextures.Display1}.png"))
            
            else:
                self.SM64DisplayLabel1.setPixmap(self.TextureFiltering("resources/img/PlaceHolderCap.png"))
                self.SM64DisplayLabel2.setPixmap(self.TextureFiltering("resources/img/PlaceHolderHair.png"))
                self.SM64DisplayLabel3.setPixmap(self.TextureFiltering("resources/img/PlaceHolderMustache.png"))
                self.SM64DisplayLabel4.setPixmap(self.TextureFiltering("resources/img/PlaceHolderButton.png"))
                
                if os.path.exists("{}/{}.png".format(PathToTextures, Option.SM64Name + Option.Cap)):
                    self.SM64DisplayLabel1.setPixmap(self.TextureFiltering(f"{PathToTextures}/{Option.SM64Name + Option.Cap}.png"))
                    CheckSM64 += 1
                if os.path.exists("{}/{}.png".format(PathToTextures, Option.SM64Name + Option.Hair)):
                    self.SM64DisplayLabel2.setPixmap(self.TextureFiltering(f"{PathToTextures}/{Option.SM64Name + Option.Hair}.png"))
                    CheckSM64 += 1
                if os.path.exists("{}/{}.png".format(PathToTextures, Option.SM64Name + Option.Mustache)):
                    self.SM64DisplayLabel3.setPixmap(self.TextureFiltering(f"{PathToTextures}/{Option.SM64Name + Option.Mustache}.png"))
                    CheckSM64 += 1
                if os.path.exists("{}/{}.png".format(PathToTextures, Option.SM64Name + Option.Button)):
                    self.SM64DisplayLabel4.setPixmap(self.TextureFiltering(f"{PathToTextures}/{Option.SM64Name + Option.Button}.png"))
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
        FolderNames = self.listWidget.selectedItems()
        if not FolderNames:
            return
        FolderName = FolderNames[0]
        PathToTextures = FolderName.data(0, Qt.UserRole)
        
        if Type == "SM64Dir":
            PasteName = Option.SM64Name
        else:
            PasteName = Type
        
        if os.path.isfile("{}/other.ini".format(PathToTextures)) == True:
            Config.read("{}/other.ini".format(PathToTextures), encoding = "utf-8")
            ConfigOther = Config["OTHER"]
            OtherTextures.Textures = ConfigOther.get("Other_Textures", OtherTextures.Textures).split(";")
            try:
                TexturesRAM1 = [item.split(",") for item in ConfigOther.get("Other_TexturesRAM", OtherTextures.TexturesRAM).replace(" ", "").split(";")]
                OtherTextures.TexturesRAM = [[int(x, 16) for x in sublist[:2]] + sublist[2:] for sublist in TexturesRAM1]
            except:
                pass
            NewOtherTextures = []
            for i in OtherTextures.Textures:
                if i.find("#") != -1:
                    NewOtherTextures.append(i[i.find("#"):])
        
        # Find out what textures we need to change
        ChangeTextureListAll = []
        if os.path.isfile("{}/other.ini".format(PathToTextures)) == True:
            if OtherTextures.ApplyEverything == "1":
                for i in os.listdir("{}/".format(PathToTextures)):
                    if i.endswith(".png"):
                        if i.find("#") != -1:
                            ChangeTextureListAll.append([i[i.find("#"):-4]])
            else:
                for i in OtherTextures.Textures:
                    if i.find("#") != -1:
                        ChangeTextureListAll.append([i[i.find("#"):]])
        elif self.Mode == "Eyes":
            ChangeTextureListAll = [[Option.Eyes1], [Option.Eyes2], [Option.Eyes3]]
        else:
            ChangeTextureListAll = [[Option.Cap], [Option.Hair], [Option.Mustache], [Option.Button]]
        
        # Remove the cache file some GFX plugins create because it may prevent new textures from loading in place of old ones that were cached
        self.GetAddNames()
        AllNamesList = AddNamesList.copy()
        AllNamesList.append(Option.SM64Name)
        for i in AllNamesList:
            if os.path.isfile("{}cache.ini".format(Option.HiResDir + i + "/")):
                os.remove("{}cache.ini".format(Option.HiResDir + i + "/"))
            
            if os.path.isfile("{}Cache.ini".format(Option.HiResDir + i + "/")):
                os.remove("{}Cache.ini".format(Option.HiResDir + i + "/"))
        
        # Changing the textures
        ChangeTextureListTexturePack = ChangeTextureListAll
        if Option.EnableRAMMod == "1":
            ChangeTextureListRAM = []
            ChangeTextureListTexturePack = []
            if os.path.isfile("{}/other.ini".format(PathToTextures)) == True:
                if OtherTextures.ApplyEverything == "0":
                    TexturesRAM1 = [item.split(",") for item in ConfigOther.get("Other_TexturesRAM", OtherTextures.TexturesRAM).replace(" ", "").split(";")]
                    try:
                        OtherTextures.TexturesRAM = [[int(x, 16) for x in sublist[:2]] + sublist[2:] for sublist in TexturesRAM1]
                    except:
                        OtherTextures.TexturesRAM = []
                    
                    # Merge the two lists
                    OtherMerged = [[NewOtherTextures[i], OtherTextures.TexturesRAM[i]] if i < len(OtherTextures.TexturesRAM) else [NewOtherTextures[i]] for i in range(len(NewOtherTextures))]

                    # Check if all lists have two items
                    if all(len(sublist) == 3 for sublist in OtherMerged):
                        pass
                    else:
                        # Separate single-item lists
                        ChangeTextureListTexturePack = [sublist for sublist in OtherMerged if (len(sublist) == 3) or (len(sublist) == 1)]
                        ChangeTextureListRAM = [sublist for sublist in OtherMerged if len(sublist) == 2]
                    
                    if Option.RadioRAM == "0":
                        if all(len(sublist) == 3 for sublist in OtherMerged):
                            ChangeTextureListTexturePack = []
                        else:
                            pass
                    elif Option.RadioRAM == "1":
                        if not ChangeTextureListRAM:
                            pass
                        else:
                            ChangeTextureListTexturePack = []
                    else:
                        ChangeTextureListTexturePack = []
                elif (OtherTextures.ApplyEverything == "1") and (Option.RadioRAM == "2"):
                    ChangeTextureListTexturePack = []
            else:
                if self.Mode == "Eyes":
                    ChangeTextureListRAM = [[Option.Eyes1, [TextureAddresses.Seg04, TextureAddresses.ListEyes[0]]],
                                            [Option.Eyes2, [TextureAddresses.Seg04, TextureAddresses.ListEyes[1]]],
                                            [Option.Eyes3, [TextureAddresses.Seg04, TextureAddresses.ListEyes[2]]]]
                else:
                    ChangeTextureListRAM = [[Option.Cap, [TextureAddresses.Seg04, TextureAddresses.ListCHMB[0]]],
                                            [Option.Hair, [TextureAddresses.Seg04, TextureAddresses.ListCHMB[1]]],
                                            [Option.Mustache, [TextureAddresses.Seg04, TextureAddresses.ListCHMB[2]]],
                                            [Option.Button, [TextureAddresses.Seg04, TextureAddresses.ListCHMB[3]]]]
            
            if not ChangeTextureListRAM:
                pass
            else:
                try:
                    Utils.find_base_address()
                    for i, j in enumerate(ChangeTextureListRAM):
                        if 1 == 1:
                            img = Image.open("{}/{}.png".format(PathToTextures, Option.SM64Name + j[0])).convert("RGBA")
        
                            imgList = list(img.getdata())
                            
                            imgList5551 = []
                            
                            for k in imgList:
                                imgList5551.append(RAMFunctions.rgba8888_to_rgba5551(k))
                            
                            lines = []
                            rearranged_lines = []
                            for k in imgList5551:
                                lines.append(k)
                            for k in range(0, len(lines), 2):
                                if k + 1 < len(lines):
                                    rearranged_lines.append(lines[k + 1])
                                rearranged_lines.append(lines[k])
                                
                            for k, l in enumerate(rearranged_lines):
                                Utils.write_short(Utils.base_address + int(ChangeTextureListRAM[i][1][0]) + int(ChangeTextureListRAM[i][1][1]) + ((k * 2)), l)
                except:
                    pass
        
        if not ChangeTextureListTexturePack:
            pass
        else:
            for i in ChangeTextureListTexturePack:
                try:
                    if os.path.exists(Option.HiResDir + PasteName + "/") == False:
                        os.mkdir(Option.HiResDir + PasteName + "/")
                    shutil.copyfile("{}/{}.png".format(PathToTextures, Option.SM64Name + i[0]), "{}{}.png".format(Option.HiResDir + PasteName + "/" + PasteName, i[0]))
                except:
                    pass
                    
        #г8н8767658нн89ен897н89н89489п6рнругрнешнр4ащцрнгпгтнукшгпггшпнешщу34ееукеукеконщ9укерпшгкрукейц4е4ейуееукегщм8егенщ586о7ншп54некнеуеу4еопг45ноцгшн5487енг54нкецуукеукеенекее453е4е344е4е4е44е44е4це4еее —SUPERMARIOGAMER1

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
        self.SwitchItemsButton.setText(_translate("MainWindow", "Switch"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.submenuHiRes.setTitle(_translate("MainWindow", "Hi-res folders"))
        self.HiResClearSM64.setText(_translate("MainWindow", "Clear SM64"))
        self.HiResClearAdd.setText(_translate("MainWindow", "Clear Additional"))
        self.HiResOpenSM64.setText(_translate("MainWindow", "Open hi-res folder"))
        self.actionOpenKataraktaFolder.setText(_translate("MainWindow", "Open katarakta folder"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionStayOnTop.setText(_translate("MainWindow", "Stay on Top"))
        self.actionUpdate.setText(_translate("MainWindow", "Check for Updates"))
        self.actionRefresh.setText(_translate("MainWindow", "Refresh List"))
        self.actionDarkMode.setText(_translate("MainWindow", "Dark Mode"))
        self.submenuEyeBorders.setTitle(_translate("MainWindow", "Remove Texture Borders"))
        self.EyeBordersCurrent.setText(_translate("MainWindow", "Currently Selected"))
        self.EyeBordersAll.setText(_translate("MainWindow", "Every Texture"))
        self.actionFixBlackTextures.setText(_translate("MainWindow", "Fix Black Textures"))
        self.submenuEyeStates.setTitle(_translate("MainWindow", "Eye States"))
        self.submenuUtilities.setTitle(_translate("MainWindow", "Utilities"))
        self.actionStateFixBody.setText(_translate("MainWindow", "Fix Body State Reset"))
        self.actionStateEyes0.setText(_translate("MainWindow", "State 0"))
        self.actionStateEyes1.setText(_translate("MainWindow", "State 1"))
        self.actionStateEyes2.setText(_translate("MainWindow", "State 2"))
        self.actionStateEyes3.setText(_translate("MainWindow", "State 3"))
        self.actionStateEyes4.setText(_translate("MainWindow", "State 4"))
        self.actionStateEyes5.setText(_translate("MainWindow", "State 5"))
        self.actionStateEyes6.setText(_translate("MainWindow", "State 6"))
        self.actionStateEyes7.setText(_translate("MainWindow", "State 7"))
        self.actionStateEyes8.setText(_translate("MainWindow", "State 8"))
        self.actionDebugCrash.setText(_translate("MainWindow", "Debug Crash"))
        self.actionDebugCrashEffect.setText(_translate("MainWindow", "Debug Crash (with style)"))

    def retranslateUiOther(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "{} {} ({})".format(Language.MW_Title, AppVersion, AppEdition)))
        setTextList = [
                    [self.ApplySM64,                 Language.MW_ApplySM64],
                    [self.actionAbout,               Language.MW_actionAbout],
                    [self.SwitchItemsButton,         Language.MW_SwitchItemsButton],
                    [self.HiResClearSM64,            Language.MW_HiResClearSM64],
                    [self.HiResClearAdd,             Language.MW_HiResCleadAdd],
                    [self.HiResOpenSM64,             Language.MW_HiResOpenSM64],
                    [self.actionOpenKataraktaFolder, Language.MW_actionOpenKataraktaFolder],
                    [self.actionSettings,            Language.MW_actionSettings],
                    [self.actionStayOnTop,           Language.MW_actionStayOnTop],
                    [self.actionUpdate,              Language.MW_actionUpdate],
                    [self.actionRefresh,             Language.MW_Refresh],
                    [self.actionDarkMode,            Language.MW_actionDarkMode],
                    [self.EyeBordersCurrent,         Language.MW_EyeBordersCurrent],
                    [self.EyeBordersAll,             Language.MW_EyeBordersAll],
                    [self.actionFixBlackTextures,    Language.MW_actionFixBlackTextures],
                    [self.actionStateFixBody,        Language.MW_actionStateFixBody],
                    [self.actionStateEyes0,       f"{Language.MW_EyeState} 0"],
                    [self.actionStateEyes1,       f"{Language.MW_EyeState} 1"],
                    [self.actionStateEyes2,       f"{Language.MW_EyeState} 2"],
                    [self.actionStateEyes3,       f"{Language.MW_EyeState} 3"],
                    [self.actionStateEyes4,       f"{Language.MW_EyeState} 4"],
                    [self.actionStateEyes5,       f"{Language.MW_EyeState} 5"],
                    [self.actionStateEyes6,       f"{Language.MW_EyeState} 6"],
                    [self.actionStateEyes7,       f"{Language.MW_EyeState} 7"],
                    [self.actionStateEyes8,       f"{Language.MW_EyeState} 8"],
                    [self.actionDebugCrash,          Language.MW_actionDebugCrash],
                    [self.actionDebugCrashEffect,    Language.MW_actionDebugCrashEffect]
                    ]
        setTitleList = [
                    [self.groupBox,                  ""],
                    [self.menuHelp,                  Language.MW_menuHelp],
                    [self.menuOptions,               Language.MW_menuOptions],
                    [self.submenuHiRes,              Language.MW_submenuHiRes],
                    [self.submenuEyeBorders,         Language.MW_submenuEyeBorders],
                    [self.submenuEyeStates,          Language.MW_submenuEyeStates],
                    [self.submenuUtilities,          Language.MW_submenuUtilities]
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
    
    def DebugCrash(self):
        raise RuntimeError("Intentional crash / Преднамеренный вылет / Навмисний збій.")
    
    def DebugCrashEffect(self):
        self.labelExplode.setGeometry(QtCore.QRect(0, 0, MainWindow.width(), MainWindow.height()))
        self.labelExplode.show()
        
        self.movie = QtGui.QMovie("resources/img/CrashExplosion.gif")
        self.labelExplode.setMovie(self.movie)
        self.ThreadSound = threading.Thread(target = self.ExplodeSound, daemon = True)
        self.movie.start()
        self.movie.jumpToNextFrame()
        self.movie.jumpToNextFrame()
        self.movie.jumpToNextFrame()
        self.movie.jumpToNextFrame()
        self.movie.jumpToNextFrame()
        self.movie.jumpToNextFrame()
        self.movie.jumpToNextFrame()
        self.movie.jumpToNextFrame()
        self.ThreadSound.start()
        
        self.ThreadHide = threading.Thread(target = self.HideThingy, daemon = True)
        self.ThreadHide.start()
        
        QtCore.QTimer.singleShot(1200, self.DebugCrash)
    
    def HideThingy(self):
        timesleep(1.5)
        self.labelExplode.hide()
    
    def ExplodeSound(self):
        timesleep(0.1)
        playsound(os.getcwd() + "/resources/sound/DebugExplosion.mp3")

class Ui_AboutWindow(object):
    def setupUi(self, AboutWindow):

        AboutWindow.setObjectName("About katarakta")
        AboutWindow.setFixedSize(520, 421)
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
        self.LineLegalNotice.setGeometry(QtCore.QRect(20, 350, 481, 3))
        self.LineLegalNotice.setFrameShape(QtWidgets.QFrame.HLine)
        self.LineLegalNotice.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.LabelLegalNotice = QtWidgets.QLabel(AboutWindow)
        self.LabelLegalNotice.setGeometry(QtCore.QRect(20, 368, 481, 30))
        self.LabelLegalNotice.setObjectName("LabelLegalNotice")
        self.LabelLegalNotice.setAlignment(Qt.AlignCenter)
        self.LabelLegalNotice.setStyleSheet("font-size: 11px")
        
        AboutWindow.setWindowFlags(AboutWindow.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint & ~QtCore.Qt.WindowMinimizeButtonHint )
        
        AboutWindow.setWindowIcon(QtGui.QIcon(kataraktaIcon))
        
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
        self.LabelAuthor.setText(_translate("AboutWindow", "By DanilAstroid (<a href = 'https://www.youtube.com/channel/UCCrO_HQsasKN7Zwlp3D8UWQ'>YouTube</a>, <a href = 'https://github.com/vazhka-dolya/'>GitHub</a>).<br><br>Thanks to the following people for testing katarakta:<br>• Blender_Blenderovych (<a href = 'https://www.youtube.com/channel/UCGxro_VNeDQBY9k8_jitMCw'>YouTube 1</a>, <a href = 'https://www.youtube.com/channel/UCBkB7pjgU1cjKvjg_OzjzIg'>YouTube 2</a>)<br>• SDRM45 (<a href = 'https://www.youtube.com/channel/UC-3gc0FmQA2_Z2-MIS5sZNQ'>YouTube</a>)<br><br>Thanks to the following people for help:<br>• GlitchyPSI (<a href = 'https://www.youtube.com/channel/UCnUer0eafhVWqjX-T4TMNiw'>YouTube</a>, <a href = 'https://github.com/GlitchyPSIX'>GitHub</a>)"))
        self.LabelAddInfo.setText(_translate("AboutWindow", "This project uses the GNU General Public License v3.0<br><br><a href = 'https://github.com/vazhka-dolya/katarakta/issues/'>Report issues</a>"))
        self.LabelLegalNotice.setText(_translate("AboutWindow", "This program is not affiliated with or sponsored by Nintendo and does not claim ownership over\nany of Nintendo's intellectual property used (such as the characters in the loading screens)."))

    def retranslateUiOther(self, AboutWindow):
        _translate = QtCore.QCoreApplication.translate
        AboutWindow.setWindowTitle(_translate("AboutWindow", Language.AW_Title))
        self.LabelName.setText(_translate("AboutWindow", Language.AW_LabelName))
        self.LabelVersion.setText(_translate("AboutWindow", f"{Language.AW_LabelVersion} {AppVersion}\n{Language.AW_LabelEdition} {AppEdition}"))
        self.LabelAuthor.setText(_translate("AboutWindow", f"{Language.AW_LabelAuthor} DanilAstroid (<a href = 'https://www.youtube.com/channel/UCCrO_HQsasKN7Zwlp3D8UWQ'>YouTube</a>, <a href = 'https://github.com/vazhka-dolya/'>GitHub</a>).<br><br>{Language.AW_SpecialThanks}<br>• Blender_Blenderovych (<a href = 'https://www.youtube.com/channel/UCGxro_VNeDQBY9k8_jitMCw'>YouTube 1</a>, <a href = 'https://www.youtube.com/channel/UCBkB7pjgU1cjKvjg_OzjzIg'>YouTube 2</a>)<br>• SDRM45 (<a href = 'https://www.youtube.com/channel/UC-3gc0FmQA2_Z2-MIS5sZNQ'>YouTube</a>)<br><br>{Language.AW_SpecialThanksHelp}<br>• GlitchyPSI (<a href = 'https://www.youtube.com/channel/UCnUer0eafhVWqjX-T4TMNiw'>YouTube</a>, <a href = 'https://github.com/GlitchyPSIX'>GitHub</a>)"))
        self.LabelAddInfo.setText(_translate("AboutWindow", f"{Language.AW_LabelAddInfo}<br><br><a href = 'https://github.com/vazhka-dolya/katarakta/issues/'>{Language.AW_LabelReportIssue}</a>"))
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
            UpdateWindow.setWindowIcon(QtGui.QIcon("resources/img/UpdaterIcon.png"))
        except:
            pass

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
        self.labelLanguageRestart.hide()
        
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
        self.CheckEnableDebugOptions = QtWidgets.QCheckBox(self.groupMisc)
        self.CheckEnableDebugOptions.setGeometry(QtCore.QRect(10, 83, 501, 17))
        self.CheckEnableDebugOptions.setObjectName("CheckEnableDebugOptions")

        if IsTestVersion is False:
            if Option.StartUpCheckForUpdates == "1":
                if IsTestVersion is False:
                    self.checkUpdates.setChecked(True)
        else:
            self.groupUpdates.setEnabled(False)

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
        
        if Option.EnableDebugOptions == "1":
            self.CheckEnableDebugOptions.setChecked(True)
        
        def CheckEnableDebugOptions():
            global _EnableDebugOptions
            if self.CheckEnableDebugOptions.isChecked() == True:
                _EnableDebugOptions = "1"
            else:
                _EnableDebugOptions = "0"
            return _EnableDebugOptions
        
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
        self.BG_ButtonConfigure.setGeometry(self.BG_ButtonDefault.x(), self.BG_ButtonDefault.y() + 52, 100, 23)
        self.BG_ButtonConfigure.clicked.connect(lambda: BG_Configure())

        self.BG_ButtonReset = QtWidgets.QPushButton(self.groupEyeBG)
        self.BG_ButtonReset.setObjectName("BG_ButtonReset")
        self.BG_ButtonReset.setGeometry(self.BG_ButtonDefault.x() + 104, self.BG_ButtonDefault.y() + 52, 100, 23)
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

        self.CheckMirrorUI = QtWidgets.QCheckBox(self.groupEyeBG)
        self.CheckMirrorUI.setGeometry(QtCore.QRect(224, 100, 501, 17))
        self.CheckMirrorUI.setObjectName("CheckMirrorUI")
        
        def CheckMirrorUI():
            global _CheckMirrorUI
            if self.CheckMirrorUI.isChecked() == True:
                _CheckMirrorUI = "1"
            else:
                _CheckMirrorUI = "0"
            return _CheckMirrorUI
        
        if Option.CheckMirrorUI == "1":
            self.CheckMirrorUI.setChecked(True)

        self.CheckMirrorMenubar = QtWidgets.QCheckBox(self.groupEyeBG)
        self.CheckMirrorMenubar.setGeometry(QtCore.QRect(224, 120, 501, 17))
        self.CheckMirrorMenubar.setObjectName("CheckMirrorMenubar")
        
        def CheckMirrorMenubar():
            global _CheckMirrorMenubar
            if self.CheckMirrorMenubar.isChecked() == True:
                _CheckMirrorMenubar = "1"
            else:
                _CheckMirrorMenubar = "0"
            return _CheckMirrorMenubar
        
        if Option.CheckMirrorMenubar == "1":
            self.CheckMirrorMenubar.setChecked(True)
        
        self.RadioFilteringNone = QtWidgets.QRadioButton(self.groupEyeBG)
        self.RadioFilteringNone.setGeometry(QtCore.QRect(224, 20, 481, 17))
        self.RadioFilteringNone.setObjectName("RadioFilteringNone")
        
        self.RadioFilteringBilinear = QtWidgets.QRadioButton(self.groupEyeBG)
        self.RadioFilteringBilinear.setGeometry(QtCore.QRect(224, 40, 481, 17))
        self.RadioFilteringBilinear.setObjectName("RadioFilteringBilinear")
        
        self.RadioFilteringN64 = QtWidgets.QRadioButton(self.groupEyeBG)
        self.RadioFilteringN64.setGeometry(QtCore.QRect(224, 60, 481, 17))
        self.RadioFilteringN64.setObjectName("RadioFilteringN64")

        def RadioFiltering():
            global _RadioFiltering
            if self.RadioFilteringNone.isChecked() == True:
                _RadioFiltering = "0"
            elif self.RadioFilteringBilinear.isChecked() == True:
                _RadioFiltering = "1"
            elif self.RadioFilteringN64.isChecked() == True:
                _RadioFiltering = "2"
            else:
                _RadioFiltering = "0"
        
        if Option.RadioFiltering == "0":
            self.RadioFilteringNone.setChecked(True)
        elif Option.RadioFiltering == "1":
            self.RadioFilteringBilinear.setChecked(True)
        elif Option.RadioFiltering == "2":
            self.RadioFilteringN64.setChecked(True)
        else:
            self.RadioFilteringBilinear.setChecked(True)
        
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
        self.SpinEyeListRowHeight.setGeometry(QtCore.QRect(10, 113, 50, 20))
        self.SpinEyeListRowHeight.setObjectName("SpinEyeListRowHeight")
        self.SpinEyeListRowHeight.setMinimum(-9)
        self.SpinEyeListRowHeight.setMaximum(999)
        self.SpinEyeListRowHeight.textChanged.connect(self.DemoSetRowHeight)
        
        self.LabelRowHeight = QtWidgets.QLabel(self.groupEyeList)
        self.LabelRowHeight.setObjectName("LabelRowHeight")
        self.LabelRowHeight.setGeometry(QtCore.QRect(65, 113, 208, 20))
        
        self.DemoSetIcons
        
        self.LabelEyeListWarning = QtWidgets.QLabel(self.groupEyeList)
        self.LabelEyeListWarning.setObjectName("LabelEyeListWarning")
        self.LabelEyeListWarning.setGeometry(QtCore.QRect(10, 60, 288, 49))

        # Uncomment these if you need to see the boundaries of the labels:
        #self.LabelRowHeight.setStyleSheet("background-color:#7F7F7F")
        #self.LabelEyeListWarning.setStyleSheet("background-color:#7F7F7F")
        
        self.LabelEyeListDemo = QtWidgets.QLabel(self.groupEyeList)
        self.LabelEyeListDemo.setObjectName("LabelEyeListDemo")
        self.LabelEyeListDemo.setGeometry(QtCore.QRect(308, 10, 288, 25))
        
        self.EyeListDemo = QtWidgets.QTreeWidget(self.groupEyeList)
        self.EyeListDemo.setGeometry(QtCore.QRect(308, 40, 188, 118))
        for i in range(1, self.EyeListDemo.model().columnCount()):
            self.EyeListDemo.header().hideSection(i)
        self.EyeListDemo.header().setStretchLastSection(False)
        self.EyeListDemo.header().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
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

        self.CheckMirrorEyeList = QtWidgets.QCheckBox(self.groupEyeList)
        self.CheckMirrorEyeList.setGeometry(QtCore.QRect(10, 138, 501, 17))
        self.CheckMirrorEyeList.setObjectName("CheckMirrorEyeList")
        self.CheckMirrorEyeList.stateChanged.connect(self.DemoSetIcons)
        
        def CheckMirrorEyeList():
            global _CheckMirrorEyeList
            if self.CheckMirrorEyeList.isChecked() == True:
                _CheckMirrorEyeList = "1"
            else:
                _CheckMirrorEyeList = "0"
            return _CheckMirrorEyeList
        
        if Option.CheckMirrorEyeList == "1":
            self.CheckMirrorEyeList.setChecked(True)
        
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
        
        self.TabRAM = QtWidgets.QWidget()
        self.TabRAM.setObjectName("RAM Modifications")
        
        self.groupRAMReplace = QtWidgets.QGroupBox(self.TabRAM)
        self.groupRAMReplace.setGeometry(QtCore.QRect(10, 0, 506, 106))
        self.groupRAMReplace.setObjectName("groupRAMReplace")
        
        self.CheckEnableRAMMod = QtWidgets.QCheckBox(self.groupRAMReplace)
        self.CheckEnableRAMMod.setGeometry(QtCore.QRect(10, 20, 501, 17))
        self.CheckEnableRAMMod.setObjectName("CheckEnableRAMMod")
        
        self.RadioRAMIfCannotReplace = QtWidgets.QRadioButton(self.groupRAMReplace)
        self.RadioRAMIfCannotReplace.setGeometry(QtCore.QRect(30, 40, 481, 17))
        self.RadioRAMIfCannotReplace.setObjectName("RadioRAMIfCannotReplace")
        
        self.RadioRAMIfNone = QtWidgets.QRadioButton(self.groupRAMReplace)
        self.RadioRAMIfNone.setGeometry(QtCore.QRect(30, 60, 481, 17))
        self.RadioRAMIfNone.setObjectName("RadioRAMIfNone")
        
        self.RadioRAMOnly = QtWidgets.QRadioButton(self.groupRAMReplace)
        self.RadioRAMOnly.setGeometry(QtCore.QRect(30, 80, 481, 17))
        self.RadioRAMOnly.setObjectName("RadioRAMOnly")
        
        self.groupRAMUtilities = QtWidgets.QGroupBox(self.TabRAM)
        self.groupRAMUtilities.setGeometry(QtCore.QRect(10, 105, 506, 66))
        self.groupRAMUtilities.setObjectName("groupRAMUtilities")
        
        self.CheckEnableRAMUtilities = QtWidgets.QCheckBox(self.groupRAMUtilities)
        self.CheckEnableRAMUtilities.setGeometry(QtCore.QRect(10, 20, 501, 17))
        self.CheckEnableRAMUtilities.setObjectName("CheckEnableRAMUtilities")
        
        self.CheckAutoFixBody = QtWidgets.QCheckBox(self.groupRAMUtilities)
        self.CheckAutoFixBody.setGeometry(QtCore.QRect(10, 40, 501, 17))
        self.CheckAutoFixBody.setObjectName("CheckAutoFixBody")
        
        def CheckEnableRAMMod():
            global _EnableRAMMod
            if self.CheckEnableRAMMod.isChecked() == True:
                _EnableRAMMod = "1"
            else:
                _EnableRAMMod = "0"
            return _EnableRAMMod
        
        if Option.EnableRAMMod == "1":
            self.CheckEnableRAMMod.setChecked(True)
        
        def CheckEnableRAMUtilities():
            global _EnableRAMUtilities
            if self.CheckEnableRAMUtilities.isChecked() == True:
                _EnableRAMUtilities = "1"
            else:
                _EnableRAMUtilities = "0"
            return _EnableRAMUtilities
        
        if Option.EnableRAMUtilities == "1":
            self.CheckEnableRAMUtilities.setChecked(True)
        
        def CheckAutoFixBody():
            global _AutoFixBody
            if self.CheckAutoFixBody.isChecked() == True:
                _AutoFixBody = "1"
            else:
                _AutoFixBody = "0"
            return _AutoFixBody
        
        if Option.AutoFixBody == "1":
            self.CheckAutoFixBody.setChecked(True)
        
        def RadioRAM():
            global _RadioRAM
            if self.RadioRAMIfCannotReplace.isChecked() == True:
                _RadioRAM = "0"
            elif self.RadioRAMIfNone.isChecked() == True:
                _RadioRAM = "1"
            elif self.RadioRAMOnly.isChecked() == True:
                _RadioRAM = "2"
            else:
                _RadioRAM = "0"
        
        if Option.RadioRAM == "0":
            self.RadioRAMIfCannotReplace.setChecked(True)
        elif Option.RadioRAM == "1":
            self.RadioRAMIfNone.setChecked(True)
        elif Option.RadioRAM == "2":
            self.RadioRAMOnly.setChecked(True)
        else:
            self.RadioRAMIfCannotReplace.setChecked(True)
        
        self.tabWidget.addTab(self.TabRAM, "")

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
            RadioFiltering()
            CheckEnableRAMMod()
            CheckAutoFixBody()
            RadioRAM()
            CheckEnableRAMUtilities()
            CheckEnableDebugOptions()
            CheckMirrorUI()
            CheckMirrorMenubar()
            CheckMirrorEyeList()
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
            Config.set("OPTIONS", "EnableRAMMod", _EnableRAMMod)
            Config.set("OPTIONS", "AutoFixBody", _AutoFixBody)
            Config.set("OPTIONS", "RadioRAM", _RadioRAM)
            Config.set("OPTIONS", "EnableRAMUtilities", _EnableRAMUtilities)
            Config.set("OPTIONS", "EnableDebugOptions", _EnableDebugOptions)
            Config.set("OPTIONS", "RadioFiltering", _RadioFiltering)
            Config.set("OPTIONS", "CheckMirrorUI", _CheckMirrorUI)
            Config.set("OPTIONS", "CheckMirrorMenubar", _CheckMirrorMenubar)
            Config.set("OPTIONS", "CheckMirrorEyeList", _CheckMirrorEyeList)
            
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

            LoadLanguage()
            self.retranslateUiEnglish(SettingsWindow)
            if Language.Properties_InnerName != "English":
                self.retranslateUiOther(SettingsWindow)
            CheckLanguage()
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
    
    def DemoSetIcons(self):
        DemoPixmapSet = ["resources/img/Demo/DemoAngry.png", "resources/img/Demo/DemoAngryLeft.png", "resources/img/Demo/DemoAngryRight.png", "resources/img/Demo/DemoDerp.png", "resources/img/Demo/DemoHappy.png", "resources/img/Demo/DemoSad.png", "resources/img/Demo/DemoSurprisedScared.png", "resources/img/Demo/DemoSurprisedScaredLeft.png", "resources/img/Demo/DemoSurprisedScaredRight.png"]
        if self.CheckMirrorEyeList.isChecked():
            self.EyeListDemo.setLayoutDirection(Qt.RightToLeft)
        else:
            self.EyeListDemo.setLayoutDirection(Qt.LeftToRight)
        
        if self.CheckEyeListIcons.isChecked():
            if self.CheckEyeListIconBG.isChecked():
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
        self.BG_Label.setText(_translate("SettingsWindow", "Texture display's background:"))
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TabRAM), _translate("TabRAM", "RAM Modifications"))
        self.CheckEnableRAMMod.setText("Replacing textures in RAM (EXPERIMENTAL, currently supports RGBA16 only)")
        self.CheckAutoFixBody.setText("Automatically fix body state when using the Eye States utility")
        self.groupRAMReplace.setTitle("Replacing textures in RAM")
        self.RadioRAMIfCannotReplace.setText("Use texture pack textures for any textures that can't be replaced in RAM")
        self.RadioRAMIfNone.setText("Use texture pack textures only if no textures can be replaced in RAM")
        self.RadioRAMOnly.setText("Don't use texture pack textures at all")
        self.groupRAMUtilities.setTitle("RAM Utilities")
        self.CheckEnableRAMUtilities.setText("Enable RAM Utilities")
        self.CheckEnableDebugOptions.setText("Enable debug options")
        self.RadioFilteringNone.setText("No filtering")
        self.RadioFilteringBilinear.setText("Bilinear filtering (common on emulators)")
        self.RadioFilteringN64.setText("3-point filtering (used by Nintendo 64)")
        self.CheckMirrorUI.setText("Mirror the main window's UI")
        self.CheckMirrorMenubar.setText("Mirror the main window's menu bar")
        self.CheckMirrorEyeList.setText("Mirror the texture list")

    def retranslateUiOther(self, SettingsWindow):
        _translate = QtCore.QCoreApplication.translate
        SettingsWindow.setWindowTitle(_translate("SettingsWindow", Language.SW_Title))
        setTextList = [
                    [self.labelLanguageRestart,           Language.SW_labelLanguageRestart],
                    [self.checkUpdates,                   Language.SW_checkUpdates],
                    [self.labelUpdates,                   Language.SW_labelUpdates],
                    [self.checkStayOnTop,                 Language.SW_checkStayOnTop],
                    [self.labelHiResSM64,                 Language.SW_labelHiResSM64],
                    [self.labelEyesOpen,                  Language.SW_labelEyesOpen],
                    [self.labelEyesHalfopen,              Language.SW_labelEyesHalfopen],
                    [self.labelEyesClosed,                Language.SW_labelEyesClosed],
                    [self.labelCap,                       Language.SW_labelCap],
                    [self.labelSidehair,                  Language.SW_labelSidehair],
                    [self.labelMustache,                  Language.SW_labelMustache],
                    [self.labelButton,                    Language.SW_labelButton],
                    [self.labelSM64Name,                  Language.SW_labelSM64Name],
                    [self.labelAddNames,                  Language.SW_labelAddNames],
                    [self.pushClose,                      Language.SW_pushClose],
                    [self.pushApply,                      Language.SW_pushApply],
                    [self.pushApplyClose,                 Language.SW_pushApplyClose],
                    [self.CheckDoNotMoveSwitchVertically, Language.SW_CheckDoNotMoveSwitchVertically],
                    [self.CheckEyeBordersWarning,         Language.SW_CheckEyeBordersWarning],
                    [self.BG_ButtonConfigure,             Language.SW_BG_ButtonConfigure],
                    [self.BG_ButtonReset,                 Language.SW_BG_ButtonReset],
                    [self.BG_Label,                       Language.SW_BG_Label],
                    [self.CheckTextureBorder,             Language.SW_CheckTextureBorder],
                    [self.CheckEyeListIcons,              Language.SW_CheckEyeListIcons],
                    [self.CheckEyeListIconBG,             Language.SW_CheckEyeListIconBG],
                    [self.LabelEyeListWarning,            Language.SW_LabelEyeListWarning],
                    [self.LabelEyeListDemo,               Language.SW_LabelEyeListDemo],
                    [self.LabelRowHeight,                 Language.SW_LabelRowHeight],
                    [self.CheckEnableRAMMod,              Language.SW_CheckEnableRAMMod],
                    [self.CheckAutoFixBody,               Language.SW_CheckAutoFixBody],
                    [self.RadioRAMIfCannotReplace,        Language.SW_RadioRAMIfCannotReplace],
                    [self.RadioRAMIfNone,                 Language.SW_RadioRAMIfNone],
                    [self.RadioRAMOnly,                   Language.SW_RadioRAMOnly],
                    [self.CheckEnableRAMUtilities,        Language.SW_CheckEnableRAMUtilities],
                    [self.CheckEnableDebugOptions,        Language.SW_CheckEnableDebugOptions],
                    [self.RadioFilteringNone,             Language.SW_RadioFilteringNone],
                    [self.RadioFilteringBilinear,         Language.SW_RadioFilteringBilinear],
                    [self.RadioFilteringN64,              Language.SW_RadioFilteringN64],
                    [self.CheckMirrorUI,                  Language.SW_CheckMirrorUI],
                    [self.CheckMirrorMenubar,             Language.SW_CheckMirrorMenubar],
                    [self.CheckMirrorEyeList,             Language.SW_CheckMirrorEyeList]
                    ]
        setTitleList = [
                    [self.groupLanguage,     Language.SW_groupLanguage],
                    [self.groupUpdates,      Language.SW_groupUpdates],
                    [self.groupMisc,         Language.SW_groupMisc],
                    [self.groupSM64,         Language.SW_groupSM64],
                    [self.groupNames,        Language.SW_groupNames],
                    [self.groupEyeBG,        Language.SW_groupEyeBG],
                    [self.groupEyeList,      Language.SW_groupEyeList],
                    [self.groupRAMReplace,   Language.SW_groupRAMReplace],
                    [self.groupRAMUtilities, Language.SW_groupRAMUtilities]
                    ]
        setTabTextList = [
                    [self.tabWidget, Language.SW_TabGeneral,    self.TabGeneral],
                    [self.tabWidget, Language.SW_TabTextures,   self.TabTextures],
                    [self.tabWidget, Language.SW_TabAppearance, self.TabAppearance],
                    [self.tabWidget, Language.SW_TabRAM,        self.TabRAM]
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

class TextureAddresses:
    Seg04 =    0x7EC20
    
    ListEyes = [0x3090, 0x3890, 0x4090]
    ListCHMB = [0x1890, 0x2090, 0x2890, 0x1090]

class RAMFunctions:
    def pushEyesFunc(MainWindow, value):
        Utils.find_base_address()
        
        if Option.AutoFixBody == "1":
            RAMFunctions.pushFixBodyFunc(MainWindow)
        
        RAMFunctions.setEyesState(value)
    
    def pushFixBodyFunc(MainWindow):
        Utils.find_base_address()
        
        RAMFunctions.fixResetBodyState()

    def fixResetBodyState():
        # Prevents Mario from getting his body state reset every damn frame
        Utils.write_uint(sys.modules["__main__"].Utils.base_address + 0x254338, 0x27BDFFF8)
        Utils.write_uint(sys.modules["__main__"].Utils.base_address + 0x254338 + 4, 0x8C8E0098)
        Utils.write_uint(sys.modules["__main__"].Utils.base_address + 0x254338 + 8, 0xAFAE0004)
        Utils.write_uint(sys.modules["__main__"].Utils.base_address + 0x254338 + 12, 0x00000000)
        Utils.write_uint(sys.modules["__main__"].Utils.base_address + 0x254338 + 16, 0x00000000)
        Utils.write_uint(sys.modules["__main__"].Utils.base_address + 0x254338 + 20, 0x00000000)
        Utils.write_uint(sys.modules["__main__"].Utils.base_address + 0x254338 + 24, 0x00000000)
        Utils.write_uint(sys.modules["__main__"].Utils.base_address + 0x254338 + 28, 0x00000000)
        Utils.write_uint(sys.modules["__main__"].Utils.base_address + 0x254338 + 32, 0x00000000)
        Utils.write_uint(sys.modules["__main__"].Utils.base_address + 0x254338 + 36, 0x00000000)
        Utils.write_uint(sys.modules["__main__"].Utils.base_address + 0x254338 + 40, 0x8FAF0004)
        Utils.write_uint(sys.modules["__main__"].Utils.base_address + 0x254338 + 44, 0xA5E00008)
        Utils.write_uint(sys.modules["__main__"].Utils.base_address + 0x254338 + 48, 0x8FB80004)
        Utils.write_uint(sys.modules["__main__"].Utils.base_address + 0x254338 + 52, 0xA3000007)
        Utils.write_uint(sys.modules["__main__"].Utils.base_address + 0x254338 + 56, 0x8C990004)
        Utils.write_uint(sys.modules["__main__"].Utils.base_address + 0x254338 + 60, 0x2401FFBF)
        Utils.write_uint(sys.modules["__main__"].Utils.base_address + 0x254338 + 64, 0x03216024)
        Utils.write_uint(sys.modules["__main__"].Utils.base_address + 0x254338 + 68, 0xAC884004)
        Utils.write_uint(sys.modules["__main__"].Utils.base_address + 0x254338 + 72, 0x10000001)
        Utils.write_uint(sys.modules["__main__"].Utils.base_address + 0x254338 + 76, 0x00000000)
        Utils.write_uint(sys.modules["__main__"].Utils.base_address + 0x254338 + 80, 0x03E00008)
        Utils.write_uint(sys.modules["__main__"].Utils.base_address + 0x254338 + 84, 0x27BD0008)
    
    def setEyesState(value):
        data = int(value).to_bytes(1, byteorder = "little", signed = True)
        Utils.write_bytes(sys.modules["__main__"].Utils.base_address + 0x33B3B6, data)
    
    def rgba8888_to_rgba5551(rgba8888):
        r, g, b, a = rgba8888
        r5 = (r >> 3) & 0x1F
        g5 = (g >> 3) & 0x1F
        b5 = (b >> 3) & 0x1F
        a1 = (a >> 7) & 0x01
        return (r5 << 11) | (g5 << 6) | (b5 << 1) | a1

    def rgba5551_to_rgba8888(rgba5551):
        r5 = (rgba5551 >> 11) & 0x1F
        g5 = (rgba5551 >> 6) & 0x1F
        b5 = (rgba5551 >> 1) & 0x1F
        a1 = rgba5551 & 0x01
        r = (r5 << 3) | (r5 >> 2)
        g = (g5 << 3) | (g5 >> 2)
        b = (b5 << 3) | (b5 >> 2)
        a = 255 if a1 else 0
        return (r, g, b, a)

class Updatable:
    def __init__(self):
        pass
    
    def update(self):
        pass
    
    def reset(self):
        pass

class Utils:
    module_list: List[Updatable] = []
    base_address: int = 0
    is_emu_open = False
    emu_process = None
    emu_process_handle = None
    PROCESS_ALL_ACCESS = 0x01F0FF
    
    @staticmethod
    def find_emu_process():
        import psutil
        for proc in psutil.process_iter(["pid", "name"]):
            if "project64" in proc.info["name"].lower():
                Utils.emu_process = proc
                Utils.emu_process_handle = ctypes.windll.kernel32.OpenProcess(Utils.PROCESS_ALL_ACCESS, False, proc.info["pid"])
                Utils.is_emu_open = True
                break
    
    def ensure_emu_process():
        if not Utils.emu_process_handle:
            Utils.find_emu_process()
    
    @staticmethod
    def find_base_address():
        Utils.ensure_emu_process()
        
        value = 0
        start = 0x20000000
        stop = 0xF0000000
        step = 0x10000
        
        if Utils.base_address > 0:
            buffer = (ctypes.c_char * 4)()
            bytes_read = ctypes.c_size_t()
            success = ctypes.windll.kernel32.ReadProcessMemory(Utils.emu_process_handle, Utils.base_address, buffer, 4, ctypes.byref(bytes_read))
            if success and bytes_read.value == 4:
                value = int.from_bytes(buffer, byteorder = "little")
                if value == 0x3C1A8032:
                    return
            else:
                Utils.find_emu_process
        
        for scan_address in range(start, stop, step):
            buffer = (ctypes.c_char * 4)()
            bytes_read = ctypes.c_size_t()
            success = ctypes.windll.kernel32.ReadProcessMemory(Utils.emu_process_handle, scan_address, buffer, 4, ctypes.byref(bytes_read))
            if success and bytes_read.value == 4:
                value = int.from_bytes(buffer, byteorder = "little")
                if value == 0x3C1A8032:
                    Utils.base_address = scan_address
                    return
            else:
                continue
        
        Utils.base_address = 0
    
    @staticmethod
    def wait_for_next_frame():
        vi_number = Utils.read_short(Utils.base_address + 0x32D580)
        while Utils.read_short(Utils.base_address + 0x32D580) == vi_number:
            time.sleep(0.001) # Unsure if this will work properly
    
    @staticmethod
    def read_bytes(address, size):
        buffer = (ctypes.c_char * size)()
        bytes_read = ctypes.c_size_t()
        ctypes.windll.kernel32.ReadProcessMemory(Utils.emu_process_handle, address, buffer, size, ctypes.byref(bytes_read))
        return bytes(buffer[:bytes_read.value])
    
    @staticmethod
    def read_short(address):
        buffer = Utils.read_bytes(address, 2)
        return int.from_bytes(buffer, byteorder = "little")

    @staticmethod
    def read_uint(address):
        buffer = Utils.read_bytes(address, 4)
        return int.from_bytes(buffer, byteorder="little")

    @staticmethod
    def read_ulong(address):
        buffer = Utils.read_bytes(address, 8)
        return int.from_bytes(buffer, byteorder="little")

    @staticmethod
    def write_bytes(address, data):
        data_bytes = bytes(data)
        bytes_written = ctypes.c_size_t()
        ctypes.windll.kernel32.WriteProcessMemory(Utils.emu_process_handle, address, data_bytes, len(data_bytes), ctypes.byref(bytes_written))

    @staticmethod
    def write_batch_bytes(addresses, data, use_base):
        data = Utils.swap_endian(data, 4)
        base_addr = Utils.base_address if use_base else 0
        for addr in addresses:
            address = base_addr + int(addr, 16)
            Utils.write_bytes(address, data)

    @staticmethod
    def write_short(address, data):
        data_bytes = data.to_bytes(2, byteorder="little")
        Utils.write_bytes(address, data_bytes)

    @staticmethod
    def write_uint(address, data):
        data_bytes = data.to_bytes(4, byteorder="little")
        Utils.write_bytes(address, data_bytes)

    @staticmethod
    def write_ulong(address, data):
        data_bytes = data.to_bytes(8, byteorder="little")
        Utils.write_bytes(address, data_bytes)

    @staticmethod
    def swap_endian(array, word_size):
        result = bytearray()
        for i in range(0, len(array), word_size):
            word = array[i:i+word_size]
            result.extend(word[::-1])
        return bytes(result)

    @staticmethod
    def get_key(vkey):
        import win32api
        return win32api.GetAsyncKeyState(vkey) != 0
    
if __name__ == "__main__":
    global app
    sys.excepthook = HandleException
    
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
    
    try:
        MainWindow = Ui_MainWindow() #QtWidgets.QMainWindow()
        MainWindow.setupUi(MainWindow)
        #ui = Ui_MainWindow()
        #ui.setupUi(MainWindow)
        MainWindow.show()
    except:
        HandleException("", traceback.format_exc(), "")
    
    try:
        Splash.finish(MainWindow)
    except:
        pass
    
    sys.exit(app.exec_())
