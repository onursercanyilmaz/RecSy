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
import re
from PyQt5 import QtCore,QtWidgets
from PyQt5.QtCore import QPoint, Qt, QTimer, QSize
from PyQt5.QtGui import QColor, QMovie, QIcon
from PyQt5.QtWidgets import *


from models import recommender
from models.dbHelper import DBHelper
from models.user import *
from ui.pyUI.scenes import login, signUp, favorites
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
username = ""
id = 0
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


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
        self.username = self.ui.lineEdit_Username.text()
        self.password = self.ui.lineEdit_Password.text()

        connection = sqlite3.connect("C:/Users/onursercanyilmaz/Documents/GitHub/RecSy/db/RESCSYdb.db")

        result = connection.execute('''SELECT * FROM users WHERE username=? and password=?''', (self.username, self.password))
        user = result.fetchall()

        if ((len(user) > 0)):
            print("USER FOUND")
            userId = user[0][0]
            userName = user[0][1]
            userMail = user[0][3]
            global id
            id = userId
            global username
            username = userName
            self.mainScene = MainMenu()
            self.mainScene.show()
            self.close()

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("ACCESS DENIED!")
            msg.setInformativeText('Your username or password is WRONG!')
            msg.setWindowTitle("Error")
            msg.setMinimumSize(400, 100)
            msg.setWindowIcon(QIcon("C:/Users\onursercanyilmaz\Documents\GitHub\RecSy\img\RecSy.png"))
            msg.exec_()




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
        self.ui.btnSignUp.clicked.connect(self.register)

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


    global regex
    def check(self,email):
        if (re.search(regex, email)):
            return True
        else:
            return  False

    def register(self):
        print("sign up button clicked")
        self.username = self.ui.lineEdit_Username.text()
        self.password = self.ui.lineEdit_Password.text()
        self.email = self.ui.lineEdit_Email.text()

        if self.check(self.email):
            conn = sqlite3.connect('C:/Users\onursercanyilmaz\Documents\GitHub\RecSy\db\RESCSYdb.db')
            self.result = conn.execute('''SELECT username,email FROM users WHERE username=? or email=?''',(self.username,self.email))



            if len(self.result.fetchall())>0:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Invalid Information")
                msg.setInformativeText('Username or email has Already Taken!')
                msg.setWindowTitle("Error")
                msg.setMinimumSize(400, 100)
                msg.setWindowIcon(QIcon("C:/Users\onursercanyilmaz\Documents\GitHub\RecSy\img\RecSy.png"))
                msg.exec_()

            else:
                conn.execute('''INSERT INTO users(username,password,email) VALUES(?,?,?)''', (self.username, self.password, self.email))
                conn.commit()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.NoIcon)
                msg.setText("Signed Up Successfully!")
                msg.setInformativeText('You can login.')
                msg.setWindowTitle("Successfull Process!")
                msg.setMinimumSize(400, 100)
                msg.setWindowIcon(QIcon("C:/Users\onursercanyilmaz\Documents\GitHub\RecSy\img\RecSy.png"))
                msg.exec_()

            conn.close()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("EMAIL INVALID")
            msg.setInformativeText('Please enter a real mail address!')
            msg.setWindowTitle("Error")
            msg.setMinimumSize(400, 100)
            msg.setWindowIcon(QIcon("C:/Users\onursercanyilmaz\Documents\GitHub\RecSy\img\RecSy.png"))
            msg.exec_()






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

        self.ui.btnBack.clicked.connect(self.directToHome)
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
        DBHelper.loadToTVSeriesComboBox(DBHelper, self.ui.comboBox_TvSeries)
        self.ui.btnBack.clicked.connect(self.directToHome)
        self.ui.btnSelect.clicked.connect(self.selectTVSeries)

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

    def selectTVSeries(self):

        self.seriesName = self.getTVSeriesName()
        self.recommendedSeries = recommender.tvSeriesRecommendations(self.seriesName, df_TVSeries)


        self.seriesRecs = TVSeriesRecommendation()

        for i in range(0,5):
            self.item = QtWidgets.QListWidgetItem()
            self.item.setCheckState(QtCore.Qt.Unchecked)

            #self.item = self.seriesRecs.ui.list_SeriesRecommendations.item(i)

            self.item.setText(self.recommendedSeries['item'+str(i+1)]['title'] + " -- Similarity: " + str(self.recommendedSeries['item'+str(i+1)]['similarity']))
            self.seriesRecs.ui.list_SeriesRecommendations.addItem(self.item)


        self.seriesRecs.show()
        self.close()


    def getTVSeriesName(self):
        self.currentSelected = self.ui.comboBox_TvSeries.currentText()
        return self.currentSelected






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
        self.ui.btnRemoveFavBook.clicked.connect(self.removeBooksFromFavorites)
        self.ui.btnRemoveFavTvSeries.clicked.connect(self.removeSeriesFromFavorites)


        self.loadFavBooks()
        self.loadFavTvSeries()


        global username
        self.ui.label_9.setText(username+"'s Favorites")


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

    def loadFavBooks(self):
        self.ui.list_favBooks.clear()
        global id
        DBHelper.loadFavoriteBooks(DBHelper, self.ui.list_favBooks, id)

    def loadFavTvSeries(self):
        self.ui.list_favtvSeries.clear()
        global id
        DBHelper.loadFavoriteTVSeries(DBHelper, self.ui.list_favtvSeries, id)

    def checkedFavorites(self,favList):
        self.checkedItems=[]
        for index in range(favList.count()):
            if favList.item(index).checkState() == Qt.Checked:
                self.checkedItems.append(favList.item(index))
        return self.checkedItems

    def showMessage(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.NoIcon)
        msg.setText("Removed Successfully!")
        msg.setInformativeText('')
        msg.setWindowTitle("Process Completed!")
        msg.setMinimumSize(400, 100)
        msg.setWindowIcon(QIcon("C:/Users\onursercanyilmaz\Documents\GitHub\RecSy\img\RecSy.png"))
        msg.exec_()

    def removeBooksFromFavorites(self):
        global id #for user_id
        for i in self.checkedFavorites(self.ui.list_favBooks):
            self.bookInfo = i.text().split(" -- ")
            self.bookName = self.bookInfo[0]
            self.bookAuthor = self.bookInfo[1]
            self.bookId = DBHelper.getBookIdByTitleAndAuthor(DBHelper,self.bookName,self.bookAuthor)

            DBHelper.removeFavoriteBook(DBHelper,self.bookId,id)
        self.loadFavBooks()
        self.showMessage()

    def removeSeriesFromFavorites(self):
        global id #for user_id
        for i in self.checkedFavorites(self.ui.list_favtvSeries):
            self.seriesName = i.text()

            self.seriesId = DBHelper.getTVSeriesIdByTitle(DBHelper,self.seriesName)

            DBHelper.removeFavoriteTVSeries(DBHelper,self.seriesId,id)
        self.loadFavTvSeries()
        self.showMessage()


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
        self.ui.btnLogout.clicked.connect(self.logOut)


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
    def logOut(self):
        self.directLogin = Login()
        self.directLogin.show()
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

        self.ui.btnGoHome.clicked.connect(self.directToHome)
        self.ui.btnAddFav.clicked.connect(self.addToFavorites)

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

    def chooseFavorites(self):
        self.checkedItems=[]
        for index in range(self.ui.list_bookRecommendations.count()):
            if self.ui.list_bookRecommendations.item(index).checkState() == Qt.Checked:
                self.checkedItems.append(self.ui.list_bookRecommendations.item(index))
        print(self.checkedItems[0].text())
        return self.checkedItems

    def addToFavorites(self):
        global id
        for i in self.chooseFavorites():
            self.bookWithoutSimilarity = i.text().split(" -- ")
            self.bookName = self.bookWithoutSimilarity[0]
            self.bookAuthor = self.bookWithoutSimilarity[1]

            self.bookName = self.bookName.replace('"' , '' )
            self.bookName = self.bookName.replace("#" , '')
            self.bookName = self.bookName.replace("`", '')

            self.bookAuthor = self.bookAuthor.replace('"', '')
            self.bookAuthor = self.bookAuthor.replace("#", '')
            self.bookAuthor = self.bookAuthor.replace("`", '')


            self.bookId = DBHelper.getBookIdByTitleAndAuthor(DBHelper,self.bookName,self.bookAuthor)
            print(self.bookId)
            #self.theBook = self.bookName + " -- " + self.bookAuthor

            DBHelper.addFavoriteBook(DBHelper,id,self.bookId)
        self.showMessage()

    def showMessage(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.NoIcon)
        msg.setText("Books Added Successfully!")
        msg.setInformativeText('')
        msg.setWindowTitle("Process Completed!")
        msg.setMinimumSize(400, 100)
        msg.setWindowIcon(QIcon("C:/Users\onursercanyilmaz\Documents\GitHub\RecSy\img\RecSy.png"))
        msg.exec_()




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


        self.ui.btnBack.clicked.connect(self.directToHome)
        self.ui.btnAddFavorite.clicked.connect(self.addToFavorites)

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

    def chooseFavorites(self):
        self.checkedItems=[]
        for index in range(self.ui.list_SeriesRecommendations.count()):
            if self.ui.list_SeriesRecommendations.item(index).checkState() == Qt.Checked:
                self.checkedItems.append(self.ui.list_SeriesRecommendations.item(index))
        print(self.checkedItems[0].text())
        return self.checkedItems

    def addToFavorites(self):
        global id
        for i in self.chooseFavorites():
            self.seriesWithoutSimilarity = i.text().split(" -- ")
            self.seriesName = self.seriesWithoutSimilarity[0]
            print(self.seriesName)
            self.seriesId = DBHelper.getTVSeriesIdByTitle(DBHelper,self.seriesName)
            print(self.seriesId)

            DBHelper.addFavoriteTVSeries(DBHelper,id,self.seriesId)
        self.showMessage()

    def showMessage(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.NoIcon)
        msg.setText("TV Series Added Successfully!")
        msg.setInformativeText('')
        msg.setWindowTitle("Process Completed!")
        msg.setMinimumSize(400, 100)
        msg.setWindowIcon(QIcon("C:/Users\onursercanyilmaz\Documents\GitHub\RecSy\img\RecSy.png"))
        msg.exec_()


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
    window = Login()
    # app.setWindowIcon(QIcon("RecSy.ico"))

    sys.exit(app.exec_())
