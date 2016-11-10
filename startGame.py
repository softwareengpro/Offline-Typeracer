from PyQt4 import QtCore, QtGui
#from selectSession import Ui_Form
import selectSession, Practice_start, wordMap, timeMap, random, re, usernameWindow, resultWindow
from time import time
#from PyQt4.QtCore import QTimer
from PyQt4.QtCore import QTimer
import feedparser

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
        if userText != '': 
            self.startgame.clicked.connect(self.selectMode)
        else:
            self.startgame.clicked.connect(self.firstNameDialog)

    def update_currentAffairs(self):
        currentAffairs = open("currentAffairs.txt", "r+")
        d = feedparser.parse('http://www.jagranjosh.com/rss/josh/current_affairs.xml')
        for i in range(0, 20):
            currentAffairs.write(str(d['entries'][i]['title'].encode('ascii', 'ignore') + '\n'))
        currentAffairs.close()

    def update_news(self):
        news = open("news.txt", "r+")
        c = feedparser.parse('http://timesofindia.indiatimes.com/rssfeedstopstories.cms')
        for i in range(0, 5):
            news.write(str(c['entries'][i]['title'].encode('ascii', 'ignore') + '\n'))
        news.close()


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

        #sessionMode = selectSession.Ui_Form()
        sessionMode.setupUi(self.obj)
        self.obj.show()
        self.startgame.hide()
        self.close.hide()
        sessionMode.close.clicked.connect(self.closeApp) 
        sessionMode.practice_session.clicked.connect(self.selectTopic)  

    def selectTopic(self):
        self.obj.hide()
        #wordObj = wordMap.Ui_Form()
        sessionMode.practice_session.hide()
        sessionMode.create_challenge.hide()
        sessionMode.acceptchallenge.hide()
        sessionMode.label.hide()
        wordObj.setupUi(self.obj)
        self.obj.show()
        wordObj.paragraph.clicked.connect(self.selectTimeMap)
        wordObj.news.clicked.connect(self.sessionPracticeGK)
        wordObj.news.clicked.connect(self.selectNews)
        wordObj.gk.clicked.connect(self.sessionPracticeGK)
        wordObj.gk.clicked.connect(self.currentAffairs)
        wordObj.audio.clicked.connect(self.audioSection)

    def selectTimeMap(self):
        self.obj.hide()
        #print wordObj
        wordObj.Chose_topic.hide()
        wordObj.paragraph.hide()
        wordObj.news.hide()
        wordObj.gk.hide()
        wordObj.audio.hide()
        #mapTime = timeMap.Ui_Form()
        mapTime.setupUi(self.obj)
        mapTime.min1.clicked.connect(self.sessionPractice)
        mapTime.min1.clicked.connect(self.selectParagraph)
        #mapTime.min1.clicked.connect(self.resultWindow)

        mapTime.min2.clicked.connect(self.changeValue2)
        mapTime.min2.clicked.connect(self.sessionPractice)
        mapTime.min2.clicked.connect(self.selectParagraph)

        mapTime.min3.clicked.connect(self.changeValue3)
        mapTime.min3.clicked.connect(self.sessionPractice)
        mapTime.min3.clicked.connect(self.selectParagraph)
        #Form.setEnabled(false)
        self.obj.show()

    #it change the value of i to select the no pf line
    def changeValue2(self):
        global i
        i = 4
        print "changed"

    def changeValue3(self):
        global i
        i = 6
        print "changed"

    def tick(self):
        print "self"
        print "tick"

    def sessionPractice(self):
        #import Qtimer
        self.obj.hide()
        #prac_sess = Practice_start.Ui_Form()
        mapTime.timeMap.hide()
        mapTime.min1.hide()
        mapTime.min2.hide()
        mapTime.min3.hide()
        prac_sess.setupUi(self.obj)
        self.obj.show()
        #prac_sess.start_Timer()
        timer.timeout.connect(self.startIn)
        timer.start(1000)
        prac_sess.editPara.textChanged.connect(self.text_changed)
        prac_sess.finish.clicked.connect(self.firstActivity)
        prac_sess.finish.clicked.connect(self.resultSection)
        prac_sess.finish.clicked.connect(self.final_time)
        #self.start_Timer()
        #prac_sess.practice_session()
        #prac_sess.start_Timer()
        #print(timer.start(1000))
        #prac_sess.tick()
        #print "timer"
        #prac_sess.startIn()

    def sessionPracticeGK(self):
        self.obj.hide()
        prac_sess.setupUi(self.obj)
        self.obj.show()
        #prac_sess.start_Timer()
        timer.timeout.connect(self.startIn)
        timer.start(1000)
        prac_sess.editPara.textChanged.connect(self.text_changed)
        prac_sess.finish.clicked.connect(self.firstActivity)
        prac_sess.finish.clicked.connect(self.resultSection)
        prac_sess.finish.clicked.connect(self.final_time)


    def startIn(self):
        #ui = Ui_Form()
        #print "not call startIn"
        #q = self.timer.q
        if timer.q < 6:
            prac_sess.update_progressbar(timer.q)
            #print self
            print 'tick'
            timer.q += 1
        elif timer.q == 6:
            #self.selectParagraph()
            timer.q = 7
        else:
            prac_sess.editPara.setReadOnly(False)
            self.begin_time = time()

    def selectParagraph(self):
        import time
        lines = open('story.txt').read().splitlines()
        #print(lines[10])
        self.myline = ""
        prac_sess.st = ""
        print "hhiiii "
        print i
        for j in range(0, 2*i):
            #print "asdf"
            while len(self.myline) <= 20:
                self.myline = random.choice(lines)
                #print self.myline
            prac_sess.st = self.myline + prac_sess.st
            self.myline = ""
        prac_sess.st = prac_sess.st.replace('\xc2\xa0', ' ')
        prac_sess.st = prac_sess.st.replace('\xe2\x80\x9c', ' ')
        prac_sess.st = prac_sess.st.replace('\xe2\x80\x9d', ' ')
        prac_sess.st = prac_sess.st.replace('\xe2\x80\x99', ' ')
        prac_sess.st = prac_sess.st.replace('\xc2', ' ')
        prac_sess.showPara.setText(prac_sess.st)
        #self.resultSection()

    def resultSection(self):
        self.resultWindow()

    def selectNews(self):
        print "Have to implement"
        lines = open('news.txt').read().splitlines()
        prac_sess.st = ""
        for j in lines:
            prac_sess.st = prac_sess.st + j + '\n'
        prac_sess.showPara.setText(prac_sess.st)
        #lines = open('news.txt').read().splitlines()
        #prac_sess.showPara.append(random.choice(lines))
        #prac_sess.showPara.append(random.choice(lines))

    def currentAffairs(self):
        print "implment"
        lines = open('currentAffairs.txt').read().splitlines()
        prac_sess.st = ""
        for j in range (0, 9):
            text = random.choice(lines)
            prac_sess.st = prac_sess.st + '\n' + text
        prac_sess.showPara.setText(prac_sess.st)
        #Have to implement

    def audioSection(self):
        print "Implement"
        #Have to implement

    def resultWindow(self):
        self.result = QtGui.QDialog()
        resultWin.setupUi(self.result)
        #hBoxLayout = QHBoxLayout()
        self.result.show()
        resultWin.typeTime.setText("Total")
        resultWin.userWPM.setText("W")
        resultWin.userAccuracy.setText("A")

    def enterUsername(self):
        #app1 = QtGui.QApplication(sys.argv)
        usernameWin.setupUi(username)
        usernameWin.ok.clicked.connect(self.getUsername)
        usernameWin.cancel.clicked.connect(self.hideUsernameWindow)
        username.show()
        #app1.exec_()

    def getUsername(self):
        user = usernameWin.username.text()
        file.write(user)
        userText = file.read()
        if userText != '':
            username.hide()

    def hideUsernameWindow(self):
        username.hide()

    def firstNameDialog(self):
        d = QtGui.QDialog()
        b1 = QtGui.QPushButton("First enter your Name",d)
        b1.move(50,50)
        d.setWindowTitle("Dialog")
        #d.setWindowModality(Qt.ApplicationModal)
        d.exec_()

    def text_changed(self):
        prac_sess.editPara.setReadOnly(True)
        mytext = prac_sess.editPara.toPlainText()
        global input_l
        input_l=len(mytext)
        print input_l
        if input_l == 1:
            start_time = time()
            print start_time
        para_l = len(prac_sess.st)
        print input_l
        print para_l
        if input_l <= para_l:
            if mytext == prac_sess.st[0:input_l]:
                print "match"
                prac_sess.editPara.setStyleSheet("QTextEdit {color:black}")
            else: 
                prac_sess.editPara.setStyleSheet("QTextEdit {color:red}")
                wrongType.append(prac_sess.st[input_l-1])
                print wrongType
            if input_l <= para_l:
                prac_sess.editPara.setReadOnly(False)
        else:
            self.final_time()
            self.resultSection()

    #initial activity
    def firstActivity(self):
        prac_sess.progressBar.hide()
        prac_sess.timeToStart.hide()
        prac_sess.showPara.hide()
        prac_sess.editPara.hide()
        prac_sess.finish.hide()
        prac_sess.label.hide()
        prac_sess.label_2.hide()
        self.setupUi(self.obj)
        self.startgame.show()
        self.close.show()
        self.obj.show()

    def begin_time(self):
        start_time = time()
        print start_time
        #return start_time

    def final_time(self):
        end_time = time()
        #begin = self.begin_time()
        print "hiii"
        print start_time
        total_time = (end_time - start_time)/60
        print total_time
        resultWin.typeTime.setText(str(total_time))
        print input_l
        word_length = float(input_l/4)
        self.wpm(total_time, word_length)

    def wpm(self, t, l):
        t = round(t, 2)
        print t
        print l
        word_p_m = float(l)/t
        #print word_p_m
        wpm = round(word_p_m, 2)
        print wpm
        resultWin.userWPM.setText(str(wpm))
        self.accuracy()

    def accuracy(self):
        print "have to implement"
        wrongType_l = len(wrongType)
        k =len(prac_sess.st)
        #word_left = k - input_l
        correct = float(k) - float(wrongType_l)
        correctPercentage = (float(correct)/float(k)) * 100
        print "Accuracy"
        Accurate = round(correctPercentage, 2)
        resultWin.userAccuracy.setText(str(Accurate))


"""    def startInFive(self):
        d = QtGui.QDialog()
        b1 = QtGui.QTextEdit("Start In",d)
        b2 = QtGui.QProgressBar(d)
        b1.move(10,50)
        b1.setReadOnly(True)
        b1.setGeometry(QtCore.QRect(70, 10, 104, 31))
        b2.setGeometry(QtCore.QRect(70, 60, 104, 31))
        d.setWindowTitle("Dialog")
        #d.setWindowModality(Qt.ApplicationModal)
        d.exec_()"""


if __name__ == "__main__":
    import sys
    from time import time
    file = open("username.txt","rw+")
    userText = file.read()
    wrongType = []
    i = 2
    input_l = 0
    para_l = 0

    start_time = time()
    print start_time
    app = QtGui.QApplication(sys.argv)
    O = QtGui.QWidget()
    ui = Ui_O()
    ui.setupUi(O)
    O.show()

    ui.update_currentAffairs()
    ui.update_news()

    #creating an object 
    wordObj = wordMap.Ui_Form() #create an global object of wordMap
    prac_sess = Practice_start.Ui_Form() #create an global object of practice_start session
    sessionMode = selectSession.Ui_Form() #create an global object of select session
    mapTime = timeMap.Ui_Form() #create an global object of timeMap
    usernameWin = usernameWindow.Ui_Form() #create an global object of usernameWindow

    #section for username
    username = QtGui.QWidget()
    resultWin = resultWindow.Ui_Dialog()
    if userText == '':
        ui.enterUsername()

    #cretae a timer
    timer = QTimer()
    timer.q = 0
    app.exec_()
    sys.exit(0)
