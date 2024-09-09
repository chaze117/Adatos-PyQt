import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.resize(476, 308)
		self.centralwidget = QtWidgets.QWidget(MainWindow)

		# Languages are not selected initially hence initialised to zero.
		self.langs ={'c':0, 'cpp':0, 'java':0, 'python':0}
		
		# For showing message 
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(140, 80, 191, 20))
		
		self.checkBox_c = QtWidgets.QCheckBox(self.centralwidget)
		self.checkBox_c.setGeometry(QtCore.QRect(170, 120, 81, 20))
		self.checkBox_c.stateChanged.connect(self.checkedc)
		
		self.checkBox_cpp = QtWidgets.QCheckBox(self.centralwidget)
		self.checkBox_cpp.setGeometry(QtCore.QRect(170, 140, 81, 20))
		self.checkBox_cpp.stateChanged.connect(self.checkedcpp)
		
		self.checkBox_java = QtWidgets.QCheckBox(self.centralwidget)
		self.checkBox_java.setGeometry(QtCore.QRect(170, 160, 81, 20))
		self.checkBox_java.stateChanged.connect(self.checkedjava)
		
		self.checkBox_py = QtWidgets.QCheckBox(self.centralwidget)
		self.checkBox_py.setGeometry(QtCore.QRect(170, 180, 81, 20))
		self.checkBox_py.stateChanged.connect(self.checkedpy)
		
		MainWindow.setCentralWidget(self.centralwidget)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
		
	def checkedc(self, checked):
		if checked:
			self.langs['c']= 1
		else:
			self.langs['c']= 0
		self.show()

	def checkedcpp(self, checked):
		if checked:
			self.langs['cpp']= 1
		else:
			self.langs['cpp']= 0
		self.show()
			
	def checkedjava(self, checked):
		if checked:
			self.langs['java']= 1
		else:
			self.langs['java']= 0
		self.show()
			
	def checkedpy(self, checked):
		if checked:
			self.langs['python']= 1
		else:
			self.langs['python']= 0
		self.show()		 
	
	# For showing updated list of all selected languages.		 
	def show(self):
		checkedlangs =', '.join([key for key in self.langs.keys()
										if self.langs[key]== 1]) 
		
		# Updates message having list of all selected languages. 
		self.label.setText("You know "+checkedlangs)
	
		
	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

		self.label.setText(_translate("MainWindow", "Select your preferred language"))
		self.checkBox_c.setText(_translate("MainWindow", "C"))
		self.checkBox_cpp.setText(_translate("MainWindow", "C++"))
		self.checkBox_java.setText(_translate("MainWindow", "Java"))
		self.checkBox_py.setText(_translate("MainWindow", "Python"))

if __name__ == "__main__": 
	app = QtWidgets.QApplication(sys.argv) 

	MainWindow = QtWidgets.QMainWindow() 
	ui = Ui_MainWindow() 
	ui.setupUi(MainWindow) 
	MainWindow.show() 
	sys.exit(app.exec_()) 
