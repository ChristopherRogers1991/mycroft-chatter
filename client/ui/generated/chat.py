# -*- coding: utf-8 -*-

"""
This file is primarily generated via running source/chatmainwindow.ui through
pyuic5. The only modification made is that the class should extend
QtWidgets.QMainWindow - pyuic5 always leaves it as object.

source/chatmainwindow.ui borrows heavily from the chat example project
distrubted with the pyqt5 source found on
https://www.riverbankcomputing.com/software/pyqt/download5/
"""

# Form implementation generated from reading ui file 'source/chatmainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.1

from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets


class Ui_ChatMainWindow(QtWidgets.QMainWindow):

    def setupUi(self, ChatMainWindow):

        ChatMainWindow.setObjectName("ChatMainWindow")
        ChatMainWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(ChatMainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.hboxlayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.hboxlayout.setContentsMargins(9, 9, 9, 9)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")

        self.vboxlayout = QtWidgets.QVBoxLayout()
        self.vboxlayout.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.chatHistory = QtWidgets.QTextBrowser(self.centralwidget)
        self.chatHistory.setAcceptDrops(False)
        self.chatHistory.setAcceptRichText(True)
        self.chatHistory.setObjectName("chatHistory")

        self.vboxlayout.addWidget(self.chatHistory)

        self.hboxlayout1 = QtWidgets.QHBoxLayout()
        self.hboxlayout1.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.messageLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.messageLineEdit.setObjectName("messageLineEdit")

        self.hboxlayout1.addWidget(self.messageLineEdit)

        self.sendButton = QtWidgets.QPushButton(self.centralwidget)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sendButton.sizePolicy().hasHeightForWidth())

        self.sendButton.setSizePolicy(sizePolicy)
        self.sendButton.setWhatsThis("")
        self.sendButton.setObjectName("sendButton")
        self.hboxlayout1.addWidget(self.sendButton)

        self.vboxlayout.addLayout(self.hboxlayout1)

        self.hboxlayout.addLayout(self.vboxlayout)

        ChatMainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(ChatMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")

        self.menuQuit = QtWidgets.QMenu(self.menubar)
        self.menuQuit.setObjectName("menuQuit")

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        ChatMainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(ChatMainWindow)
        self.statusbar.setObjectName("statusbar")

        ChatMainWindow.setStatusBar(self.statusbar)

        self.actionQuit = QtWidgets.QAction(ChatMainWindow)
        self.actionQuit.setObjectName("actionQuit")

        self.actionAboutQt = QtWidgets.QAction(ChatMainWindow)
        self.actionAboutQt.setObjectName("actionAboutQt")

        self.menuQuit.addAction(self.actionAboutQt)

        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuQuit.menuAction())

        self.retranslateUi(ChatMainWindow)

        self.messageLineEdit.returnPressed.connect(self.sendButton.animateClick)

        self.actionQuit.triggered['bool'].connect(ChatMainWindow.close)

        QtCore.QMetaObject.connectSlotsByName(ChatMainWindow)
        ChatMainWindow.setTabOrder(self.chatHistory, self.messageLineEdit)
        ChatMainWindow.setTabOrder(self.messageLineEdit, self.sendButton)

    def retranslateUi(self, ChatMainWindow):
        _translate = QtCore.QCoreApplication.translate
        ChatMainWindow.setWindowTitle(_translate("ChatMainWindow", "Hey Mycroft"))
        self.chatHistory.setToolTip(_translate("ChatMainWindow", "Messages sent and received from Mycroft"))
        self.messageLineEdit.setPlaceholderText(_translate("ChatMainWindow", "Hey Mycroft..."))
        self.sendButton.setToolTip(_translate("ChatMainWindow", "Sends a message to Mycroft"))
        self.sendButton.setText(_translate("ChatMainWindow", "Send"))
        self.menuQuit.setTitle(_translate("ChatMainWindow", "Help"))
        self.menuFile.setTitle(_translate("ChatMainWindow", "File"))
        self.actionQuit.setText(_translate("ChatMainWindow", "Quit"))
        self.actionQuit.setShortcut(_translate("ChatMainWindow", "Ctrl+Q"))
        self.actionAboutQt.setText(_translate("ChatMainWindow", "About Qt..."))

