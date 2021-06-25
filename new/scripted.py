"""
! WARNING: THIS IS CURRENTLY UNDER CONSTRUCTION AND WILL NOT FUNCTION.
FIXME: everything in this.
"""
from time import sleep
import keyboard
import random
def runScriptedSpammer(self, filePath):
    try:
        self.startButton.setText("Starting in 5 seconds")
        file = open(filePath[1], "r")
        ac = str(file.read())
        split_up_script = []
        split_up_script = ac.splitlines()
        splsc = split_up_script
        wait_time = self.timeBetweenMessages.value()
        chunkyBoiCount = self.chunkCount.value()
        randomTime = self.randomizeTimeScripted.checkState()
        n_elem = len(split_up_script)
        time_remaining = n_elem * wait_time + n_elem//chunkyBoiCount * wait_time * 1.5
        old_time = time_remaining
        sleep(5)
        i = 0
        ln = 0
        self.startButton.setText("Start!")
        for split_up_script in split_up_script:
            if randomTime >= 1:
                wait_time = round(random.uniform(0.5, 2), 2)
                self.minutesRemainingLabel.setText("Cannot calculate")
            ln += 1
            keyboard.write(splsc[i])
            sleep(0.001)
            keyboard.press_and_release("shift+enter")
            i += 1
            time_remaining = n_elem * wait_time - i * wait_time + n_elem//chunkyBoiCount * wait_time*1.5
            time_remaining_minutes = int(time_remaining)//60
            time_percent = round(time_remaining/old_time * 100)
            if randomTime == 0:
                self.minutesRemainingDisplay.setProperty("value", time_remaining_minutes)
                self.progressBar.setProperty("value", time_percent)
            print(f"{i}/{n_elem}")
            if chunkyBoiCount == ln:
                print("----------")
                keyboard.press_and_release("enter")
                ln = 0
                sleep(wait_time*1.5)
            sleep(wait_time)
            if i == n_elem:
                self.minutesRemainingLabel.setText("Minutes remaining (approximate)")
    except:
        self.startButton.setText("Please select a script file!")
        sleep(1.5)
        self.startButton.setText("Start!")