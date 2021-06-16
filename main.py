import sys, os
from PyQt5 import QtCore, QtGui, QtWidgets
import keyboard
from time import sleep
import threading

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

    def start_thread(self):
        threading.Thread(target=self.main_prog).start()
    
    def setupUi(self, Spammer):
        Spammer.setObjectName("Spammer")
        Spammer.resize(480, 184)
        Spammer.setMinimumSize(QtCore.QSize(480, 184)) # +24!
        Spammer.setMaximumSize(QtCore.QSize(480, 184))
        Spammer.setMouseTracking(False)
        
        self.centralwidget = QtWidgets.QWidget(Spammer)
        self.centralwidget.setObjectName("centralwidget")

        # Progress bar
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 39+24, 461, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setProperty("textVisible", False)
        self.progressBar.setObjectName("progressBar")

        # Minutes remaining display
        self.minutesRemainingDisplay = QtWidgets.QLCDNumber(self.centralwidget)
        self.minutesRemainingDisplay.setGeometry(QtCore.QRect(10, 9, 64, 23))
        self.minutesRemainingDisplay.setObjectName("minutesRemainingDisplay")

        # Label
        self.minutesRemainingLabel = QtWidgets.QLabel(self.centralwidget)
        self.minutesRemainingLabel.setGeometry(QtCore.QRect(80, 10, 160, 20))
        self.minutesRemainingLabel.setObjectName("minutesRemainingLabel")

        # Percent remaining display
        self.percentRemaining = QtWidgets.QLCDNumber(self.centralwidget)
        self.percentRemaining.setGeometry(QtCore.QRect(10, 34, 64, 23))
        self.percentRemaining.setObjectName("percentRemaining")

        # Label
        self.percentRemainingLabel = QtWidgets.QLabel(self.centralwidget)
        self.percentRemainingLabel.setGeometry(QtCore.QRect(80, 35, 160, 20))
        self.percentRemainingLabel.setObjectName("percentRemainingLabel")

        # Time between messages county thing
        self.timeBetweenMessages = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.timeBetweenMessages.setGeometry(QtCore.QRect(410, 10, 62, 22))
        self.timeBetweenMessages.setObjectName("timeBetweenMessages")
        self.timeBetweenMessages.setProperty("singleStep", 0.1)
        self.timeBetweenMessages.setProperty("value", 0.4)

        # Label
        self.timeBetweenMessagesLabel = QtWidgets.QLabel(self.centralwidget)
        self.timeBetweenMessagesLabel.setGeometry(QtCore.QRect(290, 10, 131, 20))
        self.timeBetweenMessagesLabel.setObjectName("timeBetweenMessagesLabel")

        # Chunky boi count
        self.chunkCount = QtWidgets.QSpinBox(self.centralwidget)
        self.chunkCount.setGeometry(QtCore.QRect(410, 35, 62, 22))
        self.chunkCount.setObjectName("chunkCount")
        self.chunkCount.setProperty("sigleStep", 1)
        self.chunkCount.setProperty("value", 5)
        self.chunkCount.setProperty("minimum", 3)
        self.chunkCount.setProperty("maximum", 15)

        # Label
        self.chunkCountLabel = QtWidgets.QLabel(self.centralwidget)
        self.chunkCountLabel.setGeometry(QtCore.QRect(316, 35, 131, 20))
        self.timeBetweenMessagesLabel.setObjectName("chunkCountLabel")

        # Start button
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(10, 69+24, 461, 41))
        self.startButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.startButton.setObjectName("startButton")
        self.startButton.clicked.connect(self.start_thread)

        # File Button
        self.fileButton = QtWidgets.QPushButton(self.centralwidget)
        self.fileButton.setGeometry(QtCore.QRect(10, 110+24, 461, 41))
        self.fileButton.setObjectName("fileButton")
        self.fileButton.clicked.connect(self.getFile)

        Spammer.setCentralWidget(self.centralwidget)


        self.retranslateUi(Spammer)
        QtCore.QMetaObject.connectSlotsByName(Spammer)

    def retranslateUi(self, Spammer):
        _translate = QtCore.QCoreApplication.translate
        Spammer.setWindowTitle(_translate("Spammer", "Sequential spammer"))
        self.startButton.setToolTip(_translate("Spammer", "Spamming will start after a 5 second delay"))
        self.progressBar.setToolTip(_translate("Spammer", "Shows progress of spammer, kinda inverted but whatever"))
        self.startButton.setText(_translate("Spammer", "Start!"))
        self.timeBetweenMessagesLabel.setText(_translate("Spammer", "Time between messages"))
        self.minutesRemainingLabel.setText(_translate("Spammer", "Minutes remaining (approximate)"))
        self.fileButton.setText(_translate("Spammer", "Select script file"))
        self.chunkCountLabel.setText(_translate("Spammer", "Message block size"))
        self.percentRemainingLabel.setText(_translate("Spammer", "Percent remaining (approximate)"))
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Spammer = QtWidgets.QMainWindow()
    ui = Ui_Spammer()
    ui.setupUi(Spammer)
    Spammer.show()
    sys.exit(app.exec_())