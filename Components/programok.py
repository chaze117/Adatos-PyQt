from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import qtawesome as qta
import re

class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data
        self.hheaders = ["ID","Név","Születési Idő","TAJ Szám","Adóazonosító","Jogviszony kezdete"]


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

class Programok(QWidget):
    def __init__(self, parent):
        super(QWidget,self).__init__(parent)
        self.progCB = QComboBox(editable=True)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.progCB)
        self.table = QTableView()
        self.layout.addWidget(self.table)
        
        self.bottomFrame = QFrame()
        self.bottomFrame.setFixedSize(115,65)
        self.layout.addWidget(self.bottomFrame)
        self.bottomFrame.layout = QGridLayout()
        self.bottomFrame.setLayout(self.bottomFrame.layout)



        self.mkigeny = QPushButton(qta.icon('mdi6.account-arrow-down'),"")
        self.mkigeny.setIconSize(QSize(40,40))
        self.mkigeny.setFixedSize(50,50)
        self.mkigeny.setToolTip("Munkaerőigény")
        self.bottomFrame.layout.addWidget(self.mkigeny,0,0)

        self.rename = QPushButton(qta.icon('ei.pencil'),"")
        self.rename.setIconSize(QSize(40,40))
        self.rename.setToolTip("Átnevezés elektronikus beküldéshez")
        self.rename.setFixedSize(50,50)
        self.bottomFrame.layout.addWidget(self.rename,0,1)


        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.setLayout(self.layout)
    def update(self,value):
        self.oLabel.setText(f"Lejár {value} napon belül")