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