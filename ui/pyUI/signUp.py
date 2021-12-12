# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signUp.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SignUpForm(object):
    def setupUi(self, SignUpForm):
        SignUpForm.setObjectName("SignUpForm")
        SignUpForm.resize(980, 635)
        self.signUpFrame = QtWidgets.QFrame(SignUpForm)
        self.signUpFrame.setGeometry(QtCore.QRect(80, 50, 791, 541))
        self.signUpFrame.setStyleSheet("QFrame{background:#F6F7F7;\n"
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
        self.signUpFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.signUpFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.signUpFrame.setObjectName("signUpFrame")
        self.groupBox = QtWidgets.QGroupBox(self.signUpFrame)
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
        self.btnClose.setGeometry(QtCore.QRect(40, 20, 20, 20))
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
        self.btnMinimize.setGeometry(QtCore.QRect(60, 20, 20, 20))
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
        self.label = QtWidgets.QLabel(self.signUpFrame)
        self.label.setGeometry(QtCore.QRect(80, 60, 461, 161))
        self.label.setStyleSheet("image: url(:/logo/img/RecSy.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.signUpFrame)
        self.label_2.setGeometry(QtCore.QRect(410, 110, 171, 50))
        self.label_2.setStyleSheet("QLabel{\n"
"font-size:40px;\n"
"color:darkblue;\n"
"font-weight:bold;\n"
"font-family:Google Sans;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.btnSignUp = QtWidgets.QPushButton(self.signUpFrame)
        self.btnSignUp.setGeometry(QtCore.QRect(360, 410, 121, 51))
        self.btnSignUp.setStyleSheet("QPushButton{\n"
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
        self.btnSignUp.setObjectName("btnSignUp")
        self.btnDirectLogin = QtWidgets.QPushButton(self.signUpFrame)
        self.btnDirectLogin.setGeometry(QtCore.QRect(280, 480, 281, 20))
        self.btnDirectLogin.setStyleSheet("QPushButton{\n"
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
        self.btnDirectLogin.setObjectName("btnDirectLogin")
        self.splitter = QtWidgets.QSplitter(self.signUpFrame)
        self.splitter.setGeometry(QtCore.QRect(290, 220, 301, 151))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.lineEdit_Username = QtWidgets.QLineEdit(self.splitter)
        self.lineEdit_Username.setStyleSheet("QLineEdit{\n"
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
        self.lineEdit_Username.setObjectName("lineEdit_Username")
        self.lineEdit_Email = QtWidgets.QLineEdit(self.splitter)
        self.lineEdit_Email.setStyleSheet("QLineEdit{\n"
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
        self.lineEdit_Email.setText("")
        self.lineEdit_Email.setObjectName("lineEdit_Email")
        self.lineEdit_Password = QtWidgets.QLineEdit(self.splitter)
        self.lineEdit_Password.setStyleSheet("QLineEdit{\n"
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
        self.lineEdit_Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_Password.setObjectName("lineEdit_Password")
        self.splitter_2 = QtWidgets.QSplitter(self.signUpFrame)
        self.splitter_2.setGeometry(QtCore.QRect(230, 220, 41, 151))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.label_3 = QtWidgets.QLabel(self.splitter_2)
        self.label_3.setStyleSheet("image: url(:/login_person/img/login_person.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.splitter_2)
        self.label_5.setStyleSheet("image: url(:/mail/img/mail.png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.splitter_2)
        self.label_4.setStyleSheet("image: url(:/login_lock/img/login_lock.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.splitter.raise_()
        self.splitter_2.raise_()
        self.label.raise_()
        self.groupBox.raise_()
        self.label_2.raise_()
        self.btnSignUp.raise_()
        self.btnDirectLogin.raise_()

        self.retranslateUi(SignUpForm)
        QtCore.QMetaObject.connectSlotsByName(SignUpForm)

    def retranslateUi(self, SignUpForm):
        _translate = QtCore.QCoreApplication.translate
        SignUpForm.setWindowTitle(_translate("SignUpForm", "Form"))
        self.label_2.setText(_translate("SignUpForm", "Sign Up"))
        self.btnSignUp.setText(_translate("SignUpForm", "Sign Up"))
        self.btnDirectLogin.setText(_translate("SignUpForm", "Do you have an account?"))
        self.lineEdit_Username.setPlaceholderText(_translate("SignUpForm", "Username"))
        self.lineEdit_Email.setPlaceholderText(_translate("SignUpForm", "E-mail"))
        self.lineEdit_Password.setText(_translate("SignUpForm", "abcd"))
        self.lineEdit_Password.setPlaceholderText(_translate("SignUpForm", "Password"))

import source_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SignUpForm = QtWidgets.QWidget()
    ui = Ui_SignUpForm()
    ui.setupUi(SignUpForm)
    SignUpForm.show()
    sys.exit(app.exec_())

