# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'usernameWindow.ui'
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
        Form.resize(400, 300)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(150, 80, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        self.username = QtGui.QLineEdit(Form)
        self.username.setGeometry(QtCore.QRect(120, 140, 161, 24))
        self.username.setObjectName(_fromUtf8("username"))

        self.ok = QtGui.QPushButton(Form)
        self.ok.setGeometry(QtCore.QRect(294, 240, 61, 27))
        self.ok.setObjectName(_fromUtf8("ok"))

        self.cancel = QtGui.QPushButton(Form)
        self.cancel.setGeometry(QtCore.QRect(40, 240, 61, 27))
        self.cancel.setObjectName(_fromUtf8("cancel"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "ENTER YOUR NAME", None))
        self.label.setText(_translate("Form", "Enter your name", None))
        self.ok.setText(_translate("Form", "OK", None))
        self.cancel.setText(_translate("Form", "CANCEL", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

