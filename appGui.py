# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui',
# licensing of 'app.ui' applies.
#
# Created: Sun Mar 29 23:44:24 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 351)
        Form.setMaximumSize(QtCore.QSize(400, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../assets/vbscript.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        #Form.setModal(False)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 381, 118))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setContentsMargins(7, 7, 7, 7)
        self.verticalLayout.setObjectName("verticalLayout")
        self.passLengthLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.passLengthLabel.setFont(font)
        self.passLengthLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.passLengthLabel.setObjectName("passLengthLabel")
        self.verticalLayout.addWidget(self.passLengthLabel)
        self.passLength = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.passLength.setMaximumSize(QtCore.QSize(1670, 50))
        self.passLength.setObjectName("passLength")
        self.verticalLayout.addWidget(self.passLength)
        self.verticalLayout.setStretch(1, 1)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 300, 361, 41))
        self.pushButton.setObjectName("pushButton")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(20, 150, 361, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.passwordLabel = QtWidgets.QLabel(Form)
        self.passwordLabel.setGeometry(QtCore.QRect(20, 180, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.passwordLabel.setWordWrap(True)
        self.passwordLabel.setObjectName("passwordLabel")
        self.password = QtWidgets.QLineEdit(Form)
        self.password.setGeometry(QtCore.QRect(20, 230, 361, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.password.setFont(font)
        self.password.setAlignment(QtCore.Qt.AlignCenter)
        self.password.setReadOnly(True)
        self.password.setObjectName("password")

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.passwordLabel.update)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Password Generator", None, -1))
        self.passLengthLabel.setText(QtWidgets.QApplication.translate("Form", "Put password length", None, -1))
        self.passLength.setPlaceholderText(QtWidgets.QApplication.translate("Form", "Put Text here...", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Form", "Generate Password", None, -1))
        self.passwordLabel.setText(QtWidgets.QApplication.translate("Form", "Password", None, -1))

    def changePasswordOutput(self, Form, text):
        self.password.setText(QtWidgets.QApplication.translate("Form", text, None, -1))  

    def getPasswordLength(self, Form):
        return self.passLength.toPlainText() # get value in edit text.