# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Test.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Test(object):
    def setupUi(self, Test):
        Test.setObjectName("Test")
        Test.resize(311, 122)
        self.buttonBox = QtWidgets.QDialogButtonBox(Test)
        self.buttonBox.setGeometry(QtCore.QRect(0, 80, 291, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Test)
        self.label.setGeometry(QtCore.QRect(80, 10, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Test)
        self.textEdit.setGeometry(QtCore.QRect(80, 40, 151, 31))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(Test)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Test)
        self.buttonBox.accepted.connect(Test.accept)
        self.buttonBox.rejected.connect(Test.reject)
        QtCore.QMetaObject.connectSlotsByName(Test)

    def retranslateUi(self, Test):
        _translate = QtCore.QCoreApplication.translate
        Test.setWindowTitle(_translate("Test", "Test"))
        self.label.setText(_translate("Test", "Bienvenu dans le jeux"))
        self.label_2.setText(_translate("Test", "Nick:"))


app = QtGui.QGuiApplication(sys.argv)
window = Ui_Test()
