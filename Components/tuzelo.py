from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import qtawesome as qta


class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data
        self.hheaders = ["ID","Név", "Utca", "Házszám"]

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])
    
    def headerData(self, section, orientation, role):           # <<<<<<<<<<<<<<< NEW DEF
        # row and column headers
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self.hheaders[section]
        return QVariant()

class Tuzelo(QWidget):
    def __init__(self, parent):
        super(QWidget,self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.table = QTableView()
        self.layout.addWidget(self.table)


        self.BF = QFrame()
        self.layout.addWidget(self.BF)
        self.BF.setFixedSize(110,65)
        self.BF.layout = QGridLayout()
        self.BF.setLayout(self.BF.layout)

        self.newD = QPushButton(qta.icon('fa.refresh'),"")
        self.newD.setIconSize(QSize(40,40))
        self.newD.setToolTip("Lista frissítése")
        self.BF.layout.addWidget(self.newD,0,0)

        self.newD2 = QPushButton(qta.icon('fa.print'),"")
        self.newD2.setIconSize(QSize(40,40))
        self.newD2.setToolTip("Lista nyomtatása")

        self.BF.layout.addWidget(self.newD2,0,1)