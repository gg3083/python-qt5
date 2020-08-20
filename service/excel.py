# -*- coding: utf-8 -*-
import datetime
import os

import xlrd
import xlwt

from xlutils.copy import copy

from model.ExcelParam import ExcelParam


def createSheet(fileName):
    exists = os.path.exists( fileName)
    if not exists:
        workbook = xlrd.open_workbook(r'./template.xlsx')
        sheet1 = workbook.sheet_by_name('Sheet1')
        wb = xlwt.Workbook()
        ws = wb.add_sheet('Sheet1')
        titles = sheet1.row_values(0)
        for i in range(0, len(titles)):
            ws.write(0, i, titles[i])
        wb.save(fileName)
    else:
        print("1存在了")

def writeSheet(list, fileName):
    workbook = xlrd.open_workbook(fileName)
    row = workbook.sheets()[0].nrows  # 获取已有的行数
    print(row)
    excel = copy(workbook)  # 将xlrd的对象转化为xlwt的对象
    ws = excel.get_sheet(0)  # 获取要操作的sheet
    # print(sheet1.row_values(0))
    for i in range(0, len(list)):
        ws.write(row+i, 0, list[i].id)
        ws.write(row+i, 1, list[i].country)
        ws.write(row+i, 2, list[i].company)
        ws.write(row+i, 3, list[i].domain)
        ws.write(row+i, 4, list[i].sale)
        ws.write(row+i, 5, list[i].person)
        ws.write(row+i, 6, list[i].phone)
        ws.write(row+i, 7, list[i].address)
    excel.save(fileName)


if __name__ == '__main__':
    list = []
    for i in range(10):
        param = ExcelParam()
        j = str(i)
        param.id = i
        param.person = '联系人'+j
        param.sale = '销售' + j
        param.address = '地址 ' + j
        param.phone = '电话'+j
        param.domain = '网站' + j
        param.company = '公司' + j
        param.country = '国家' + j
        list.append(param)
    fileName = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + "_kjs.xls"
    createSheet(fileName)
    print(len(list))
    writeSheet(list, fileName)