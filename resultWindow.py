# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resultWindow.ui'
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


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(800, 600)
        Dialog.setStyleSheet(_fromUtf8("background-color: rgb(85, 170, 127);\n"
""))
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(400, 390, 341, 32))
        self.buttonBox.setStyleSheet(_fromUtf8("color: rgb(0, 0, 49);"))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.yourScore = QtGui.QLabel(Dialog)
        self.yourScore.setGeometry(QtCore.QRect(340, 160, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.yourScore.setFont(font)
        self.yourScore.setStyleSheet(_fromUtf8("\n"
"color: rgb(0, 0, 49);"))
        self.yourScore.setObjectName(_fromUtf8("yourScore"))
        self.time = QtGui.QLabel(Dialog)
        self.time.setGeometry(QtCore.QRect(400, 220, 91, 21))
        self.time.setStyleSheet(_fromUtf8("color: rgb(0, 0, 49);"))
        self.time.setObjectName(_fromUtf8("time"))
        self.wpm = QtGui.QLabel(Dialog)
        self.wpm.setGeometry(QtCore.QRect(600, 220, 161, 20))
        self.wpm.setStyleSheet(_fromUtf8("color: rgb(0, 0, 49);"))
        self.wpm.setObjectName(_fromUtf8("wpm"))
        self.accuracy = QtGui.QLabel(Dialog)
        self.accuracy.setGeometry(QtCore.QRect(100, 220, 111, 20))
        self.accuracy.setStyleSheet(_fromUtf8("color: rgb(0, 0, 49);"))
        self.accuracy.setObjectName(_fromUtf8("accuracy"))
        self.userWPM = QtGui.QTextEdit(Dialog)
        self.userWPM.setGeometry(QtCore.QRect(620, 260, 104, 31))
        self.userWPM.setObjectName(_fromUtf8("userWPM"))
        self.typeTime = QtGui.QTextEdit(Dialog)
        self.typeTime.setGeometry(QtCore.QRect(400, 260, 104, 31))
        self.typeTime.setObjectName(_fromUtf8("typeTime"))
        self.userAccuracy = QtGui.QTextEdit(Dialog)
        self.userAccuracy.setGeometry(QtCore.QRect(120, 260, 104, 31))
        self.userAccuracy.setObjectName(_fromUtf8("userAccuracy"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.yourScore.setText(_translate("Dialog", "YOUR SCORE", None))
        self.time.setText(_translate("Dialog", "Time taken", None))
        self.wpm.setText(_translate("Dialog", "word per minute speed", None))
        self.accuracy.setText(_translate("Dialog", "     Accuracy", None))



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

