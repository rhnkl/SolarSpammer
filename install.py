import os
import platform
if platform.system() == "Windows":
    os.system('cmd /k "py -m pip install PyQt5 & py -m pip install keyboard"')
if platform.system() == "Linux":
    os.system('pip install PyQt5 ; pip install keyboard')
if platform.system() == "Darwin":
    os.system('pip install PyQt5 ; pip install keyboard')