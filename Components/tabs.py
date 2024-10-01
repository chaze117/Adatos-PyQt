from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import Components.foadatok as foadatok
import Components.orvosi as orvosi
import Components.programok as programok
import Components.tuzelo as tuzelo
import Components.munkairanyito as munkairanyito
import Components.beallitasok as beallitasok
import Components.lista as Lista

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
        self.tab4 = tuzelo.Tuzelo(self.tabs)
        self.tab5 = munkairanyito.Munkairanyito(self.tabs)
        self.tab6 = beallitasok.Beallitasok(self.tabs) 
        self.tab7 = Lista.Lista(self.tabs,window=self.parent())  
        # Add tabs
        self.tabs.addTab(self.tab1,"Fő Adatok")
        self.tabs.addTab(self.tab2,"Orvosi")
        self.tabs.addTab(self.tab3,"Programok")
        self.tabs.addTab(self.tab4,"Tüzelő")
        self.tabs.addTab(self.tab5,"Munkairányító")
        self.tabs.addTab(self.tab7,"Lista rendezés")
        self.tabs.addTab(self.tab6,"Beállítások")    
        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)