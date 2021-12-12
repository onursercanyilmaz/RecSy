# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chooseTvSeries.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChooseTvSeriesForm(object):
    def setupUi(self, ChooseTvSeriesForm):
        ChooseTvSeriesForm.setObjectName("ChooseTvSeriesForm")
        ChooseTvSeriesForm.resize(1199, 698)
        self.verticalLayout = QtWidgets.QVBoxLayout(ChooseTvSeriesForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.chooseTvSeriesFrame = QtWidgets.QFrame(ChooseTvSeriesForm)
        self.chooseTvSeriesFrame.setStyleSheet("QFrame{background:#300331;\n"
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
        self.chooseTvSeriesFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.chooseTvSeriesFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.chooseTvSeriesFrame.setObjectName("chooseTvSeriesFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.chooseTvSeriesFrame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.splitter_2 = QtWidgets.QSplitter(self.chooseTvSeriesFrame)
        self.splitter_2.setStyleSheet("background:none;")
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.layoutWidget_4 = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.barLogo_2 = QtWidgets.QVBoxLayout(self.layoutWidget_4)
        self.barLogo_2.setContentsMargins(0, 0, 0, 0)
        self.barLogo_2.setObjectName("barLogo_2")
        self.TabBar_2 = QtWidgets.QGroupBox(self.layoutWidget_4)
        self.TabBar_2.setMinimumSize(QtCore.QSize(0, 50))
        self.TabBar_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.TabBar_2.setStyleSheet("background:#920C7C;\n"
"border: 2px solid white;\n"
"border-radius:0;\n"
"border-top-left-radius: 40;\n"
"border-top-right-radius: 40;\n"
"")
        self.TabBar_2.setTitle("")
        self.TabBar_2.setObjectName("TabBar_2")
        self.btnClose = QtWidgets.QPushButton(self.TabBar_2)
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
        self.btnMinimize = QtWidgets.QPushButton(self.TabBar_2)
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
        self.btnZoom = QtWidgets.QPushButton(self.TabBar_2)
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
        self.barLogo_2.addWidget(self.TabBar_2)
        self.BooksLogo_2 = QtWidgets.QGroupBox(self.layoutWidget_4)
        self.BooksLogo_2.setMinimumSize(QtCore.QSize(0, 75))
        self.BooksLogo_2.setStyleSheet("border:none;")
        self.BooksLogo_2.setTitle("")
        self.BooksLogo_2.setObjectName("BooksLogo_2")
        self.label_10 = QtWidgets.QLabel(self.BooksLogo_2)
        self.label_10.setGeometry(QtCore.QRect(10, 10, 511, 75))
        self.label_10.setMinimumSize(QtCore.QSize(50, 75))
        self.label_10.setStyleSheet("background:none;\n"
"font-size:36px;\n"
"color:white;\n"
"font-weight:bold;\n"
"font-family:google sans;\n"
"image: url(:/logo/img/RecSy.png);")
        self.label_10.setObjectName("label_10")
        self.barLogo_2.addWidget(self.BooksLogo_2)
        self.layoutWidget_5 = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.WholeBody_2 = QtWidgets.QVBoxLayout(self.layoutWidget_5)
        self.WholeBody_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.WholeBody_2.setContentsMargins(25, 0, 25, 15)
        self.WholeBody_2.setObjectName("WholeBody_2")
        self.body_2 = QtWidgets.QSplitter(self.layoutWidget_5)
        self.body_2.setStyleSheet("QSplitter::handle {\n"
"    background: none;\n"
"}")
        self.body_2.setOrientation(QtCore.Qt.Vertical)
        self.body_2.setObjectName("body_2")
        self.hereIs_2 = QtWidgets.QSplitter(self.body_2)
        self.hereIs_2.setOrientation(QtCore.Qt.Vertical)
        self.hereIs_2.setObjectName("hereIs_2")
        self.layoutWidget_6 = QtWidgets.QWidget(self.hereIs_2)
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 50)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget_6)
        self.label_4.setStyleSheet("QLabel{\n"
"font-size:45px;\n"
"color:#920C7C;\n"
"font-weight:bold;\n"
"font-family:Google Sans;\n"
"}")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget_6)
        self.label_5.setStyleSheet("QLabel{\n"
"font-size:40px;\n"
"color:#920C7C;\n"
"font-weight:bold;\n"
"font-family:Google Sans;\n"
"}")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.comboBox_TvSeries = QtWidgets.QComboBox(self.body_2)
        self.comboBox_TvSeries.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_TvSeries.sizePolicy().hasHeightForWidth())
        self.comboBox_TvSeries.setSizePolicy(sizePolicy)
        self.comboBox_TvSeries.setMinimumSize(QtCore.QSize(0, 300))
        self.comboBox_TvSeries.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_TvSeries.setStyleSheet("QComboBox{color:white;\n"
"background:#300331;\n"
"font-size:30px;\n"
"font-weight:bold;\n"
"font-family:google sans;\n"
"text-align:center;\n"
"margin-bottom:100px;\n"
"border:1px solid white;\n"
"border-radius:25px;\n"
" padding-left: 75px;\n"
" padding-right: 75px;\n"
"margin-left:75px;\n"
"margin-top:55px;\n"
"margin-right:75px;}\n"
"\n"
"\n"
"")
        self.comboBox_TvSeries.setEditable(True)
        self.comboBox_TvSeries.setFrame(True)
        self.comboBox_TvSeries.setObjectName("comboBox_TvSeries")
        self.comboBox_TvSeries.addItem("")
        self.comboBox_TvSeries.addItem("")
        self.comboBox_TvSeries.addItem("")
        self.comboBox_TvSeries.addItem("")
        self.comboBox_TvSeries.addItem("")
        self.comboBox_TvSeries.addItem("")
        self.comboBox_TvSeries.addItem("")
        self.comboBox_TvSeries.addItem("")
        self.comboBox_TvSeries.addItem("")
        self.comboBox_TvSeries.addItem("")
        self.comboBox_TvSeries.addItem("")
        self.comboBox_TvSeries.addItem("")
        self.comboBox_TvSeries.addItem("")
        self.comboBox_TvSeries.addItem("")
        self.WholeBody_2.addWidget(self.body_2)
        self.bottomBar_2 = QtWidgets.QSplitter(self.layoutWidget_5)
        self.bottomBar_2.setMinimumSize(QtCore.QSize(0, 50))
        self.bottomBar_2.setStyleSheet("QSplitter::handle {\n"
"    background: none;\n"
"}")
        self.bottomBar_2.setOrientation(QtCore.Qt.Horizontal)
        self.bottomBar_2.setObjectName("bottomBar_2")
        self.btnBack = QtWidgets.QToolButton(self.bottomBar_2)
        self.btnBack.setStyleSheet("QToolButton{\n"
"background:transparent;\n"
"image: url(:/back/img/back.png);\n"
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
        self.btnBack.setText("")
        self.btnBack.setObjectName("btnBack")
        self.btnSelect = QtWidgets.QPushButton(self.bottomBar_2)
        self.btnSelect.setStyleSheet("QPushButton{\n"
"background-color: #37AED4;\n"
"border-style: solid;\n"
"border-color: #37AED4;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"font-family:Google Sans;\n"
"font-weight: bold;\n"
"font-size:25px;\n"
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
        self.btnSelect.setObjectName("btnSelect")
        self.WholeBody_2.addWidget(self.bottomBar_2)
        self.horizontalLayout_2.addWidget(self.splitter_2)
        self.verticalLayout.addWidget(self.chooseTvSeriesFrame)

        self.retranslateUi(ChooseTvSeriesForm)
        QtCore.QMetaObject.connectSlotsByName(ChooseTvSeriesForm)

    def retranslateUi(self, ChooseTvSeriesForm):
        _translate = QtCore.QCoreApplication.translate
        ChooseTvSeriesForm.setWindowTitle(_translate("ChooseTvSeriesForm", "Form"))
        self.label_10.setText(_translate("ChooseTvSeriesForm", "TV Series"))
        self.label_4.setText(_translate("ChooseTvSeriesForm", "Plsease select your"))
        self.label_5.setText(_translate("ChooseTvSeriesForm", "favorite tv series!"))
        self.comboBox_TvSeries.setItemText(0, _translate("ChooseTvSeriesForm", "New Item"))
        self.comboBox_TvSeries.setItemText(1, _translate("ChooseTvSeriesForm", "New Item"))
        self.comboBox_TvSeries.setItemText(2, _translate("ChooseTvSeriesForm", "New Item"))
        self.comboBox_TvSeries.setItemText(3, _translate("ChooseTvSeriesForm", "New Item"))
        self.comboBox_TvSeries.setItemText(4, _translate("ChooseTvSeriesForm", "New Item"))
        self.comboBox_TvSeries.setItemText(5, _translate("ChooseTvSeriesForm", "New Item"))
        self.comboBox_TvSeries.setItemText(6, _translate("ChooseTvSeriesForm", "New Item"))
        self.comboBox_TvSeries.setItemText(7, _translate("ChooseTvSeriesForm", "New Item"))
        self.comboBox_TvSeries.setItemText(8, _translate("ChooseTvSeriesForm", "New Item"))
        self.comboBox_TvSeries.setItemText(9, _translate("ChooseTvSeriesForm", "New Item"))
        self.comboBox_TvSeries.setItemText(10, _translate("ChooseTvSeriesForm", "New Item"))
        self.comboBox_TvSeries.setItemText(11, _translate("ChooseTvSeriesForm", "New Item"))
        self.comboBox_TvSeries.setItemText(12, _translate("ChooseTvSeriesForm", "New Item"))
        self.comboBox_TvSeries.setItemText(13, _translate("ChooseTvSeriesForm", "xxx"))
        self.btnSelect.setText(_translate("ChooseTvSeriesForm", "Select"))

import source_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ChooseTvSeriesForm = QtWidgets.QWidget()
    ui = Ui_ChooseTvSeriesForm()
    ui.setupUi(ChooseTvSeriesForm)
    ChooseTvSeriesForm.show()
    sys.exit(app.exec_())

