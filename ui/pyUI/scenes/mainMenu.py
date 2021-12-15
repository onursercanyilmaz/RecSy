# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainMenu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QPoint

from PyQt5.QtWidgets import QMainWindow

from models.taskBar import TaskBarManagement


class Ui_MainMenu(object):
    def setupUi(self, MainMenuForm):
        MainMenuForm.setObjectName("MainWindow")
        MainMenuForm.resize(1200, 675)

        self.centralwidgetMainMenu = QtWidgets.QWidget(MainMenuForm)
        self.centralwidgetMainMenu.setObjectName("centralwidgetMainMenu")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidgetMainMenu)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainFrame = QtWidgets.QFrame(self.centralwidgetMainMenu)


        self.mainFrame.setStyleSheet("QFrame{background:#300331;\n"
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
        self.mainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainFrame.setObjectName("mainFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.mainFrame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter = QtWidgets.QSplitter(self.mainFrame)
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
        self.btnClose.clicked.connect(TaskBarManagement.close)
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
        self.btnminimize.clicked.connect(TaskBarManagement.minimize)
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
        self.btnZoom.clicked.connect(TaskBarManagement.zoom)
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
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.BooksLogo)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_9 = QtWidgets.QLabel(self.BooksLogo)
        self.label_9.setMinimumSize(QtCore.QSize(50, 50))
        self.label_9.setStyleSheet("background:none;\n"
"font-size:30px;\n"
"color:white;\n"
"font-weight:bold;\n"
"font-family:google sans;\n"
"image: url(:/logo/img/RecSy.png);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_5.addWidget(self.label_9)
        self.btnGoProfile_2 = QtWidgets.QToolButton(self.BooksLogo)
        self.btnGoProfile_2.setMinimumSize(QtCore.QSize(60, 60))
        self.btnGoProfile_2.setStyleSheet("QToolButton{\n"
"background:transparent;\n"
"image: url(:/profile/img/profile.png);\n"
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
        self.btnGoProfile_2.setText("")
        self.btnGoProfile_2.setObjectName("btnGoProfile_2")
        self.horizontalLayout_5.addWidget(self.btnGoProfile_2)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.barLogo.addWidget(self.BooksLogo)
        self.layoutWidget_2 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.WholeBody = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.WholeBody.setContentsMargins(25, 0, 25, 15)
        self.WholeBody.setObjectName("WholeBody")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_2.setStyleSheet("QLabel{\n"
"font-size:45px;\n"
"color:#920C7C;\n"
"font-weight:bold;\n"
"font-family:Google Sans;\n"
"}")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_3.setStyleSheet("QLabel{\n"
"font-size:40px;\n"
"color:#920C7C;\n"
"font-weight:bold;\n"
"font-family:Google Sans;\n"
"}")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.WholeBody.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 30)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnChooseBookCategory = QtWidgets.QToolButton(self.layoutWidget_2)
        self.btnChooseBookCategory.setMinimumSize(QtCore.QSize(300, 300))
        self.btnChooseBookCategory.setStyleSheet("QToolButton{\n"
"background:transparent;\n"
"image: url(:/book/img/book.png);\n"
"alignment:center;\n"
"}\n"
"QToolButton:hover {\n"
"background: #920C7C;\n"
"border: solid 1px;\n"
"border-radius:55;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"border-style: inset;\n"
"background: qradialgradient(\n"
"cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
");}")
        self.btnChooseBookCategory.setText("")
        self.btnChooseBookCategory.setObjectName("btnChooseBookCategory")
        self.horizontalLayout_2.addWidget(self.btnChooseBookCategory)
        self.btnChooseMovieCategory = QtWidgets.QToolButton(self.layoutWidget_2)
        self.btnChooseMovieCategory.setMinimumSize(QtCore.QSize(300, 300))
        self.btnChooseMovieCategory.setStyleSheet("QToolButton{\n"
"image: url(:/popcorn/img/popcorn.png);\n"
"background:transparent;\n"
"}\n"
"QToolButton:hover {\n"
"background: #920C7C;\n"
"border: solid 1px;\n"
"border-radius:55;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"border-style: inset;\n"
"background: qradialgradient(\n"
"cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
");}")
        self.btnChooseMovieCategory.setText("")
        self.btnChooseMovieCategory.setObjectName("btnChooseMovieCategory")
        self.horizontalLayout_2.addWidget(self.btnChooseMovieCategory)
        self.WholeBody.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addWidget(self.splitter)
        self.verticalLayout.addWidget(self.mainFrame)
        MainMenuForm.setCentralWidget(self.centralwidgetMainMenu)

        self.retranslateUi(MainMenuForm)
        QtCore.QMetaObject.connectSlotsByName(MainMenuForm)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Would you like to "))
        self.label_3.setText(_translate("MainWindow", "read or watch?"))

import source
class MyWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainMenu()
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

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainMenuForm = MyWindow()
    """QtWidgets.QWidget()
    ui = Ui_MainForm()
    ui.setupUi(MainForm)"""
    #MainForm.show()
    sys.exit(app.exec_())

