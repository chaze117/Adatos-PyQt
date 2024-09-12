from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import qtawesome as qta
import re

class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data
        self.hheaders = ["ID","Név", "Születési Hely", "Születési Idő","Anyja Neve","Cím", "TAJ Szám","Érvényes"]


    def data(self, index, role):
        if role == Qt.DisplayRole:
           value = self._data[index.row()][index.column()]
           if index.column() == 6:    # Betrag
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

class Orvosi(QWidget):
    def __init__(self, parent):
        super(QWidget,self).__init__(parent)
        self.progCB = QComboBox(editable=True)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.progCB)
        self.table = QTableView()
        self.layout.addWidget(self.table)


        self.bottomFrame = QFrame()
        self.bottomFrame.setFixedSize(300,150)
        self.layout.addWidget(self.bottomFrame)
        self.bottomFrame.layout = QGridLayout()
        self.bottomFrame.setLayout(self.bottomFrame.layout)
        self.oLabel = QLabel("Lejár 30 napon belül")
        self.bottomFrame.layout.addWidget(self.oLabel,0,0)
        self.oSlider = QSlider(Qt.Orientation.Horizontal, self)
        self.oSlider.setRange(0,365)
        self.oSlider.setValue(30)
        self.oSlider.setMaximumSize(300,20)
        self.bottomFrame.layout.addWidget(self.oSlider,1,0)
        self.Grid2 = QFrame()
        self.Grid2.layout = QGridLayout()
        self.Grid2.setLayout(self.Grid2.layout)
        self.bottomFrame.layout.addWidget(self.Grid2,2,0)
        self.Grid2.setFixedSize(110,65)

        self.printList = QPushButton(qta.icon('mdi.format-list-bulleted'),"")
        self.printList.setIconSize(QSize(40,40))
        self.printList.setFixedSize(50,50)
        self.printList.setToolTip("Lista nyomtatása")
        self.Grid2.layout.addWidget(self.printList,0,0)

        self.print = QPushButton(qta.icon('fa.print'),"")
        self.print.setIconSize(QSize(40,40))
        self.print.setToolTip("Alkalmasságik nyomtatása")
        self.print.setFixedSize(50,50)
        self.Grid2.layout.addWidget(self.print,0,1)


        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.setLayout(self.layout)
