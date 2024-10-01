from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import qtawesome as qta
from Components.classes import *
import Components.firebase as FB

class Lista(QWidget):
    def __init__(self, parent, window):
        super(QWidget,self).__init__(parent)
        self.checked = False
        self.Window = window
        self.layout = QGridLayout(self)
        self.setLayout(self.layout)
        self.toggle = ToggleButton(parent=self)
        self.layout.addWidget(self.toggle,0,0,1,0)
        self.toggle.clicked.connect(self.ontoggle)
        self.CB1 = QComboBox()
        self.layout.addWidget(self.CB1,1,0)
        self.CB2 = QComboBox()
        self.layout.addWidget(self.CB2,1,1)
        self.table1 = DraggableTableWidget(5,3)
        self.layout.addWidget(self.table1,2,0)
        self.table2 = DraggableTableWidget(1,3)
        self.layout.addWidget(self.table2,2,1)
        for munkairanyito in self.Window.Munkairanyitok:
            if munkairanyito is not None:
                self.CB1.addItem(f"{munkairanyito.id}. {munkairanyito.nev}")
                self.CB2.addItem(f"{munkairanyito.id}. {munkairanyito.nev}")
        self.CB1.currentIndexChanged.connect(self.Cb1changed)
        self.CB2.currentIndexChanged.connect(self.Cb2changed)
        self.table2.dropEvent = self.dropEvent2
        self.table1.dropEvent = self.dropEvent1
        #self.table1.drag
    def ontoggle(self,checked):
        self.checked = checked
        if checked == True:
            self.CB1.clear()
            self.CB2.clear()
            for program in self.Window.Programok:
                if program is not None:
                    self.CB1.addItem(f"{program.id}. {program.r_nev}")
                    self.CB2.addItem(f"{program.id}. {program.r_nev}")
        else:
            self.CB1.clear()
            self.CB2.clear()
            for munkairanyito in self.Window.Munkairanyitok:
                if munkairanyito is not None:
                    self.CB1.addItem(f"{munkairanyito.id}. {munkairanyito.nev}")
                    self.CB2.addItem(f"{munkairanyito.id}. {munkairanyito.nev}")
    
    def Cb1changed(self):
        if self.CB1.currentIndex() > -1:
            id = int(self.CB1.currentText().split('.')[0])
            if self.checked == True:
                self.table1.clearContents()
                self.table1.setRowCount(1)
                self.table1.setColumnCount(3)
                Dolgozok = list(filter(lambda dolgozo: dolgozo is not None and dolgozo.pid == id,self.Window.Dolgozok))
                Dolgozok = sorted(Dolgozok, key=lambda x: x.nev)
                for dolgozo in Dolgozok:
                        rowCount = self.table1.rowCount()
                        if rowCount < len(Dolgozok):
                            self.table1.insertRow(rowCount)
                        self.table1.setItem(rowCount-1,0,QTableWidgetItem(str(dolgozo.id)))
                        self.table1.setItem(rowCount-1,1,QTableWidgetItem(dolgozo.nev))
                        self.table1.setItem(rowCount-1,2,QTableWidgetItem(dolgozo.sz_ido[0:10].replace('-','.')))
            else:
                self.table1.clearContents()
                self.table1.setRowCount(1)
                self.table1.setColumnCount(3)
                Dolgozok = list(filter(lambda dolgozo: dolgozo is not None and dolgozo.mir == id,self.Window.Dolgozok))
                Dolgozok = sorted(Dolgozok, key=lambda x: x.nev)
                for dolgozo in Dolgozok:
                        rowCount = self.table1.rowCount()
                        if rowCount < len(Dolgozok):
                            self.table1.insertRow(rowCount)
                        self.table1.setItem(rowCount-1,0,QTableWidgetItem(str(dolgozo.id)))
                        self.table1.setItem(rowCount-1,1,QTableWidgetItem(dolgozo.nev))
                        self.table1.setItem(rowCount-1,2,QTableWidgetItem(dolgozo.sz_ido[0:10].replace('-','.')))
            self.table1.resizeColumnsToContents()
        
    def Cb2changed(self):
        if self.CB2.currentIndex() > -1:
            id = int(self.CB2.currentText().split('.')[0])
            if self.checked == True:
                self.table2.clearContents()
                self.table2.setRowCount(1)
                self.table2.setColumnCount(3)
                Dolgozok = list(filter(lambda dolgozo: dolgozo is not None and dolgozo.pid == id,self.Window.Dolgozok))
                Dolgozok = sorted(Dolgozok, key=lambda x: x.nev)
                for dolgozo in Dolgozok:
                        rowCount = self.table2.rowCount()
                        if rowCount < len(Dolgozok):
                            self.table2.insertRow(rowCount)
                        self.table2.setItem(rowCount-1,0,QTableWidgetItem(str(dolgozo.id)))
                        self.table2.setItem(rowCount-1,1,QTableWidgetItem(dolgozo.nev))
                        self.table2.setItem(rowCount-1,2,QTableWidgetItem(dolgozo.sz_ido[0:10].replace('-','.')))
                self.table2.resizeColumnsToContents()
            else:
                self.table2.clearContents()
                self.table2.setRowCount(1)
                self.table2.setColumnCount(3)
                Dolgozok = list(filter(lambda dolgozo: dolgozo is not None and dolgozo.mir == id,self.Window.Dolgozok))
                Dolgozok = sorted(Dolgozok, key=lambda x: x.nev)
                for dolgozo in Dolgozok:
                        rowCount = self.table2.rowCount()
                        if rowCount < len(Dolgozok):
                            self.table2.insertRow(rowCount)
                        self.table2.setItem(rowCount-1,0,QTableWidgetItem(str(dolgozo.id)))
                        self.table2.setItem(rowCount-1,1,QTableWidgetItem(dolgozo.nev))
                        self.table2.setItem(rowCount-1,2,QTableWidgetItem(dolgozo.sz_ido[0:10].replace('-','.')))
            self.table2.resizeColumnsToContents()

    def dropEvent2(self, event):
        if event.source() == self:
            event.ignore()
            return

        # Retrieve the dropped data as a list of strings
        dropped_text = event.mimeData().text().splitlines()
        id = dropped_text[0]
        child = ""
        if self.checked == True: child="pid"
        else: child="mir"
        newid = self.CB2.currentText().split(".")[0]
        row_position = self.table2.rowCount()
        self.table2.setRowCount(row_position + 1)
        
        for column, text in enumerate(dropped_text):
            self.table2.setItem(row_position, column, QTableWidgetItem(text))
        ref = db.reference(f"dolgozok/{id}")
        ref.child(child).set(newid)
        self.Window.Dolgozok = FB.getDolgozok()
        self.Cb1changed()
        self.Cb2changed()
        event.acceptProposedAction()

    def dropEvent1(self, event):
        if event.source() == self:
            event.ignore()
            return

        # Retrieve the dropped data as a list of strings
        dropped_text = event.mimeData().text().splitlines()
        id = dropped_text[0]
        child = ""
        if self.checked == True: child="pid"
        else: child="mir"
        newid = self.CB1.currentText().split(".")[0]
        row_position = self.table1.rowCount()
        self.table1.setRowCount(row_position + 1)
        
        for column, text in enumerate(dropped_text):
            self.table1.setItem(row_position, column, QTableWidgetItem(text))
        ref = db.reference(f"dolgozok/{id}")
        ref.child(child).set(newid)
        self.Window.Dolgozok = FB.getDolgozok()
        self.Cb1changed()
        self.Cb2changed()
        event.acceptProposedAction()