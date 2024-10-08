from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import qtawesome as qta
import re
from datetime import datetime as DT

class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data
        self.hheaders = ["ID","Név","Születési Idő","TAJ Szám","Jogviszony Vége"]


    def data(self, index, role):
        if role == Qt.DisplayRole:
           value = self._data[index.row()][index.column()]
           if index.column() == 3:    # Betrag
                return re.sub(r'(\d{3})(?=\d)', r'\1-', str(value)[::-1])[::-1]
           else:
                return value

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])
    def headerData(self, section, orientation, role):           # <<<<<<<<<<<<<<< NEW DEF
        # row and column headers
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self.hheaders[section]
        return QVariant()
    
class Munkairanyito(QWidget):
    def __init__(self, parent):
        super(QWidget,self).__init__(parent)
        self.munkCB = QComboBox(editable=True)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.munkCB)
        self.table = QTableView()
        self.layout.addWidget(self.table)
        
        
        self.BF = QFrame()
        self.BF.layout=QVBoxLayout()
        self.BF.setLayout(self.BF.layout)
        self.layout.addWidget(self.BF)
        self.BF.setFixedSize(200,50)

        self.honap = QDateEdit()
        self.honap.setDisplayFormat("yyyy.MMMM")
        self.BF.layout.addWidget(self.honap)
        self.honap.setDate(QDate(DT.now().year,DT.now().month,DT.now().day))


        self.bottomFrame = QFrame()
        self.bottomFrame.setFixedSize(65,65)
        self.layout.addWidget(self.bottomFrame)
        self.bottomFrame.layout = QGridLayout()
        self.bottomFrame.setLayout(self.bottomFrame.layout)

        

        self.jelenleti = QPushButton(qta.icon('fa5s.book-open'),"")
        self.jelenleti.setIconSize(QSize(40,40))
        self.jelenleti.setFixedSize(50,50)
        self.jelenleti.setToolTip("Jelenléti nyomtatása")
        self.bottomFrame.layout.addWidget(self.jelenleti,0,0)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.setLayout(self.layout)