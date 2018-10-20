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
        self.messagesList = QtWidgets.QListWidget(self.centralwidget)
        self.messagesList.setMinimumSize(QtCore.QSize(350, 0))
        self.messagesList.setObjectName("messagesList")
        self.gridLayout.addWidget(self.messagesList, 0, 1, 1, 1)
        self.conversationsList = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.conversationsList.sizePolicy().hasHeightForWidth())
        self.conversationsList.setSizePolicy(sizePolicy)
        self.conversationsList.setMinimumSize(QtCore.QSize(240, 0))
        self.conversationsList.setMaximumSize(QtCore.QSize(240, 16777215))
        self.conversationsList.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.conversationsList.setObjectName("conversationsList")
        self.gridLayout.addWidget(self.conversationsList, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 876, 20))
        self.menubar.setObjectName("menubar")
        self.menuPlaceholder = QtWidgets.QMenu(self.menubar)
        self.menuPlaceholder.setObjectName("menuPlaceholder")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionSearch = QtWidgets.QAction(MainWindow)
        self.actionSearch.setObjectName("actionSearch")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuPlaceholder.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuPlaceholder.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionSearch)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "fb-archive-browser"))
        self.menuPlaceholder.setTitle(_translate("MainWindow", "&File"))
        self.menuHelp.setTitle(_translate("MainWindow", "&Help"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionSearch.setText(_translate("MainWindow", "Search"))
        self.actionSearch.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionAbout.setText(_translate("MainWindow", "&About"))
        self.actionExit.setText(_translate("MainWindow", "&Exit"))

