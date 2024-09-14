from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import qtawesome as qta
from Components.classes import *



class FoAdatok(QWidget):
    def __init__(self, parent):
        super(QWidget,self).__init__(parent)

        self.searchCB = ExtendedComboBox()

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.searchCB)
        self.setLayout(self.layout)

        self.MainFrame = QFrame()
        self.layout.addWidget(self.MainFrame)
        self.MainFrame.layout = QGridLayout()

        self.szemadatF = SzemelyiAdatok(self)
        self.szemadatF.setFixedSize(550,420)

        

        self.adoF = Adokedvezmenyek(self)
        self.adoF.setFixedSize(550,420)

        self.jvF = Jogviszony(self)
        self.jvF.setFixedSize(550,290)
        
        self.buttonsF = Buttons(self)
        self.buttonsF.setFixedSize(170,170)


        self.MainFrame.layout.addWidget(self.szemadatF,1,1)
        self.MainFrame.layout.addWidget(self.adoF,1,2)
        self.MainFrame.layout.addWidget(self.jvF,2,1)
        self.MainFrame.layout.addWidget(self.buttonsF,2,2)
        self.MainFrame.setLayout(self.MainFrame.layout)

class SzemelyiAdatok(QGroupBox):
    def __init__(self, parent):
        super(QGroupBox,self).__init__(parent)
        self.setTitle("Személyi Adatok")
        self.layout = QGridLayout(self)
        self.nameL = QLabel("Név:")
        self.layout.addWidget(self.nameL,1,0)
        self.nameT = QLineEdit()
        self.layout.addWidget(self.nameT,1,1)
        self.lnameL = QLabel("Lánykori Név:")
        self.layout.addWidget(self.lnameL,2,0)
        self.lnameT = QLineEdit()
        self.layout.addWidget(self.lnameT,2,1)
        self.anameL =QLabel("Anyja Neve:")
        self.layout.addWidget(self.anameL,3,0)
        self.anameT = QLineEdit()
        self.layout.addWidget(self.anameT,3,1)
        self.szhL = QLabel("Születési Hely:")
        self.layout.addWidget(self.szhL,4,0)
        self.szhT = QLineEdit()
        self.layout.addWidget(self.szhT,4,1)
        self.sziL =QLabel("Születési Idő:")
        self.layout.addWidget(self.sziL,5,0)
        self.sziD = QDateEdit(calendarPopup=True)
        self.layout.addWidget(self.sziD,5,1)
        self.adoL = QLabel("Adóazonosító:")
        self.layout.addWidget(self.adoL,6,0)
        self.adoT = QLineEdit()
        self.adoT.setInputMask("9999999999")
        self.layout.addWidget(self.adoT,6,1)
        self.tajL = QLabel("TAJ Szám:")
        self.layout.addWidget(self.tajL,7,0)
        self.tajT = QLineEdit()
        self.tajT.setInputMask("999-999-999")
        self.layout.addWidget(self.tajT,7,1)
        self.cimL = QLabel("Cím:")
        self.layout.addWidget(self.cimL,8,0)
        self.cimT = QLineEdit()
        self.layout.addWidget(self.cimT,8,1)
        self.szamlaL= QLabel("Számlaszám:")
        self.layout.addWidget(self.szamlaL,9,0)
        self.szamlaT = QLineEdit()
        self.szamlaT.setInputMask("99999999-99999999-9999999")
        self.layout.addWidget(self.szamlaT,9,1)
        self.telL = QLabel("Telefonszám:")
        self.layout.addWidget(self.telL,10,0)
        self.telT = QLineEdit()
        self.telT.setInputMask("+36/99-999-9999")
        self.layout.addWidget(self.telT,10,1)
        self.szigL = QLabel("Szem. Ig. Szám:")
        self.layout.addWidget(self.szigL,11,0)
        self.szigT = QLineEdit()
        self.szigT.setInputMask("999999>AA")
        self.layout.addWidget(self.szigT,11,1)
        self.tuzelo = QCheckBox("Tüzelő")
        self.layout.addWidget(self.tuzelo,12,1)
        
        self.setLayout(self.layout)
    
class Adokedvezmenyek(QGroupBox):
    def __init__(self, parent):
        super(QGroupBox,self).__init__(parent)
        self.setTitle("Adókedvezmények")
        self.layout = QVBoxLayout(self)
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = CSJK(self)
        self.tab2 = NETAK(self)      
        # Add tabs
        self.tabs.addTab(self.tab1,"CSJK")
        self.tabs.addTab(self.tab2,"NÉTAK")    
        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

class CSJK(QFrame):
    def __init__(self,parent):
        super(QFrame,self).__init__(parent)

        self.CSJKCB = QComboBox()
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.CSJKCB)
        self.setLayout(self.layout)
        
        self.CSJKFrame = QFrame()
        self.layout.addWidget(self.CSJKFrame)
        self.CSJKFrame.layout = QGridLayout()

        self.nameL = QLabel("Név:")
        self.CSJKFrame.layout.addWidget(self.nameL,0,0)
        self.nameT = QLineEdit()
        self.CSJKFrame.layout.addWidget(self.nameT,0,1)
        self.anevL = QLabel("Anyja Neve:")
        self.CSJKFrame.layout.addWidget(self.anevL,1,0)
        self.anevT = QLineEdit()
        self.CSJKFrame.layout.addWidget(self.anevT,1,1)
        self.szhL = QLabel("Születési Hely:")
        self.CSJKFrame.layout.addWidget(self.szhL,2,0)
        self.szhT = QLineEdit()
        self.CSJKFrame.layout.addWidget(self.szhT,2,1)
        self.sziL = QLabel("Születési Idő")
        self.CSJKFrame.layout.addWidget(self.sziL,3,0)
        self.sziD = QDateEdit(calendarPopup=True)
        self.CSJKFrame.layout.addWidget(self.sziD,3,1)
        self.adoL = QLabel("Adóazonosító:")
        self.CSJKFrame.layout.addWidget(self.adoL,4,0)
        self.adoT = QLineEdit()
        self.adoT.setInputMask("9999999999")
        self.CSJKFrame.layout.addWidget(self.adoT,4,1)
        self.tajL = QLabel("TAJ Szám:")
        self.CSJKFrame.layout.addWidget(self.tajL,5,0)
        self.tajT = QLineEdit()
        self.tajT.setInputMask("999-999-999")
        self.CSJKFrame.layout.addWidget(self.tajT,5,1)
        self.cimL = QLabel("Cím:")
        self.CSJKFrame.layout.addWidget(self.cimL,6,0)
        self.cimT = QLineEdit()
        self.CSJKFrame.layout.addWidget(self.cimT,6,1)
        
        self.buttonFrame = QFrame()
        self.buttonFrame.layout = QGridLayout()
        self.buttonFrame.setFixedSize(270,60)
        self.layout.addWidget(self.buttonFrame)

        self.newCSJK = QPushButton(qta.icon('fa.user-plus'),"")
        self.newCSJK.setIconSize(QSize(40,40))
        self.newCSJK.setFixedSize(50,50)
        self.newCSJK.setToolTip("Új gyermek")
        self.buttonFrame.layout.addWidget(self.newCSJK,0,0)

        self.editCSJK = QPushButton(qta.icon('fa5s.user-edit'),"")
        self.editCSJK.setIconSize(QSize(40,40))
        self.editCSJK.setFixedSize(50,50)
        self.editCSJK.setToolTip("Gyermek szerkesztése")
        self.buttonFrame.layout.addWidget(self.editCSJK,0,1)

        self.delCSJK = QPushButton(qta.icon('fa5s.user-minus'),"")
        self.delCSJK.setIconSize(QSize(40,40))
        self.delCSJK.setFixedSize(50,50)
        self.delCSJK.setToolTip("Gyermek törlése")
        self.buttonFrame.layout.addWidget(self.delCSJK,0,2)

        self.moveCSJK = QPushButton(qta.icon('ri.user-shared-2-fill'),"")
        self.moveCSJK.setIconSize(QSize(40,40))
        self.moveCSJK.setFixedSize(50,50)
        self.moveCSJK.setToolTip("Gyermek áthelyezése másik szülőhöz")
        self.buttonFrame.layout.addWidget(self.moveCSJK,0,3)

        self.printCSJK = QPushButton(qta.icon('fa.print'),"")
        self.printCSJK.setIconSize(QSize(40,40))
        self.printCSJK.setFixedSize(50,50)
        self.printCSJK.setToolTip("Nyomtatás")
        self.buttonFrame.layout.addWidget(self.printCSJK,0,4)


        self.buttonFrame.setLayout(self.buttonFrame.layout)
        self.CSJKFrame.setLayout(self.CSJKFrame.layout)
        
class NETAK(QFrame):
    def __init__(self,parent):
        super(QFrame,self).__init__(parent)

        self.NETAKCB = QComboBox()
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.NETAKCB)
        self.setLayout(self.layout)
        
        self.NETAKFrame = QFrame()
        self.layout.addWidget(self.NETAKFrame)
        self.NETAKFrame.layout = QGridLayout()

        self.nameL = QLabel("Név:")
        self.NETAKFrame.layout.addWidget(self.nameL,0,0)
        self.nameT = QLineEdit()
        self.NETAKFrame.layout.addWidget(self.nameT,0,1)
        self.anevL = QLabel("Anyja Neve:")
        self.NETAKFrame.layout.addWidget(self.anevL,1,0)
        self.anevT = QLineEdit()
        self.NETAKFrame.layout.addWidget(self.anevT,1,1)
        self.szhL = QLabel("Születési Hely:")
        self.NETAKFrame.layout.addWidget(self.szhL,2,0)
        self.szhT = QLineEdit()
        self.NETAKFrame.layout.addWidget(self.szhT,2,1)
        self.sziL = QLabel("Születési Idő")
        self.NETAKFrame.layout.addWidget(self.sziL,3,0)
        self.sziD = QDateEdit(calendarPopup=True)
        self.NETAKFrame.layout.addWidget(self.sziD,3,1)
        self.adoL = QLabel("Adóazonosító:")
        self.NETAKFrame.layout.addWidget(self.adoL,4,0)
        self.adoT = QLineEdit()
        self.adoT.setInputMask("9999999999")
        self.NETAKFrame.layout.addWidget(self.adoT,4,1)

        
        self.buttonFrame = QFrame()
        self.buttonFrame.layout = QGridLayout()
        self.buttonFrame.setFixedSize(220,60)
        self.layout.addWidget(self.buttonFrame)


        self.newNETAK = QPushButton(qta.icon('fa.user-plus'),"")
        self.newNETAK.setIconSize(QSize(40,40))
        self.newNETAK.setFixedSize(50,50)
        self.newNETAK.setToolTip("Új gyermek")
        self.buttonFrame.layout.addWidget(self.newNETAK,0,0)

        self.editNETAK = QPushButton(qta.icon('fa5s.user-edit'),"")
        self.editNETAK.setIconSize(QSize(40,40))
        self.editNETAK.setFixedSize(50,50)
        self.editNETAK.setToolTip("Gyermek szerkesztése")
        self.buttonFrame.layout.addWidget(self.editNETAK,0,1)

        self.delNETAK = QPushButton(qta.icon('fa5s.user-minus'),"")
        self.delNETAK.setIconSize(QSize(40,40))
        self.delNETAK.setFixedSize(50,50)
        self.delNETAK.setToolTip("Gyermek törlése")
        self.buttonFrame.layout.addWidget(self.delNETAK,0,2)


        self.printNETAK = QPushButton(qta.icon('fa.print'),"")
        self.printNETAK.setIconSize(QSize(40,40))
        self.printNETAK.setFixedSize(50,50)
        self.printNETAK.setToolTip("Nyomtatás")
        self.buttonFrame.layout.addWidget(self.printNETAK,0,3)


        self.buttonFrame.setLayout(self.buttonFrame.layout)
        self.NETAKFrame.setLayout(self.NETAKFrame.layout)
        
class Jogviszony(QGroupBox):
    def __init__(self, parent):
        super(QGroupBox,self).__init__(parent)
        self.setTitle("Jogviszonyhoz tartozó adatok")
        self.layout = QGridLayout(self)
        self.jkL = QLabel("Jogviszony kezdete:")
        self.layout.addWidget(self.jkL,1,0)
        self.jkD = QDateEdit(calendarPopup=True)
        self.layout.addWidget(self.jkD,1,1)

        self.jvL = QLabel("Jogviszony Vége:")
        self.layout.addWidget(self.jvL,2,0)
        self.jvD = QDateEdit(calendarPopup=True)
        self.layout.addWidget(self.jvD,2,1)

        self.nettoL = QLabel("Nettó Fizetés:")
        self.layout.addWidget(self.nettoL,3,0)
        self.nettoT = QLineEdit()
        self.layout.addWidget(self.nettoT,3,1)

        self.progL = QLabel("Program:")
        self.layout.addWidget(self.progL,4,0)
        self.progC = QComboBox()
        self.layout.addWidget(self.progC,4,1)

        self.mirL = QLabel("Munkairányító:")
        self.layout.addWidget(self.mirL,5,0)
        self.mirC = QComboBox()
        self.layout.addWidget(self.mirC,5,1)

        self.ugyL = QLabel("Ügyirat:")
        self.layout.addWidget(self.ugyL,6,0)
        self.ugyT = QLineEdit()
        self.layout.addWidget(self.ugyT,6,1)

        self.orvosiL = QLabel("Orvosi:")
        self.layout.addWidget(self.orvosiL,7,0)
        self.orvosiT = QDateEdit(calendarPopup=True)
        self.layout.addWidget(self.orvosiT,7,1)

        self.mkL = QLabel("Mukakör:")
        self.layout.addWidget(self.mkL,8,0)
        self.mkC = QComboBox()
        self.layout.addWidget(self.mkC,8,1)

        self.setLayout(self.layout)

class Buttons(QFrame):
    def __init__(self, parent):
        super(QFrame,self).__init__(parent)
        self.layout = QGridLayout(self)
        self.newD = QPushButton(qta.icon('fa.user-plus'),"")
        self.newD.setIconSize(QSize(40,40))
        self.newD.setFixedSize(50,50)
        self.newD.setToolTip("Új dolgozó")
        self.layout.addWidget(self.newD,0,0)

        self.editD = QPushButton(qta.icon('fa5s.user-edit'),"")
        self.editD.setIconSize(QSize(40,40))
        self.editD.setFixedSize(50,50)
        self.editD.setToolTip("Dolgozó szerkesztése")
        self.layout.addWidget(self.editD,0,1)

        self.delD = QPushButton(qta.icon('fa5s.user-minus'),"")
        self.delD.setIconSize(QSize(40,40))
        self.delD.setFixedSize(50,50)
        self.delD.setToolTip("Dolgozó törlése")
        self.layout.addWidget(self.delD,0,2)

        self.szamla = QPushButton(qta.icon('fa5s.file-invoice-dollar'),"")
        self.szamla.setIconSize(QSize(40,40))
        self.szamla.setFixedSize(50,50)
        self.szamla.setToolTip("Számlaszám")
        self.layout.addWidget(self.szamla,1,0)

        self.biz = QPushButton(qta.icon('fa.file-text'),"")
        self.biz.setIconSize(QSize(40,40))
        self.biz.setFixedSize(50,50)
        self.biz.setToolTip("Bizonyítvány")
        self.layout.addWidget(self.biz,1,1)

        self.tp = QPushButton(qta.icon('fa5s.file-medical'),"")
        self.tp.setIconSize(QSize(40,40))
        self.tp.setFixedSize(50,50)
        self.tp.setToolTip("Táppénz")
        self.layout.addWidget(self.tp,1,2)

        self.mk = QPushButton(qta.icon('fa5s.users-cog'),"")
        self.mk.setIconSize(QSize(40,40))
        self.mk.setFixedSize(50,50)
        self.mk.setToolTip("Munkaköri leírás")
        self.layout.addWidget(self.mk,2,0)

        self.mki = QPushButton(qta.icon('fa5s.money-bill-wave'),"")
        self.mki.setIconSize(QSize(40,40))
        self.mki.setFixedSize(50,50)
        self.mki.setToolTip("Munkáltatói igazolás")
        self.layout.addWidget(self.mki,2,1)

        self.onk = QPushButton(qta.icon('fa5s.hand-holding-heart'),"")
        self.onk.setIconSize(QSize(40,40))
        self.onk.setFixedSize(50,50)
        self.onk.setToolTip("Önkéntes munka")
        self.layout.addWidget(self.onk,2,2)

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

        pattern = QRegularExpression(self.local_completion_prefix,
                                Qt.CaseInsensitive,
                                QRegularExpression.FixedString)

        self.filterProxyModel.setFilterRegExp(pattern)

    def splitPath(self, path):
        self.local_completion_prefix = path
        self.updateModel()
        if self.filterProxyModel.rowCount() == 0:
            self.usingOriginalModel = False
            self.filterProxyModel.setSourceModel(QStringListModel([path]))
            return [path]

        return []

class AutoCompleteComboBox(QComboBox):
    def __init__(self, *args, **kwargs):
        super(AutoCompleteComboBox, self).__init__(*args, **kwargs)

        self.setEditable(True)
        self.setInsertPolicy(self.NoInsert)

        self.comp = CustomQCompleter(self)
        self.comp.setCompletionMode(QCompleter.PopupCompletion)
        self.setCompleter(self.comp)#
        self.setModel(["Lola", "Lila", "Cola", 'Lothian'])

    def setModel(self, strList):
        self.clear()
        self.insertItems(0, strList)
        self.comp.setModel(self.model())

    def focusInEvent(self, event):
        self.clearEditText()
        super(AutoCompleteComboBox, self).focusInEvent(event)

    def keyPressEvent(self, event):
        key = event.key()
        if key == 16777220:
            # Enter (if event.key() == Qt.Key_Enter) does not work
            # for some reason

            # make sure that the completer does not set the
            # currentText of the combobox to "" when pressing enter
            text = self.currentText()
            self.setCompleter(None)
            self.setEditText(text)
            self.setCompleter(self.comp)

        return super(AutoCompleteComboBox, self).keyPressEvent(event)