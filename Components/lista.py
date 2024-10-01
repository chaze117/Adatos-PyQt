from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import qtawesome as qta
from Components.classes import *
import Components.firebase as FB

class Lista(QWidget):
    def __init__(self, parent):
        super(QWidget,self).__init__(parent)
        self.checked = False
        self.layout = QGridLayout(self)
        self.setLayout(self.layout)
        self.toggle = ToggleButton(parent=self)
        self.layout.addWidget(self.toggle,0,0,1,0)
        self.toggle.clicked.connect(self.ontoggle)
        self.CB1 = QComboBox()
        self.layout.addWidget(self.CB1,1,0)
        self.CB2 = QComboBox()
        self.layout.addWidget(self.CB2,1,1)
        self.table1 = DraggableTableWidget(1,3)
        self.layout.addWidget(self.table1,2,0)
        self.table2 = DraggableTableWidget(1,3)
        self.layout.addWidget(self.table2,2,1)
        self.Munkairanyitok = FB.getMunkairanyitok()
        self.Programok = FB.getProgramok()
        self.Dolgozok = FB.getDolgozok()
        for munkairanyito in self.Munkairanyitok:
            if munkairanyito is not None:
                self.CB1.addItem(f"{munkairanyito.id}. {munkairanyito.nev}")
                self.CB2.addItem(f"{munkairanyito.id}. {munkairanyito.nev}")
    
    def ontoggle(self,checked):
        self.checked = checked
        if checked == True:
            self.CB1.clear()
            self.CB2.clear()
            for program in self.Programok:
                if program is not None:
                    self.CB1.addItem(f"{program.id}. {program.r_nev}")
                    self.CB2.addItem(f"{program.id}. {program.r_nev}")
        else:
            self.CB1.clear()
            self.CB2.clear()
            for munkairanyito in self.Munkairanyitok:
                if munkairanyito is not None:
                    self.CB1.addItem(f"{munkairanyito.id}. {munkairanyito.nev}")
                    self.CB2.addItem(f"{munkairanyito.id}. {munkairanyito.nev}")
    
    def Cb1changed(self):
        if self.CB1.currentIndex() > -1:
            id = int(self.CB1.currentText().split('.')[0])
            if self.checked == True:
                for dolgozo in self.Dolgozok:
                    if dolgozo is not None and dolgozo.pid == id:
                        self.table1.setItem(self.table1.rowCount+1,0,dolgozo.id)
                        self.table1.setItem(self.table1.rowCount+1,1,dolgozo.nev)
                        self.table1.setItem(self.table1.rowCount+1,2,dolgozo.sz_ido)
