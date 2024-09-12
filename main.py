from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import windowses
import darkdetect
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import datetime
from datetime import date, timedelta
from Components.orvosi import TableModel as orvosiTM
from Components.programok import TableModel as progTM
from Components.tuzelo import TableModel as tuzeloTM
from Components.munkairanyito import TableModel as mirTM
from Components.classes import *
import Components.functions as F

def IsDark():
    if darkdetect.isDark() == True:
        return 1
    else:
        return 0

app = QApplication(sys.argv+ ['-platform', f'windows:darkmode={IsDark()}'])
window = windowses.MainWindow()
app.exec_()

