from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import qdarktheme
import Components.tabs as tabs
import qtawesome as qta
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from Components.classes import *
from datetime import date
import Components.firebase as FB
import Components.functions as F


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args,**kwargs)
        self.setWindowTitle("Adatkezelő Alkalmazás")
        height = 825
        self.setGeometry(200,50,1165,height)
        self.setFixedSize(1165,height)
        self.setWindowIcon(QIcon('icon.ico'))
        qdarktheme.setup_theme("auto")
        self.tabs_widget= tabs.Tabs(self)
        self.setCentralWidget(self.tabs_widget)
        self.setStyleSheet('font-size: 10pt; font-family: Arial;')
        self.show()
        self.tabs_widget.tab1.buttonsF.newD.clicked.connect(self.newDolgozo)

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
        completer = CustomQCompleter(self.tabs_widget.tab1.searchCB)
        completer.setCompletionMode(QCompleter.PopupCompletion)
        completer.setModel(self.tabs_widget.tab1.searchCB.model())
        self.tabs_widget.tab1.searchCB.setCompleter(completer)

        
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