from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from typing import Any
from dataclasses import dataclass
import json
from firebase_admin import db



class ExtendedComboBox(QComboBox):
    def __init__(self, parent=None):
        super(ExtendedComboBox, self).__init__(parent)

        self.setFocusPolicy(Qt.StrongFocus)
        self.setEditable(True)

        # add a filter model to filter matching items
        self.pFilterModel = QSortFilterProxyModel(self)
        self.pFilterModel.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.pFilterModel.setSourceModel(self.model())

        # add a completer, which uses the filter model
        self.completer = QCompleter(self.pFilterModel, self)
        # always show all (filtered) completions
        self.completer.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
        self.setCompleter(self.completer)

        # connect signals
        self.lineEdit().textEdited.connect(self.pFilterModel.setFilterFixedString)
        self.completer.activated.connect(self.on_completer_activated)


    # on selection of an item from the completer, select the corresponding item from combobox 
    def on_completer_activated(self, text):
        if text:
            index = self.findText(text)
            self.setCurrentIndex(index)
            #self.activated[str].emit(self.itemText(index))


    # on model change, update the models of the filter and completer as well 
    def setModel(self, model):
        super(ExtendedComboBox, self).setModel(model)
        self.pFilterModel.setSourceModel(model)
        self.completer.setModel(self.pFilterModel)


    # on model column change, update the model column of the filter and completer as well
    def setModelColumn(self, column):
        self.completer.setCompletionColumn(column)
        self.pFilterModel.setFilterKeyColumn(column)
        super(ExtendedComboBox, self).setModelColumn(column)    

@dataclass
class Dolgozo:
    a_nev: str
    ado_sz: str
    cim: str
    id: int
    jog_k: str
    jog_v: str
    l_nev: str
    mir: int
    munkakor: int
    nev: str
    orvosi: str
    pid: int
    sz_hely: str
    sz_ido: str
    szamla_sz: str
    szigsz: str
    taj_sz: str
    tel_sz: str
    tuzelo: bool
    ugyirat: str
    
    def toJSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__, 
            sort_keys=True,
            indent=4)
    
    @staticmethod
    def from_dict(obj: Any) -> 'Dolgozo':
					if obj is not None:
									_a_nev = obj['a_nev']
									_ado_sz = str(obj.get("ado_sz"))
									_cim = str(obj.get("cim"))
									_id = int(obj.get("id"))
									_jog_k = str(obj.get("jog_k"))
									_jog_v = str(obj.get("jog_v"))
									_l_nev = str(obj.get("l_nev"))
									_mir = int(obj.get("mir"))
									_munkakor = int(obj.get("munkakor"))
									_nev = str(obj.get("nev"))
									_orvosi = str(obj.get("orvosi"))
									_pid = int(obj.get("pid"))
									_sz_hely = str(obj.get("sz_hely"))
									_sz_ido = str(obj.get("sz_ido"))
									_szamla_sz = str(obj.get("szamla_sz"))
									_szigsz = str(obj.get("szigsz"))
									_taj_sz = str(obj.get("taj_sz"))
									_tel_sz = str(obj.get("tel_sz"))
									_tuzelo = obj.get("tuzelo")
									_ugyirat = str(obj.get("ugyirat"))
									return Dolgozo(_a_nev, _ado_sz, _cim,  _id, _jog_k, _jog_v, _l_nev, _mir, _munkakor,  _nev, _orvosi, _pid, _sz_hely, _sz_ido,  _szamla_sz, _szigsz, _taj_sz, _tel_sz, _tuzelo, _ugyirat)

@dataclass
class Gyerek:
    a_nev: str
    ado: str
    cim: str
    id: int
    nev: str
    sz_hely: str
    sz_id: int
    sz_ido: str
    taj: str

    def toJSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__, 
            sort_keys=True,
            indent=4)

    @staticmethod
    def from_dict(obj: Any) -> 'Gyerek':
        if obj is not None:
            _a_nev = str(obj.get("a_nev"))
            _ado = str(obj.get("ado"))
            _cim = str(obj.get("cim"))
            _id = int(obj.get("id"))
            _nev = str(obj.get("nev"))
            _sz_hely = str(obj.get("sz_hely"))
            _sz_id = int(obj.get("sz_id"))
            _sz_ido = str(obj.get("sz_ido"))
            _taj = str(obj.get("taj"))
            return Gyerek(_a_nev, _ado, _cim, _id, _nev, _sz_hely, _sz_id, _sz_ido, _taj)

@dataclass
class Gyerek_NETAK:
    a_nev: str
    ado: str
    id: int
    nev: str
    sz_hely: str
    sz_id: int
    sz_ido: str

    def toJSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__, 
            sort_keys=True,
            indent=4)

    @staticmethod
    def from_dict(obj: Any) -> 'Gyerek_NETAK':
        if obj is not None:
            _a_nev = str(obj.get("a_nev"))
            _ado = str(obj.get("ado"))
            _id = int(obj.get("id"))
            _nev = str(obj.get("nev"))
            _sz_hely = str(obj.get("sz_hely"))
            _sz_id = int(obj.get("sz_id"))
            _sz_ido = str(obj.get("sz_ido"))
            return Gyerek_NETAK(_a_nev, _ado, _id, _nev, _sz_hely, _sz_id, _sz_ido)

@dataclass
class Munkairanyito:
        id:int
        nev:str

        def toJSON(self):
            return json.dumps(
                self,
                default=lambda o: o.__dict__, 
                sort_keys=True,
                indent=4)

        @staticmethod
        def from_dict(obj:Any) -> 'Munkairanyito':
                if obj is not None:
                        _id = int(obj.get("id"))
                        _nev = str(obj.get("nev"))
                        return Munkairanyito(_id,_nev)

@dataclass
class Munkakor:
        id:int
        nev:str
        brutto:int
        netto:int

        def toJSON(self):
            return json.dumps(
                self,
                default=lambda o: o.__dict__, 
                sort_keys=True,
                indent=4)
        @staticmethod
        def from_dict(obj:Any) -> 'Munkakor':
                if obj is not None:
                        _id = int(obj.get("id"))
                        _nev = str(obj.get("nev"))
                        _brutto = int(obj.get("brutto"))
                        _netto = int(obj.get("netto"))
                        return Munkakor(_id,_nev,_brutto,_netto)

@dataclass
class Program:
        id: int
        r_nev:str
        h_nev:str
        hatosagi:str

        def toJSON(self):
            return json.dumps(
                self,
                default=lambda o: o.__dict__, 
                sort_keys=True,
                indent=4)

        @staticmethod
        def from_dict(obj:Any) -> 'Program':
                if obj is not None:
                        _id = int(obj.get("id"))
                        _r_nev = str(obj.get("r_nev"))
                        _h_nev = str(obj.get("h_nev"))
                        _hatosagi = str(obj.get("hatosagi"))
                        return Program(_id,_r_nev,_h_nev,_hatosagi)
                
@dataclass
class Szamlaszam:
        id:int
        base64:str

        def toJSON(self):
            return json.dumps(
                self,
                default=lambda o: o.__dict__, 
                sort_keys=True,
                indent=4)
        
        @staticmethod
        def from_dict(obj:Any) -> 'Szamlaszam':
                if obj is not None:
                        _id = int(obj.get("id"))
                        _base64 = str(obj.get("base64"))
                        return Szamlaszam(_id,_base64)
                
class ToggleButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__("Munkairányító", parent)
        self.setCheckable(True)  # Allows the button to have checked/unchecked states
        self.setFixedSize(200, 40)
        self.setStyleSheet(self.get_stylesheet(False))
        self.toggled.connect(self.on_toggled)

    def on_toggled(self, checked):
        self.setText("Program" if checked else "Munkairányító")



    def get_stylesheet(self, checked):
        if checked:
            return """
                QPushButton {
                    background-color: green;
                    color: white;
                    border: 2px solid #5A5A5A;
                    border-radius: 20px;
                }
            """
        else:
            return """
                QPushButton {
                    background-color: lightgray;
                    color: black;
                    border: 2px solid #5A5A5A;
                    border-radius: 20px;
                }
            """
    def getMunkairanyitok():
        ref = db.reference("munkairanyitok")
        _temp = ref.get()
        Munkairanyitok = []
        for i in range(0,len(_temp)):
            Munkairanyitok.append(Munkairanyito.from_dict(_temp[i]))
        return Munkairanyitok
        
class DraggableTableWidget(QTableWidget):
    def __init__(self, rows, columns):
        super().__init__(rows, columns)
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.setDefaultDropAction(Qt.DropAction.MoveAction)
        self.setHorizontalHeaderLabels(["ID","Név","Születési idő"])
    def startDrag(self, supportedActions):
        drag = QDrag(self)
        mime_data = QMimeData()

        selected_items = self.selectedItems()
        if not selected_items:
            return

        # Extract the row of the first selected item
        row = selected_items[0].row()
        
        # Collect all column data for this row
        self.dragged_row_data = [self.item(row, col).text() for col in range(self.columnCount())]
        
        # Set the dragged row data as text in MIME data
        mime_data.setText("\n".join(self.dragged_row_data))
        drag.setMimeData(mime_data)

        # Execute the drag and drop operation
        drop_action = drag.exec(Qt.DropAction.MoveAction)

        # Remove the row if the drag operation was successful
        if drop_action == Qt.DropAction.MoveAction:
            self.removeRow(row)

    def dragEnterEvent(self, event):
        if event.source() != self:
            event.acceptProposedAction()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        event.acceptProposedAction()

    def dropEvent(self, event):
        if event.source() == self:
            event.ignore()
            return

        # Retrieve the dropped data as a list of strings
        dropped_text = event.mimeData().text().splitlines()
        # Add the dropped data as a new row
        row_position = self.rowCount()
        self.setRowCount(row_position + 1)
        
        for column, text in enumerate(dropped_text):
            self.setItem(row_position, column, QTableWidgetItem(text))

        event.acceptProposedAction()
    
    def addRow(self, rowData):
          row = self.rowCount()
          self.insertRow(row)
          for column, data in enumerate(rowData):
            self.setItem(row, column, QTableWidgetItem(str(data)))

class DraggableTableWidgetTuzelo(QTableWidget):
    def __init__(self, rows, columns):
        super().__init__(rows, columns)
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.setDefaultDropAction(Qt.DropAction.MoveAction)
        self.setHorizontalHeaderLabels(["ID","Név", "Utca", "Házszám"])

    def startDrag(self, supportedActions):
        drag = QDrag(self)
        mime_data = QMimeData()

        selected_items = self.selectedItems()
        if not selected_items:
            return

        # Extract the row of the first selected item
        row = selected_items[0].row()
        
        # Collect all column data for this row
        self.dragged_row_data = [self.item(row, col).text() for col in range(self.columnCount())]
        
        # Set the dragged row data as text in MIME data
        mime_data.setText("\n".join(self.dragged_row_data))
        drag.setMimeData(mime_data)

        # Execute the drag and drop operation
        drop_action = drag.exec(Qt.DropAction.MoveAction)

        # Remove the row if the drag operation was successful
        if drop_action == Qt.DropAction.MoveAction:
            self.removeRow(row)

    def dragEnterEvent(self, event):
        if event.source() != self:
            event.acceptProposedAction()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        event.acceptProposedAction()

    def dropEvent(self, event):
        if event.source() == self:
            event.ignore()
            return

        # Retrieve the dropped data as a list of strings
        dropped_text = event.mimeData().text().splitlines()
        # Add the dropped data as a new row
        row_position = self.rowCount()
        self.setRowCount(row_position + 1)
        
        for column, text in enumerate(dropped_text):
            self.setItem(row_position, column, QTableWidgetItem(text))

        event.acceptProposedAction()
    
    def addRow(self, rowData):
          row = self.rowCount()
          self.insertRow(row)
          for column, data in enumerate(rowData):
            self.setItem(row, column, QTableWidgetItem(str(data)))

    def clearTable(self):
        self.setRowCount(0)

class TuzeloTableModel(QAbstractTableModel):
    def __init__(self, data):
        super(TuzeloTableModel, self).__init__()
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