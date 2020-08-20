import requests
import json
import re
import datetime;

import xlwt as xlwt
from fake_useragent import UserAgent

from model.ExcelParam import ExcelParam

def get_base_data(url, pageNo, headers, list):
    res = requests.get(url + str(pageNo), headers=headers)
    json_res = json.loads(res.text)
    try:
        json_data = json_res["Data"]
        json_count = json_res["Count"]
        if json_data is None:
            return 0
        i = 0
        for item in json_data:
            param = ExcelParam()
            param.id = i + (pageNo - 1) * 10
            param.country = item['CountryName']
            param.company = item['PrimaryName']
            param.domain = item['Domian']
            param.person = '加载中...'
            param.phone = item['TelephoneNumber']
            param.address = item['Address']
            param.sale = item['YearlyRevenue']
            param.dnbNumber = item['DnbNumber']
            list.append(param)
            i = i + 1
        return json_count
    except:
        return 0


def getPersonInfo(cookie, list):

    url = "https://vip.lsmaps.com/BusinessData/CompanyReport?u="
    ua = UserAgent()
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Host': 'vip.lsmaps.com',
        'Referer': 'https://www.baidu.com',
        'User-Agent': ua.random,
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': cookie,
    }
    for item in list:
        detailHtml = requests.get(url + item.dnbNumber, headers=headers)
        detailHtml.encoding = 'utf-8'
        reg = re.search(r'"fullName":.*', detailHtml.text)
        person = '--'
        try:
            if len(reg.group(0)) > 0:
                person = reg.group(0).split(":")[1]
                person = person.strip(" ").strip("\"").replace('\"', '').replace(",", "")

        except Exception as e:
            print(e)
        item.person = person
    return list

def writeExcel(list, fileName):
    wb = xlwt.Workbook()
    # 添加一个表
    ws = wb.add_sheet('sheet1')
    # 添加标题
    ws.write(0, 0, '序号')
    ws.write(0, 1, '国家')
    ws.write(0, 2, '公司名称')
    ws.write(0, 3, '网址')
    ws.write(0, 4, '销售额(年)')
    ws.write(0, 5, '联系人')
    ws.write(0, 6, '电话/手机')
    ws.write(0, 7, '地址')
    for i in range(1, len(list) + 1):
        ws.write(i, 0, i)
        ws.write(i, 1, list[i - 1].country)
        ws.write(i, 2, list[i - 1].company)
        ws.write(i, 3, list[i - 1].domain)
        ws.write(i, 4, list[i - 1].sale)
        ws.write(i, 5, list[i - 1].person)
        ws.write(i, 6, list[i - 1].phone)
        ws.write(i, 7, list[i - 1].address)
    # 3个参数分别为行号，列号，和内容
    # 需要注意的是行号和列号都是从0开始的

    # 保存excel文件
    wb.save(fileName)



def  executeSearch(searchKey, countryCode, cookie):
    time = datetime.datetime.now().timestamp()

    ua = UserAgent()
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Host': 'vip.lsmaps.com',
        'Referer': 'https://www.baidu.com',
        'User-Agent': ua.random,
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': cookie,
    }
    url = "https://vip.lsmaps.com/api/RestBusinessCompany?companyName="+searchKey+"&countryCode="+countryCode+"&SicCode=&pageindex="

    list = []
    pageNo = 1
    while True:
        pageMax = get_base_data(url, pageNo, headers, list)
        pageNo = pageNo + 1
        # if pageNo > 2:
        if pageNo > pageMax/10 + 1:
            break
    # list = get_person_info(detailUrl, headers, list)
    return list
