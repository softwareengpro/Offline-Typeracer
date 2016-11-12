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
        self.chose_topic = QtGui.QLabel(Form)
        self.chose_topic.setGeometry(QtCore.QRect(320, 160, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.chose_topic.setFont(font)
        self.chose_topic.setMouseTracking(False)
        self.chose_topic.setStyleSheet(_fromUtf8("color: rgb(0, 0, 130);"))
        self.chose_topic.setObjectName(_fromUtf8("chose_topic"))
        self.Paragraph = QtGui.QPushButton(Form)
        self.Paragraph.setGeometry(QtCore.QRect(360, 250, 85, 27))
        self.Paragraph.setStyleSheet(_fromUtf8("color: rgb(0, 0, 49);"))
        self.Paragraph.setObjectName(_fromUtf8("paragraph"))
        self.News = QtGui.QPushButton(Form)
        self.News.setGeometry(QtCore.QRect(360, 350, 85, 27))
        self.News.setStyleSheet(_fromUtf8("color: rgb(0, 0, 49);"))
        self.News.setObjectName(_fromUtf8("news"))
        self.Gk = QtGui.QPushButton(Form)
        self.Gk.setGeometry(QtCore.QRect(360, 300, 85, 27))
        self.Gk.setStyleSheet(_fromUtf8("color: rgb(0, 0, 49);"))
        self.Gk.setObjectName(_fromUtf8("gk"))
        self.Back = QtGui.QPushButton(Form)
        self.Back.setGeometry(QtCore.QRect(60, 510, 51, 27))
        self.Back.setStyleSheet(_fromUtf8("color: rgb(0, 0, 49);"))
        self.Back.setObjectName(_fromUtf8("back"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.chose_topic.setText(_translate("Form", "     Choose Topic", None))
        self.Paragraph.setText(_translate("Form", "PARAGRAPH", None))
        self.News.setText(_translate("Form", "NEWS", None))
        self.Gk.setText(_translate("Form", "GK", None))
        self.Back.setText(_translate("Form", "Back", None))
        #self.close.setText(_translate("Form", "CLOSE", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
