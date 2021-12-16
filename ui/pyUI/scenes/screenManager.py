# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainzhbIGI.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sqlite3
import sys

import pandas as pd
from PyQt5 import QtCore,QtWidgets
from PyQt5.QtCore import QPoint, Qt, QTimer, QSize
from PyQt5.QtGui import QColor, QMovie
from PyQt5.QtWidgets import *


from models import recommender
from models.dbHelper import DBHelper
from ui.pyUI.scenes import login, signUp
from ui.pyUI.scenes.bookRecommendation import Ui_BookRecommendationForm
from ui.pyUI.scenes.chooseBook import Ui_ChooseBookForm
from ui.pyUI.scenes.chooseTvSeries import Ui_ChooseTVSeriesForm
from ui.pyUI.scenes.favorites import Ui_FavoritesForm
from ui.pyUI.scenes.mainMenu import Ui_MainMenu
from ui.pyUI.scenes.splash import Ui_SplashForm
## ==> GLOBALS
from ui.pyUI.scenes.tvSeriesRecommendation import Ui_TvSeriesRecommendationForm

counter = 0
df_Books = pd.read_csv('C:/Users\onursercanyilmaz\Documents\GitHub\RecSy\ml\df_books.csv')
df_TVSeries = pd.read_csv('C:/Users\onursercanyilmaz\Documents\GitHub\RecSy\ml\df_tvSeries.csv')
recommendedBooks = {}


# YOUR APPLICATION
class Login(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = login.Ui_LoginForm()
        self.ui.setupUi(self)

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.oldPos = self.pos()
        self.show()

        self.ui.btnDirectSignUp.clicked.connect(self.directToSignUp)
        self.ui.btnLogin.clicked.connect(self.loginCheck)

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def directToSignUp(self):
        self.main = SignUp()
        self.main.show()
        self.close()

    def loginCheck(self):
        print("login button clicked")
        username = self.ui.lineEdit_Username.text()
        password = self.ui.lineEdit_Password.text()

        connection = sqlite3.connect("C:/Users/onursercanyilmaz/Documents/GitHub/RecSy/db/RESCSYdb.db")

        result = connection.execute('''SELECT * FROM users WHERE username=? and password=?''', (username, password))

        if ((len(result.fetchall()) > 0)):
            print("USER FOUND")
            self.mainScene = MainMenu()
            self.mainScene.show()
            self.close()
        else:
            print("USER NOT FOUND")
            self.msgBox = QMessageBox.warning(self.ui.loginFrame, "WARNING", "Your Password INCORRECT!")
            self.msgBox.execute()


class SignUp(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = signUp.Ui_SignUpForm()
        self.ui.setupUi(self)
        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.oldPos = self.pos()
        self.show()

        self.ui.btnDirectLogin.clicked.connect(self.directToLogin)

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def directToLogin(self):
        self.sign = Login()
        self.sign.show()
        self.close()


class ChooseBook(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_ChooseBookForm()
        self.ui.setupUi(self)

        DBHelper.loadBooksToComboBox(DBHelper, self.ui.comboBox_Books)


        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.oldPos = self.pos()
        self.show()

        self.ui.btnBack.clicked.connect(self.directToHome),



        self.ui.btnSelect.clicked.connect(self.selectBook)

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def directToHome(self):
        self.main = MainMenu()
        self.main.show()
        self.close()

    def loadLading(self):
        self.loadingWidget = LoadingScreen()
        self.loadingWidget.show()

    def selectBook(self):

        self.bookName = self.getBookName()
        self.recommendedBooks = recommender.bookRecommendations(self.bookName, df_Books)

        self.bookRecs = BookRecommendation()

        for i in range(0,5):
            self.item = QtWidgets.QListWidgetItem()
            self.item.setCheckState(QtCore.Qt.Unchecked)
            self.item = self.bookRecs.ui.list_bookRecommendations.item(i)
            self.item.setText(self.recommendedBooks['item'+str(i+1)]['title'] + " -- " + self.recommendedBooks['item'+str(i+1)]['author'] + " -- Similarity: " + str(self.recommendedBooks['item'+str(i+1)]['similarity']))
            self.bookRecs.ui.list_bookRecommendations.addItem(self.item)

        self.bookRecs.show()
        self.close()


    def getBookName(self):
        self.currentSelected = self.ui.comboBox_Books.currentText()
        self.bookInfo = self.currentSelected.split(' -- ')
        self.bookName = self.bookInfo[0]
        return  self.bookName




class ChooseTVSeries(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_ChooseTVSeriesForm()
        self.ui.setupUi(self)

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.oldPos = self.pos()

        self.show()

        self.ui.btnBack.clicked.connect(self.directToHome)

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def directToHome(self):
        self.main = MainMenu()
        self.main.show()
        self.close()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


class Favorites(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_FavoritesForm()
        self.ui.setupUi(self)

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.oldPos = self.pos()
        self.show()

        self.ui.btnGoHome.clicked.connect(self.directToHome)

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def directToHome(self):
        self.main = MainMenu()
        self.main.show()
        self.close()


class MainMenu(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainMenu()
        self.ui.setupUi(self)

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.oldPos = self.pos()

        self.show()

        self.ui.btnChooseBookCategory.clicked.connect(self.directToChooseBook)
        self.ui.btnChooseMovieCategory.clicked.connect(self.directToChooseTVSeries)
        self.ui.btnGoProfile_2.clicked.connect(self.directToFavorites)

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def directToChooseBook(self):
        print("clicked")
        self.directChooseBook = ChooseBook()
        self.directChooseBook.show()
        self.close()

    def directToChooseTVSeries(self):
        self.directChooseTVSeries = ChooseTVSeries()
        self.directChooseTVSeries.show()
        self.close()

    def directToFavorites(self):
        self.directFavorites = Favorites()
        self.directFavorites.show()
        self.close()


class BookRecommendation(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_BookRecommendationForm()
        self.ui.setupUi(self)

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.oldPos = self.pos()
        self.show()

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()




class TVSeriesRecommendation(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_TvSeriesRecommendationForm()
        self.ui.setupUi(self)

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.oldPos = self.pos()
        self.show()

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()


# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashForm()
        self.ui.setupUi(self)

        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        # ♣self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):
        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = Login()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1


class LoadingScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(200, 200)

        ## REMOVE TITLE BAR
        # self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.label_loading = QLabel(self)
        self.label_loading.resize(200, 200)
        self.movie = QMovie('C:/Users\onursercanyilmaz\Documents\GitHub\RecSy\img\loading.gif')
        self.movie.scaledSize()
        self.movie.setScaledSize(QSize().scaled(200, 200, Qt.KeepAspectRatio))

        self.label_loading.setMovie(self.movie)

        timer = QTimer(self)
        self.startAnimation()
        timer.singleShot(4000, self.stopAnimation)

        self.show()

    def startAnimation(self):
        self.movie.start()

    def stopAnimation(self):
        self.movie.stop()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChooseBook()
    # app.setWindowIcon(QIcon("RecSy.ico"))

    sys.exit(app.exec_())
