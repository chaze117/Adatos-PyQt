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


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args,**kwargs)
        self.setWindowTitle("Adatkezelő Alaklmazás")
        height = 825
        self.setGeometry(200,50,1165,height)
        self.setFixedSize(1165,height)
        self.setWindowIcon(QIcon('icon.ico'))
        qdarktheme.setup_theme("auto")
        self.tabs_widget= tabs.Tabs(self)
        self.setCentralWidget(self.tabs_widget)
        self.setStyleSheet('font-size: 10pt; font-family: Arial;')
        self.show()
        self.szemButtons = self.tabs_widget.tab1.buttonsF
        self.szemButtons.newD.clicked.connect(self.newDolgozo)
        self.Dolgozok = []
        self.Dolgozok = FB.getDolgozok()
        FB.fillSearchCB(self.Dolgozok, self.tabs_widget.tab1.searchCB)

        
    def newDolgozo(self):
            self.dialog = NewDolgozo(parent=self)
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
            FB.fillSearchCB(self.parent().Dolgozok, self.parent().tabs_widget.tab1.searchCB)
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

        


        
        