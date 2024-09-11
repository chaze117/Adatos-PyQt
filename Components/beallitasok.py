from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import qtawesome as qta
import qdarktheme

class Beallitasok(QWidget):
    def __init__(self, parent):
        super(QWidget,self).__init__(parent)
        self.layout = QGridLayout(self)
        self.nullFrame = QFrame()
        #region Munkakörök
        self.munkakorok = QGroupBox()
        self.munkakorok.setTitle("Munkakörök")
        self.munkakorok.setFixedSize(380,230)
        self.munkakorok.layout = QVBoxLayout()
        self.mkCb = QComboBox()
        self.munkakorok.layout.addWidget(self.mkCb)
        self.munkakorok.setLayout(self.munkakorok.layout)
        self.layout.addWidget(self.munkakorok,0,0)
        self.mkGrid = QFrame()
        self.mkGrid.layout = QGridLayout()
        self.mkGrid.setLayout(self.mkGrid.layout)
        self.mkGrid.setFixedSize(360,100)
        self.munkakorok.layout.addWidget(self.mkGrid)
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
        self.mkButGrid = QFrame()
        self.mkButGrid.layout = QGridLayout()
        self.mkButGrid.setLayout(self.mkButGrid.layout)
        self.mkButGrid.setFixedSize(195,65)
        self.munkakorok.layout.addWidget(self.mkButGrid)

        self.mknew = QPushButton(qta.icon('ei.plus'),"")
        self.mknew.setIconSize(QSize(40,40))
        self.mknew.setToolTip("Új munkakör")
        self.mkButGrid.layout.addWidget(self.mknew,0,0)

        self.mkedit = QPushButton(qta.icon('ei.pencil'),"")
        self.mkedit.setIconSize(QSize(40,40))
        self.mkedit.setToolTip("Munkakör szerkeszése")
        self.mkButGrid.layout.addWidget(self.mkedit,0,1)

        self.mkdel = QPushButton(qta.icon('fa.trash-o'),"")
        self.mkdel.setIconSize(QSize(40,40))
        self.mkdel.setToolTip("Munkakör törlése")
        self.mkButGrid.layout.addWidget(self.mkdel,0,2)
        #endregion
        #region Munkairányítók
        self.munkairanyitok = QGroupBox()
        self.munkairanyitok.setTitle("Munkairányítók")
        self.munkairanyitok.setFixedSize(380,160)
        self.munkairanyitok.layout = QVBoxLayout()
        self.miCb = QComboBox()
        self.munkairanyitok.layout.addWidget(self.miCb)
        self.munkairanyitok.setLayout(self.munkairanyitok.layout)
        self.layout.addWidget(self.munkairanyitok,1,0)
        self.miGrid = QFrame()
        self.miGrid.layout = QGridLayout()
        self.miGrid.setLayout(self.miGrid.layout)
        self.miGrid.setFixedSize(360,35)
        self.munkairanyitok.layout.addWidget(self.miGrid)
        self.minameL = QLabel("Megnevezés:")
        self.miGrid.layout.addWidget(self.minameL,0,0)
        self.minameT = QLineEdit()
        self.miGrid.layout.addWidget(self.minameT,0,1)
        self.miButGrid = QFrame()
        self.miButGrid.layout = QGridLayout()
        self.miButGrid.setLayout(self.miButGrid.layout)
        self.miButGrid.setFixedSize(195,65)
        self.munkairanyitok.layout.addWidget(self.miButGrid)

        self.minew = QPushButton(qta.icon('ei.plus'),"")
        self.minew.setIconSize(QSize(40,40))
        self.minew.setToolTip("Új munkairányító")
        self.miButGrid.layout.addWidget(self.minew,0,0)

        self.miedit = QPushButton(qta.icon('ei.pencil'),"")
        self.miedit.setIconSize(QSize(40,40))
        self.miedit.setToolTip("Munkairányító szerkeszése")
        self.miButGrid.layout.addWidget(self.miedit,0,1)

        self.midel = QPushButton(qta.icon('fa.trash-o'),"")
        self.midel.setIconSize(QSize(40,40))
        self.midel.setToolTip("Munkairányító törlése")
        self.miButGrid.layout.addWidget(self.midel,0,2)
        #endregion
        #region Programok
        self.programok = QGroupBox()
        self.programok.setTitle("Programok")
        self.programok.setFixedSize(380,250)
        self.programok.layout = QVBoxLayout()
        self.pgCb = QComboBox()
        self.programok.layout.addWidget(self.pgCb)
        self.programok.setLayout(self.programok.layout)
        self.layout.addWidget(self.programok,2,0)
        self.pgGrid = QFrame()
        self.pgGrid.layout = QGridLayout()
        self.pgGrid.setLayout(self.pgGrid.layout)
        self.pgGrid.setFixedSize(360,120)
        self.programok.layout.addWidget(self.pgGrid)
        self.pghnevL = QLabel("Hosszú név:")
        self.pgGrid.layout.addWidget(self.pghnevL,1,0)
        self.pghnevT = QLineEdit()
        self.pgGrid.layout.addWidget(self.pghnevT,1,1)
        self.pgrnevL = QLabel("Rövid név:")
        self.pgGrid.layout.addWidget(self.pgrnevL,2,0)
        self.pgrnevT = QLineEdit()
        self.pgGrid.layout.addWidget(self.pgrnevT,2,1)
        self.pghatL = QLabel("Hatósági:")
        self.pgGrid.layout.addWidget(self.pghatL,3,0)
        self.pghatT = QLineEdit()
        self.pgGrid.layout.addWidget(self.pghatT,3,1)
        self.pgButGrid = QFrame()
        self.pgButGrid.layout = QGridLayout()
        self.pgButGrid.setLayout(self.pgButGrid.layout)
        self.pgButGrid.setFixedSize(195,65)
        self.programok.layout.addWidget(self.pgButGrid)

        self.pgnew = QPushButton(qta.icon('ei.plus'),"")
        self.pgnew.setIconSize(QSize(40,40))
        self.pgnew.setToolTip("Új program")
        self.pgButGrid.layout.addWidget(self.pgnew,0,0)

        self.pgedit = QPushButton(qta.icon('ei.pencil'),"")
        self.pgedit.setIconSize(QSize(40,40))
        self.pgedit.setToolTip("Program szerkeszése")
        self.pgButGrid.layout.addWidget(self.pgedit,0,1)

        self.pgdel = QPushButton(qta.icon('fa.trash-o'),"")
        self.pgdel.setIconSize(QSize(40,40))
        self.pgdel.setToolTip("Program törlése")
        self.pgButGrid.layout.addWidget(self.pgdel,0,2)
        #endregion
        self.layout.addWidget(self.nullFrame,0,1)
