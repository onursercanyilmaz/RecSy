# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QWidget


class Login_UI(object):
    def setupUi(self, Login_Form):
        Login_Form.setObjectName("Form")
        Login_Form.resize(980, 636)
        self.centralwidget = QWidget(Login_Form)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setStyleSheet(u"QFrame {	\n"
                                           "	background-color: rgb(56, 58, 89);	\n"
                                           "	color: rgb(220, 220, 220);\n"
                                           "	border-radius: 10px;\n"
                                           "}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.frame = QtWidgets.QFrame(Login_Form)
        self.frame.setGeometry(QtCore.QRect(100, 50, 791, 541))
        self.frame.setStyleSheet("QWidget{background:#F6F7F7;\n"
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
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 791, 51))
        self.groupBox.setStyleSheet("background:#920C7C;\n"
"border: 2px solid white;\n"
"border-radius:0;\n"
"border-top-left-radius: 40;\n"
"border-top-right-radius: 40;\n"
"")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(730, 20, 20, 20))
        self.pushButton.setStyleSheet("QPushButton{\n"
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
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(710, 20, 20, 20))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
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
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(691, 20, 20, 20))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
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
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(80, 60, 461, 161))
        self.label.setStyleSheet("image: url(:/logo/img/RecSy.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(430, 110, 107, 50))
        self.label_2.setStyleSheet("QLabel{\n"
"font-size:40px;\n"
"color:darkblue;\n"
"font-weight:bold;\n"
"font-family:Google Sans;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(330, 390, 121, 51))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
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
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(260, 480, 281, 20))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
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
        self.pushButton_5.setObjectName("pushButton_5")
        self.splitter_2 = QtWidgets.QSplitter(self.frame)
        self.splitter_2.setGeometry(QtCore.QRect(240, 230, 361, 111))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.lineEdit = QtWidgets.QLineEdit(self.splitter_2)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
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
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.splitter_2)
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
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
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.splitter_3 = QtWidgets.QSplitter(self.frame)
        self.splitter_3.setGeometry(QtCore.QRect(190, 210, 41, 131))
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
        self.label.raise_()
        self.groupBox.raise_()
        self.label_2.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.label_3.raise_()
        self.label_4.raise_()


        self.retranslateUi(Login_Form)
        QtCore.QMetaObject.connectSlotsByName(Login_Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Login"))
        self.pushButton_4.setText(_translate("Form", "Login"))
        self.pushButton_5.setText(_translate("Form", "Don\'t you have an account?"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Username"))
        self.lineEdit_2.setText(_translate("Form", "abcd"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Password"))

import source


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Login_UI()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

