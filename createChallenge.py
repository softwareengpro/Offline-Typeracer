# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'acceptChallenge.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(800, 600)
        self.createChallenge = QtGui.QPushButton(Form)
        self.createChallenge.setGeometry(QtCore.QRect(330, 370, 101, 27))
        self.createChallenge.setStyleSheet(_fromUtf8("color: rgb(0, 0, 49);"))
        self.createChallenge.setObjectName(_fromUtf8("createChallenge"))
        self.createLabel = QtGui.QLabel(Form)
        self.createLabel.setGeometry(QtCore.QRect(300, 200, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.createLabel.setFont(font)
        self.createLabel.setStyleSheet(_fromUtf8("color: rgb(0, 0, 184);"))
        self.createLabel.setObjectName(_fromUtf8("createLabel"))
        self.back = QtGui.QPushButton(Form)
        self.back.setGeometry(QtCore.QRect(20, 500, 85, 27))
        self.back.setStyleSheet(_fromUtf8("color: rgb(0, 0, 49);"))
        self.back.setObjectName(_fromUtf8("back"))
        # self.close = QtGui.QPushButton(Form)
        # self.close.setGeometry(QtCore.QRect(680, 510, 85, 27))
        # self.close.setStyleSheet(_fromUtf8("color: rgb(0, 0, 49);"))
        # self.close.setObjectName(_fromUtf8("close"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.createChallenge.setText(_translate("Form", "Create Challenge", None))
        self.createLabel.setText(_translate("Form", "Create challenge", None))
        self.back.setText(_translate("Form", "Back", None))
        #self.close.setText(_translate("Form", "Close", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

