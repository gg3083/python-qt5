import _thread
import datetime
import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QHeaderView, QTableWidget, \
    QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets, Qt

from model.ExcelParam import ExcelParam
from service.country import getCountryInfo
from service.login import login
from service.search import executeSearch, writeExcel, getPersonInfo

REQUEST_COOKIE = ''

class MyIndexWidows(QMainWindow):
    def __init__(self):
        super(MyIndexWidows, self).__init__()
        self.ui = Ui_IndexWindow()
        self.ui.setupUi(self)

    def open(self):
        self.show()

class MyContainerWidows(QMainWindow):
    def __init__(self):
        super(MyContainerWidows, self).__init__()
        self.ui = Ui_ContainerWindow()
        self.ui.setupUi(self)

    def open(self):
        self.show()

class Ui_IndexWindow(object):

    def setupUi(self, IndexWindow):
        IndexWindow.setObjectName("IndexWindow")
        IndexWindow.resize(720, 327)
        self.centralwidget = QtWidgets.QWidget(IndexWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(190, 70, 331, 31))
        self.lineEdit.setToolTipDuration(1)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 130, 331, 31))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 110, 58, 16))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 70, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 130, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 190, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(540, 80, 101, 16))
        self.label_4.setToolTip("")
        self.label_4.setStyleSheet("color:red;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(540, 140, 101, 16))
        self.label_5.setToolTip("")
        self.label_5.setStyleSheet("color:red;")
        self.label_5.setObjectName("label_5")
        IndexWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(IndexWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 720, 22))
        self.menubar.setObjectName("menubar")
        IndexWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(IndexWindow)
        self.statusbar.setObjectName("statusbar")
        IndexWindow.setStatusBar(self.statusbar)

        ## 自定义逻辑
        self.pushButton.clicked.connect(self.getLoginInfo)

        self.retranslateUi(IndexWindow)
        QtCore.QMetaObject.connectSlotsByName(IndexWindow)

    def retranslateUi(self, IndexWindow):
        _translate = QtCore.QCoreApplication.translate
        IndexWindow.setWindowTitle(_translate("IndexWindow", "跨境搜搜索登录"))
        self.lineEdit.setToolTip(_translate("IndexWindow", "账号不能为空"))
        self.label_2.setText(_translate("IndexWindow", "账号："))
        self.label_3.setText(_translate("IndexWindow", "密码："))
        self.pushButton.setText(_translate("IndexWindow", "立即登录"))

    def getLoginInfo(self, IndexWindow):
        _translate = QtCore.QCoreApplication.translate
        name = self.lineEdit.text()
        if len(name) <= 0:
            self.label_4.setText(_translate("IndexWindow", "账号不能为空"))
            return
        password = self.lineEdit_2.text()
        if len(password) <= 0:
            self.label_5.setText(_translate("IndexWindow", "密码不能为空"))
            return
        self.label_4.setText(_translate("IndexWindow", ""))
        self.label_5.setText(_translate("IndexWindow", ""))
        print(name, password)
        cookie = login(name, password)
        if len(cookie) > 0:
            global REQUEST_COOKIE
            REQUEST_COOKIE = cookie
            print("登录后的全局cookie为:{}", REQUEST_COOKIE)
            ui_hello.show()
            ui_hello.ui.setCountry()
            MainWindow.close()
        else:
            msg_box = QtWidgets.QMessageBox
            msg_box.warning(self.centralwidget, "警告", "用户名或密码错误！", msg_box.Yes)
            self.lineEdit.setFocus()



class Ui_ContainerWindow(object):
    def setupUi(self, ContainerWindow):
        ContainerWindow.setObjectName("ContainerWindow")
        ContainerWindow.resize(1200, 600)
        self.centralwidget = QtWidgets.QWidget(ContainerWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 20, 231, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 20, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(680, 20, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.toolButton.setFont(font)
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_2.setGeometry(QtCore.QRect(790, 20, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.toolButton_2.setFont(font)
        self.toolButton_2.setObjectName("toolButton_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 70, 1171, 461))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        row_name = [
            '序号',
            '国家',
            '公司名称',
            '网址',
            '销售额',
            '联系人',
            '手机/电话',
            '地址',
        ]
        self.tableWidget.setHorizontalHeaderLabels(row_name)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  #设置列宽的适应方式
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1100, 10, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(420, 10, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox.setFont(font)
        self.comboBox.setEditable(True)
        self.comboBox.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBox.setIconSize(QtCore.QSize(24, 24))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        ContainerWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ContainerWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 22))
        self.menubar.setObjectName("menubar")
        ContainerWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ContainerWindow)
        self.statusbar.setObjectName("statusbar")
        ContainerWindow.setStatusBar(self.statusbar)

        ## 自定义逻辑
        self.pushButton_3.clicked.connect(self.logout)
        self.toolButton.clicked.connect(self.search)
        self.toolButton_2.clicked.connect(self.exportExcel)

        self.retranslateUi(ContainerWindow)
        QtCore.QMetaObject.connectSlotsByName(ContainerWindow)

    def retranslateUi(self, ContainerWindow):
        _translate = QtCore.QCoreApplication.translate
        ContainerWindow.setWindowTitle(_translate("ContainerWindow", "跨境搜搜索"))
        self.label.setText(_translate("ContainerWindow", "关键词："))
        self.label_2.setText(_translate("ContainerWindow", "指定国家："))
        self.toolButton.setText(_translate("ContainerWindow", "搜索"))
        self.toolButton_2.setText(_translate("ContainerWindow", "导出"))
        self.pushButton_3.setText(_translate("ContainerWindow", "退出账号"))

    def setCountry(self):
        # cookie = '__RequestVerificationToken=r3C7PlD_eIf0-QzESJyJM4C3hlScMIM5Dp0VA0jNIdy14D8MbsZ3ye7nNeWy5DnGsym20A2; _safe_token_=49E6D91D60E8B75893028E43A2B7DB77D68106626E9ED6FAF1401B99A03AB7F266EC5802FF2EC3AA24BF97CEEA50A1EFEF7CFEF51A55645F18286944C678935B; lsxx=01B8515C797DA1B830BCC72BF7D47613F33DAAC25177BB040150C5982FB8156F9BD023A3F6CFE043C0B24B8AFFFAB770A53B63A65AF77B73926D0BF5EF5F1266FB4445EBB5324AE929670A26A04F4FB366DF0AC1F9851C38A375B9A44DF1396DC5EE4482633088D8C6FBD55FE2794646272E9DEF67CF4C3FA57AB4E38FD01C15B912AF0EE88AF720767AFF3F'
        global REQUEST_COOKIE
        cookie = REQUEST_COOKIE
        print("请求的cookie为:{}", cookie)
        countryList = getCountryInfo(cookie)
        print(len(countryList))
        if len(countryList):
            self.comboBox.addItems(countryList)
        else:
            QMessageBox.warning(self.centralwidget, "警告", "获取国家信息失败！", QMessageBox.Yes)

    def logout(self):
        global REQUEST_COOKIE
        REQUEST_COOKIE = ''
        MainWindow.show()
        ui_hello.close()


    def search(self):
        searchKey = self.lineEdit.text()
        if len(searchKey) <= 0:
            QMessageBox.warning(self.centralwidget, "警告", "搜索关键字不能为空！", QMessageBox.Yes)
            return
        country = self.comboBox.currentText()
        if len(country) <= 0:
            QMessageBox.warning(self.centralwidget, "警告", "国家不能为空！", QMessageBox.Yes)
            return
        print(searchKey, country)
        if len(country.split("—")) != 3:
            QMessageBox.warning(self.centralwidget, "警告", "选择的国家格式有误！", QMessageBox.Yes)
            return
        countryCode = country.split("—")[2]
        global REQUEST_COOKIE
        listData = executeSearch(searchKey, countryCode, REQUEST_COOKIE)
        if len(listData) == 0:
            QMessageBox.warning(self.centralwidget, "警告", "该关键词查询不到数据,请更换关键词后再试！", QMessageBox.Yes)
            return
        self.tableWidget.setRowCount(len(listData))

        for i in range(len(listData)):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(i+1)))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(listData[i].country))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(listData[i].company))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(listData[i].domain))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(listData[i].sale))
            self.tableWidget.setItem(i, 5, QTableWidgetItem(listData[i].person))
            self.tableWidget.setItem(i, 6, QTableWidgetItem(listData[i].phone))
            self.tableWidget.setItem(i, 7, QTableWidgetItem(listData[i].address))

        # 分三个线程去显示数据
        # 第一次显示10个
        # 如果所有数据大于20 第二次显示所有数据减10除以2 否则就直接显示剩余的
        # 第三次显示剩余
        if len(listData) > 10:
            try:
                _thread.start_new_thread(self.getPerson, (REQUEST_COOKIE, listData[:10]))
                if len(listData) < 20:
                    _thread.start_new_thread(self.getPerson, (REQUEST_COOKIE, listData[10:]))
                else:
                    second = (len(listData) - 10) // 2 + 10
                    _thread.start_new_thread(self.getPerson, (REQUEST_COOKIE, listData[10:second]))
                    _thread.start_new_thread(self.getPerson, (REQUEST_COOKIE, listData[second:]))
            except:
                print("Error: 无法启动线程")
            print("开始获取联系人1")
        else:
            try:
                _thread.start_new_thread(self.getPerson, (REQUEST_COOKIE, listData))
            except:
                print("Error: 无法启动线程")
            print("开始获取联系人2")

    def getPerson(self, cookie, listData):
        personList = getPersonInfo(cookie, listData)
        for item in personList:
            print(item['index'], QTableWidgetItem(item['person']))
            self.tableWidget.setItem(item['index'], 5, QTableWidgetItem(item['person']))


    def exportExcel(self):
        rowNum = self.tableWidget.rowCount()
        if rowNum <= 0:
            QMessageBox.warning(self.centralwidget, "警告", "表格中没有数据,无法导出！", QMessageBox.Yes)
            return
        # columnNum = self.tableWidget.columnCount()
        excelList = []
        for i in range(rowNum):
            param = ExcelParam()
            param.id = self.tableWidget.item(i, 0).text()
            param.country = self.tableWidget.item(i, 1).text()
            param.company = self.tableWidget.item(i, 2).text()
            param.domain = self.tableWidget.item(i, 3).text()
            param.sale = self.tableWidget.item(i, 4).text()
            param.person = self.tableWidget.item(i, 5).text()
            param.phone = self.tableWidget.item(i, 6).text()
            param.address = self.tableWidget.item(i, 7).text()
            excelList.append(param)
        fileName = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + "_kjs.xls"
        file_path = QFileDialog.getSaveFileName(self.centralwidget, "save file", fileName, os.path.expanduser('~'))

        writeExcel(excelList, file_path[0])

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MyIndexWidows()
    ui_hello = MyContainerWidows()
    ui.ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

