# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\lucyc\Desktop\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(466, 519)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QTextBrowser(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(120, 30, 231, 51))
        self.title.setObjectName("title")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 370, 341, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.output_file_path = QtWidgets.QTextEdit(self.layoutWidget)
        self.output_file_path.setMaximumSize(QtCore.QSize(258, 29))
        self.output_file_path.setObjectName("output_file_path")
        self.horizontalLayout_5.addWidget(self.output_file_path)
        self.select_output_file_path = QtWidgets.QPushButton(self.layoutWidget)
        self.select_output_file_path.setObjectName("select_output_file_path")
        self.horizontalLayout_5.addWidget(self.select_output_file_path)
        self.JASONface = QtWidgets.QLabel(self.centralwidget)
        self.JASONface.setGeometry(QtCore.QRect(280, 170, 121, 181))
        self.JASONface.setMinimumSize(QtCore.QSize(111, 181))
        self.JASONface.setObjectName("JASONface")
        self.save_data = QtWidgets.QPushButton(self.centralwidget)
        self.save_data.setGeometry(QtCore.QRect(130, 430, 81, 31))
        self.save_data.setObjectName("save_data")
        self.initallmemory = QtWidgets.QPushButton(self.centralwidget)
        self.initallmemory.setGeometry(QtCore.QRect(240, 430, 111, 31))
        self.initallmemory.setObjectName("initallmemory")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(60, 100, 341, 41))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.input_file_path = QtWidgets.QTextEdit(self.widget)
        self.input_file_path.setMaximumSize(QtCore.QSize(258, 29))
        self.input_file_path.setObjectName("input_file_path")
        self.horizontalLayout.addWidget(self.input_file_path)
        self.select_input_file_path = QtWidgets.QPushButton(self.widget)
        self.select_input_file_path.setObjectName("select_input_file_path")
        self.horizontalLayout.addWidget(self.select_input_file_path)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(60, 170, 178, 181))
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget1)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.tra_select = QtWidgets.QComboBox(self.widget1)
        self.tra_select.setObjectName("tra_select")
        self.tra_select.addItem("")
        self.tra_select.addItem("")
        self.horizontalLayout_2.addWidget(self.tra_select)
        self.tra_select_buttom = QtWidgets.QPushButton(self.widget1)
        self.tra_select_buttom.setObjectName("tra_select_buttom")
        self.horizontalLayout_2.addWidget(self.tra_select_buttom)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.ana_select = QtWidgets.QComboBox(self.widget1)
        self.ana_select.setObjectName("ana_select")
        self.ana_select.addItem("")
        self.horizontalLayout_3.addWidget(self.ana_select)
        self.ana_select_buttom = QtWidgets.QPushButton(self.widget1)
        self.ana_select_buttom.setObjectName("ana_select_buttom")
        self.horizontalLayout_3.addWidget(self.ana_select_buttom)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.tsr_select = QtWidgets.QComboBox(self.widget1)
        self.tsr_select.setObjectName("tsr_select")
        self.tsr_select.addItem("")
        self.horizontalLayout_4.addWidget(self.tsr_select)
        self.tsr_select_buttom = QtWidgets.QPushButton(self.widget1)
        self.tsr_select_buttom.setObjectName("tsr_select_buttom")
        self.horizontalLayout_4.addWidget(self.tsr_select_buttom)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 466, 23))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.title.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" dir=\'rtl\' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; font-weight:600;\">ASDAN_TOOLKIT</span></p></body></html>"))
        self.select_output_file_path.setText(_translate("mainWindow", "save_path"))
        self.JASONface.setText(_translate("mainWindow", "TextLabel"))
        self.save_data.setText(_translate("mainWindow", "SAVE"))
        self.initallmemory.setText(_translate("mainWindow", "INIT ALL MEMORY"))
        self.select_input_file_path.setText(_translate("mainWindow", "FILE_path"))
        self.label_3.setText(_translate("mainWindow", "TRA"))
        self.tra_select.setItemText(0, _translate("mainWindow", "city"))
        self.tra_select.setItemText(1, _translate("mainWindow", "fcity"))
        self.tra_select_buttom.setText(_translate("mainWindow", "start"))
        self.label.setText(_translate("mainWindow", "ANA"))
        self.ana_select.setItemText(0, _translate("mainWindow", "JCT"))
        self.ana_select_buttom.setText(_translate("mainWindow", "start"))
        self.label_2.setText(_translate("mainWindow", "TSR"))
        self.tsr_select.setItemText(0, _translate("mainWindow", "JCT"))
        self.tsr_select_buttom.setText(_translate("mainWindow", "start"))
