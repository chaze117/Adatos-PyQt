from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtWebEngineWidgets import *
from PyQt6.QtPrintSupport import *
import Components.tabs as tabs
import qtawesome as qta
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from Components.classes import *
from datetime import date
import Components.firebase as FB
import Components.functions as F
import pdfcreation.munkaltatoi as MIG
import locale
import os
import win32api
import time



class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args,**kwargs)
        locale.setlocale(locale.LC_ALL, '')
        self.setWindowTitle("Adatkezelő Alkalmazás")
        height = 825
        self.setGeometry(200,50,1165,height)
        self.setFixedSize(1165,height)
        self.setWindowIcon(QIcon('icon.ico'))

        self.tabs_widget= tabs.Tabs(self)
        self.setCentralWidget(self.tabs_widget)
        self.setStyleSheet('font-size: 10pt; font-family: Arial;')
        self.show()

        self.tabs_widget.tab1.buttonsF.newD.clicked.connect(self.newDolgozo)
        self.tabs_widget.tab1.buttonsF.editD.clicked.connect(lambda: F.modDolgozo(self))
        self.tabs_widget.tab1.buttonsF.delD.clicked.connect(lambda: F.delDolgozo(self))
        self.tabs_widget.tab1.buttonsF.mki.clicked.connect(self.MakeMig)

        self.tabs_widget.tab1.adoF.tab1.newCSJK.clicked.connect(self.newCSJK)
        self.tabs_widget.tab1.adoF.tab1.editCSJK.clicked.connect(lambda: F.modCSJK(self))
        self.tabs_widget.tab1.adoF.tab1.delCSJK.clicked.connect(lambda: F.delCSJK(self))
        self.tabs_widget.tab1.adoF.tab1.moveCSJK.clicked.connect(self.moveCSJK)

        self.tabs_widget.tab1.adoF.tab2.newNETAK.clicked.connect(self.newNETAK)
        self.tabs_widget.tab1.adoF.tab2.editNETAK.clicked.connect(lambda: F.modNETAK(self))
        self.tabs_widget.tab1.adoF.tab2.delNETAK.clicked.connect(lambda: F.delNETAK(self))

        self.tabs_widget.tab6.mknew.clicked.connect(self.newMunkakor)
        self.tabs_widget.tab6.mkedit.clicked.connect(lambda: F.modMunkakor(self))
        self.tabs_widget.tab6.mkdel.clicked.connect(lambda: F.delMunkakor(self))

        self.tabs_widget.tab6.minew.clicked.connect(self.newMunkairanyito)
        self.tabs_widget.tab6.miedit.clicked.connect(lambda: F.modMunkairanyito(self))
        self.tabs_widget.tab6.midel.clicked.connect(lambda: F.delMunkairanyito(self))

        self.tabs_widget.tab6.pgnew.clicked.connect(self.newProgram)
        self.tabs_widget.tab6.pgedit.clicked.connect(lambda: F.modProgram(self))
        self.tabs_widget.tab6.pgdel.clicked.connect(lambda: F.delProgram(self))

        self.Dolgozok = FB.getDolgozok()
        self.Gyerekek = FB.getGyerekek()
        self.Gyerekek_n = FB.getNGyerekek()
        self.Munkairanyitok = FB.getMunkairanyitok()
        self.Munkakorok = FB.getMunkakorok()
        self.Programok = FB.getProgramok()
        self.Szamlaszamok = FB.getSzamlaszamok()

        F.fillSearchCB(self)
        F.fillMunkakorCB(self)
        F.fillProgramCB(self)
        F.fillMunkairanyitoCB(self)
        F.fillTuzeloData(self,False)

        self.tabs_widget.tab1.searchCB.currentIndexChanged.connect(lambda: F.SelectedDolgozo(self))
        self.tabs_widget.tab1.adoF.tab1.CSJKCB.currentIndexChanged.connect(lambda: F.SelectedCSJK(self.tabs_widget.tab1.adoF.tab1.CSJKCB.currentIndex(),self))
        self.tabs_widget.tab1.adoF.tab2.NETAKCB.currentIndexChanged.connect(lambda: F.SelectedNETAK(self.tabs_widget.tab1.adoF.tab2.NETAKCB.currentIndex(),self))
        self.tabs_widget.tab2.progCB.currentIndexChanged.connect(lambda: F.fillOrvosiData(self))
        self.tabs_widget.tab2.oSlider.valueChanged.connect(lambda: F.fillOrvosiData(self))
        self.tabs_widget.tab3.progCB.currentIndexChanged.connect(lambda: F.fillProgramData(self))
        self.tabs_widget.tab4.refresh.clicked.connect(lambda: F.fillTuzeloData(self,True))
        self.tabs_widget.tab5.munkCB.currentIndexChanged.connect(lambda: F.FillMunkairanyitoData(self))
        self.tabs_widget.tab6.mkCb.currentIndexChanged.connect(lambda: F.settingsMunkakorok(self))
        self.tabs_widget.tab6.miCb.currentIndexChanged.connect(lambda: F.settingsMunkairanyitok(self))
        self.tabs_widget.tab6.pgCb.currentIndexChanged.connect(lambda: F.settingsProgramok(self))


        self.tabs_widget.tab1.searchCB.setInsertPolicy(QComboBox.NoInsert)




    def newDolgozo(self):
            self.dialog = NewDolgozo(parent=self)
            self.dialog.show()

    def newMunkakor(self):
         self.dialog = NewMunkakor(parent=self)
         self.dialog.show()

    def newMunkairanyito(self):
         self.dialog = NewMunkairanyito(parent=self)
         self.dialog.show()

    def newProgram(self):
        self.dialog = NewProgram(parent=self)
        self.dialog.show()

    def newCSJK(self):
        if self.tabs_widget.tab1.searchCB.currentText() != '':
            pid = self.tabs_widget.tab1.searchCB.currentText().split('.')
            pid=int(pid[0])
            self.dialog = NewCSJK(parent=self, pid=pid)
            self.dialog.show()

    def moveCSJK(self):
        if self.tabs_widget.tab1.adoF.tab1.CSJKCB.currentText() != '':
            id = self.tabs_widget.tab1.adoF.tab1.CSJKCB.currentText().split('.')
            id = int(id[0])
            if self.tabs_widget.tab1.searchCB.currentText() != '':
                pid = self.tabs_widget.tab1.searchCB.currentText().split('.')
                pid = int(pid[0])
            self.dialog = MoveCSJK(parent=self,id=id,pid=pid)
            self.dialog.show()

    def newNETAK(self):
      if self.tabs_widget.tab1.searchCB.currentText() != '':
            pid = self.tabs_widget.tab1.searchCB.currentText().split('.')
            pid=int(pid[0])
            self.dialog = NewNETAK(parent=self, pid=pid)
            self.dialog.show()

    def MakeMig(self):
        if self.tabs_widget.tab1.searchCB.currentIndex() > -1:
            id = self.tabs_widget.tab1.searchCB.currentText().split('.')
            szemAdatok = self.tabs_widget.tab1.szemadatF
            jogvAdatok = self.tabs_widget.tab1.jvF
            _c = szemAdatok.cimT.text().split(' ')
            cim = None
            x = None
            try:
                x = int(_c[0])
                cim = szemAdatok.cimT.text()
            except:
                cim = f"3931 Mezőzombor, {szemAdatok.cimT.text()}"
            MIG.generateMig([
                szemAdatok.nameT.text(),
                szemAdatok.szhT.text(),
                szemAdatok.sziD.date().toString("yyyy.MM.dd."),
                szemAdatok.anameT.text(),
                szemAdatok.adoT.text(),
                szemAdatok.tajT.text(),
                cim,
                f"{self.Munkakorok[self.Dolgozok[int(id[0])].munkakor].brutto:n} Ft/hó",
                f"{int(jogvAdatok.nettoT.text()):n} Ft/hó",
                jogvAdatok.jkD.date().toString("yyyy.MM.dd."),
                jogvAdatok.jvD.date().toString("yyyy.MM.dd."),
                ])
            self.dialog = PDFView(filename="mig.pdf")
            self.dialog.show()

class NewDolgozo(QMainWindow):
    def __init__(self, *args,parent=None, **kwargs):
        super(NewDolgozo,self).__init__(*args,parent,**kwargs)
        self.setWindowTitle("Új dolgozó")
        self.setWindowIcon(QIcon('icon.ico'))
        self.setFixedSize(500,500)
        self.MainFrame = QFrame()
        self.MainFrame.setStyleSheet('font: bold 10pt; font-family: Arial;')
        self.setCentralWidget(self.MainFrame)
        self.MainFrame.layout = QGridLayout()
        self.nameL = QLabel("Név:")
        self.MainFrame.layout.addWidget(self.nameL,0,0)
        self.nameT = QLineEdit()
        self.MainFrame.layout.addWidget(self.nameT,0,1)
        self.lnameL = QLabel("Lánykori Név:")
        self.MainFrame.layout.addWidget(self.lnameL,1,0)
        self.lnameT = QLineEdit()
        self.MainFrame.layout.addWidget(self.lnameT,1,1)
        self.anameL =QLabel("Anyja Neve:")
        self.MainFrame.layout.addWidget(self.anameL,2,0)
        self.anameT = QLineEdit()
        self.MainFrame.layout.addWidget(self.anameT,2,1)
        self.szhL = QLabel("Születési Hely:")
        self.MainFrame.layout.addWidget(self.szhL,3,0)
        self.szhT = QLineEdit()
        self.MainFrame.layout.addWidget(self.szhT,3,1)
        self.sziL =QLabel("Születési Idő:")
        self.MainFrame.layout.addWidget(self.sziL,4,0)
        self.sziD = QDateEdit(calendarPopup=True)
        self.MainFrame.layout.addWidget(self.sziD,4,1)
        self.adoL = QLabel("Adóazonosító:")
        self.MainFrame.layout.addWidget(self.adoL,5,0)
        self.adoT = QLineEdit()
        self.adoT.setInputMask("9999999999")
        self.MainFrame.layout.addWidget(self.adoT,5,1)
        self.tajL = QLabel("TAJ Szám:")
        self.MainFrame.layout.addWidget(self.tajL,6,0)
        self.tajT = QLineEdit()
        self.tajT.setInputMask("999-999-999")
        self.MainFrame.layout.addWidget(self.tajT,6,1)
        self.cimL = QLabel("Cím:")
        self.MainFrame.layout.addWidget(self.cimL,7,0)
        self.cimT = QLineEdit()
        self.MainFrame.layout.addWidget(self.cimT,7,1)
        self.szamlaL= QLabel("Számlaszám:")
        self.MainFrame.layout.addWidget(self.szamlaL,8,0)
        self.szamlaT = QLineEdit()
        self.szamlaT.setInputMask("99999999-99999999-9999999")
        self.MainFrame.layout.addWidget(self.szamlaT,8,1)
        self.telL = QLabel("Telefonszám:")
        self.MainFrame.layout.addWidget(self.telL,9,0)
        self.telT = QLineEdit()
        self.telT.setInputMask("+36/99-999-9999")
        self.MainFrame.layout.addWidget(self.telT,9,1)
        self.szigL = QLabel("Szem. Ig. Szám:")
        self.MainFrame.layout.addWidget(self.szigL,10,0)
        self.szigT = QLineEdit()
        self.szigT.setInputMask("999999>AA")
        self.MainFrame.layout.addWidget(self.szigT,10,1)
        self.tuzelo = QCheckBox("Tüzelő")
        self.MainFrame.layout.addWidget(self.tuzelo,11,1)
        self.newD = QPushButton(qta.icon('fa.floppy-o'),"")
        self.newD.setIconSize(QSize(40,40))
        self.newD.setFixedSize(50,50)
        self.newD.setToolTip("Hozzáadás")
        self.newD.clicked.connect(self.saveClicked)
        self.MainFrame.layout.addWidget(self.newD,11,0)
        self.MainFrame.setLayout(self.MainFrame.layout)

    def closeEvent(self, event):
            self.parent().Dolgozok = FB.getDolgozok()
            F.fillSearchCB(self.parent())
            event.accept()

    def saveClicked(self):
        today = date.today()
        ref = db.reference('dolgozok')
        _temp = ref.get()
        Dolgozok = []
        for i in range(0,len(_temp)):
            Dolgozok.append(Dolgozo.from_dict(_temp[i]))
        nextID = int(Dolgozok[len(Dolgozok)-1].id)+1
        dolgozo = Dolgozo(
            self.anameT.text(),
            self.adoT.text(),
            self.cimT.text(),
            nextID,
            str(today),
            str(today),
            self.lnameT.text(),
            1,
            0,
            self.nameT.text(),
            str(today),
            1,
            self.szhT.text(),
            self.sziD.date().toString("yyyy-MM-dd"),
            self.szamlaT.text().replace('-',''),
            self.szigT.text(),
            self.tajT.text().replace('-',''),
            self.telT.text().replace("+36","").replace("-","").replace("/",""),
            self.tuzelo.isChecked(),
            "")
        ref = db.reference(f"dolgozok/")
        d = json.loads(dolgozo.toJSON())
        ref.child(str(dolgozo.id)).set(d)
        self.close()

class NewMunkakor(QMainWindow):
    def __init__(self, *args,parent=None, **kwargs):
        super(NewMunkakor,self).__init__(*args,parent,**kwargs)
        self.setWindowTitle("Új Munkakör")
        self.setWindowIcon(QIcon('icon.ico'))
        self.setFixedSize(380,175)

        self.MainFrame = QFrame()
        self.MainFrame.setStyleSheet('font: bold 10pt; font-family: Arial;')
        self.setCentralWidget(self.MainFrame)
        self.MainFrame.layout = QVBoxLayout()
        self.MainFrame.setLayout(self.MainFrame.layout)

        self.mkGrid = QFrame()
        self.mkGrid.layout = QGridLayout()
        self.mkGrid.setLayout(self.mkGrid.layout)
        self.mkGrid.setFixedSize(360,150)
        self.MainFrame.layout.addWidget(self.mkGrid)

        self.mknameL = QLabel("Megnevezés:")
        self.mkGrid.layout.addWidget(self.mknameL,0,0)
        self.mknameT = QLineEdit()
        self.mkGrid.layout.addWidget(self.mknameT,0,1)

        self.mknetL = QLabel("Nettó:")
        self.mkGrid.layout.addWidget(self.mknetL,1,0)
        self.mknetT = QLineEdit()
        self.mkGrid.layout.addWidget(self.mknetT,1,1)

        self.mkbrutL = QLabel("Bruttó:")
        self.mkGrid.layout.addWidget(self.mkbrutL,2,0)
        self.mkbrutT = QLineEdit()
        self.mkGrid.layout.addWidget(self.mkbrutT,2,1)


        self.mknew = QPushButton(qta.icon('fa.floppy-o'),"")
        self.mknew.setIconSize(QSize(40,40))
        self.mknew.setFixedSize(50,50)
        self.mknew.setToolTip("Új munkakör")
        self.mkGrid.layout.addWidget(self.mknew,3,0)
        self.mknew.clicked.connect(self.saveClicked)

    def closeEvent(self,event):
        self.parent().Munkakorok = FB.getMunkakorok()
        F.fillMunkakorCB(self.parent())
        event.accept()

    def saveClicked(self):
        ref = db.reference("munkakorok")
        _temp = ref.get()
        Munkakorok = []
        for i in range(0,len(_temp)):
            Munkakorok.append(Munkakor.from_dict(_temp[i]))
        nextID = int(Munkakorok[len(Munkakorok)-1].id)+1
        munkakor = Munkakor(
             nextID,
             self.mknameT.text(),
             self.mkbrutT.text(),
             self.mknetT.text())
        m = json.loads(munkakor.toJSON())
        ref.child(str(munkakor.id)).set(m)
        self.close()

class NewMunkairanyito(QMainWindow):
    def __init__(self, *args, parent=None, **kwargs):
        super(NewMunkairanyito,self).__init__(*args,parent,**kwargs)
        self.setWindowTitle("Új Munkairányító")
        self.setWindowIcon(QIcon('icon.ico'))
        self.setFixedSize(380,110)

        self.MainFrame = QFrame()
        self.MainFrame.setStyleSheet('font: bold 10pt; font-family: Arial;')
        self.setCentralWidget(self.MainFrame)
        self.MainFrame.layout = QVBoxLayout()
        self.MainFrame.setLayout(self.MainFrame.layout)

        self.mkGrid = QFrame()
        self.mkGrid.layout = QGridLayout()
        self.mkGrid.setLayout(self.mkGrid.layout)
        self.mkGrid.setFixedSize(360,100)
        self.MainFrame.layout.addWidget(self.mkGrid)

        self.mknameL = QLabel("Megnevezés:")
        self.mkGrid.layout.addWidget(self.mknameL,0,0)
        self.mknameT = QLineEdit()
        self.mkGrid.layout.addWidget(self.mknameT,0,1)

        self.mknew = QPushButton(qta.icon('fa.floppy-o'),"")
        self.mknew.setIconSize(QSize(40,40))
        self.mknew.setFixedSize(50,50)
        self.mknew.setToolTip("Új munkairányító")
        self.mkGrid.layout.addWidget(self.mknew,1,0)
        self.mknew.clicked.connect(self.saveClicked)

    def closeEvent(self,event):
        self.parent().Munkairanyitok = FB.getMunkairanyitok()
        F.fillMunkairanyitoCB(self.parent())
        event.accept()

    def saveClicked(self):
        ref = db.reference("munkairanyitok")
        _temp = ref.get()
        Munkairanyitok = []
        for i in range(0,len(_temp)):
            Munkairanyitok.append(Munkairanyito.from_dict(_temp[i]))
        nextID = int(Munkairanyitok[len(Munkairanyitok)-1].id)+1
        munkairanyito = Munkairanyito(nextID,self.mknameT.text())
        m = json.loads(munkairanyito.toJSON())
        ref.child(str(munkairanyito.id)).set(m)
        self.close()

class NewProgram(QMainWindow):
    def __init__(self, *args, parent=None, **kwargs):
        super(NewProgram,self).__init__(*args,parent,**kwargs)
        self.setWindowTitle("Új Program")
        self.setWindowIcon(QIcon('icon.ico'))
        self.MainFrame = QFrame()
        self.setFixedSize(380,220)
        self.MainFrame.setStyleSheet('font: bold 10pt; font-family: Arial;')
        self.setCentralWidget(self.MainFrame)
        self.MainFrame.layout = QVBoxLayout()
        self.MainFrame.setLayout(self.MainFrame.layout)

        self.mkGrid = QFrame()
        self.mkGrid.layout = QGridLayout()
        self.mkGrid.setLayout(self.mkGrid.layout)
        self.mkGrid.setFixedSize(360,210)
        self.MainFrame.layout.addWidget(self.mkGrid)

        self.pghnevL = QLabel("Hosszú név:")
        self.mkGrid.layout.addWidget(self.pghnevL,1,0)
        self.pghnevT = QLineEdit()
        self.mkGrid.layout.addWidget(self.pghnevT,1,1)
        self.pgrnevL = QLabel("Rövid név:")
        self.mkGrid.layout.addWidget(self.pgrnevL,2,0)
        self.pgrnevT = QLineEdit()
        self.mkGrid.layout.addWidget(self.pgrnevT,2,1)
        self.pghatL = QLabel("Hatósági:")
        self.mkGrid.layout.addWidget(self.pghatL,3,0)
        self.pghatT = QLineEdit()
        self.mkGrid.layout.addWidget(self.pghatT,3,1)

        self.mknew = QPushButton(qta.icon('fa.floppy-o'),"")
        self.mknew.setIconSize(QSize(40,40))
        self.mknew.setFixedSize(50,50)
        self.mknew.setToolTip("Új program")
        self.mkGrid.layout.addWidget(self.mknew,4,0)
        self.mknew.clicked.connect(self.saveClicked)

    def closeEvent(self,event):
        self.parent().Programok = FB.getProgramok()
        F.fillProgramCB(self.parent())
        event.accept()

    def saveClicked(self):
        ref = db.reference("programok")
        _temp = ref.get()
        Programok = []
        for i in range(0,len(_temp)):
            Programok.append(Program.from_dict(_temp[i]))
        nextID = int(Programok[len(Programok)-1].id)+1
        program = Program(nextID,self.pgrnevT.text(),self.pghnevT.text(),self.pghatT.text())
        m = json.loads(program.toJSON())
        ref.child(str(program.id)).set(m)
        self.close()

class NewCSJK(QMainWindow):
    def __init__(self, *args,parent=None, pid=None,**kwargs):
        super(NewCSJK,self).__init__(*args,parent, **kwargs)
        self.setWindowTitle("Új Gyermek")
        self.setWindowIcon(QIcon('icon.ico'))
        self.MainFrame = QFrame()
        self.setFixedSize(380,300)
        self.MainFrame.setStyleSheet('font: bold 10pt; font-family: Arial;')
        self.setCentralWidget(self.MainFrame)
        self.MainFrame.layout = QVBoxLayout()
        self.MainFrame.setLayout(self.MainFrame.layout)
        self.Parent = parent
        self.pid = pid
        self.mkGrid = QFrame()
        self.mkGrid.layout = QGridLayout()
        self.mkGrid.setLayout(self.mkGrid.layout)
        self.mkGrid.setFixedSize(360,290)
        self.MainFrame.layout.addWidget(self.mkGrid)

        self.nameL = QLabel("Név:")
        self.mkGrid.layout.addWidget(self.nameL,0,0)
        self.nameT = QLineEdit()
        self.mkGrid.layout.addWidget(self.nameT,0,1)
        self.anevL = QLabel("Anyja Neve:")
        self.mkGrid.layout.addWidget(self.anevL,1,0)
        self.anevT = QLineEdit()
        self.mkGrid.layout.addWidget(self.anevT,1,1)
        self.szhL = QLabel("Születési Hely:")
        self.mkGrid.layout.addWidget(self.szhL,2,0)
        self.szhT = QLineEdit()
        self.mkGrid.layout.addWidget(self.szhT,2,1)
        self.sziL = QLabel("Születési Idő")
        self.mkGrid.layout.addWidget(self.sziL,3,0)
        self.sziD = QDateEdit(calendarPopup=True)
        self.mkGrid.layout.addWidget(self.sziD,3,1)
        self.adoL = QLabel("Adóazonosító:")
        self.mkGrid.layout.addWidget(self.adoL,4,0)
        self.adoT = QLineEdit()
        self.adoT.setInputMask("9999999999")
        self.mkGrid.layout.addWidget(self.adoT,4,1)
        self.tajL = QLabel("TAJ Szám:")
        self.mkGrid.layout.addWidget(self.tajL,5,0)
        self.tajT = QLineEdit()
        self.tajT.setInputMask("999-999-999")
        self.mkGrid.layout.addWidget(self.tajT,5,1)
        self.cimL = QLabel("Cím:")
        self.mkGrid.layout.addWidget(self.cimL,6,0)
        self.cimT = QLineEdit()
        self.mkGrid.layout.addWidget(self.cimT,6,1)

        self.mknew = QPushButton(qta.icon('fa.floppy-o'),"")
        self.mknew.setIconSize(QSize(40,40))
        self.mknew.setFixedSize(50,50)
        self.mknew.setToolTip("Új Gyermek")
        self.mkGrid.layout.addWidget(self.mknew,7,0)
        self.mknew.clicked.connect(self.saveClicked)

    def closeEvent(self, event):
        self.Parent.Gyerekek = FB.getGyerekek()
        F.fillCSJK(self.parent(), self.pid)
        event.accept()

    def saveClicked(self):
        ref = db.reference("gyerek")
        _temp = ref.get()
        Gyerekek = []
        for i in range(0,len(_temp)):
            Gyerekek.append(Gyerek.from_dict(_temp[i]))
        nextID = int(Gyerekek[len(Gyerekek)-1].id)+1
        gyerek = Gyerek(
            self.anevT.text(),
            self.adoT.text(),
            self.cimT.text(),
            nextID,
            self.nameT.text(),
            self.szhT.text(),
            self.pid,
            self.sziD.date().toString("yyyy-MM-dd"),
            self.tajT.text().replace("-","")
        )
        m = json.loads(gyerek.toJSON())
        ref.child(str(gyerek.id)).set(m)
        self.close()

class MoveCSJK(QMainWindow):
    def __init__(self, *args,parent=None, id=None, pid=None,**kwargs):
        super(MoveCSJK,self).__init__(*args,parent, **kwargs)
        self.id = id
        self.pid = pid
        self.setWindowTitle("Gyermek áthelyezése másik szülőhöz")
        self.setWindowIcon(QIcon('icon.ico'))
        self.MainFrame = QFrame()
        self.setFixedSize(380,100)
        self.MainFrame.setStyleSheet('font: bold 10pt; font-family: Arial;')
        self.setCentralWidget(self.MainFrame)
        self.MainFrame.layout = QVBoxLayout()
        self.MainFrame.setLayout(self.MainFrame.layout)

        self.dolgCB = QComboBox()
        self.MainFrame.layout.addWidget(self.dolgCB)
        for dolgozo in parent.Dolgozok:
            if dolgozo is not None:
                self.dolgCB.addItem(f"{dolgozo.id}. {dolgozo.nev} - {dolgozo.sz_ido[0:10].replace('-','.')}")
        self.moveCSJK = QPushButton(qta.icon('ri.user-shared-2-fill'),"")
        self.moveCSJK.setIconSize(QSize(40,40))
        self.moveCSJK.setFixedSize(50,50)
        self.moveCSJK.setToolTip("Gyermek áthelyezése másik szülőhöz")
        self.MainFrame.layout.addWidget(self.moveCSJK)
        self.moveCSJK.clicked.connect(self.moveClicked)

    def closeEvent(self, event):
        self.parent().Gyerekek = FB.getGyerekek()
        F.fillCSJK(self.parent(),self.pid)

    def moveClicked(self):
        sz_id = self.dolgCB.currentText().split('.')
        ref = db.reference("gyerek")
        ref.child(str(self.id)).update({"sz_id": sz_id[0]})
        self.close()

class NewNETAK(QMainWindow):
    def __init__(self, *args,parent=None, pid=None,**kwargs):
        super(NewNETAK,self).__init__(*args,parent, **kwargs)
        self.setWindowTitle("Új Gyermek")
        self.setWindowIcon(QIcon('icon.ico'))
        self.MainFrame = QFrame()
        self.setFixedSize(380,220)
        self.MainFrame.setStyleSheet('font: bold 10pt; font-family: Arial;')
        self.setCentralWidget(self.MainFrame)
        self.MainFrame.layout = QGridLayout()
        self.MainFrame.setLayout(self.MainFrame.layout)
        self.pid = pid
        self.Parent = parent
        self.nameL = QLabel("Név:")
        self.MainFrame.layout.addWidget(self.nameL,0,0)
        self.nameT = QLineEdit()
        self.MainFrame.layout.addWidget(self.nameT,0,1)
        self.anevL = QLabel("Anyja Neve:")
        self.MainFrame.layout.addWidget(self.anevL,1,0)
        self.anevT = QLineEdit()
        self.MainFrame.layout.addWidget(self.anevT,1,1)
        self.szhL = QLabel("Születési Hely:")
        self.MainFrame.layout.addWidget(self.szhL,2,0)
        self.szhT = QLineEdit()
        self.MainFrame.layout.addWidget(self.szhT,2,1)
        self.sziL = QLabel("Születési Idő")
        self.MainFrame.layout.addWidget(self.sziL,3,0)
        self.sziD = QDateEdit(calendarPopup=True)
        self.MainFrame.layout.addWidget(self.sziD,3,1)
        self.adoL = QLabel("Adóazonosító:")
        self.MainFrame.layout.addWidget(self.adoL,4,0)
        self.adoT = QLineEdit()
        self.adoT.setInputMask("9999999999")
        self.MainFrame.layout.addWidget(self.adoT,4,1)

        self.mknew = QPushButton(qta.icon('fa.floppy-o'),"")
        self.mknew.setIconSize(QSize(40,40))
        self.mknew.setFixedSize(50,50)
        self.mknew.setToolTip("Új Gyermek")
        self.MainFrame.layout.addWidget(self.mknew,5,0)
        self.mknew.clicked.connect(self.saveClicked)

    def closeEvent(self, event):
        self.Parent.Gyerekek_n = FB.getNGyerekek()
        F.fillNETAK(self.parent(), self.pid)
        event.accept()

    def saveClicked(self):
        ref = db.reference("gyerek_netak")
        _temp = ref.get()
        Gyerekek = []
        for i in range(0,len(_temp)):
            Gyerekek.append(Gyerek_NETAK.from_dict(_temp[i]))
        nextID = int(Gyerekek[len(Gyerekek)-1].id)+1
        gyerek = Gyerek_NETAK(
            self.anevT.text(),
            self.adoT.text(),
            nextID,
            self.nameT.text(),
            self.szhT.text(),
            self.pid,
            self.sziD.date().toString("yyyy-MM-dd")
        )
        m = json.loads(gyerek.toJSON())
        ref.child(str(gyerek.id)).set(m)
        self.close()

class PDFView(QMainWindow):
    def __init__(self, *args,filename=None, **kwargs):
        super(PDFView,self).__init__(*args, **kwargs)
        self.setWindowTitle(f"PDF Olvasó: {filename}")
        self.setWindowIcon(QIcon('icon.ico'))
        self.showMaximized()
        self.filename = filename
        layout = QVBoxLayout()
        self.web_view = QWebEngineView()
        self.settings = self.web_view.settings()
        self.settings.setAttribute(self.settings.WebAttribute.PluginsEnabled, True)
        self.settings.setAttribute(self.settings.WebAttribute.PdfViewerEnabled, True)
        self.settings.setAttribute(self.settings.WebAttribute.JavascriptCanOpenWindows, True)
        self.settings.setAttribute(self.settings.WebAttribute.PrintElementBackgrounds, True)
        self.web_view.page().printRequested.connect(self.handle_print_requested)
        layout.addWidget(self.web_view)
        self.container = QWidget()
        self.container.setLayout(layout)
        self.setCentralWidget(self.container)
        cwd = os.getcwd()
        self.fullpath = rf"{cwd}\{filename}"
        self.web_view.setUrl(QUrl.fromLocalFile(self.fullpath))

    def handle_print_requested(self):
        if not self.fullpath:
            print("No PDF file loaded for printing.")
            return
        self.show_print_dialog()
    
    def show_print_dialog(self):
        """Shows a print dialog and prints the file."""
        printer = QPrinter()
        dialog = QPrintDialog(printer, self)
        if dialog.exec() == QPrintDialog.DialogCode.Accepted:
            self.print_file_with_printer()
    
    def print_file_with_printer(self):
        if not os.path.exists(self.fullpath):
            print(f"File {self.fullpath} does not exist.")
            return
        try:
            win32api.ShellExecute(0, "print", self.fullpath, None, ".", 0)
        except:
            print("exeption")
        

    def closeEvent(self, event):
        os.remove(self.filename)
        event.accept()

