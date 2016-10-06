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

        self.finish_para = 0

        #Add progress bar
        self.progressBar = QtGui.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(230, 40, 118, 23))
        self.progressBar.setMinimumSize(QtCore.QSize(118, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(5)

        #Add text box
        self.timeToStart = QtGui.QTextEdit(Form)
        self.timeToStart.setGeometry(QtCore.QRect(80, 40, 111, 31))
        self.timeToStart.setObjectName(_fromUtf8("timeToStart"))
        self.timeToStart.setReadOnly(True)
        self.timeToStart.setText(" Start in ")

        # Add show text paragraph
        self.showPara = QtGui.QTextEdit(Form)
        self.st = "Anil kumar"
        self.showPara.setText(self.st)
        self.showPara.setGeometry(QtCore.QRect(170, 130, 371, 121))
        self.showPara.setObjectName(_fromUtf8("showPara"))
        self.showPara.setReadOnly(True)

        # Add Edit text box
        self.editPara = QtGui.QTextEdit(Form)
        self.editPara.setGeometry(QtCore.QRect(170, 300, 371, 121))
        self.editPara.setObjectName(_fromUtf8("editPara"))
        self.editPara.setReadOnly(True)
        #if self.finish_para == 0:
        self.editPara.textChanged.connect(self.text_changed)

        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(170, 110, 81, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        # add Ok button
        self.finish = QtGui.QPushButton(Form)
        self.finish.setGeometry(QtCore.QRect(490, 510, 51, 27))
        self.finish.setObjectName(_fromUtf8("finish"))

        # Add cancel button
        self.Cancel = QtGui.QPushButton(Form)
        self.Cancel.setGeometry(QtCore.QRect(570, 510, 51, 27))
        self.Cancel.setObjectName(_fromUtf8("Cancel"))
        self.Cancel.clicked.connect(self.closeApp)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Game TypeRacer", None))
        self.label.setText(_translate("Form", "Type Here", None))
        self.label_2.setText(_translate("Form", "Your Paragraph", None))
        self.finish.setText(_translate("Form", "Finish", None))
        self.Cancel.setText(_translate("Form", "Cancel", None))

    def text_changed(self):
        self.editPara.setReadOnly(True)
        mytext = self.editPara.toPlainText()
        l=len(mytext)
        k=len(self.st)
        if k > l:
            if mytext == self.st[0:l]:
                print "match"
                self.editPara.setStyleSheet("QTextEdit {color:black}")
                '''if len(self.st) >= l:
                                                        print ""                                     
                                                        #self.editPara.setReadOnly(True)
                                                    else:
                                                        self.editPara.setReadOnly(False)'''
            else:
                self.editPara.setStyleSheet("QTextEdit {color:red}")
            self.editPara.setReadOnly(False)
        """else:
                                    self.editPara.setText("")
                                    #self.finish_para = 1
                                    #self.editPara.setReadOnly(True)"""

    #function to update progress bar
    def update_progressbar(self, val):
        self.progressBar.setValue(val)
        if val == 5:
            self.timeToStart.setText("Go..Game will start ")
            self.timeToStart.setStyleSheet("QTextEdit {color:green}")

    #function to directly close App 
    def closeApp(self):
        print "Cancel pressed"
        app.exit()


    #function to start game in 4sec
    def startIn(self):
        if timer.q < 6:
            self.update_progressbar(timer.q)
            print 'tick'
            timer.q += 1
        else:
            self.editPara.setReadOnly(False)

if __name__ == "__main__":
    import sys
    from PyQt4.QtCore import QTimer
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()

    #set timer
    timer = QTimer()
    timer.q = 0
    timer.timeout.connect(ui.startIn)
    timer.start(1000)

    sys.exit(app.exec_())

