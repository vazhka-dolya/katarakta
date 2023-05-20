#GPL-3.0-only

import os
import configparser
import shutil
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget
import sys

class Options():
    SM64Dir = ""
    AddDir = ""
    Eyes1 = ""
    Eyes2 = ""
    Eyes3 = ""
    AddEyes1 = ""
    AddEyes2 = ""
    AddEyes3 = ""
    Language = ""

AppVersion = "1.0.0"

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
        
    if "OPTIONS" in Config:
        ConfigSecond = Config["OPTIONS"]
        Option.Language = ConfigSecond.get("Language", Option.Language)

LoadConfig()

# Find Folders in eyes\
EyeFolders = os.listdir("eyes\\")
FolderName = ""

class Ui_MainWindow(object):
    def OpenAboutWindow(self):
        self.AboutWindow = QtWidgets.QMainWindow()
        self.AboutWindowUi = Ui_AboutWindow()
        self.AboutWindowUi.setupUi(self.AboutWindow)
        self.AboutWindow.show()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(518, 563)
        MainWindow.setFixedSize(MainWindow.size())
        #MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.World))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        try:
            MainWindow.setWindowIcon(QtGui.QIcon("img\\256icon.png"))
        except:
            pass
        
        CopyEyesErrorBoxTitle = ""
        CopyEyesErrorBoxMessage = ""

        #Found eye folders label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 101, 16))
        self.label.setObjectName("label")

        #Eyes list
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 30, 201, 481))
        self.listWidget.setObjectName("listWidget")

        self.listWidget.addItems(EyeFolders)

        self.listWidget.itemClicked.connect(lambda: self.OnSelectionChanged(self.listWidget.currentItem().text()))

        #Displaying eye textures
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(240, 10, 120, 351))
        self.groupBox.setObjectName("groupBox")
        self.SM64DisplayLabel1 = QtWidgets.QLabel(self.groupBox)
        self.SM64DisplayLabel1.setEnabled(True)
        self.SM64DisplayLabel1.setGeometry(QtCore.QRect(10, 20, 101, 101))
        self.SM64DisplayLabel1.setText("")
        self.SM64DisplayLabel1.setPixmap(QtGui.QPixmap("img\\PlaceHolderEye1.png"))
        self.SM64DisplayLabel1.setScaledContents(True)
        self.SM64DisplayLabel1.setObjectName("SM64DisplayLabel1")
        self.SM64DisplayLabel2 = QtWidgets.QLabel(self.groupBox)
        self.SM64DisplayLabel2.setGeometry(QtCore.QRect(10, 130, 101, 101))
        self.SM64DisplayLabel2.setText("")
        self.SM64DisplayLabel2.setPixmap(QtGui.QPixmap("img\\PlaceHolderEye2.png"))
        self.SM64DisplayLabel2.setScaledContents(True)
        self.SM64DisplayLabel2.setObjectName("SM64DisplayLabel2")
        self.SM64DisplayLabel3 = QtWidgets.QLabel(self.groupBox)
        self.SM64DisplayLabel3.setGeometry(QtCore.QRect(10, 240, 101, 101))
        self.SM64DisplayLabel3.setText("")
        self.SM64DisplayLabel3.setPixmap(QtGui.QPixmap("img\\PlaceHolderEye3.png"))
        self.SM64DisplayLabel3.setScaledContents(True)
        self.SM64DisplayLabel3.setObjectName("SM64DisplayLabel3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(380, 10, 120, 351))
        self.groupBox_2.setObjectName("groupBox_2")
        self.AddDisplayLabel1 = QtWidgets.QLabel(self.groupBox_2)
        self.AddDisplayLabel1.setGeometry(QtCore.QRect(10, 20, 101, 101))
        self.AddDisplayLabel1.setText("")
        self.AddDisplayLabel1.setPixmap(QtGui.QPixmap("img\\PlaceHolderEye1.png"))
        self.AddDisplayLabel1.setScaledContents(True)
        self.AddDisplayLabel1.setObjectName("AddDisplayLabel1")
        self.AddDisplayLabel2 = QtWidgets.QLabel(self.groupBox_2)
        self.AddDisplayLabel2.setGeometry(QtCore.QRect(10, 130, 101, 101))
        self.AddDisplayLabel2.setText("")
        self.AddDisplayLabel2.setPixmap(QtGui.QPixmap("img\\PlaceHolderEye2.png"))
        self.AddDisplayLabel2.setScaledContents(True)
        self.AddDisplayLabel2.setObjectName("AddDisplayLabel2")
        self.AddDisplayLabel3 = QtWidgets.QLabel(self.groupBox_2)
        self.AddDisplayLabel3.setGeometry(QtCore.QRect(10, 240, 101, 101))
        self.AddDisplayLabel3.setText("")
        self.AddDisplayLabel3.setPixmap(QtGui.QPixmap("img\\PlaceHolderEye3.png"))
        self.AddDisplayLabel3.setScaledContents(True)
        self.AddDisplayLabel3.setObjectName("AddDisplayLabel3")

        MainWindow.setCentralWidget(self.centralwidget)

        #Apply buttons
        self.ApplySM64 = QtWidgets.QPushButton(self.centralwidget)
        self.ApplySM64.setGeometry(QtCore.QRect(240, 371, 71, 23))
        self.ApplySM64.setObjectName("ApplySM64")
        self.ApplySM64.clicked.connect(lambda: self.CopyEyes("SM64Dir", self.listWidget.currentItem().text()))
        
        self.ApplyAdd = QtWidgets.QPushButton(self.centralwidget)
        self.ApplyAdd.setGeometry(QtCore.QRect(380, 371, 91, 23))
        self.ApplyAdd.setObjectName("ApplyAdd")
        self.ApplyAdd.clicked.connect(lambda: self.CopyEyes("AddDir", self.listWidget.currentItem().text()))

        #Refresh eye list button
        self.Refresh = QtWidgets.QPushButton(self.centralwidget)
        self.Refresh.setGeometry(QtCore.QRect(240, 489, 71, 23))
        self.Refresh.setObjectName("RefreshButton")
        self.Refresh.clicked.connect(lambda: self.RefreshEyeList())

        #Menu bar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 518, 21))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        #self.menuLanguage = QtWidgets.QMenu(self.menuOptions)
        #self.menuLanguage.setObjectName("menuLanguage")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        #self.actionEnglish = QtWidgets.QAction(MainWindow)
        #self.actionEnglish.setObjectName("actionEnglish")
        #self.menuLanguage.addAction(self.actionEnglish)
        #self.actionUkrainian = QtWidgets.QAction(MainWindow)
        #self.actionUkrainian.setObjectName("actionUkrainian")
        #self.menuLanguage.addAction(self.actionUkrainian)
        #self.actionRussian = QtWidgets.QAction(MainWindow)
        #self.actionRussian.setObjectName("actionRussian")
        #self.menuLanguage.addAction(self.actionRussian)
        self.menuHelp.addAction(self.actionAbout)
        #self.menuOptions.addAction(self.menuLanguage.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.actionAbout.triggered.connect(self.OpenAboutWindow)

        if Option.Language == "English":
            self.retranslateUiEnglish(MainWindow)
            self.Update()

        elif Option.Language == "Ukrainian":
            self.retranslateUiUkrainian(MainWindow)
            self.Update()
        
        elif Option.Language == "Russian":
            self.retranslateUiRussian(MainWindow)
            self.Update()
        
        else:
            self.retranslateUiEnglish(MainWindow)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def Update(self):
        self.label.adjustSize()
        self.ApplySM64.adjustSize()
        self.ApplyAdd.adjustSize()
        #self.groupBox.adjustSize()
        #self.groupBox_2.adjustSize()
        self.menuHelp.adjustSize()
        #self.menuLanguage.adjustSize()
        self.Refresh.adjustSize()

    def RefreshEyeList(self):
        EyeFolders = os.listdir("eyes\\")
        self.listWidget.clear()
        self.listWidget.addItems(EyeFolders)

    def OnSelectionChanged(self, FolderName):
        if os.path.exists("eyes\\{}\\{}.png".format(FolderName, Option.Eyes1)):
            self.SM64DisplayLabel1.setPixmap(QtGui.QPixmap("eyes\\{}\\{}.png".format(FolderName, Option.Eyes1)))
        else:
            self.SM64DisplayLabel1.setPixmap(QtGui.QPixmap("img\\PlaceHolderEye1.png"))
            
        if os.path.exists("eyes\\{}\\{}.png".format(FolderName, Option.Eyes2)):
            self.SM64DisplayLabel2.setPixmap(QtGui.QPixmap("eyes\\{}\\{}.png".format(FolderName, Option.Eyes2)))
        else:
            self.SM64DisplayLabel2.setPixmap(QtGui.QPixmap("img\\PlaceHolderEye2.png"))
            
        if os.path.exists("eyes\\{}\\{}.png".format(FolderName, Option.Eyes3)):
            self.SM64DisplayLabel3.setPixmap(QtGui.QPixmap("eyes\\{}\\{}.png".format(FolderName, Option.Eyes3)))
        else:
            self.SM64DisplayLabel3.setPixmap(QtGui.QPixmap("img\\PlaceHolderEye3.png"))
            
        if os.path.exists("eyes\\{}\\{}.png".format(FolderName, Option.AddEyes1)):
            self.AddDisplayLabel1.setPixmap(QtGui.QPixmap("eyes\\{}\\{}.png".format(FolderName, Option.AddEyes1)))
        else:
            self.AddDisplayLabel1.setPixmap(QtGui.QPixmap("img\\PlaceHolderEye1.png"))
            
        if os.path.exists("eyes\\{}\\{}.png".format(FolderName, Option.AddEyes2)):
            self.AddDisplayLabel2.setPixmap(QtGui.QPixmap("eyes\\{}\\{}.png".format(FolderName, Option.AddEyes2)))
        else:
            self.AddDisplayLabel2.setPixmap(QtGui.QPixmap("img\\PlaceHolderEye2.png"))
            
        if os.path.exists("eyes\\{}\\{}.png".format(FolderName, Option.AddEyes3)):
            self.AddDisplayLabel3.setPixmap(QtGui.QPixmap("eyes\\{}\\{}.png".format(FolderName, Option.AddEyes3)))
        else:
            self.AddDisplayLabel3.setPixmap(QtGui.QPixmap("img\\PlaceHolderEye3.png"))

    def CopyEyes(self, Type, FolderName):
        if Type == "SM64Dir":
            Path = Option.SM64Dir
            try:
                shutil.copyfile("eyes\\{}\\{}.png".format(FolderName, Option.Eyes1), "{}{}.png".format(Path, Option.Eyes1))
                shutil.copyfile("eyes\\{}\\{}.png".format(FolderName, Option.Eyes2), "{}{}.png".format(Path, Option.Eyes2))
                shutil.copyfile("eyes\\{}\\{}.png".format(FolderName, Option.Eyes3), "{}{}.png".format(Path, Option.Eyes3))
            except:
                ShowCopyEyesErrorBox = CopyEyesErrorBox.exec_()
        if Type == "AddDir":
            Path = Option.AddDir
            try:
                shutil.copyfile("eyes\\{}\\{}.png".format(FolderName, Option.AddEyes1), "{}{}.png".format(Path, Option.AddEyes1))
                shutil.copyfile("eyes\\{}\\{}.png".format(FolderName, Option.AddEyes2), "{}{}.png".format(Path, Option.AddEyes2))
                shutil.copyfile("eyes\\{}\\{}.png".format(FolderName, Option.AddEyes3), "{}{}.png".format(Path, Option.AddEyes3))
            except:
                ShowCopyEyesErrorBox = CopyEyesErrorBox.exec_()

    def retranslateUiEnglish(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "katarakta {}".format(AppVersion)))
        self.label.setText(_translate("MainWindow", "Found eye folders"))
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
        self.Refresh.setText(_translate("MainWindow", "Refresh"))

    def retranslateUiUkrainian(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "katarakta {}".format(AppVersion)))
        self.label.setText(_translate("MainWindow", "Знайдені папки з очами:"))
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
        self.Refresh.setText(_translate("MainWindow", "Оновити"))

    def retranslateUiRussian(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "katarakta {}".format(AppVersion)))
        self.label.setText(_translate("MainWindow", "Найденные папки с глазами"))
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
        self.ApplyAdd.setGeometry(QtCore.QRect(350, 371, 91, 23))
        self.Refresh.setText(_translate("MainWindow", "Обновить"))

class Ui_AboutWindow(object):
    def setupUi(self, AboutWindow):
        AboutWindow.setObjectName("About katarakta")
        AboutWindow.resize(520, 256)
        AboutWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.World))
        self.LabelName = QtWidgets.QLabel(AboutWindow)
        self.LabelName.setGeometry(QtCore.QRect(240, 80, 271, 71))
        self.LabelName.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setItalic(False)
        self.LabelName.setFont(font)
        self.LabelName.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.World))
        self.LabelName.setScaledContents(False)
        self.LabelName.setObjectName("LabelName")
        self.LabelVersion = QtWidgets.QLabel(AboutWindow)
        self.LabelVersion.setGeometry(QtCore.QRect(240, 150, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.LabelVersion.setFont(font)
        self.LabelVersion.setObjectName("LabelVersion")
        self.LabelAuthor = QtWidgets.QLabel(AboutWindow)
        self.LabelAuthor.setGeometry(QtCore.QRect(20, 230, 481, 16))
        self.LabelAuthor.setObjectName("LabelAuthor")
        self.LabelIcon = QtWidgets.QLabel(AboutWindow)
        self.LabelIcon.setGeometry(QtCore.QRect(20, 20, 201, 201))
        self.LabelIcon.setText("")
        self.LabelIcon.setPixmap(QtGui.QPixmap("img\\768icon.png"))
        self.LabelIcon.setScaledContents(True)
        self.LabelIcon.setObjectName("LabelIcon")
        AboutWindow.setFixedSize(AboutWindow.size())
        
        try:
            AboutWindow.setWindowIcon(QtGui.QIcon("img\\256icon.png"))
        except:
            pass

        if Option.Language == "English":
            self.retranslateUiEnglish(AboutWindow)
            self.Update()

        elif Option.Language == "Ukrainian":
            self.retranslateUiUkrainian(AboutWindow)
            self.Update()
        
        elif Option.Language == "Russian":
            self.retranslateUiRussian(AboutWindow)
            self.Update()
        
        else:
            self.retranslateUiEnglish(MainWindow)
        
        QtCore.QMetaObject.connectSlotsByName(AboutWindow)
        
    def Update(self):
        self.LabelName.adjustSize()
        self.LabelVersion.adjustSize()
        self.LabelAuthor.adjustSize()
    
    def retranslateUiEnglish(self, AboutWindow):
        _translate = QtCore.QCoreApplication.translate
        AboutWindow.setWindowTitle(_translate("AboutWindow", "About katarakta"))
        self.LabelName.setText(_translate("AboutWindow", "katarakta"))
        self.LabelVersion.setText(_translate("AboutWindow", "Version: {}".format(AppVersion)))
        self.LabelAuthor.setText(_translate("AboutWindow", "By DanilAstroid (https://github.com/vazhka-dolya/)"))
    
    def retranslateUiUkrainian(self, AboutWindow):
        _translate = QtCore.QCoreApplication.translate
        AboutWindow.setWindowTitle(_translate("AboutWindow", "Про katarakta"))
        self.LabelName.setText(_translate("AboutWindow", "katarakta"))
        self.LabelVersion.setText(_translate("AboutWindow", "Версія: {}".format(AppVersion)))
        self.LabelAuthor.setText(_translate("AboutWindow", "Від DanilAstroid (https://github.com/vazhka-dolya/)"))
    
    def retranslateUiRussian(self, AboutWindow):
        _translate = QtCore.QCoreApplication.translate
        AboutWindow.setWindowTitle(_translate("AboutWindow", "О katarakta"))
        self.LabelName.setText(_translate("AboutWindow", "katarakta"))
        self.LabelVersion.setText(_translate("AboutWindow", "Версия: {}".format(AppVersion)))
        self.LabelAuthor.setText(_translate("AboutWindow", "От DanilAstroid (https://github.com/vazhka-dolya/)"))

if Option.Language == "English":
    CopyEyesErrorBoxTitle = "Error"
    CopyEyesErrorBoxMessage = "An error occured!\nMake sure that:\n- You entered the correct path in config.txt\n- You entered the correct eye texture name in config.txt\n- You have the eye textures in the folder"

elif Option.Language == "Ukrainian":
    CopyEyesErrorBoxTitle = "Помилка"
    CopyEyesErrorBoxMessage = "Сталая помилка!\nПереконайтеся, що:\n- Ви ввели існуючий шлях до hi-res текстур у config.txt\n- Ви ввели правильні назви текстур очей у config.txt\n- У самій папці є текстури очей"

elif Option.Language == "Russian":
    CopyEyesErrorBoxTitle = "Ошибка"
    CopyEyesErrorBoxMessage = "Произошла ошибка!\nУбедитесь, что:\n- Вы ввели существующий путь к hi-res текстурам в config.txt\n- Вы ввели правильные названия текстур глаз в config.txt\n- У вас есть сами текстуры глаз в папке"

else:
    CopyEyesErrorBoxTitle = "Error"
    CopyEyesErrorBoxMessage = "An error occured!\nMake sure that:\n- You entered the correct path in config.txt\n- You entered the correct eye texture name in config.txt\n- You have the eye textures in the folder"

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
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
    sys.exit(app.exec_())

#print("Welcome to katarakta!\nType help to view all commands and what they do.\nMake sure to also check config.txt if you didn't already, there is some vital stuff.")
#while True:
#    Command = input("> ")
#    if Command == "help":
#        print("Commands:\nhelp - Displays this message.\ncopys - Copies the eye textures from the eyes folder to your SM64 folder.\ncopya - Copies the eye textures from the eyes folder to your additional folder.\nquit - Quit katarakta.\n")
#    elif Command == "copys":
#        FolderName = input("Folder name: ")
#        CopyEyes("SM64Dir", FolderName)
#    elif Command == "copya":
#        FolderName = input("Folder name: ")
#        CopyEyes("AddDir", Foldername)
#    elif Command == "quit":
#        quit()
#    else:
#        print("Command not found!")
