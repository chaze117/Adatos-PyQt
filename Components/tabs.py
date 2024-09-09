from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import Components.foadatok as foadatok
import Components.orvosi as orvosi
import Components.programok as programok

class Tabs(QWidget):
    def __init__(self, parent):
        super(QWidget,self).__init__(parent)
        self.setStyleSheet(' font: bold')
        self.layout = QVBoxLayout(self)
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = foadatok.FoAdatok(self.tabs)
        self.tab2 = orvosi.Orvosi(self.tabs)
        self.tab3 = programok.Programok(self.tabs)
        self.tab4 = QWidget()
        self.tab5 = QWidget()
        self.tab6 = QWidget()        
        # Add tabs
        self.tabs.addTab(self.tab1,"Fő Adatok")
        self.tabs.addTab(self.tab2,"Orvosi")
        self.tabs.addTab(self.tab3,"Programok")
        self.tabs.addTab(self.tab4,"Tüzelő")
        self.tabs.addTab(self.tab5,"Munkairányító")
        self.tabs.addTab(self.tab6,"Beállítások")    
        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)