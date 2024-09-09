from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import qdarktheme
import Components.tabs as tabs

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args,**kwargs)
        self.setWindowTitle("Adatkezelő Alaklmazás")
        height = 825
        self.setGeometry(200,50,1165,height)
        self.setFixedSize(1165,height)
        self.setWindowIcon(QIcon('icon.ico'))
        qdarktheme.setup_theme("auto")
        self.table_widget= tabs.Tabs(self)
        self.setCentralWidget(self.table_widget)
        self.setStyleSheet('font-size: 10pt; font-family: Arial;')
        self.show()
        
        