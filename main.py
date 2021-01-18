#!/bin/python

import sys

from PySide2 import QtCore
from PySide2 import QtWidgets 
from PySide2 import QtGui

from PyQt5.QtWidgets import QApplication, QWidget


# the gui pthon file.
import appGui

# the password generator
import generator

text = None  #generator.generatePassword()
passwordLength = None

class qtWindow(appGui.Ui_Form, QtWidgets.QMainWindow):
	def __init__(self):
		super(qtWindow, self). __init__()
		self.setupUi(self)
		self.pushButton.clicked.connect(self.clickedGeneratePassword) # Event handling: Button clicked
		

	def clickedGeneratePassword(self):

		try:
			passwordLength = int(self.getPasswordLength(self))

		except:
			passwordLength = None

		if passwordLength != None:
			text = generator.generatePassword(passwordLength + 1)
			self.changePasswordOutput(self, text)
		
		else:
			text = generator.generatePassword()
			self.changePasswordOutput(self, text)
			

if __name__ == '__main__':
	
	app = QApplication(sys.argv)

	root = qtWindow()
	root.resize(400,400)
	root.show()

	sys.exit(app.exec_())