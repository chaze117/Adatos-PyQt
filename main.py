import sys
import windows
import darkdetect
from Components.classes import *


def IsDark():
    if darkdetect.isDark() == True:
        return 1
    else:
        return 0

app = QApplication(sys.argv+ ['-platform', f'windows:darkmode={IsDark()}'])
window = windows.MainWindow()
app.exec_()

