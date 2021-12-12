# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'splash.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SplashForm(object):
    def setupUi(self, SplashForm):
        SplashForm.setObjectName("SplashForm")
        SplashForm.resize(988, 642)
        self.splashFrame = QtWidgets.QFrame(SplashForm)
        self.splashFrame.setGeometry(QtCore.QRect(100, 50, 791, 541))
        self.splashFrame.setStyleSheet("QFrame{background:#F6F7F7;\n"
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
        self.splashFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.splashFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.splashFrame.setObjectName("splashFrame")
        self.groupBox = QtWidgets.QGroupBox(self.splashFrame)
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
        self.label = QtWidgets.QLabel(self.splashFrame)
        self.label.setGeometry(QtCore.QRect(60, 10, 651, 471))
        self.label.setStyleSheet("image: url(:/logo/img/RecSy.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.splitter_3 = QtWidgets.QSplitter(self.splashFrame)
        self.splitter_3.setGeometry(QtCore.QRect(190, 210, 41, 131))
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.progressBar = QtWidgets.QProgressBar(self.splashFrame)
        self.progressBar.setGeometry(QtCore.QRect(110, 400, 571, 31))
        self.progressBar.setStyleSheet("QProgressBar {\n"
"\n"
"background-color: #530D63;\n"
"color: rgb(200, 200, 200);\n"
"border-style: none;\n"
"border-radius: 15px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"\n"
"QProgressBar::chunk{\n"
"border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.splitter_3.raise_()
        self.label.raise_()
        self.groupBox.raise_()
        self.progressBar.raise_()

        self.retranslateUi(SplashForm)
        QtCore.QMetaObject.connectSlotsByName(SplashForm)

    def retranslateUi(self, SplashForm):
        _translate = QtCore.QCoreApplication.translate
        SplashForm.setWindowTitle(_translate("SplashForm", "Form"))

import source_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SplashForm = QtWidgets.QWidget()
    ui = Ui_SplashForm()
    ui.setupUi(SplashForm)
    SplashForm.show()
    sys.exit(app.exec_())

