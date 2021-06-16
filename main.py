import sys, os
from PyQt5 import QtCore, QtGui, QtWidgets
import keyboard
from time import sleep
import threading
import random
import string

print(" ______     ______     __         ______     ______        ______     ______   ______     __    __     __    __     ______     ______    ")
print('/\  ___\   /\  __ \   /\ \       /\  __ \   /\  == \      /\  ___\   /\  == \ /\  __ \   /\ "-./  \   /\ "-./  \   /\  ___\   /\  == \   ')
print('\ \___  \  \ \ \/\ \  \ \ \____  \ \  __ \  \ \  __<      \ \___  \  \ \  _-/ \ \  __ \  \ \ \-./\ \  \ \ \-./\ \  \ \  __\   \ \  __<   ')
print(' \/\_____\  \ \_____\  \ \_____\  \ \_\ \_\  \ \_\ \_\     \/\_____\  \ \_\    \ \_\ \_\  \ \_\ \ \_\  \ \_\ \ \_\  \ \_____\  \ \_\ \_\ ')
print('  \/_____/   \/_____/   \/_____/   \/_/\/_/   \/_/ /_/      \/_____/   \/_/     \/_/\/_/   \/_/  \/_/   \/_/  \/_/   \/_____/   \/_/ /_/ ')
print(' ')

class Ui_Spammer(object):

    def getFile(self):
        self.getFileDialog = QtWidgets.QFileDialog.getOpenFileName(self.centralwidget)
        try:
            global filePath
            filePath = str(self.getFileDialog).split("'")
            fpd = filePath[1].split("/", 3)
            global filePathDisplay
            filePathDisplay = fpd[3]
        except:
            return
        self.fileButton.setText(f"Select script file\n{filePathDisplay}")

    def main_prog(self):
        try:
            if filePathDisplay:
                print("WARNING: \n IF YOU WANT TO EXIT EARLY, CLOSE THE TERMINAL WINDOW AND NOT THE GUI")
                file = open(filePath[1], "r")
                ac = str(file.read())
                split_up_script = []
                split_up_script = ac.splitlines()
                splsc = split_up_script
                wait_time = self.timeBetweenMessages.value()
                chunkyBoiCount = self.chunkCount.value()
                n_elem = len(split_up_script)
                time_remaining = n_elem * wait_time + n_elem//chunkyBoiCount * wait_time*1.5
                old_time = time_remaining
                sleep(5)
                i = 0
                ln = 0
                for split_up_script in split_up_script:
                    ln += 1
                    keyboard.write(splsc[i])
                    sleep(0.001)
                    keyboard.press_and_release("shift+enter")
                    i += 1
                    time_remaining = n_elem * wait_time - i * wait_time + n_elem//chunkyBoiCount * wait_time*1.5
                    time_remaining_minutes = int(time_remaining)//60
                    time_percent = round(time_remaining/old_time * 100)
                    print(f"{i}/{n_elem}")
                    self.percentRemaining.setProperty("value", time_percent)
                    self.minutesRemainingDisplay.setProperty("value", time_remaining_minutes)
                    self.progressBar.setProperty("value", time_percent)
                    if chunkyBoiCount == ln:
                        print("----------")
                        keyboard.press_and_release("enter")
                        ln = 0
                        sleep(wait_time*1.5)
                    sleep(wait_time)
        except:
            self.startButton.setText("Please select a script file!")
            sleep(1.5)
            self.startButton.setText("Start!")

    def main_prog_rand(self):
        content = self.startingString.text()
        times = self.spamAmount.value()
        waitTime = self.timeBetween.value()
        randomTime = self.randomizeTime.checkState()
        STR_GEN = string.ascii_uppercase + string.digits + string.punctuation
        d = 0
        sleep(5)
        for i in range(times):
            keyboard.write(content + "{ " + ''.join(random.choice(STR_GEN) for _ in range(self.suffixLength.value())) + '}')
            sleep(0.001)
            keyboard.press_and_release("enter")
            if randomTime == 0:
                sleep(waitTime)
            else:
                sleepyTime = round(random.uniform(0.5, 2), 2)
                sleep(sleepyTime)
            d += 1
            print(f"{d}/{times}")
            timeLeft = times * waitTime - d * waitTime
            self.minutesLeft.setProperty("value", round(timeLeft/60))

    def start_thread(self):
        threading.Thread(target=self.main_prog).start()
    
    def start_rand_thread(self):
        threading.Thread(target=self.main_prog_rand).start()
    
    def setupUi(self, Spammer):
        Spammer.setObjectName("Spammer")
        Spammer.resize(480, 200)
        Spammer.setMinimumSize(QtCore.QSize(480, 200))
        Spammer.setMaximumSize(QtCore.QSize(480, 200))
        Spammer.setMouseTracking(False)
        
        self.centralwidget = QtWidgets.QWidget(Spammer)
        self.centralwidget.setObjectName("centralwidget")

# ----------------------------FIRST TAB-------------------------------- #

        # Tabs
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 491, 201))
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName(u"Script Spammer")

        # Progress bar
        self.progressBar = QtWidgets.QProgressBar(self.tab)
        self.progressBar.setGeometry(QtCore.QRect(10, 39+24, 461, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setProperty("textVisible", False)
        self.progressBar.setObjectName("progressBar")

        # Minutes remaining display
        self.minutesRemainingDisplay = QtWidgets.QLCDNumber(self.tab)
        self.minutesRemainingDisplay.setGeometry(QtCore.QRect(10, 9, 64, 23))
        self.minutesRemainingDisplay.setObjectName("minutesRemainingDisplay")

        # Label
        self.minutesRemainingLabel = QtWidgets.QLabel(self.tab)
        self.minutesRemainingLabel.setGeometry(QtCore.QRect(80, 10, 160, 20))
        self.minutesRemainingLabel.setObjectName("minutesRemainingLabel")

        # Percent remaining display
        self.percentRemaining = QtWidgets.QLCDNumber(self.tab)
        self.percentRemaining.setGeometry(QtCore.QRect(10, 34, 64, 23))
        self.percentRemaining.setObjectName("percentRemaining")

        # Label
        self.percentRemainingLabel = QtWidgets.QLabel(self.tab)
        self.percentRemainingLabel.setGeometry(QtCore.QRect(80, 35, 160, 20))
        self.percentRemainingLabel.setObjectName("percentRemainingLabel")

        # Time between messages county thing
        self.timeBetweenMessages = QtWidgets.QDoubleSpinBox(self.tab)
        self.timeBetweenMessages.setGeometry(QtCore.QRect(410, 10, 62, 22))
        self.timeBetweenMessages.setObjectName("timeBetweenMessages")
        self.timeBetweenMessages.setProperty("singleStep", 0.1)
        self.timeBetweenMessages.setProperty("value", 0.4)
        self.timeBetweenMessages.setProperty("decimals", 1)

        # Label
        self.timeBetweenMessagesLabel = QtWidgets.QLabel(self.tab)
        self.timeBetweenMessagesLabel.setGeometry(QtCore.QRect(290, 10, 131, 20))
        self.timeBetweenMessagesLabel.setObjectName("timeBetweenMessagesLabel")

        # Chunky boi count
        self.chunkCount = QtWidgets.QSpinBox(self.tab)
        self.chunkCount.setGeometry(QtCore.QRect(410, 35, 62, 22))
        self.chunkCount.setObjectName("chunkCount")
        self.chunkCount.setProperty("sigleStep", 1)
        self.chunkCount.setProperty("value", 5)
        self.chunkCount.setProperty("minimum", 3)
        self.chunkCount.setProperty("maximum", 15)
        self.chunkCount.setProperty("decimals", 0)

        # Label
        self.chunkCountLabel = QtWidgets.QLabel(self.tab)
        self.chunkCountLabel.setGeometry(QtCore.QRect(316, 35, 131, 20))
        self.timeBetweenMessagesLabel.setObjectName("chunkCountLabel")

        # Start button
        self.startButton = QtWidgets.QPushButton(self.tab)
        self.startButton.setGeometry(QtCore.QRect(10, 69+24, 461, 41))
        self.startButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.startButton.setObjectName("startButton")
        self.startButton.clicked.connect(self.start_thread)

        # File Button
        self.fileButton = QtWidgets.QPushButton(self.tab)
        self.fileButton.setGeometry(QtCore.QRect(10, 110+24, 461, 41))
        self.fileButton.setObjectName("fileButton")
        self.fileButton.clicked.connect(self.getFile)

# -----------------------------SECOND TAB------------------------------------ #

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName(u"Unique spammer")
        self.tabWidget.addTab(self.tab_2, "")
        
        # Input for the starter string to build off of
        self.startingString = QtWidgets.QLineEdit(self.tab_2)
        self.startingString.setGeometry(QtCore.QRect(250, 20, 221, 20))
        self.startingString.setObjectName("startingString")
        
        # Label for above feature
        self.startingStringLabel = QtWidgets.QLabel(self.tab_2)
        self.startingStringLabel.setGeometry(QtCore.QRect(175, 20, 71, 16))
        self.startingStringLabel.setObjectName("startingStringLabel")
        
        # How many times to spam
        self.spamAmount = QtWidgets.QSpinBox(self.tab_2)
        self.spamAmount.setGeometry(QtCore.QRect(371, 50, 101, 22))
        self.spamAmount.setMaximum(7000)
        self.spamAmount.setSingleStep(10)
        self.spamAmount.setProperty("value", 100)
        self.spamAmount.setObjectName("spamAmount")
        
        # Label for above feature
        self.spamTimesLabel = QtWidgets.QLabel(self.tab_2)
        self.spamTimesLabel.setGeometry(QtCore.QRect(300, 50, 71, 20))
        self.spamTimesLabel.setObjectName("spamTimesLabel")
        
        # Minutes left display
        self.minutesLeft = QtWidgets.QLCDNumber(self.tab_2)
        self.minutesLeft.setGeometry(QtCore.QRect(0, 80, 64, 23))
        self.minutesLeft.setObjectName("lcdNumber")
        
        # Label for above feature
        self.minutesLeftLabel = QtWidgets.QLabel(self.tab_2)
        self.minutesLeftLabel.setGeometry(QtCore.QRect(70, 81, 61, 20))
        self.minutesLeftLabel.setObjectName("label")
        
        # Select the time between messages, aka spam rate
        self.timeBetween = QtWidgets.QDoubleSpinBox(self.tab_2)
        self.timeBetween.setObjectName(u"timeBetweenMessages")
        self.timeBetween.setGeometry(QtCore.QRect(410, 80, 62, 22))
        self.timeBetween.setProperty("singleStep", 0.1)
        self.timeBetween.setProperty("decimals", 1)
        self.timeBetween.setProperty("minimum", 0.1)
        self.timeBetween.setProperty("value", 1.0)
        
        # Label for above feature
        self.TBMLabel = QtWidgets.QLabel(self.tab_2)
        self.TBMLabel.setObjectName(u"TBMLabel")
        self.TBMLabel.setGeometry(QtCore.QRect(290, 80, 121, 20))
        
        # Changes the length of the randomized suffix
        self.suffixLength = QtWidgets.QSpinBox(self.tab_2)
        self.suffixLength.setObjectName(u"suffixLength")
        self.suffixLength.setGeometry(QtCore.QRect(0, 50, 42, 22))
        self.suffixLength.setMinimum(4)
        self.suffixLength.setMaximum(100)
        self.suffixLength.setValue(16)
        
        # Label for above feature
        self.suffixLengthLabel = QtWidgets.QLabel(self.tab_2)
        self.suffixLengthLabel.setObjectName(u"suffixLengthLabel")
        self.suffixLengthLabel.setGeometry(QtCore.QRect(50, 50, 81, 20))
        
        # Thing to slightly modify the time between each message
        self.randomizeTime = QtWidgets.QCheckBox(self.tab_2)
        self.randomizeTime.setObjectName(u"randomizeTime")
        self.randomizeTime.setGeometry(QtCore.QRect(0, 20, 101, 21))
        
        # Start button
        self.startSemiButton = QtWidgets.QPushButton(self.tab_2)
        self.startSemiButton.setGeometry(QtCore.QRect(0, 106, 477, 70))
        self.startSemiButton.setObjectName("pushButton")
        self.startSemiButton.clicked.connect(self.start_rand_thread)
        
# --------------------------------------------------------------------------- #

        Spammer.setCentralWidget(self.centralwidget)

        self.retranslateUi(Spammer)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Spammer)

    def retranslateUi(self, Spammer):
        _translate = QtCore.QCoreApplication.translate
        Spammer.setWindowTitle(_translate("Spammer", "Solar Spammer"))
        
        self.startButton.setToolTip(_translate("Spammer", "Spamming will start after a 5 second delay"))
        self.progressBar.setToolTip(_translate("Spammer", "Shows progress of spammer, kinda inverted but whatever"))
        self.startButton.setText(_translate("Spammer", "Start!"))
        self.timeBetweenMessagesLabel.setText(_translate("Spammer", "Time between messages"))
        self.minutesRemainingLabel.setText(_translate("Spammer", "Minutes remaining (approximate)"))
        self.fileButton.setText(_translate("Spammer", "Select script file"))
        self.chunkCountLabel.setText(_translate("Spammer", "Message block size"))
        self.percentRemainingLabel.setText(_translate("Spammer", "Percent remaining (approximate)"))
        
        self.startSemiButton.setText(QtCore.QCoreApplication.translate("Spammer", u"Start!", None))
        self.minutesLeftLabel.setText(QtCore.QCoreApplication.translate("Spammer", u"Minutes left", None))
        self.spamTimesLabel.setText(QtCore.QCoreApplication.translate("Spammer", u"Times to spam", None))
        self.startingStringLabel.setText(QtCore.QCoreApplication.translate("Spammer", u"Starting String", None))
        self.TBMLabel.setText(QtCore.QCoreApplication.translate("Spammer", u"Time between messages" ))
        self.suffixLengthLabel.setText(QtCore.QCoreApplication.translate("Spammer", u"Length of suffix" ))
        self.randomizeTime.setText(QtCore.QCoreApplication.translate("Spammer", u"Randomize time", None))
        
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtCore.QCoreApplication.translate("Spammer", u"From Script", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtCore.QCoreApplication.translate("Spammer", u"Semi-randomized", None))
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Spammer = QtWidgets.QMainWindow()
    ui = Ui_Spammer()
    ui.setupUi(Spammer)
    Spammer.show()
    sys.exit(app.exec_())
