from PyQt4 import QtCore, QtGui
#from selectSession import Ui_Form
import selectSession, Practice_start, wordMap, timeMap
#from PyQt4.QtCore import QTimer
from PyQt4.QtCore import QTimer

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

class Ui_O(object):
    def setupUi(self, O):
        O.setObjectName(_fromUtf8("O"))
        O.resize(700, 500)

        self.centralwidget = QtGui.QWidget(O)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.startgame = QtGui.QPushButton(self.centralwidget)
        self.startgame.setGeometry(QtCore.QRect(330, 200, 85, 27))
        self.startgame.setObjectName(_fromUtf8("startgame"))
        #self.startgame.clicked.connect(self.newWindow)


        self.close = QtGui.QPushButton(self.centralwidget)
        self.close.setGeometry(QtCore.QRect(330, 270, 85, 27))
        self.close.setObjectName(_fromUtf8("close"))
        

        self.retranslateUi(O)
        QtCore.QMetaObject.connectSlotsByName(O)

        self.obj = O

    def retranslateUi(self, O):
        O.setWindowTitle(_translate("O", "OFFLINE TYPERACER", None))
        self.startgame.setText(_translate("O", "StarGame", None))
        self.close.setText(_translate("O", "Close", None))
        self.close.clicked.connect(self.closeApp)
        self.startgame.clicked.connect(self.selectMode)

    def closeApp(self):
        print "Cancel pressed"
        #choice = QtGui.QMessageBox.question(self,'Extract!',"Get into the chopper?",QtGui.QMessageBox.Ok | QtGui.QMessageBox.No)
        #if choice == QMessageBox.Ok:
        sys.exit()
        #else:
        #    pass
        #app.quit()

    def selectMode(self):
        self.obj.hide()
        #layout = QtGui.QHBoxLayout(O)
        #s = QtGui.QWidget()
        #layout.removeWidget(self.obj)

        sec = selectSession.Ui_Form()
        sec.setupUi(self.obj)
        self.obj.show()
        self.startgame.hide()
        self.close.hide()
        sec.close.clicked.connect(self.closeApp) 
        sec.practice_session.clicked.connect(self.selectTopic)  
        #sec.practice_session.clicked.connect(self.sessionPractice)

    def selectTopic(self):
        self.obj.hide()
        topic = wordMap.Ui_Form()
        topic.setupUi(self.obj)
        self.obj.show()
        topic.paragraph.clicked.connect(self.selectTimeMap)

    def selectTimeMap(self):
        self.obj.hide()
        time = timeMap.Ui_Form()
        time.setupUi(self.obj)
        #Form.setEnabled(false)
        self.obj.show()

    def sessionPractice(self):
        #import Qtimer
    	self.obj.hide()
        prac_sess = Practice_start.Ui_Form()
        prac_sess.setupUi(self.obj)
        self.obj.show()
        #prac_sess.practice_session()
        #prac_sess.start_Timer()
        timer = QTimer()
        timer.q = 0
        timer.timeout.connect(prac_sess.startIn)
        timer.start(1000)
        #prac_sess.startIn()

    	"""prac = Practice_start.Ui_Form()
        prac.setupUi(self.obj)
        self.obj.show()
        timer = QTimer()
        timer.q = 0
        timer.timeout.connect(prac.startIn)
        timer.start(1000)

        # app.exit()

        def newWindow(self):
                        #import sys
                        #app = QtGui.QApplication(sys.argv)
        Form = QtGui.QWidget()
        ui = selectSession.Ui_Form()
        ui.setupUi(Form)
        Form.show()
                        #O.hide()
        sys.exit(app.exec_())"""

if __name__ == "__main__":
    import sys
    #import selectSession
    app = QtGui.QApplication(sys.argv)
    O = QtGui.QWidget()
    ui = Ui_O()
    ui.setupUi(O)
    O.show()
    #layout = QtGui.QHBoxLayout(O)
    #print layout
    app.exec_()
    #print "hi"
    # app = QtGui.QApplication(sys.argv)
    # O = QtGui.QWidget()
    # sec = Ui_Form()
    # sec.setupUi(O)
    # O.show()
    # app.exec_()
    sys.exit(0)
