# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Practice.ui'
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
        Form.resize(709, 558)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(170, 280, 50, 14))
        self.label.setObjectName(_fromUtf8("label"))

        self.showPara = QtGui.QTextEdit(Form)
        self.st = "Anil"
        self.showPara.setText(self.st)
        self.showPara.setGeometry(QtCore.QRect(170, 130, 371, 121))
        self.showPara.setObjectName(_fromUtf8("showPara"))
        self.showPara.setReadOnly(True)


        self.editPara = QtGui.QTextEdit(Form)
        self.editPara.setGeometry(QtCore.QRect(170, 300, 371, 121))
        self.editPara.setObjectName(_fromUtf8("editPara"))
        self.editPara.textChanged.connect(self.text_changed)
        #self.editPara.textCursor().insertHtml('normal text')
        #self.editPara.setReadOnly(True)
        #self.mytext = self.editPara.toPlainText()
        #QString *mytext = self.editPara->toPlainText();
        #print self.mytext
        #self.editPara.setReadOnly(False)
        #self.editPara.textCursor().insertHtml('<b></b>')

        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(170, 110, 81, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.finish = QtGui.QPushButton(Form)
        self.finish.setGeometry(QtCore.QRect(490, 510, 51, 27))
        self.finish.setObjectName(_fromUtf8("finish"))

        self.Cancel = QtGui.QPushButton(Form)
        self.Cancel.setGeometry(QtCore.QRect(570, 510, 51, 27))
        self.Cancel.setObjectName(_fromUtf8("Cancel"))
        self.Cancel.clicked.connect(self.closeApp)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Type Here", None))
        self.label_2.setText(_translate("Form", "Your Paragraph", None))
        self.finish.setText(_translate("Form", "Finish", None))
        self.Cancel.setText(_translate("Form", "Cancel", None))

    def text_changed(self):
        self.editPara.setReadOnly(True)
        mytext = self.editPara.toPlainText()
        l = len(mytext)
        print l
        print self.st[0:l]
        if mytext == self.st[0:l]:
            print "match"
            #self.editPara.textCursor().insertHtml('<b>mytext</b>')
        #print mytext
        else:
            self.editPara.setTextColor(GlobalColor('255,0,0'));

        self.editPara.setReadOnly(False)

    def closeApp(self):
        print "Cancel pressed"
        app.exit()



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

