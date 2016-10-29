# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'timeMap.ui'
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
        self.timeMap = QtGui.QLabel(Form)
        self.timeMap.setGeometry(QtCore.QRect(320, 120, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.timeMap.setFont(font)
        self.timeMap.setObjectName(_fromUtf8("timeMap"))
        self.min1 = QtGui.QPushButton(Form)
        self.min1.setGeometry(QtCore.QRect(390, 210, 41, 27))
        self.min1.setObjectName(_fromUtf8("min1"))
        self.min2 = QtGui.QPushButton(Form)
        self.min2.setGeometry(QtCore.QRect(270, 300, 41, 27))
        self.min2.setObjectName(_fromUtf8("min2"))
        self.min3 = QtGui.QPushButton(Form)
        self.min3.setGeometry(QtCore.QRect(500, 300, 41, 27))
        self.min3.setObjectName(_fromUtf8("min3"))
        self.back = QtGui.QPushButton(Form)
        self.back.setGeometry(QtCore.QRect(60, 510, 51, 27))
        self.back.setObjectName(_fromUtf8("back"))
        self.close = QtGui.QPushButton(Form)
        self.close.setGeometry(QtCore.QRect(660, 510, 51, 27))
        self.close.setObjectName(_fromUtf8("close"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.timeMap.setText(_translate("Form", "  Choose Time Map", None))
        self.min1.setText(_translate("Form", "1 Min", None))
        self.min2.setText(_translate("Form", "2 Min", None))
        self.min3.setText(_translate("Form", "3 Min", None))
        self.back.setText(_translate("Form", "BACK", None))
        self.close.setText(_translate("Form", "CLOSE", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

