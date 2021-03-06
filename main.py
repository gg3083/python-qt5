import _thread
import datetime
import os
import sys
import threading
import time
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QHeaderView, QTableWidget, \
    QFileDialog, QComboBox, QCompleter
from PyQt5 import QtCore, QtGui, QtWidgets

from model.ExcelParam import ExcelParam
from service.country import getCountryInfo
from service.excel import createSheet, writeSheet
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
        self.label_2.setGeometry(QtCore.QRect(100, 70, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 130, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
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
        self.label_4.setGeometry(QtCore.QRect(540, 80, 121, 16))
        self.label_4.setToolTip("")
        self.label_4.setStyleSheet("color:red;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(540, 140, 131, 16))
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
        cookie = login(name, password)
        if len(cookie) > 0:
            global REQUEST_COOKIE
            REQUEST_COOKIE = cookie
            ui_hello.show()
            ui_hello.ui.setCountry()
            MainWindow.close()
        else:
            msg_box = QtWidgets.QMessageBox
            msg_box.warning(self.centralwidget, "警告", "目标网站异常或者用户名/密码错误！", msg_box.Yes)
            self.lineEdit.setFocus()

# 搜索算法
class ExtendedComboBox(QComboBox):
    def __init__(self, parent=None):
        super(ExtendedComboBox, self).__init__(parent)

        self.setFocusPolicy(Qt.StrongFocus)
        self.setEditable(True)

        # add a filter model to filter matching items
        self.pFilterModel = QSortFilterProxyModel(self)
        self.pFilterModel.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.pFilterModel.setSourceModel(self.model())

        # add a completer, which uses the filter model
        self.completer = QCompleter(self.pFilterModel, self)
        # always show all (filtered) completions
        self.completer.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
        self.setCompleter(self.completer)

        # connect signals
        self.lineEdit().textEdited.connect(self.pFilterModel.setFilterFixedString)
        self.completer.activated.connect(self.on_completer_activated)


    # on selection of an item from the completer, select the corresponding item from combobox
    def on_completer_activated(self, text):
        if text:
            index = self.findText(text)
            self.setCurrentIndex(index)
            self.activated[str].emit(self.itemText(index))


    # on model change, update the models of the filter and completer as well
    def setModel(self, model):
        super(ExtendedComboBox, self).setModel(model)
        self.pFilterModel.setSourceModel(model)
        self.completer.setModel(self.pFilterModel)


    # on model column change, update the model column of the filter and completer as well
    def setModelColumn(self, column):
        self.completer.setCompletionColumn(column)
        self.pFilterModel.setFilterKeyColumn(column)
        super(ExtendedComboBox, self).setModelColumn(column)


class Ui_ContainerWindow(object):
    def setupUi(self, ContainerWindow):
        ContainerWindow.setObjectName("ContainerWindow")
        ContainerWindow.resize(1200, 600)
        self.centralwidget = QtWidgets.QWidget(ContainerWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 20, 181, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(300, 20, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(780, 20, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.toolButton.setFont(font)
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_2.setGeometry(QtCore.QRect(880, 20, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
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
        self.pushButton_3.setGeometry(QtCore.QRect(1070, 20, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")

        self.comboBox = ExtendedComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(420, 20, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setEditable(True)
        self.comboBox.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBox.setIconSize(QtCore.QSize(20, 20))
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
        #
        # self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        # self.progressBar.setGeometry(QtCore.QRect(1050, 530, 118, 51))
        # self.progressBar.setProperty("value", 0)
        # self.progressBar.setObjectName("progressBar")

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
        countryList = getCountryInfo(cookie)
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
        if len(country.split("—")) != 3:
            QMessageBox.warning(self.centralwidget, "警告", "选择的国家格式有误！", QMessageBox.Yes)
            return
        countryCode = country.split("—")[2]
        global REQUEST_COOKIE

        listData = executeSearch(searchKey, countryCode, REQUEST_COOKIE)
        if len(listData) <= 0:
            QMessageBox.warning(self.centralwidget, "警告", "该关键词查询不到数据,请更换关键词后再试!", QMessageBox.Yes)
            return
        # 开始获取联系人 10条数据为一组
        # 取10条数据，暂停1秒
        loopNum = len(listData)//10 + 1
        fileName = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + "_kjs.xls"
        print("生成的地址:", fileName)
        resList = []
        createSheet(fileName)
        for i in range(loopNum):
            itemList = getPersonInfo(REQUEST_COOKIE,listData[i * 10: (i+1)*10])
            writeSheet(itemList, fileName)
            resList.extend(itemList)
            time.sleep(1)

        self.tableWidget.setRowCount(len(resList))

        for i in range(len(resList)):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(i+1)))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(resList[i].country))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(resList[i].company))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(resList[i].domain))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(resList[i].sale))
            self.tableWidget.setItem(i, 5, QTableWidgetItem(resList[i].person))
            self.tableWidget.setItem(i, 6, QTableWidgetItem(resList[i].phone))
            self.tableWidget.setItem(i, 7, QTableWidgetItem(resList[i].address))


    def exportExcel(self):
        rowNum = self.tableWidget.rowCount()
        print(rowNum)
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
            if self.tableWidget.item(i, 5).text() == '加载中...':
                QMessageBox.warning(self.centralwidget, "警告", "联系人还未加载完成,禁止导出！", QMessageBox.Yes)
                return
            excelList.append(param)
        fileName = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + "_kjs.xls"
        file_path, ok = QFileDialog.getSaveFileName(self.centralwidget, "save file", fileName, os.path.expanduser('~'))
        if ok:
            writeExcel(excelList, file_path)
        else:
            QMessageBox.warning(self.centralwidget, "警告", "取消导出！", QMessageBox.Yes)

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MyIndexWidows()
    ui_hello = MyContainerWidows()
    ui.ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

