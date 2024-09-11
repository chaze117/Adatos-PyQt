from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from typing import Any
from dataclasses import dataclass
import json

class CustomQCompleter(QCompleter):
    """
    adapted from: http://stackoverflow.com/a/7767999/2156909
    """
    def __init__(self, *args):#parent=None):
        super(CustomQCompleter, self).__init__(*args)
        self.local_completion_prefix = ""
        self.source_model = None
        self.filterProxyModel = QSortFilterProxyModel(self)
        self.usingOriginalModel = False

    def setModel(self, model):
        self.source_model = model
        self.filterProxyModel = QSortFilterProxyModel(self)
        self.filterProxyModel.setSourceModel(self.source_model)
        super(CustomQCompleter, self).setModel(self.filterProxyModel)
        self.usingOriginalModel = True

    def updateModel(self):
        if not self.usingOriginalModel:
            self.filterProxyModel.setSourceModel(self.source_model)

        pattern = QRegExp(self.local_completion_prefix,
                                Qt.CaseInsensitive,
                                QRegExp.FixedString)

        self.filterProxyModel.setFilterRegExp(pattern)

    def splitPath(self, path):
        self.local_completion_prefix = path
        self.updateModel()
        if self.filterProxyModel.rowCount() == 0:
            self.usingOriginalModel = False
            self.filterProxyModel.setSourceModel(QStringListModel([path]))
            return [path]

        return []

@dataclass
class Dolgozo:
    a_nev: str
    ado_sz: str
    cim: str
    csjk: bool
    dolgozik: bool
    ebed: bool
    id: int
    jog_k: str
    jog_v: str
    l_nev: str
    mir: int
    munkakor: int
    netak: bool
    nev: str
    orvosi: str
    pid: int
    sz_hely: str
    sz_ido: str
    szabi: float
    szamla_sz: str
    szigsz: str
    taj_sz: str
    tel_sz: str
    tuzelo: bool
    ugyirat: str
    ures: bool
    
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
									_csjk = obj.get("csjk")
									_dolgozik = obj.get("dolgozik")
									_ebed = obj.get("ebed")
									_id = int(obj.get("id"))
									_jog_k = str(obj.get("jog_k"))
									_jog_v = str(obj.get("jog_v"))
									_l_nev = str(obj.get("l_nev"))
									_mir = int(obj.get("mir"))
									_munkakor = int(obj.get("munkakor"))
									_netak = obj.get("netak")
									_nev = str(obj.get("nev"))
									_orvosi = str(obj.get("orvosi"))
									_pid = int(obj.get("pid"))
									_sz_hely = str(obj.get("sz_hely"))
									_sz_ido = str(obj.get("sz_ido"))
									_szabi = float(obj.get("szabi"))
									_szamla_sz = str(obj.get("szamla_sz"))
									_szigsz = str(obj.get("szigsz"))
									_taj_sz = str(obj.get("taj_sz"))
									_tel_sz = str(obj.get("tel_sz"))
									_tuzelo = obj.get("tuzelo")
									_ugyirat = str(obj.get("ugyirat"))
									_ures = obj.get("ures")
									return Dolgozo(_a_nev, _ado_sz, _cim, _csjk, _dolgozik, _ebed, _id, _jog_k, _jog_v, _l_nev, _mir, _munkakor, _netak, _nev, _orvosi, _pid, _sz_hely, _sz_ido, _szabi, _szamla_sz, _szigsz, _taj_sz, _tel_sz, _tuzelo, _ugyirat, _ures)

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
        
        @staticmethod
        def from_dict(obj:Any) -> 'Szamlaszam':
                if obj is not None:
                        _id = int(obj.get("id"))
                        _base64 = str(obj.get("base64"))
                        return Szamlaszam(_id,_base64)