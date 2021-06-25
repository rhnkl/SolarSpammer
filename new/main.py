from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QApplication, QGraphicsOpacityEffect, QStackedWidget
from PyQt5.QtCore import QPropertyAnimation, QSequentialAnimationGroup, QPoint, QEasingCurve

class welcomeScreen(QDialog):
    def __init__(self):
        super(welcomeScreen, self).__init__()
        loadUi("resources/welcome.ui", self)
        self.uiScriptBasedSpammer.clicked.connect(self.gotoscript)
        self.uiUniqueSpammer.clicked.connect(self.gotounique)
        self.aboutButton.clicked.connect(self.gotoabout)
        
        self.animation = QPropertyAnimation(self.welcomeLabel, b"pos")
        self.animation.setDuration(1400)
        self.animation.setEndValue(QPoint(50, 30))
        self.animation.setEasingCurve(QEasingCurve.OutCubic)
        
        self.solaranim = QPropertyAnimation(self.solarLabel, b"pos")
        self.solaranim.setDuration(1400)
        self.solaranim.setEndValue(QPoint(50, 30))
        self.solaranim.setEasingCurve(QEasingCurve.OutCubic)
        
        self.animgroup = QSequentialAnimationGroup()
        self.animgroup.addAnimation(self.animation)
        self.animgroup.addAnimation(self.solaranim)
        self.animgroup.start()
        
    def gotoscript(self):
        scriptBasedScreen = scripted()
        widget.addWidget(scriptBasedScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setWindowTitle("{solar} - Script spammer")
        
    def gotounique(self):
        unique = uniqueSpammer()
        widget.addWidget(unique)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setWindowTitle("{solar} - Unique spammer")
        
    def gotoabout(self):
        abt = aboutUs()
        widget.addWidget(abt)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setWindowTitle("{solar} - About")

        
class scripted(QDialog):
    def __init__(self):
        super(scripted, self).__init__()
        loadUi("resources/scriptBased.ui", self)
        self.backButton.clicked.connect(self.gotowelcome)
        self.scriptFile.clicked.connect(self.getFile)
        
        self.animation = QPropertyAnimation(self.scriptbasedLabel, b"pos")
        self.animation.setDuration(2000)
        self.animation.setEndValue(QPoint(0, 30))
        self.animation.setEasingCurve(QEasingCurve.OutCubic)
        self.animation.start()
        
    def gotowelcome(self):
        welcome = welcomeScreen()
        widget.addWidget(welcome)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setWindowTitle("{solar} - Welcome")
        
        
    def getFile(self):
        self.getFileDialog = QtWidgets.QFileDialog.getOpenFileName()
        try:
            filePathPre = str(self.getFileDialog).split("'")[1]
            if filePathPre == "":
                print("No file selected")
            else:
                global filePath
                filePath = filePathPre
                print(filePath)
        except: return
        
class uniqueSpammer(QDialog):
    def __init__(self):
        super(uniqueSpammer, self).__init__()
        loadUi("resources/unique.ui", self)
        self.uniqueBack.clicked.connect(self.gotwelcome)
        
        self.animation = QPropertyAnimation(self.uniqueLabel, b"pos")
        self.animation.setDuration(2000)
        self.animation.setEndValue(QPoint(0, 30))
        self.animation.setEasingCurve(QEasingCurve.OutCubic)
        self.animation.start()
        
    def gotwelcome(self):
        welcome = welcomeScreen()
        widget.addWidget(welcome)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setWindowTitle("{solar} - Welcome")
        
class aboutUs(QDialog):
    def __init__(self):
        super(aboutUs, self).__init__()
        loadUi("resources/about.ui", self)
        self.abtBack.clicked.connect(self.gootowelcome)
        
        self.animation = QPropertyAnimation(self.aboutLabel, b"pos")
        self.animation.setDuration(1400)
        self.animation.setEndValue(QPoint(-10, 30))
        self.animation.setEasingCurve(QEasingCurve.OutCubic)
        
        self.solaranim = QPropertyAnimation(self.solarLabel, b"pos")
        self.solaranim.setDuration(1400)
        self.solaranim.setEndValue(QPoint(20, 30))
        self.solaranim.setEasingCurve(QEasingCurve.OutCubic)
        
        self.body = QPropertyAnimation(self.about, b"pos")
        self.body.setDuration(2500)
        self.body.setEndValue(QPoint(200, 150))
        self.body.setEasingCurve(QEasingCurve.OutCirc)
        
        self.animgroup = QSequentialAnimationGroup()
        self.animgroup.addAnimation(self.animation)
        self.animgroup.addAnimation(self.solaranim)
        self.animgroup.addAnimation(self.body)
        self.animgroup.start()
        
    def gootowelcome(self):
        welcome = welcomeScreen()
        widget.addWidget(welcome)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setWindowTitle("{solar} - Welcome")

     
import sys
from ctypes import windll
myappid = 'trident.solar.solar.1.0.0'
windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
app = QApplication(sys.argv)
welcome = welcomeScreen()
widget = QStackedWidget()
widget.addWidget(welcome)
widget.setFixedWidth(1151)
widget.setFixedHeight(650)
widget.setWindowTitle("{solar} - Welcome")
widget.setWindowIcon(QIcon("assets/icon.png"))
widget.show()
try: sys.exit(app.exec_())
except: pass