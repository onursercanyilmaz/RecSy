# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'favorites.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FavoritesForm(object):
    def setupUi(self, FavoritesForm):
        FavoritesForm.setObjectName("FavoritesForm")
        FavoritesForm.resize(1330, 742)
        FavoritesForm.setStyleSheet(" border-style: solid;\n"
"  border-color: #ff0000; /* red */")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(FavoritesForm)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.favoritesFrame = QtWidgets.QFrame(FavoritesForm)
        self.favoritesFrame.setStyleSheet("QFrame{background:#300331;\n"
"border-style: solid;\n"
"  border-color: red;\n"
"border-radius:40;}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"background: qradialgradient(\n"
"cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
");\n"
"}\n"
"\n"
"QSplitter::handle {\n"
"    background: none;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border-style: inset;\n"
"background: qradialgradient(\n"
"cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
");}")
        self.favoritesFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.favoritesFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.favoritesFrame.setObjectName("favoritesFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.favoritesFrame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter = QtWidgets.QSplitter(self.favoritesFrame)
        self.splitter.setStyleSheet("background:none;")
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.barLogo = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.barLogo.setContentsMargins(0, 0, 0, 0)
        self.barLogo.setObjectName("barLogo")
        self.TabBar = QtWidgets.QGroupBox(self.layoutWidget)
        self.TabBar.setMinimumSize(QtCore.QSize(0, 50))
        self.TabBar.setMaximumSize(QtCore.QSize(16777215, 50))
        self.TabBar.setStyleSheet("background:#920C7C;\n"
"border: 2px solid white;\n"
"border-radius:0;\n"
"border-top-left-radius: 40;\n"
"border-top-right-radius: 40;\n"
"")
        self.TabBar.setTitle("")
        self.TabBar.setObjectName("TabBar")
        self.btnClose = QtWidgets.QPushButton(self.TabBar)
        self.btnClose.setGeometry(QtCore.QRect(30, 20, 20, 20))
        self.btnClose.setStyleSheet("QPushButton{\n"
"background-color: #FD5754;\n"
"border-style: solid;\n"
"border-color: white;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: #37AED4;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border-style: inset;\n"
"background: qradialgradient(\n"
"cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
");}")
        self.btnClose.setText("")
        self.btnClose.setObjectName("btnClose")
        self.btnminimize = QtWidgets.QPushButton(self.TabBar)
        self.btnminimize.setGeometry(QtCore.QRect(50, 20, 20, 20))
        self.btnminimize.setStyleSheet("QPushButton{\n"
"background-color: #F9B637;\n"
"border-style: solid;\n"
"border-color: white;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: #37AED4;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border-style: inset;\n"
"background: qradialgradient(\n"
"cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
");}")
        self.btnminimize.setText("")
        self.btnminimize.setObjectName("btnminimize")
        self.btnZoom = QtWidgets.QPushButton(self.TabBar)
        self.btnZoom.setGeometry(QtCore.QRect(70, 20, 20, 20))
        self.btnZoom.setStyleSheet("QPushButton{\n"
"background-color: #34C848;\n"
"border-style: solid;\n"
"border-color: white;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"background: #37AED4;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border-style: inset;\n"
"background: qradialgradient(\n"
"cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
");}")
        self.btnZoom.setText("")
        self.btnZoom.setObjectName("btnZoom")
        self.barLogo.addWidget(self.TabBar)
        self.BooksLogo = QtWidgets.QGroupBox(self.layoutWidget)
        self.BooksLogo.setMinimumSize(QtCore.QSize(0, 75))
        self.BooksLogo.setStyleSheet("border:none;")
        self.BooksLogo.setTitle("")
        self.BooksLogo.setObjectName("BooksLogo")
        self.label_9 = QtWidgets.QLabel(self.BooksLogo)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 571, 75))
        self.label_9.setMinimumSize(QtCore.QSize(50, 75))
        self.label_9.setStyleSheet("background:none;\n"
"font-size:30px;\n"
"color:white;\n"
"font-weight:bold;\n"
"font-family:google sans;\n"
"image: url(:/logo/img/RecSy.png);")
        self.label_9.setObjectName("label_9")
        self.barLogo.addWidget(self.BooksLogo)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.WholeBody = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.WholeBody.setContentsMargins(25, 0, 25, 15)
        self.WholeBody.setObjectName("WholeBody")
        self.body = QtWidgets.QSplitter(self.layoutWidget1)
        self.body.setStyleSheet("QSplitter::handle {\n"
"    background: none;\n"
"}")
        self.body.setOrientation(QtCore.Qt.Vertical)
        self.body.setObjectName("body")
        self.hereIs = QtWidgets.QSplitter(self.body)
        self.hereIs.setOrientation(QtCore.Qt.Vertical)
        self.hereIs.setObjectName("hereIs")
        self.layoutWidget2 = QtWidgets.QWidget(self.hereIs)
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.profilePic = QtWidgets.QLabel(self.layoutWidget2)
        self.profilePic.setMinimumSize(QtCore.QSize(0, 100))
        self.profilePic.setStyleSheet("image: url(:/favoritesPerson/img/favorites_person.png);")
        self.profilePic.setText("")
        self.profilePic.setObjectName("profilePic")
        self.verticalLayout_3.addWidget(self.profilePic)
        self.gridLayoutWidget = QtWidgets.QWidget(self.body)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.list_favBooks = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.list_favBooks.setMinimumSize(QtCore.QSize(0, 300))
        self.list_favBooks.setStyleSheet("QListWidget{\n"
"color:white;\n"
"font-size:30px;\n"
"font-family:Google Sans;\n"
"background:#300331;\n"
"border:1px solid white;\n"
"padding:30px;\n"
"\n"
"}")
        self.list_favBooks.setObjectName("list_favBooks")
        item = QtWidgets.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.list_favBooks.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_favBooks.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_favBooks.addItem(item)
        self.gridLayout_2.addWidget(self.list_favBooks, 4, 0, 1, 1)
        self.list_favtvSeries = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.list_favtvSeries.setMinimumSize(QtCore.QSize(0, 300))
        self.list_favtvSeries.setStyleSheet("QListWidget{\n"
"color:white;\n"
"font-size:30px;\n"
"font-family:Google Sans;\n"
"background:#300331;\n"
"border:1px solid white;\n"
"padding:30px;\n"
"\n"
"}")
        self.list_favtvSeries.setObjectName("list_favtvSeries")
        self.gridLayout_2.addWidget(self.list_favtvSeries, 4, 1, 1, 1)
        self.label_added_books = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_added_books.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_added_books.setStyleSheet("color:white;\n"
"font-size:25px;\n"
"font-family: google sans;\n"
"font-weight:bold;\n"
"\n"
"\n"
"")
        self.label_added_books.setAlignment(QtCore.Qt.AlignCenter)
        self.label_added_books.setObjectName("label_added_books")
        self.gridLayout_2.addWidget(self.label_added_books, 1, 0, 1, 1)
        self.label_added_tvSeries = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_added_tvSeries.setStyleSheet("color:white;\n"
"font-size:25px;\n"
"font-family: google sans;\n"
"font-weight:bold;\n"
"\n"
"\n"
"")
        self.label_added_tvSeries.setAlignment(QtCore.Qt.AlignCenter)
        self.label_added_tvSeries.setObjectName("label_added_tvSeries")
        self.gridLayout_2.addWidget(self.label_added_tvSeries, 1, 1, 1, 1)
        self.WholeBody.addWidget(self.body)
        self.bottomBar = QtWidgets.QSplitter(self.layoutWidget1)
        self.bottomBar.setMinimumSize(QtCore.QSize(0, 50))
        self.bottomBar.setStyleSheet("QSplitter::handle {\n"
"    background: none;\n"
"}")
        self.bottomBar.setOrientation(QtCore.Qt.Horizontal)
        self.bottomBar.setObjectName("bottomBar")
        self.btnRemoveFavBook = QtWidgets.QToolButton(self.bottomBar)
        self.btnRemoveFavBook.setStyleSheet("QToolButton{\n"
"background:transparent;\n"
"    image: url(:/removeFavorite/img/removeFavorite.png);\n"
"}\n"
"QToolButton:hover {\n"
"background: #920C7C;\n"
"border: solid 1px;\n"
"border-radius:25;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"border-style: inset;\n"
"background: #37AED4;}")
        self.btnRemoveFavBook.setText("")
        self.btnRemoveFavBook.setObjectName("btnRemoveFavBook")
        self.btnGoHome = QtWidgets.QToolButton(self.bottomBar)
        self.btnGoHome.setStyleSheet("QToolButton{\n"
"background:transparent;\n"
"    image: url(:/home/img/home.png);\n"
"}\n"
"QToolButton:hover {\n"
"background: #920C7C;\n"
"border: solid 1px;\n"
"border-radius:25;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"border-style: inset;\n"
"background: #37AED4;}")
        self.btnGoHome.setText("")
        self.btnGoHome.setObjectName("btnGoHome")
        self.btnRemoveFavTvSeries = QtWidgets.QToolButton(self.bottomBar)
        self.btnRemoveFavTvSeries.setStyleSheet("QToolButton{\n"
"background:transparent;\n"
"image: url(:/removeFavorite/img/removeFavorite.png);\n"
"text-align: left;\n"
"}\n"
"QToolButton:hover {\n"
"background: #920C7C;\n"
"border: solid 1px;\n"
"border-radius:25;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"border-style: inset;\n"
"background: #37AED4;}")
        self.btnRemoveFavTvSeries.setText("")
        self.btnRemoveFavTvSeries.setObjectName("btnRemoveFavTvSeries")
        self.WholeBody.addWidget(self.bottomBar)
        self.horizontalLayout.addWidget(self.splitter)
        self.verticalLayout_4.addWidget(self.favoritesFrame)

        self.retranslateUi(FavoritesForm)
        QtCore.QMetaObject.connectSlotsByName(FavoritesForm)

    def retranslateUi(self, FavoritesForm):
        _translate = QtCore.QCoreApplication.translate
        FavoritesForm.setWindowTitle(_translate("FavoritesForm", "Form"))
        self.label_9.setText(_translate("FavoritesForm", "My Favorites"))
        __sortingEnabled = self.list_favBooks.isSortingEnabled()
        self.list_favBooks.setSortingEnabled(False)
        item = self.list_favBooks.item(0)
        item.setText(_translate("FavoritesForm", "New ItemNew ItemNew ItemNew ItemNew ItemNew ItemNew ItemNew ItemNew Item"))
        item = self.list_favBooks.item(1)
        item.setText(_translate("FavoritesForm", "New Item"))
        item = self.list_favBooks.item(2)
        item.setText(_translate("FavoritesForm", "New Item"))
        self.list_favBooks.setSortingEnabled(__sortingEnabled)
        self.label_added_books.setText(_translate("FavoritesForm", "Added Books"))
        self.label_added_tvSeries.setText(_translate("FavoritesForm", "Added TV Series"))

import source_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FavoritesForm = QtWidgets.QWidget()
    ui = Ui_FavoritesForm()
    ui.setupUi(FavoritesForm)
    FavoritesForm.show()
    sys.exit(app.exec_())

