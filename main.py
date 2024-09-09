from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import mainwindow
import darkdetect

def IsDark():
    if darkdetect.isDark() == True:
        return 1
    else:
        return 0

app = QApplication(sys.argv+ ['-platform', f'windows:darkmode={IsDark()}'])
window = mainwindow.MainWindow()
app.exec_()

