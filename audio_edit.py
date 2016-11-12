# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'audio_player.ui'
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

class Ui_Audio(object):
    def setupUi(self, Audio):
        Audio.setObjectName(_fromUtf8("Audio"))
        Audio.resize(580, 500)
        self.centralWidget = QtGui.QWidget(Audio)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))

        self.play = QtGui.QPushButton(self.centralWidget)
        self.play.setGeometry(QtCore.QRect(20, 60, 84, 41))
        self.play.setObjectName(_fromUtf8("play"))

        self.horizontalSlider = QtGui.QSlider(self.centralWidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(120, 70, 451, 20))
        self.horizontalSlider.setProperty("value", 24)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))

        self.audioTextEdit = QtGui.QTextEdit(self.centralWidget)
        self.audioTextEdit.setGeometry(QtCore.QRect(50, 190, 481, 131))
        self.audioTextEdit.setObjectName(_fromUtf8("audioTextEdit"))
        self.audioTextEdit.setReadOnly(True)

        self.type = QtGui.QLabel(self.centralWidget)
        self.type.setGeometry(QtCore.QRect(60, 160, 61, 16))
        self.type.setObjectName(_fromUtf8("type"))

        self.close = QtGui.QPushButton(self.centralWidget)
        self.close.setGeometry(QtCore.QRect(460, 400, 85, 27))
        self.close.setObjectName(_fromUtf8("close"))

        self.finish = QtGui.QPushButton(self.centralWidget)
        self.finish.setGeometry(QtCore.QRect(350, 400, 85, 27))
        self.finish.setObjectName(_fromUtf8("finish"))

        self.retranslateUi(Audio)
        QtCore.QMetaObject.connectSlotsByName(Audio)

    def retranslateUi(self, Audio):
        Audio.setWindowTitle(_translate("Audio", "Audio", None))
        self.play.setText(_translate("Audio", "Play", None))
        self.type.setText(_translate("Audio", "Type Here", None))
        self.close.setText(_translate("Audio", "Close", None))
        self.finish.setText(_translate("Audio", "Finish", None))
        #self.actionOpen.setText(_translate("Audio", "&Open", None))
        #self.actionQuit.setText(_translate("Audio", "&Quit", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Audio = QtGui.QMainWindow()
    ui = Ui_Audio()
    ui.setupUi(Audio)
    Audio.show()
    sys.exit(app.exec_())

