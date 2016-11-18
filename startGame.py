from PyQt4 import QtCore, QtGui
#from selectSession import Ui_Form
import selectSession, Practice_start, wordMap, timeMap, random, re, usernameWindow, resultWindow, createChallenge, challengeWordMap, challengeTimeMap, multiType
from time import time
#from PyQt4.QtCore import QTimer
from PyQt4.QtCore import QTimer
import feedparser
import urllib2
import audio_edit, Join
#from PySide.phonon import Phonon
import socket
import threading

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
        O.resize(800, 600)
        O.setAutoFillBackground(False)
        O.setStyleSheet(_fromUtf8("background-color: rgb(85, 170, 127);\n"
""))
        #O.setAnimated(True)
        #O.setDocumentMode(False)
        # O.setTabShape(QtGui.QTabWidget.Rounded)
        # O.setDockNestingEnabled(False)
        # O.setDockOptions(QtGui.QMainWindow.AllowTabbedDocks|QtGui.QMainWindow.AnimatedDocks)
        # O.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(O)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.startgame = QtGui.QPushButton(self.centralwidget)
        self.startgame.setGeometry(QtCore.QRect(210, 280, 85, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startgame.sizePolicy().hasHeightForWidth())
        self.startgame.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.startgame.setFont(font)
        self.startgame.setAutoFillBackground(False)
        self.startgame.setStyleSheet(_fromUtf8("color: rgb(0, 0, 49);"))
        self.startgame.setAutoDefault(False)
        self.startgame.setDefault(False)
        self.startgame.setFlat(False)
        self.startgame.setObjectName(_fromUtf8("startgame"))
        self.close = QtGui.QPushButton(self.centralwidget)
        self.close.setGeometry(QtCore.QRect(210, 400, 85, 27))
        self.close.setStyleSheet(_fromUtf8("\n"
"color: rgb(0, 0, 49);"))
        self.close.setObjectName(_fromUtf8("close"))
        self.proName = QtGui.QLabel(self.centralwidget)
        self.proName.setGeometry(QtCore.QRect(280, 50, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.proName.setFont(font)
        self.proName.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.proName.setObjectName(_fromUtf8("proName"))
        self.showUserName = QtGui.QLineEdit(self.centralwidget)
        self.showUserName.setGeometry(QtCore.QRect(330, 170, 131, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.showUserName.setFont(font)
        self.showUserName.setStyleSheet(_fromUtf8("alternate-background-color: rgb(255, 255, 255);"))
        self.showUserName.setObjectName(_fromUtf8("showUserName"))
        self.showUserName.setReadOnly(True)
        self.changeUserName = QtGui.QPushButton(self.centralwidget)
        self.changeUserName.setGeometry(QtCore.QRect(470, 280, 111, 27))
        self.changeUserName.setStyleSheet(_fromUtf8("color: rgb(0, 0, 49);"))
        self.changeUserName.setObjectName(_fromUtf8("changeUserName"))
        self.Score = QtGui.QPushButton(self.centralwidget)
        self.Score.setGeometry(QtCore.QRect(470, 400, 111, 27))
        self.Score.setStyleSheet(_fromUtf8("color: rgb(0, 0, 49);"))
        self.Score.setObjectName(_fromUtf8("Score"))
        self.Instrution = QtGui.QPushButton(self.centralwidget)
        self.Instrution.setGeometry(QtCore.QRect(330, 500, 111, 27))
        self.Instrution.setStyleSheet(_fromUtf8("color: rgb(0, 0, 49);"))
        self.Instrution.setObjectName(_fromUtf8("Instrution"))
        #O.setCentralWidget(self.centralwidget)
        # self.statusbar = QtGui.QStatusBar(O)
        # self.statusbar.setObjectName(_fromUtf8("statusbar"))
        # O.setStatusBar(self.statusbar)
        self.obj = O

        self.retranslateUi(O)
        QtCore.QMetaObject.connectSlotsByName(O)

    def retranslateUi(self, O):
        O.setWindowTitle(_translate("O", "MainWindow", None))
        self.startgame.setText(_translate("O", "StarGame", None))
        self.close.setText(_translate("O", "Close", None))
        self.proName.setText(_translate("O", "  OFFLINE TYPERACER", None))
        self.showUserName.setText(_translate("O", "      Hello asdfg", None))
        self.changeUserName.setText(_translate("O", "Change Username", None))
        self.Score.setText(_translate("O", "Score", None))
        self.Instrution.setText(_translate("0", "Instruction", None))

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
        c = feedparser.parse('http://www.thehindu.com/news/?service=rss')
        for i in range(0, 100):
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
        self.showUserName.hide()
        self.changeUserName.hide()
        self.Instrution.hide()
        self.Score.hide()
        sessionMode.close.clicked.connect(self.closeApp) 
        sessionMode.practice_session.clicked.connect(self.selectTopic)  
        sessionMode.acceptchallenge.clicked.connect(self.joinChallenge)
        sessionMode.create_challenge.clicked.connect(self.challengeWordmap)
        sessionMode.back.clicked.connect(self.back2_1)

#For Challenge
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    def challengeWordmap(self):
        self.obj.hide()
        #wordObj = wordMap.Ui_Form()
        sessionMode.practice_session.hide()
        sessionMode.create_challenge.hide()
        sessionMode.acceptchallenge.hide()
        sessionMode.label.hide()
        sessionMode.back.hide()
        wordMapChallenge.setupUi(self.obj)
        self.obj.show()
        wordMapChallenge.Paragraph.clicked.connect(self.timeMapChallenge)
        wordMapChallenge.News.clicked.connect(self.internet_on)
        wordMapChallenge.Gk.clicked.connect(self.challengeCreate)
        wordMapChallenge.Back.clicked.connect(self.backword_session)

    def challengeCreate(self):
        self.obj.hide()
        challengeCreate.setupUi(self.obj)   
        self.obj.show()
        wordMapChallenge.chose_topic.hide()
        wordMapChallenge.Paragraph.hide()
        wordMapChallenge.News.hide()
        wordMapChallenge.Gk.hide()
        timeChallenge.Back.hide()
        timeChallenge.Min1.hide()
        timeChallenge.Min2.hide()
        timeChallenge.Min3.hide()
        timeChallenge.TimeMap.hide()
        #timeMap.back.hide()
        wordMapChallenge.Back.hide()
        challengeCreate.back.clicked.connect(self.backChallenge_Time)
        challengeCreate.createChallenge.clicked.connect(self.serverCreate)

    def timer1(self):
        timer.timeout.connect(self.changeTimer)
        timer.start(1000)

    def changeTimer(self):
        global s
        s += 1
        print s
        # if s==5:
        #     print 'server closed'
        #     self.s.close()
        #     print self.s
        #     timer.stop()
        if Client != 1 and cont != 1:
                print "get a connection"
                #timer.stop()
                global cont
                cont = 1
                self.multiType1()
                multiTypeObject.showPara.setText(st)
        else:
            if s==60 and client == 1:
                print "no one connected"
                print "server closed"
                self.s.close()
                d = QtGui.QDialog()
                b1 = QtGui.QPushButton("Timeout, Recreate challenge",d)
                b1.move(80,50)
                d.setWindowTitle("Dialog")
                #d.setWindowModality(Qt.ApplicationModal)
                d.exec_()
                timer.stop()
                #self.selectMode()
        # else:
        #     if Client != 1:



    def serverCreate(self):
        self.timer1()
        print s
        print 'hllo'
        self.bind()


    def MyThread1(self):
        global Client
        global st
        Client, Adr=(self.s.accept())
        print type(Client)
        print 'Got a connection from: '# + str(Client) + '.'
        #self.multiType()
        st = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
        Client.send(st.encode())
        a = Client.recv(1024).decode()
        print a


    def bind(self):
        Adress=('',5000)
        MaxClient=2
        self.s = socket.socket()
        self.s.bind(Adress)
        self.s.listen(MaxClient)
        print 'server listenig'
        t1 = threading.Thread(target=self.MyThread1, args=[])
        t1.start()

    def backChallenge_Time(self):
        self.obj.hide()
        challengeCreate.createLabel.hide()
        challengeCreate.createChallenge.hide()
        challengeCreate.back.hide()
        mapTime.setupUi(self.obj)
        self.obj.show()
        wordMapChallenge.Paragraph.clicked.connect(self.timeMapChallenge)
        wordMapChallenge.News.clicked.connect(self.challengeCreate)
        wordMapChallenge.Gk.clicked.connect(self.challengeCreate)
        wordMapChallenge.Back.clicked.connect(self.backword_session)


    def timeMapChallenge(self):
        self.obj.hide()
        wordMapChallenge.chose_topic.hide()
        wordMapChallenge.Paragraph.hide()
        wordMapChallenge.News.hide()
        wordMapChallenge.Gk.hide()
        sessionMode.back.hide()
        wordMapChallenge.Back.hide()
        timeChallenge.setupUi(self.obj)
        timeChallenge.Min1.clicked.connect(self.challengeCreate)
        timeChallenge.Min2.clicked.connect(self.challengeCreate)
        timeChallenge.Min3.clicked.connect(self.challengeCreate)
        timeChallenge.Back.clicked.connect(self.backTime_wordChallenge)
        self.obj.show()

    def backTime_wordChallenge(self):
        self.obj.hide()
        wordMapChallenge.setupUi(self.obj)
        timeChallenge.Min1.hide()
        timeChallenge.Min2.hide()
        timeChallenge.Min3.hide()
        timeChallenge.TimeMap.hide()
        wordMapChallenge.Paragraph.clicked.connect(self.timeMapChallenge)
        wordMapChallenge.News.clicked.connect(self.challengeCreate)
        wordMapChallenge.Gk.clicked.connect(self.challengeCreate)
        wordMapChallenge.Back.clicked.connect(self.backword_session)
        self.obj.show()


    def joinChallenge(self):
        #self.obj.hide()
        self.obj.hide()
        sessionMode.practice_session.hide()
        sessionMode.create_challenge.hide()
        sessionMode.acceptchallenge.hide()
        sessionMode.label.hide()
        joinChallenge.setupUi(self.obj)
        self.obj.show()
        joinChallenge.joinchallenge.clicked.connect(self.clientJoin)
        joinChallenge.joinchallenge.clicked.connect(self.multiType)

    def multiType(self):
        self.obj.hide()
        joinChallenge.joinchallenge.hide()
        joinChallenge.textEdit.hide()
        joinChallenge.label.hide()
        multiTypeObject.setupUi(self.obj)
        self.obj.show()

    def multiType1(self):
        self.obj.hide()
        multiTypeObject.setupUi(self.obj)
        self.obj.show()
        timer.timeout.connect(self.startIn1)
        timer.start(1000)

    def clientJoin(self):
        print 'hello'
        joinChallenge.textEdit.setReadOnly(True)
        a = str(joinChallenge.textEdit.toPlainText())
        print a
        #print type(a)
        if a != '':
            self.clientConnect(a)
        else:
            self.noIp()
            joinChallenge.textEdit.setReadOnly(False)

    def noIp(self):
        d = QtGui.QDialog()
        b1 = QtGui.QPushButton("First enter The IP",d)
        b1.move(50,50)
        d.setWindowTitle("Dialog")
        #d.setWindowModality(Qt.ApplicationModal)
        d.exec_()

    def clientConnect(self, adress):
        Adress=(adress,5000)
        print adress
        import socket
        self.s = socket.socket()
        self.s.connect(Adress)
        data = ''
        data = self.s.recv(1024).decode()
        print (data)
        self.multiType()
        multiTypeObject.showPara.setText("data");
        self.s.send('fine'.encode())

#For going back 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>        

    def back2_1(self):
        self.obj.hide()
        self.setupUi(self.obj)
        sessionMode.back.hide()
        sessionMode.close.hide()
        self.changeUserName.clicked.connect(ui.enterUsername)
        self.Score.clicked.connect(self.resultWindow)
        self.obj.show()

    def backword_session(self):
        self.obj.hide()
        wordObj.Chose_topic.hide()
        wordObj.paragraph.hide()
        wordObj.news.hide()
        wordObj.gk.hide()
        wordObj.audio.hide()
        wordObj.back.hide()
        sessionMode.back.hide()
        sessionMode.setupUi(self.obj)
        self.obj.show()
        sessionMode.close.clicked.connect(self.closeApp) 
        sessionMode.practice_session.clicked.connect(self.selectTopic)  
        sessionMode.acceptchallenge.clicked.connect(self.joinChallenge)

    def backTime_word(self):
        self.obj.hide()
        wordObj.setupUi(self.obj)
        mapTime.min1.hide()
        mapTime.min2.hide()
        mapTime.min3.hide()
        self.obj.show()
        wordObj.paragraph.clicked.connect(self.selectTimeMap)
        wordObj.news.clicked.connect(self.internet_on)
        wordObj.gk.clicked.connect(self.sessionPracticeGK)
        wordObj.gk.clicked.connect(self.currentAffairs)
        wordObj.audio.clicked.connect(self.audioSection)
        wordObj.back.clicked.connect(self.backword_session)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


    def selectTopic(self):
        self.obj.hide()
        #wordObj = wordMap.Ui_Form()
        sessionMode.practice_session.hide()
        sessionMode.create_challenge.hide()
        sessionMode.acceptchallenge.hide()
        sessionMode.label.hide()
        sessionMode.back.hide()
        wordObj.setupUi(self.obj)
        self.obj.show()
        wordObj.paragraph.clicked.connect(self.selectTimeMap)
        wordObj.news.clicked.connect(self.internet_on)
        wordObj.gk.clicked.connect(self.sessionPracticeGK)
        wordObj.gk.clicked.connect(self.currentAffairs)
        wordObj.audio.clicked.connect(self.audioSection)
        wordObj.back.clicked.connect(self.backword_session)


    def internet_on(self):
        for timeout in [1,5,10,15]:
            try:
                response=urllib2.urlopen('http://google.com',timeout=timeout)
                print "you are connect with internet"
                self.update_currentAffairs()
                self.update_news()
                self.sessionPracticeGK()
                self.selectNews()
                return True
            except urllib2.URLError as err:
                print "you are not connected"
                self.sessionPracticeGK()
                self.selectNews()
                #self.noInternet()
        return False

    def noInternet(self):
        In = QtGui.QDialog()
        I1 = QtGui.QPushButton("No internet connection",In)
        I1.move(50,50)
        In.setWindowTitle("Dialog")
        #d.setWindowModality(Qt.ApplicationModal)
        In.exec_()

    def selectTimeMap(self):
        self.obj.hide()
        #print wordObj
        wordObj.Chose_topic.hide()
        wordObj.paragraph.hide()
        wordObj.news.hide()
        wordObj.gk.hide()
        wordObj.audio.hide()
        sessionMode.back.hide()
        wordObj.back.hide()
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
        mapTime.back.clicked.connect(self.backTime_word)
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
        mapTime.back.hide()
        prac_sess.setupUi(self.obj)
        self.obj.show()
        mapTime.back.hide()
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
        wordObj.gk.hide()
        wordObj.back.hide()
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
            #timer.close()
            #self.selectParagraph()
            timer.stop()
            prac_sess.editPara.setReadOnly(False)
            self.begin_time = time()
            timer.q = 0



    def startIn1(self):
        #ui = Ui_Form()
        #print "not call startIn"
        #q = self.timer.q
        if timer.q < 6:
            multiTypeObject.update_progressbar(timer.q)
            #print self
            print 'tick'
            timer.q += 1
        elif timer.q == 6:
            #timer.close()
            #self.selectParagraph()
            multiTypeObject.editPara.setReadOnly(False)

            self.begin_time = time()

            timer.stop()
            timer.q = 0

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

#Audio Section
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    def audioSection(self):
        print "Implement"
        self.obj.hide()
        wordObj.Chose_topic.hide()
        wordObj.paragraph.hide()
        wordObj.news.hide()
        wordObj.gk.hide()
        wordObj.audio.hide()
        audioObj.setupUi(self.obj)
        audioObj.close.clicked.connect(self.closeApp)
        audioObj.play.clicked.connect(self.makethread)
        audioObj.audioTextEdit.textChanged.connect(self.audioEdit)
        audioObj.finish.clicked.connect(self.resultWindow)
        audioObj.finish.clicked.connect(self.audioResult)
        self.obj.show()
        #Have to implement

    def makethread(self):
        audioObj.audioTextEdit.setReadOnly(False)
        t2 = threading.Thread(target=self.playAudio, args=[])
        t2.start()
        
    def playAudio(self):
        print 'Audio playing'
        global start_time
        start_time = time()
        import pyttsx
        engine = pyttsx.init()
        rate = engine.getProperty('rate')
        #voices = engine.getProperty('voices')
        engine.setProperty('rate', 100)
        # for voice in voices:
        #     if voice.gender == "female":
        #         engine.setProperty('female', voice.gender)
        #         break
        global audioStr
        audioStr = 'Sally sells seashells by the seashore.'
        engine.say(audioStr)
        print "hllo"
        engine.runAndWait()

    def audioEdit(self):
        audioObj.audioTextEdit.setReadOnly(True)
        global audioEditStr
        audioEditStr = audioObj.audioTextEdit.toPlainText()
        print audioEditStr
        audioObj.audioTextEdit.setReadOnly(False)

    def audioResult(self):
        tm, line = self.count()
        tm = round(tm, 2)
        words_per_minute = self.Wpm(tm, line)
        words_per_minute = round(words_per_minute, 2)
        #percentage = self.wordcheck(line)
        #percentager = round(percentage, 2)

    def count(self):
        i = 0 
        end_time = time()
        print end_time
        final_time = (end_time - start_time) / 60
        print final_time
        resultWin.typeTime.setText(str(final_time))
        return final_time, audioStr


    def Wpm(self, time, line):
        words = line.split()
        word_length = len(words)
        words_per_m = word_length / time
        print words_per_m
        resultWin.userWPM.setText(str(words_per_m))
        return words_per_m


    # def wordcheck(self, audioEditStr):
    #     audio = audioStr.split()
    #     audioEdit = audioEditStr.split()
    #     errorcount = 0
        
    #     idx = 0
    #     for inp in audioEdit:
    #         if inp != audio[idx]:
    #             errorcount += 1
    #             if inp == audio[idx + 1]:
    #                 idx += 2
    #             elif inp != audio[idx - 1]:
    #                 idx += 1
    #         else:
    #             idx += 1
        
    #     words_left = len(audio) - len(audioEdit)
    #     correct = float(len(audio)) - float(errorcount)
    #     percentage = (((float(correct) / float(len(audioStr))) - float(words_left) / float(len(audioStr))) * 100)

        
    #     return percentage

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


    def resultWindow(self):
        self.result = QtGui.QDialog()
        resultWin.setupUi(self.result)
        #hBoxLayout = QHBoxLayout()
        # file = open('result.txt', 'r')
        # user = file.read().splitlines()
        # file.close()
        self.result.show()
        # user[0] = user[0].strip(' ')
        # print user[0]
        # print userText
        d = {}
        with open("result.txt") as f:
            for line in f:
                (key, val) = line.split()
                print key
                print val
                d[key] = val
        if d['usernam'] == userText:
            #print d
            resultWin.typeTime.setText(d['total_time'])
            resultWin.userWPM.setText(d['wpm'])
            resultWin.userAccuracy.setText(d['Accuracy'])
        else:
            self.result.hide()
            print "You are a new User"
            d = QtGui.QDialog()
            b1 = QtGui.QPushButton("You are a new user",d)
            b1.move(50,50)
            d.setWindowTitle("Dialog")
            #d.setWindowModality(Qt.ApplicationModal)
            d.exec_()



    def enterUsername(self):
        #app1 = QtGui.QApplication(sys.argv)
        usernameWin.setupUi(username)
        usernameWin.ok.clicked.connect(self.getUsername)
        usernameWin.ok.clicked.connect(self.hideUsernameWindow)
        usernameWin.ok.clicked.connect(self.showName)
        usernameWin.cancel.clicked.connect(self.hideUsernameWindow)
        username.show()
        #app1.exec_()

    def getUsername(self):
        user = usernameWin.username.text()
        userl = len(user)
        print userl
        file = open('username.txt', 'w')
        print user
        file.write(user)
        file.close()
        file = open('username.txt', 'r')
        userText = file.read().splitlines()
        file.close()

        #usernameWin.username.setReadOnly(False)
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
        self.obj.hide()
        prac_sess.progressBar.hide()
        prac_sess.timeToStart.hide()
        prac_sess.showPara.hide()
        prac_sess.editPara.hide()
        prac_sess.finish.hide()
        prac_sess.label.hide()
        prac_sess.label_2.hide()
        self.showUserName.setReadOnly(False)
        self.showUserName.setText(str(userText))
        print userText
        self.showUserName.setReadOnly(True)
        self.setupUi(self.obj)
        self.startgame.show()
        self.close.show()
        self.changeUserName.clicked.connect(self.enterUsername)
        self.Score.clicked.connect(self.resultWindow)
        self.Instrution.clicked.connect(self.typingManual)
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
        global result
        result = 'total_time' + ' ' + str(total_time)
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
        global result1
        result1 = 'wpm' + ' ' + str(wpm)
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
        global result2
        result2 = 'Accuracy' + ' ' + str(Accurate)
        print result + ' \n' +  result1+ ' \n' + result2
        resu = open('result.txt', 'rw+')
        resu.write('usernam' + ' ' + userText + ' \n' + result + ' \n' +  result1+ ' \n' + result2)
        resu.close()
        resultWin.userAccuracy.setText(str(Accurate))

    def showName(self):
        showUser = open('username.txt').read()
        print showUser
        self.showUserName.setText(str('   ' + 'Hello' + ' ' + showUser))

    def typingManual(self):
        import webbrowser
        webbrowser.open_new(r'Typing_manual.pdf')


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
    audioStr = ''
    audioEditStr = ''
    result = ''
    result1 = ''
    result2 = ''
    Client = 1
    st = ''
    cont = 0

    start_time = time()
    print start_time
    app = QtGui.QApplication(sys.argv)
    O = QtGui.QWidget()
    ui = Ui_O()
    ui.setupUi(O)
    ui.showName()
    ui.changeUserName.clicked.connect(ui.enterUsername)
    ui.Score.clicked.connect(ui.resultWindow)
    ui.Instrution.clicked.connect(ui.typingManual)
    O.show()

    #ui.update_currentAffairs()
    #ui.update_news()

    #creating an object 
    wordObj = wordMap.Ui_Form() #create an global object of wordMap
    prac_sess = Practice_start.Ui_Form() #create an global object of practice_start session
    sessionMode = selectSession.Ui_Form() #create an global object of select session
    mapTime = timeMap.Ui_Form() #create an global object of timeMap
    usernameWin = usernameWindow.Ui_Form() #create an global object of usernameWindow
    audioObj = audio_edit.Ui_Audio()
    challengeCreate = createChallenge.Ui_Form()
    wordMapChallenge = challengeWordMap.Ui_Form()
    timeChallenge = challengeTimeMap.Ui_Form()
    joinChallenge = Join.Ui_Dialog()
    multiTypeObject = multiType.Ui_Form()
    #startedServer = socket.socket()
    #media_obj = Phonon.MediaObject(O)
    #section for username
    username = QtGui.QWidget()
    resultWin = resultWindow.Ui_Dialog()
    if userText == '':
        ui.enterUsername()

    #cretae a timer
    timer = QTimer()
    timer.q = 0
    s = 0
    app.exec_()
    sys.exit(0)
