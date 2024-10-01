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
splash_pix = QPixmap('splash.png')  # Path to your splash image
splash = QSplashScreen(splash_pix)
splash.setMask(splash_pix.mask())  # Optional: to create a transparent mask
splash.show()
window = windows.MainWindow()
splash.hide()
app.exec_()

