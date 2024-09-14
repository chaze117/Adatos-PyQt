import sys
import windows
import darkdetect
from Components.classes import *
import qdarktheme


def IsDark():
    if darkdetect.isDark() == True:
        return 1
    else:
        return 0

app = QApplication(sys.argv+ ['-platform', f'windows:darkmode={IsDark()}'])
qdarktheme.setup_theme('auto')
window = windows.MainWindow()
app.exec_()

