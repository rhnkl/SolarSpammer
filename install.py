import os
import platform
if platform.system() == "Windows":
    os.system('cmd /k "py -m pip install PyQt5 & py -m pip install keyboard && exit && py -m pip install mouse"')
if platform.system() == "Linux" or platform.system() == "Darwin":
    os.system('pip install PyQt5 ; pip install keyboard ; pip install mouse ; exit')
