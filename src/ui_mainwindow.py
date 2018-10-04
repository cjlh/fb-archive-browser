# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(876, 602)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.messagesList = QtWidgets.QListView(self.centralwidget)
        self.messagesList.setMinimumSize(QtCore.QSize(350, 0))
        self.messagesList.setObjectName("messagesList")
        self.gridLayout.addWidget(self.messagesList, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.conversationsList = QtWidgets.QListWidget(self.centralwidget)
        self.conversationsList.setMinimumSize(QtCore.QSize(175, 0))
        self.conversationsList.setMaximumSize(QtCore.QSize(225, 16777215))
        self.conversationsList.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.conversationsList.setObjectName("conversationsList")
        self.gridLayout.addWidget(self.conversationsList, 1, 0, 1, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 876, 20))
        self.menubar.setObjectName("menubar")
        self.menuPlaceholder = QtWidgets.QMenu(self.menubar)
        self.menuPlaceholder.setObjectName("menuPlaceholder")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuPlaceholder.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "fb-archive-browser"))
        self.label.setText(_translate("MainWindow", "Conversations"))
        self.menuPlaceholder.setTitle(_translate("MainWindow", "File"))

