# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow

from ui.pyUI.taskBar import TaskBarManagement


class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        LoginForm.setObjectName("LoginForm")
        LoginForm.resize(1200, 636)
        LoginForm.setStyleSheet("")
        self.loginFrame = QtWidgets.QFrame(LoginForm)
        self.loginFrame.setGeometry(QtCore.QRect(100, 50, 791, 541))
        self.loginFrame.setStyleSheet("QFrame{background:#F6F7F7;\n"
"border-radius:40;}\n"
"\n"
"QPushButton:hover {\n"
"background: qradialgradient(\n"
"cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
");\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border-style: inset;\n"
"background: qradialgradient(\n"
"cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
");}")
        self.loginFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.loginFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.loginFrame.setObjectName("loginFrame")
        self.groupBox = QtWidgets.QGroupBox(self.loginFrame)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 791, 51))
        self.groupBox.setStyleSheet("background:#920C7C;\n"
"border: 2px solid white;\n"
"border-radius:0;\n"
"border-top-left-radius: 40;\n"
"border-top-right-radius: 40;\n"
"")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.btnClose = QtWidgets.QPushButton(self.groupBox)
        self.btnClose.setGeometry(QtCore.QRect(50, 20, 20, 20))
        self.btnClose.clicked.connect(TaskBarManagement.close)
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
        self.btnMinimize = QtWidgets.QPushButton(self.groupBox)
        self.btnMinimize.setGeometry(QtCore.QRect(70, 20, 20, 20))
        self.btnMinimize.clicked.connect(TaskBarManagement.minimize)
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
        self.label = QtWidgets.QLabel(self.loginFrame)
        self.label.setGeometry(QtCore.QRect(80, 60, 461, 161))
        self.label.setStyleSheet("image: url(:/logo/img/RecSy.png);\n"
"background:transparent;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.loginFrame)
        self.label_2.setGeometry(QtCore.QRect(430, 110, 107, 50))
        self.label_2.setStyleSheet("QLabel{\n"
"font-size:40px;\n"
"color:darkblue;\n"
"font-weight:bold;\n"
"font-family:Google Sans;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.btnLogin = QtWidgets.QPushButton(self.loginFrame)
        self.btnLogin.setGeometry(QtCore.QRect(330, 390, 121, 51))
        self.btnLogin.setStyleSheet("QPushButton{\n"
"background-color: #37AED4;\n"
"border-style: solid;\n"
"border-color: #37AED4;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"font-family:Google Sans;\n"
"font-weight: bold;\n"
"font-size:18px;\n"
"color:#300331;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"background: #300331;\n"
"color:#37AED4;\n"
"border-color: #300331;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border-style: inset;\n"
"background: qradialgradient(\n"
"cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
");}")
        self.btnLogin.setObjectName("btnLogin")
        self.btnDirectSignUp = QtWidgets.QPushButton(self.loginFrame)
        self.btnDirectSignUp.setGeometry(QtCore.QRect(260, 480, 281, 20))
        self.btnDirectSignUp.setStyleSheet("QPushButton{\n"
"background-color: transparent;\n"
"font-family:Google Sans;\n"
"font-weight: bold;\n"
"font-size:18px;\n"
"color:#300331;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"color: #37AED4;\n"
"}\n"
"")
        self.btnDirectSignUp.setObjectName("btnDirectSignUp")
        self.splitter_2 = QtWidgets.QSplitter(self.loginFrame)
        self.splitter_2.setGeometry(QtCore.QRect(240, 230, 361, 111))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.lineEdit_Username = QtWidgets.QLineEdit(self.splitter_2)
        self.lineEdit_Username.setStyleSheet("QLineEdit{\n"
"background:#37AED4;\n"
"border-style: solid;\n"
"border-color: white;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"color:#300331;\n"
"font-size:18px;\n"
"font-family:Google Sans;\n"
"padding-left: 10px;\n"
"}")
        self.lineEdit_Username.setObjectName("lineEdit_Username")
        self.lineEdit_Password = QtWidgets.QLineEdit(self.splitter_2)
        self.lineEdit_Password.setStyleSheet("QLineEdit{\n"
"background:#37AED4;\n"
"border-style: solid;\n"
"border-color: white;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"color:#300331;\n"
"font-size:15px;\n"
"font-family:Google Sans;\n"
"padding-left: 10px;\n"
"}")
        self.lineEdit_Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_Password.setObjectName("lineEdit_Password")
        self.splitter_3 = QtWidgets.QSplitter(self.loginFrame)
        self.splitter_3.setGeometry(QtCore.QRect(190, 220, 41, 131))
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.label_3 = QtWidgets.QLabel(self.splitter_3)
        self.label_3.setStyleSheet("image: url(:/login_person/img/login_person.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.splitter_3)
        self.label_4.setStyleSheet("image: url(:/login_lock/img/login_lock.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.splitter_2.raise_()
        self.splitter_3.raise_()
        self.label.raise_()
        self.groupBox.raise_()
        self.label_2.raise_()
        self.btnLogin.raise_()
        self.btnDirectSignUp.raise_()

        self.retranslateUi(LoginForm)
        QtCore.QMetaObject.connectSlotsByName(LoginForm)

    def retranslateUi(self, LoginForm):
        _translate = QtCore.QCoreApplication.translate
        LoginForm.setWindowTitle(_translate("LoginForm", "Form"))
        self.label_2.setText(_translate("LoginForm", "Login"))
        self.btnLogin.setText(_translate("LoginForm", "Login"))
        self.btnDirectSignUp.setText(_translate("LoginForm", "Don\'t you have an account?"))
        self.lineEdit_Username.setPlaceholderText(_translate("LoginForm", "Username"))
        self.lineEdit_Password.setText(_translate("LoginForm", "abcd"))
        self.lineEdit_Password.setPlaceholderText(_translate("LoginForm", "Password"))

import source
class MyWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_LoginForm()
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
    LoginForm = MyWindow()
    """QtWidgets.QWidget()
    ui = Ui_MainForm()
    ui.setupUi(MainForm)"""
    #MainForm.show()
    sys.exit(app.exec_())

