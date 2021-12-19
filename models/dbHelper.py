import sqlite3
from operator import index

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox, QListWidget


class DBHelper:
    def __init__(self):
        pass

    def getBookIdByTitleAndAuthor(self, bookName, bookAuthor):
        conn = sqlite3.connect('C:/Users\onursercanyilmaz\Documents\GitHub\RecSy\db\RESCSYdb.db')
        result = conn.execute('''SELECT book_id FROM books WHERE book_title=? and book_author=?''',
                              (bookName, bookAuthor))
        bookId = result.fetchall()
        conn.close()
        return bookId[0][0]

    def getTVSeriesIdByTitle(self, tvSeriesName):
        conn = sqlite3.connect('C:/Users\onursercanyilmaz\Documents\GitHub\RecSy\db\RESCSYdb.db')
        print("connected")
        result = conn.execute('''SELECT * FROM tv_series WHERE tv_series_title=?''', (tvSeriesName,))
        print("get ok")
        tvSeriesId = result.fetchall()

        conn.close()
        return tvSeriesId[0][0]

    def loadBooksToComboBox(self, comboBox):
        conn = sqlite3.connect('C:/Users\onursercanyilmaz\Documents\GitHub\RecSy\db\RESCSYdb.db')
        result = conn.execute('''SELECT book_id, book_title,book_author FROM books''')
        # TODO: load all "book title -- book author" to BooksCombobox... we will use id for ML part!
        for i in result:
            comboBox.addItem(i[1] + " -- " + i[2])

        conn.close()

    def loadToTVSeriesComboBox(self, comboBox):
        conn = sqlite3.connect('C:/Users\onursercanyilmaz\Documents\GitHub\RecSy\db\RESCSYdb.db')
        result = conn.execute('''SELECT tv_series_id, tv_series_title FROM tv_series''')

        # TODO: load all "tv series title " to TVSeriesCombobox

        for i in result:
            comboBox.addItem(i[1])
        conn.close()


    def loadFavoriteBooks(self, bookFavorites, userid):
        conn = sqlite3.connect('C:/Users\onursercanyilmaz\Documents\GitHub\RecSy\db\RESCSYdb.db')
        result = conn.execute(
            '''SELECT DISTINCT book_favorites.book_id, books.book_title, books.book_author FROM books LEFT JOIN book_favorites ON  books.book_id = book_favorites.book_id WHERE user_id=(?)''',
            str(userid))
        self.gotBooks= result.fetchall()

        if len(self.gotBooks) > 0:
            self.flag = 0
            for i in self.gotBooks:
                print(i[1] + " -- " + i[2])
                item = QtWidgets.QListWidgetItem()
                item.setCheckState(QtCore.Qt.Unchecked)
                item.setText(i[1] + " -- " + i[2])
                bookFavorites.addItem(item)
        else:
            self.item  = QtWidgets.QListWidgetItem()

            self.item .setText("Empty List")
            bookFavorites.addItem(self.item )

        conn.close()

    def loadFavoriteTVSeries(self,tvSeriesFavorites,userid):
        conn = sqlite3.connect('C:/Users\onursercanyilmaz\Documents\GitHub\RecSy\db\RESCSYdb.db')
        result = conn.execute(
            '''SELECT DISTINCT tv_series_favorites.tv_series_id, tv_series.tv_series_title FROM tv_series LEFT JOIN tv_series_favorites ON  tv_series.tv_series_id = tv_series_favorites.tv_series_id WHERE user_id=(?)''',
            str(userid))
        self.gotSeries = result.fetchall()

        if len(self.gotSeries) > 0:
            self.flag = 0
            for i in self.gotSeries:
                print(i[1])
                item = QtWidgets.QListWidgetItem()
                item.setCheckState(QtCore.Qt.Unchecked)
                item.setText(i[1])
                tvSeriesFavorites.addItem(item)
        else:
            self.item = QtWidgets.QListWidgetItem()

            self.item.setText("Empty List")
            tvSeriesFavorites.addItem(self.item)

        conn.close()

    def addFavoriteBook(self, user_id, book_id):
        conn = sqlite3.connect('C:/Users\onursercanyilmaz\Documents\GitHub\RecSy\db\RESCSYdb.db')
        conn.execute('''INSERT INTO book_favorites(user_id,book_id) VALUES (?,?)''', (user_id, book_id))
        print("insert is ok")
        conn.commit()
        conn.close()

    def addFavoriteTVSeries(self, user_id,series_id):
        conn = sqlite3.connect('C:/Users\onursercanyilmaz\Documents\GitHub\RecSy\db\RESCSYdb.db')
        conn.execute('''INSERT INTO tv_series_favorites(user_id,tv_series_id) VALUES (?,?)''', (user_id, series_id))
        print("insert is ok")
        conn.commit()
        conn.close()

    def addNewUser(self, username, password, email, frameName):
        conn = sqlite3.connect('C:/Users\onursercanyilmaz\Documents\GitHub\RecSy\db\RESCSYdb.db')
        result = conn.execute('''SELECT username,email FROM users''')
        for i in result:
            if i[0] == self.username or i[1] == self.email:
                msgBox = QMessageBox.warning(frameName, "WARNING", "Username or Email is ALREADY EXIST!")
                msgBox.execute()
            else:
                conn.execute('''INSERT INTO users() VALUES(?,?,?)''', (username, password, email))
                conn.commit()
        conn.close()



    def removeFavoriteBook(self,book_id,user_id):
        conn = sqlite3.connect('C:/Users\onursercanyilmaz\Documents\GitHub\RecSy\db\RESCSYdb.db')
        conn.execute('''DELETE FROM book_favorites WHERE book_id=? and user_id=?''',(book_id,user_id))

        # TODO: removing checked books to favorites and see in fav lists... after removing, use load!
        conn.commit()
        conn.close()

    def removeFavoriteTVSeries(self,series_id,user_id):
        conn = sqlite3.connect('C:/Users\onursercanyilmaz\Documents\GitHub\RecSy\db\RESCSYdb.db')
        conn.execute('''DELETE FROM tv_series_favorites WHERE tv_series_id=? and user_id=?''', (series_id, user_id))


        conn.commit()
        conn.close()

    def loadUserData(self):
        conn = sqlite3.connect('C:/Users\onursercanyilmaz\Documents\GitHub\RecSy\db\RESCSYdb.db')
        result = conn.execute('''SELECT tv_series_id, tv_series_title FROM tv_series''')

        # TODO: load user Name to show on Profile... Add a Label!
        conn.close()

    def getBookName(self, cb):
        print(cb.currentText())

