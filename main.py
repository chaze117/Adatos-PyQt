from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import windowses
import darkdetect
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import datetime
from datetime import date, timedelta
from Components.orvosi import TableModel as orvosiTM
from Components.programok import TableModel as progTM
from Components.tuzelo import TableModel as tuzeloTM
from Components.munkairanyito import TableModel as mirTM
from Components.classes import *

def IsDark():
    if darkdetect.isDark() == True:
        return 1
    else:
        return 0

app = QApplication(sys.argv+ ['-platform', f'windows:darkmode={IsDark()}'])
window = windowses.MainWindow()

cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred, {'databaseURL': 'https://zomboradat-default-rtdb.europe-west1.firebasedatabase.app/'},"sec")

#region get data
# ref = db.reference('dolgozok')
# _temp = ref.get()
# Dolgozok = []
# for i in range(0,len(_temp)):
#     Dolgozok.append(Dolgozo.from_dict(_temp[i]))


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
Buttons = window.tabs_widget.tab1.buttonsF
orvosi = window.tabs_widget.tab2
programok = window.tabs_widget.tab3
tuzelo = window.tabs_widget.tab4
munkairanyitok = window.tabs_widget.tab5
beallitasok = window.tabs_widget.tab6

# for dolgozo in Dolgozok:
#       if dolgozo is not None:
#         searchCB.addItem(f"{dolgozo.id}. {dolgozo.nev} - {dolgozo.sz_ido[0:10].replace('-','.')}")
for munkakor in Munkakorok:
       if munkakor is not None:
        JogvAdat.mkC.addItem(f"{munkakor.id}. {munkakor.nev}")
        beallitasok.mkCb.addItem(f"{munkakor.id}. {munkakor.nev}")
for program in Programok:
      if program is not None:
        JogvAdat.progC.addItem(f"{program.id}. {program.r_nev}")
        orvosi.progCB.addItem(f"{program.id}. {program.r_nev}")
        programok.progCB.addItem(f"{program.id}. {program.r_nev}")
        beallitasok.pgCb.addItem(f"{program.id}. {program.r_nev}")
for munkairanyito in Munkairanyitok:
      if munkairanyito is not None:
        JogvAdat.mirC.addItem(f"{munkairanyito.id}. {munkairanyito.nev}")
        munkairanyitok.munkCB.addItem(f"{munkairanyito.id}. {munkairanyito.nev}")
        beallitasok.miCb.addItem(f"{munkairanyito.id}. {munkairanyito.nev}")
def SelectedDolgozo(value):
    if searchCB.currentText() != '':
        id = searchCB.currentText().split('.')
        print(searchCB.currentText())
        id = int(id[0])
        
        SzemAdat.nameT.setText(window.Dolgozok[id].nev)
        SzemAdat.lnameT.setText(window.Dolgozok[id].l_nev)
        SzemAdat.anameT.setText(window.Dolgozok[id].a_nev)
        SzemAdat.szhT.setText(window.Dolgozok[id].sz_hely)
        y,m,d = window.Dolgozok[id].sz_ido[0:10].split('-')
        SzemAdat.sziD.setDate(QDate(int(y),int(m),int(d)))
        SzemAdat.adoT.setText(window.Dolgozok[id].ado_sz)
        SzemAdat.tajT.setText(window.Dolgozok[id].taj_sz)
        SzemAdat.cimT.setText(window.Dolgozok[id].cim)
        szamla = window.Dolgozok[id].szamla_sz.replace('-','').replace('8x0','00000000')
        if len(szamla) == 0:
                SzemAdat.szamlaT.setInputMask("")
        elif len(szamla) < 17:
            SzemAdat.szamlaT.setInputMask("99999999-99999999")
        else:
            SzemAdat.szamlaT.setInputMask("99999999-99999999-99999999")
        SzemAdat.szamlaT.setText(szamla)
        telefon = window.Dolgozok[id].tel_sz.replace("-","").replace("/","")
        SzemAdat.telT.setText(telefon)
        SzemAdat.szigT.setText(window.Dolgozok[id].szigsz)
        SzemAdat.tuzelo.setChecked(window.Dolgozok[id].tuzelo)
        y,m,d = window.Dolgozok[id].jog_k[0:10].split('-')
        JogvAdat.jkD.setDate(QDate(int(y),int(m),int(d)))
        y,m,d = window.Dolgozok[id].jog_v[0:10].split('-')
        JogvAdat.jvD.setDate(QDate(int(y),int(m),int(d)))
        JogvAdat.mkC.setCurrentIndex(window.Dolgozok[id].munkakor)
        JogvAdat.nettoT.setText(str(Munkakorok[window.Dolgozok[id].munkakor].netto))
        JogvAdat.progC.setCurrentIndex(window.Dolgozok[id].pid-1)
        JogvAdat.mirC.setCurrentIndex(window.Dolgozok[id].mir-1)
        JogvAdat.ugyT.setText(window.Dolgozok[id].ugyirat)
        y,m,d = window.Dolgozok[id].orvosi[0:10].split('-')
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
#region orvosi
def orvosiData(value):
    orvosi.oLabel.setText(f"Lejár {orvosi.oSlider.value()} napon belül")
    oData = []
    id = orvosi.progCB.currentText().split('.')
    id = int(id[0])
    newtime = today + timedelta(days=orvosi.oSlider.value())
    for dolgozo in window.Dolgozok:
        if dolgozo is not None and dolgozo.pid == id:
                y,m,d = dolgozo.orvosi[0:10].split('-')
                dolOrv = datetime.date(int(y),int(m),int(d))
                if dolOrv < newtime:
                    oData.append((dolgozo.id,dolgozo.nev,dolgozo.sz_hely,dolgozo.sz_ido[0:10],dolgozo.a_nev,dolgozo.cim,dolgozo.taj_sz.replace("-",""),dolgozo.orvosi[0:10].replace('-','.')))
    oData.append(("","","","","","","",""))
    model = orvosiTM(oData)
    orvosi.table.setModel(model)
orvosiData(1)
orvosi.progCB.currentIndexChanged.connect(orvosiData)
orvosi.oSlider.valueChanged.connect(orvosiData)

def programData(value):
      id = programok.progCB.currentText().split('.')
      id = int(id[0])
      progData = []
      for dolgozo in window.Dolgozok:
            if dolgozo is not None and dolgozo.pid == id:
                  progData.append((dolgozo.id,dolgozo.nev,dolgozo.sz_ido[0:10].replace('-','.'),dolgozo.taj_sz,dolgozo.ado_sz,dolgozo.jog_k[0:10].replace('-','.')))
      progData.append(("","","","","","","",""))
      model = progTM(progData)
      programok.table.setModel(model)
programok.progCB.currentIndexChanged.connect(programData)
programData(1)
tuzeloData = []
for dolgozo in window.Dolgozok:
    if dolgozo is not None and dolgozo.tuzelo == True:
            cim = dolgozo.cim.split(" ")
            hsz = cim[len(cim)-1].replace('.','')
            tuzeloData.append((dolgozo.id,dolgozo.nev,cim[0],hsz))
tuzeloData = sorted(tuzeloData, key = lambda x: (x[2], int(x[3])))
model = tuzeloTM(tuzeloData)
tuzelo.table.setModel(model)
def munkairanyitoData(value):
    id = munkairanyitok.munkCB.currentText().split('.')
    id = int(id[0])
    munkairData = []
    for dolgozo in window.Dolgozok:
          if dolgozo is not None and dolgozo.mir == id:
                munkairData.append((dolgozo.id, dolgozo.nev,dolgozo.sz_ido[0:10].replace('-','.'),dolgozo.taj_sz,dolgozo.jog_v[0:10].replace('-','.')))
    munkairData.append(("","","","",""))
    model = mirTM(munkairData)
    munkairanyitok.table.setModel(model)
munkairanyitok.munkCB.currentIndexChanged.connect(munkairanyitoData)
munkairanyitoData(1)
def setmk(value):
      id = beallitasok.mkCb.currentText().split(".")
      id = int(id[0])
      beallitasok.mknameT.setText(Munkakorok[id].nev)
      beallitasok.mkbrutT.setText(str(Munkakorok[id].brutto))
      beallitasok.mknetT.setText(str(Munkakorok[id].netto))
beallitasok.mkCb.currentIndexChanged.connect(setmk)

def setmi(value):
      id = beallitasok.miCb.currentText().split('.')
      id = int(id[0])
      beallitasok.minameT.setText(Munkairanyitok[id].nev)
beallitasok.miCb.currentIndexChanged.connect(setmi)

def setprog(value):
    id = beallitasok.pgCb.currentText().split('.')
    id = int(id[0])
    beallitasok.pghnevT.setText(Programok[id].h_nev)
    beallitasok.pgrnevT.setText(Programok[id].r_nev)
    beallitasok.pghatT.setText(Programok[id].hatosagi)
beallitasok.pgCb.currentIndexChanged.connect(setprog)
#endregion

app.exec_()

