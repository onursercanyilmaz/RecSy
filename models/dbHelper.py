import sqlite3
from operator import index

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox


class DBHelper:
    def __init__(self):
        pass






    def loadBooksToComboBox(self, comboBox):
        conn = sqlite3.connect('C:/Users\onursercanyilmaz\Documents\GitHub\RecSy\db\RESCSYdb.db');
        result = conn.execute('''SELECT book_id, book_title,book_author FROM books''')

        #TODO: load all "book title -- book author" to BooksCombobox... we will use id for ML part!
        for i in result:
            comboBox.addItem(i[1]+" -- "+i[2])
        conn.close()

    def loadToTVSeriesComboBox(self, comboBox):
        conn = sqlite3.connect('C:/Users\onursercanyilmaz\Documents\GitHub\RecSy\db\RESCSYdb.db')
        result = conn.execute('''SELECT tv_series_id, tv_series_title FROM tv_series''')

        # TODO: load all "tv series title " to TVSeriesCombobox

        for i in result:
            comboBox.addItem(i[1])
        conn.close()





    def loadFavoriteBooks(self,bookFavorites):
        conn = sqlite3.connect('C:/Users\onursercanyilmaz\Documents\GitHub\RecSy\db\RESCSYdb.db')
        result = conn.execute('''SELECT book_favorites.book_id, book_title, book_author FROM book_favorites LEFT JOIN books ON books.book_id = book_favorites.book_id ''')

        # TODO: see favorite books on list

        for i in result:
            item = QtWidgets.QListWidgetItem()
            item.setCheckState(QtCore.Qt.Unchecked)
            item.setText(i[1]+" -- "+i[2])
            bookFavorites.addItem(item)


        conn.close()



    def loadFavoriteTVSeries(self):
        conn = sqlite3.connect('C:/Users\onursercanyilmaz\Documents\GitHub\RecSy\db\RESCSYdb.db')
        result = conn.execute('''SELECT tv_series_id, tv_series_title FROM tv_series''')

        # TODO: see favorite tv series on list
        conn.close()

    def addFavoriteBook(self):
        conn = sqlite3.connect('C:/Users\onursercanyilmaz\Documents\GitHub\RecSy\db\RESCSYdb.db')
        result = conn.execute('''SELECT tv_series_id, tv_series_title FROM tv_series''')

        # TODO: adding checked books to favorites and see in fav lists...
        conn.close()

    def addFavoriteTVSeries(self):
        conn = sqlite3.connect('C:/Users\onursercanyilmaz\Documents\GitHub\RecSy\db\RESCSYdb.db')
        result = conn.execute('''SELECT tv_series_id, tv_series_title FROM tv_series''')

        # TODO: adding checked tv series to favorites and see in fav lists
        conn.close()

    def removeFavoriteBook(self):
        conn = sqlite3.connect('C:/Users\onursercanyilmaz\Documents\GitHub\RecSy\db\RESCSYdb.db')
        result = conn.execute('''SELECT tv_series_id, tv_series_title FROM tv_series''')

        # TODO: removing checked books to favorites and see in fav lists... after removing, use load!
        conn.close()

    def removeFavoriteTVSeries(self):
        conn = sqlite3.connect('C:/Users\onursercanyilmaz\Documents\GitHub\RecSy\db\RESCSYdb.db')
        result = conn.execute('''SELECT tv_series_id, tv_series_title FROM tv_series''')

        # TODO: removing checked tv series to favorites and see in fav lists... after removing, use load!
        conn.close()

    def loadUserData(self):
        conn = sqlite3.connect('C:/Users\onursercanyilmaz\Documents\GitHub\RecSy\db\RESCSYdb.db')
        result = conn.execute('''SELECT tv_series_id, tv_series_title FROM tv_series''')

        # TODO: load user Name to show on Profile... Add a Label!
        conn.close()

    def getBookName(self,cb):
        print(cb.currentText())
