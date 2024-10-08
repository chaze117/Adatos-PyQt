from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import qtawesome as qta
from Components.classes import *
from Components.functions import fillTuzeloData
from Components.functions import fillAllDolgozo
from Components.firebase import getDolgozok


class Tuzelo(QTabWidget):
    def __init__(self, parent):
        super(QWidget,self).__init__(parent)
        self.window = parent
        self.layout = QVBoxLayout(self)
        self.tabs = QTabWidget()
        self.t1 = QTabWidget()
        self.t2 = QTabWidget()
        self.tabs.addTab(self.t1,"Lista")
        self.tabs.addTab(self.t2,"Lista Szerkesztése")
        self.layout.addWidget(self.tabs)

        self.t1.layout = QVBoxLayout()
        self.t1.setLayout(self.t1.layout)
        self.table = QTableView()
        self.t1.layout.addWidget(self.table)
        self.BF = QFrame()
        self.t1.layout.addWidget(self.BF)
        self.BF.setFixedSize(115,65)
        self.BF.layout = QGridLayout()
        self.BF.setLayout(self.BF.layout)

        self.refresh = QPushButton(qta.icon('fa.refresh'),"")
        self.refresh.setIconSize(QSize(40,40))
        self.refresh.setFixedSize(50,50)
        self.refresh.setToolTip("Lista frissítése")
        self.BF.layout.addWidget(self.refresh,0,0)

        self.print = QPushButton(qta.icon('fa.print'),"")
        self.print.setIconSize(QSize(40,40))
        self.print.setToolTip("Lista nyomtatása")
        self.print.setFixedSize(50,50)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.BF.layout.addWidget(self.print,0,1)

        self.t2.layout = QGridLayout()
        self.t2.setLayout(self.t2.layout)
        self.search = QLineEdit()
        self.search.textChanged.connect(lambda: fillAllDolgozo(self.window,text=self.search.text()))
        self.t2.layout.addWidget(self.search,0,0,1,2)
        self.alltable = DraggableTableWidgetTuzelo(0,4)
        self.t2.layout.addWidget(self.alltable,1,0)
        self.tuzelotable = DraggableTableWidgetTuzelo(0,4)
        self.t2.layout.addWidget(self.tuzelotable,1,1)

        self.tuzelotable.dropEvent = self.drop2
        self.alltable.dropEvent = self.drop1

    def drop2(self,event):
        if event.source() == self:
            event.ignore()
            return
        
        dropped_text = event.mimeData().text().splitlines()
        id = dropped_text[0]
        row_position = self.tuzelotable.rowCount()
        self.tuzelotable.setRowCount(row_position + 1)
        for column, text in enumerate(dropped_text):
            self.tuzelotable.setItem(row_position, column, QTableWidgetItem(text))
        ref = db.reference(f"dolgozok/{id}")
        ref.child("tuzelo").set(True)
        self.window.Dolgozok = getDolgozok()
        fillAllDolgozo(self.window,self.search.text())
        fillTuzeloData(self.window,True)
        event.acceptProposedAction()

    def drop1(self,event):
        if event.source() == self:
            event.ignore()
            return
        dropped_text = event.mimeData().text().splitlines()
        id = dropped_text[0]
        row_position = self.alltable.rowCount()
        self.alltable.setRowCount(row_position + 1)
        for column, text in enumerate(dropped_text):
            self.alltable.setItem(row_position, column, QTableWidgetItem(text))
        ref = db.reference(f"dolgozok/{id}")
        ref.child("tuzelo").set(False)
        self.window.Dolgozok = getDolgozok()
        fillAllDolgozo(self.window,self.search.text())
        fillTuzeloData(self.window,True)
        event.acceptProposedAction()
        #for git update
