# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wordMap.ui'
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
        Form.setMinimumSize(QtCore.QSize(800, 0))
        Form.setAutoFillBackground(False)
        Form.setStyleSheet(_fromUtf8("background-color: rgb(85, 170, 127);"))
        self.Chose_topic = QtGui.QLabel(Form)
        self.Chose_topic.setGeometry(QtCore.QRect(320, 160, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Chose_topic.setFont(font)
        self.Chose_topic.setMouseTracking(False)
        self.Chose_topic.setStyleSheet(_fromUtf8("color: rgb(0, 0, 130);"))
        self.Chose_topic.setObjectName(_fromUtf8("Chose_topic"))
        self.paragraph = QtGui.QPushButton(Form)
        self.paragraph.setGeometry(QtCore.QRect(360, 250, 85, 27))
        self.paragraph.setStyleSheet(_fromUtf8("color: rgb(0, 0, 49);"))
        self.paragraph.setObjectName(_fromUtf8("paragraph"))
        self.news = QtGui.QPushButton(Form)
        self.news.setGeometry(QtCore.QRect(360, 350, 85, 27))
        self.news.setStyleSheet(_fromUtf8("color: rgb(0, 0, 49);"))
        self.news.setObjectName(_fromUtf8("news"))
        self.gk = QtGui.QPushButton(Form)
        self.gk.setGeometry(QtCore.QRect(360, 300, 85, 27))
        self.gk.setStyleSheet(_fromUtf8("color: rgb(0, 0, 49);"))
        self.gk.setObjectName(_fromUtf8("gk"))
        self.audio = QtGui.QPushButton(Form)
        self.audio.setGeometry(QtCore.QRect(360, 400, 85, 27))
        self.audio.setStyleSheet(_fromUtf8("color: rgb(0, 0, 49);"))
        self.audio.setObjectName(_fromUtf8("audio"))
        self.back = QtGui.QPushButton(Form)
        self.back.setGeometry(QtCore.QRect(60, 510, 51, 27))
        self.back.setStyleSheet(_fromUtf8("color: rgb(0, 0, 49);"))
        self.back.setObjectName(_fromUtf8("back"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.Chose_topic.setText(_translate("Form", "     Choose Topic", None))
        self.paragraph.setText(_translate("Form", "PARAGRAPH", None))
        self.news.setText(_translate("Form", "NEWS", None))
        self.gk.setText(_translate("Form", "GK", None))
        self.audio.setText(_translate("Form", "AUDIO", None))
        self.back.setText(_translate("Form", "Back", None))
        #self.close.setText(_translate("Form", "CLOSE", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

