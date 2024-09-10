from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import mainwindow
import darkdetect
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from typing import Any
from dataclasses import dataclass
from datetime import date

def IsDark():
    if darkdetect.isDark() == True:
        return 1
    else:
        return 0
    
#region autocomplete stuff
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
#endregion

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

    @staticmethod
    def from_dict(obj: Any) -> 'Dolgozo':
					if obj is not None:
									_a_nev = obj['a_nev']
									_ado_sz = str(obj.get("ado_sz"))
									_cim = str(obj.get("cim"))
									_csjk = obj.get("_csjk")
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

app = QApplication(sys.argv+ ['-platform', f'windows:darkmode={IsDark()}'])
window = mainwindow.MainWindow()

cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred, {'databaseURL': 'https://zomboradat-default-rtdb.europe-west1.firebasedatabase.app/'})


#region get data
ref = db.reference('dolgozok')
_temp = ref.get()
Dolgozok = []
for i in range(0,len(_temp)):
    Dolgozok.append(Dolgozo.from_dict(_temp[i]))


ref = db.reference('gyerek')
_temp = ref.get()
Gyerekek = []
for i in range(0,len(_temp)):
    Gyerekek.append(Gyerek.from_dict(_temp[i]))

ref = db.reference("gyerek_netak")
_temp = ref.get()
Gyerekek_n = []
for i in range(0,len(_temp)):
    Gyerekek_n.append(Gyerek_NETAK.from_dict(_temp[i]))

ref = db.reference("munkairanyitok")
_temp = ref.get()
Munkairanyitok = []
for i in range(0,len(_temp)):
    Munkairanyitok.append(Munkairanyito.from_dict(_temp[i]))

ref = db.reference("munkakorok")
_temp = ref.get()
Munkakorok = []
for i in range(0,len(_temp)):
    Munkakorok.append(Munkakor.from_dict(_temp[i]))

ref = db.reference("programok")
_temp = ref.get()
Programok = []
for i in range(0,len(_temp)):
    Programok.append(Program.from_dict(_temp[i]))

ref = db.reference("szamlaszamok")
_temp = ref.get()
Szamlaszamok = []
for i in range(0,len(_temp)):
    Szamlaszamok.append(Szamlaszam.from_dict(_temp[i]))


#endregion
#region fill fo adatok
searchCB = window.tabs_widget.tab1.searchCB
searchCB.setInsertPolicy(QComboBox.NoInsert)
completer = CustomQCompleter(searchCB)
completer.setCompletionMode(QCompleter.PopupCompletion)
completer.setModel(searchCB.model())
searchCB.setCompleter(completer)

today = date.today()
SzemAdat = window.tabs_widget.tab1.szemadatF
JogvAdat = window.tabs_widget.tab1.jvF
CSJK = window.tabs_widget.tab1.adoF.tab1
NETAK = window.tabs_widget.tab1.adoF.tab2

for dolgozo in Dolgozok:
      if dolgozo is not None:
        searchCB.addItem(f"{dolgozo.id}. {dolgozo.nev} - {dolgozo.sz_ido[0:10].replace('-','.')}")
for munkakor in Munkakorok:
       if munkakor is not None:
        JogvAdat.mkC.addItem(f"{munkakor.id}. {munkakor.nev}")
for program in Programok:
      if program is not None:
        JogvAdat.progC.addItem(f"{program.id}. {program.r_nev}")
for munkairanyito in Munkairanyitok:
      if munkairanyito is not None:
        JogvAdat.mirC.addItem(f"{munkairanyito.id}. {munkairanyito.nev}")
def SelectedDolgozo(value):
    id = searchCB.currentText().split('.')
    id = int(id[0])
    
    SzemAdat.nameT.setText(Dolgozok[id].nev)
    SzemAdat.lnameT.setText(Dolgozok[id].l_nev)
    SzemAdat.szhT.setText(Dolgozok[id].sz_hely)
    y,m,d = Dolgozok[id].sz_ido[0:10].split('-')
    SzemAdat.sziD.setDate(QDate(int(y),int(m),int(d)))
    SzemAdat.adoT.setText(Dolgozok[id].ado_sz)
    SzemAdat.tajT.setText(Dolgozok[id].taj_sz)
    SzemAdat.cimT.setText(Dolgozok[id].cim)
    szamla = Dolgozok[id].szamla_sz.replace('-','').replace('8x0','00000000')
    if len(szamla) == 0:
            SzemAdat.szamlaT.setInputMask("")
    elif len(szamla) < 17:
        SzemAdat.szamlaT.setInputMask("99999999-99999999")
    else:
        SzemAdat.szamlaT.setInputMask("99999999-99999999-99999999")
    SzemAdat.szamlaT.setText(szamla)
    telefon = Dolgozok[id].tel_sz.replace("-","").replace("/","")
    SzemAdat.telT.setText(telefon)
    SzemAdat.szigT.setText(Dolgozok[id].szigsz)
    SzemAdat.tuzelo.setChecked(Dolgozok[id].tuzelo)
    y,m,d = Dolgozok[id].jog_k[0:10].split('-')
    JogvAdat.jkD.setDate(QDate(int(y),int(m),int(d)))
    y,m,d = Dolgozok[id].jog_v[0:10].split('-')
    JogvAdat.jvD.setDate(QDate(int(y),int(m),int(d)))
    JogvAdat.mkC.setCurrentIndex(Dolgozok[id].munkakor)
    JogvAdat.nettoT.setText(str(Munkakorok[Dolgozok[id].munkakor].netto))
    JogvAdat.progC.setCurrentIndex(Dolgozok[id].pid-1)
    JogvAdat.mirC.setCurrentIndex(Dolgozok[id].mir-1)
    JogvAdat.ugyT.setText(Dolgozok[id].ugyirat)
    y,m,d = Dolgozok[id].orvosi[0:10].split('-')
    JogvAdat.orvosiT.setDate(QDate(int(y),int(m),int(d)))
    CSJK.CSJKCB.clear()
    CSJK.nameT.clear()
    CSJK.anevT.clear()
    CSJK.szhT.clear()
    CSJK.sziD.setDate(today)
    CSJK.adoT.clear()
    CSJK.tajT.clear()
    CSJK.cimT.clear()
    for gyerek in Gyerekek:
          if gyerek is not None and int(gyerek.sz_id) == id:
                CSJK.CSJKCB.addItem(f"{gyerek.id}. {gyerek.nev} - {gyerek.sz_ido[0:10].replace('-','.')}")
    NETAK.NETAKCB.clear()
    NETAK.nameT.clear()
    NETAK.anevT.clear()
    NETAK.szhT.clear()
    NETAK.sziD.setDate(today)
    NETAK.adoT.clear()
    for gyerek in Gyerekek_n:
          if gyerek is not None and int(gyerek.sz_id) == id:
                NETAK.NETAKCB.addItem(f"{gyerek.id}. {gyerek.nev} - {gyerek.sz_ido[0:10].replace('-','.')}") 
         
def SelectedCSJK(value):
    if value > -1:
        id = CSJK.CSJKCB.currentText().split('.')
        id = int(id[0])
        CSJK.nameT.setText(Gyerekek[id].nev)
        CSJK.anevT.setText(Gyerekek[id].a_nev)
        CSJK.szhT.setText(Gyerekek[id].sz_hely)
        y,m,d = Gyerekek[id].sz_ido[0:10].split('-')
        CSJK.sziD.setDate(QDate(int(y),int(m),int(d)))
        CSJK.adoT.setText(Gyerekek[id].ado)
        CSJK.tajT.setText(Gyerekek[id].taj)
        CSJK.cimT.setText(Gyerekek[id].cim)
def SelectedNETAK(value):
      if value > -1:
        id = NETAK.NETAKCB.currentText().split('.')
        id = int(id[0])
        NETAK.nameT.setText(Gyerekek_n[id].nev)
        NETAK.anevT.setText(Gyerekek_n[id].a_nev)
        NETAK.szhT.setText(Gyerekek_n[id].sz_hely)
        y,m,d = Gyerekek_n[id].sz_ido[0:10].split('-')
        NETAK.sziD.setDate(QDate(int(y),int(m),int(d)))
        NETAK.adoT.setText(Gyerekek_n[id].ado)

CSJK.CSJKCB.currentIndexChanged.connect(SelectedCSJK)
NETAK.NETAKCB.currentIndexChanged.connect(SelectedNETAK)
searchCB.currentIndexChanged.connect(SelectedDolgozo)
#endregion
app.exec_()

