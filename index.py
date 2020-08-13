# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'index.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from container import MyContainerWidows
from service.login import login

class MyIndexWidows(QMainWindow):
    def __init__(self):
        super(MyIndexWidows, self).__init__()
        self.ui = Ui_IndexWindow()
        self.ui.setupUi(self)

    def open(self):
        self.show()


class Ui_IndexWindow(object):
    REQUEST_COOKIE = ''
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1200, 600)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(390, 90, 331, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(390, 140, 331, 31))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 110, 58, 16))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(320, 90, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(320, 140, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(740, 100, 101, 16))
        self.label_4.setToolTip("")
        self.label_4.setStyleSheet("color:red;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(740, 150, 101, 16))
        self.label_5.setToolTip("")
        self.label_5.setStyleSheet("color:red;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(510, 50, 101, 16))
        self.label_6.setToolTip("")
        self.label_6.setStyleSheet("color:red;")
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(530, 220, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton.setDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.getLoginInfo)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 22))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "跨境搜搜索登录"))
        self.label_2.setText(_translate("mainWindow", "账号："))
        self.label_3.setText(_translate("mainWindow", "密码："))
        self.pushButton.setText(_translate("mainWindow", "立即登录"))

    def getLoginInfo(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        # name = self.lineEdit.text()
        # if len(name) <= 0:
        #     self.label_4.setText(_translate("IndexWindow", "账号不能为空"))
        #     return
        # password = self.lineEdit_2.text()
        # if len(password) <= 0:
        #     self.label_5.setText(_translate("IndexWindow", "密码不能为空"))
        #     return
        # self.label_4.setText(_translate("IndexWindow", ""))
        # self.label_5.setText(_translate("IndexWindow", ""))
        # print(name, password )
        # cookie = login(name, password)
        # if len(cookie) <= 0:
        #     self.label_6.setText(_translate("IndexWindow", "登录失败"))
        #     return
        # REQUEST_COOKIE = cookie
        index = MyIndexWidows()
        index.close()
        container = MyContainerWidows()
        container.open()

