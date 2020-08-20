import datetime

import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup


def openIndex2Cookie():  # 打开首页拿到cooke
    session = requests.session()
    resBody = session.get("https://vip.lsmaps.com/Common/Login?ReturnUrl=%2f")
    # indexCookie = requests.utils.dict_from_cookiejar(session.cookies)
    # print(indexCookie)
    # if len(indexCookie) < 1:
    #     raise Exception('打开跨境搜页面失败,请稍后再试！')
    body = resBody.text
    # print(body)
    soup = BeautifulSoup(body, 'html.parser')
    try:
        token = soup.find('input', {'name': 'tboxToken'}).get('value')
    except:
        return ""
    return token


def getLoginInfo(tboxAccount, tboxPassword, token):
    ua = UserAgent()
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Host': 'vip.lsmaps.com',
        'Referer': 'https://www.baidu.com',
        'User-Agent': ua.random,
        'Content-Type': 'application/x-www-form-urlencoded',
        # 'Cookie': cookie,
    }

    url = "http://vip.lsmaps.com/Common/CheckLogin"
    requestParam = {
        'tboxAccount': tboxAccount,
        'tboxPassword': tboxPassword,
        'tboxToken': token,
    }
    session = requests.session()
    resBody = session.post(url, requestParam, headers=headers)
    # print(resBody)
    # print(resBody.text)
    newCookie = requests.utils.dict_from_cookiejar(session.cookies)
    cookie = ""
    if newCookie:
        for i in newCookie:
            cookie = cookie + i + '=' + newCookie[i] + '; '
        print(cookie)
        return cookie
    else:
        return ''



def login(name, password):
    token = openIndex2Cookie()
    if len(token) < 1:
        return ""
    req_cookie = getLoginInfo(name, password, token)
    return req_cookie
