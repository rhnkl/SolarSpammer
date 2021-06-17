import os
import platform
if platform.system() == "Windows":
    os.system('cmd /k "py -m pip install PyQt5 & py -m pip install keyboard && exit"')
if platform.system() == "Linux" or platform.system() == "Darwin":
    os.system('pip install PyQt5 ; pip install keyboard ; exit')
