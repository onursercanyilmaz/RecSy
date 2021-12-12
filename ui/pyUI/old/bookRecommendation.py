# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bookRecommendation.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BookRecommendationsForm(object):
    def setupUi(self, BookRecommendationsForm):
        BookRecommendationsForm.setObjectName("BookRecommendationsForm")
        BookRecommendationsForm.resize(1330, 742)
        BookRecommendationsForm.setStyleSheet(" border-style: solid;\n"
"  border-color: #ff0000; /* red */")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(BookRecommendationsForm)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.bookrecommendationsFrame = QtWidgets.QFrame(BookRecommendationsForm)
        self.bookrecommendationsFrame.setStyleSheet("QFrame{background:#300331;\n"
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
        self.bookrecommendationsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bookrecommendationsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bookrecommendationsFrame.setObjectName("bookrecommendationsFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.bookrecommendationsFrame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter = QtWidgets.QSplitter(self.bookrecommendationsFrame)
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
        self.btnMinimize = QtWidgets.QPushButton(self.TabBar)
        self.btnMinimize.setGeometry(QtCore.QRect(50, 20, 20, 20))
        self.btnMinimize.setStyleSheet("QPushButton{\n"
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
        self.btnMinimize.setText("")
        self.btnMinimize.setObjectName("btnMinimize")
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
        self.label_BooksLogo = QtWidgets.QLabel(self.BooksLogo)
        self.label_BooksLogo.setGeometry(QtCore.QRect(10, 10, 391, 75))
        self.label_BooksLogo.setMinimumSize(QtCore.QSize(50, 75))
        self.label_BooksLogo.setStyleSheet("background:none;\n"
"font-size:36px;\n"
"color:white;\n"
"font-weight:bold;\n"
"font-family:google sans;\n"
"image: url(:/logo/img/RecSy.png);")
        self.label_BooksLogo.setObjectName("label_BooksLogo")
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
        self.label_1 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_1.setStyleSheet("QLabel{\n"
"font-size:45px;\n"
"color:#920C7C;\n"
"font-weight:bold;\n"
"font-family:Google Sans;\n"
"}")
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.verticalLayout_3.addWidget(self.label_1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_3.setStyleSheet("QLabel{\n"
"font-size:40px;\n"
"color:#920C7C;\n"
"font-weight:bold;\n"
"font-family:Google Sans;\n"
"}")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.list_bookRecommendations = QtWidgets.QListWidget(self.body)
        self.list_bookRecommendations.setStyleSheet("QListWidget{\n"
"color:white;\n"
"font-size:30px;\n"
"font-family:Google Sans;\n"
"background:#300331;\n"
"}")
        self.list_bookRecommendations.setObjectName("list_bookRecommendations")
        item = QtWidgets.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.list_bookRecommendations.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.list_bookRecommendations.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.list_bookRecommendations.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.list_bookRecommendations.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.list_bookRecommendations.addItem(item)
        self.WholeBody.addWidget(self.body)
        self.bottomBar = QtWidgets.QSplitter(self.layoutWidget1)
        self.bottomBar.setMinimumSize(QtCore.QSize(0, 50))
        self.bottomBar.setStyleSheet("QSplitter::handle {\n"
"    background: none;\n"
"}")
        self.bottomBar.setOrientation(QtCore.Qt.Horizontal)
        self.bottomBar.setObjectName("bottomBar")
        self.btnGoHome = QtWidgets.QToolButton(self.bottomBar)
        self.btnGoHome.setStyleSheet("QToolButton{\n"
"background:transparent;\n"
"image: url(:/home/img/home.png);\n"
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
        self.btnAddFav = QtWidgets.QToolButton(self.bottomBar)
        self.btnAddFav.setStyleSheet("QToolButton{\n"
"background:transparent;\n"
"image: url(:/addFavorite/img/addFavorite.png);\n"
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
        self.btnAddFav.setText("")
        self.btnAddFav.setObjectName("btnAddFav")
        self.WholeBody.addWidget(self.bottomBar)
        self.horizontalLayout.addWidget(self.splitter)
        self.verticalLayout_4.addWidget(self.bookrecommendationsFrame)

        self.retranslateUi(BookRecommendationsForm)
        self.list_bookRecommendations.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(BookRecommendationsForm)

    def retranslateUi(self, BookRecommendationsForm):
        _translate = QtCore.QCoreApplication.translate
        BookRecommendationsForm.setWindowTitle(_translate("BookRecommendationsForm", "Form"))
        self.label_BooksLogo.setText(_translate("BookRecommendationsForm", "Books"))
        self.label_1.setText(_translate("BookRecommendationsForm", "Here is top 5"))
        self.label_3.setText(_translate("BookRecommendationsForm", "recommendations to you!"))
        __sortingEnabled = self.list_bookRecommendations.isSortingEnabled()
        self.list_bookRecommendations.setSortingEnabled(False)
        item = self.list_bookRecommendations.item(0)
        item.setText(_translate("BookRecommendationsForm", "New Item"))
        item = self.list_bookRecommendations.item(1)
        item.setText(_translate("BookRecommendationsForm", "New Item"))
        item = self.list_bookRecommendations.item(2)
        item.setText(_translate("BookRecommendationsForm", "New Item"))
        item = self.list_bookRecommendations.item(3)
        item.setText(_translate("BookRecommendationsForm", "New Item"))
        item = self.list_bookRecommendations.item(4)
        item.setText(_translate("BookRecommendationsForm", "New Item"))
        self.list_bookRecommendations.setSortingEnabled(__sortingEnabled)

import source_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BookRecommendationsForm = QtWidgets.QWidget()
    ui = Ui_BookRecommendationsForm()
    ui.setupUi(BookRecommendationsForm)
    BookRecommendationsForm.show()
    sys.exit(app.exec_())

