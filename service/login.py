import datetime

import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup



def openIndex2Cookie():  # 打开首页拿到cooke
    session = requests.session()
    resBody = session.get("https://vip.lsmaps.com/Common/Login")
    indexCookie = requests.utils.dict_from_cookiejar(session.cookies)
    if len(indexCookie) < 1:
        raise Exception('打开跨境搜页面失败,请稍后再试！')
    body = resBody.text
    soup = BeautifulSoup(body, 'html.parser')
    token = soup.find('input', {'name': '__RequestVerificationToken'}).get('value')
    return indexCookie, token


def getLoginInfo(tboxAccount, tboxPassword, token, cookie):
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

    url = "http://vip.lsmaps.com/Common/CheckLogin"
    requestParam = {
                    'tboxAccount': tboxAccount,
                    'tboxPassword': tboxPassword,
                    '__RequestVerificationToken': token,
    }
    print(headers)
    session = requests.session()
    resBody = session.post(url, requestParam, headers=headers)
    # print(resBody)
    # print(resBody.text)
    newCookie = requests.utils.dict_from_cookiejar(session.cookies)
    print(newCookie)
    for i in newCookie:
        cookie = cookie + '; ' + i + '=' + newCookie[i]

    print(cookie)

if __name__ == '__main__':
    name = '15995794506@126.com'
    pwd = '15995794506'
    # token = 'Z0KqS1zdX427n92rMJqkTA1QC0iINmD8SFgU17udtfcVAIiik6_ow5r6p8x_KlPNRGuLLw2'
    # getLoginInfo(name, pwd, token)
    indexCookie, token = openIndex2Cookie()
    sumCookie = ''
    for i in indexCookie:
        if len(sumCookie) > 0:
            sumCookie = sumCookie + ';'
        sumCookie = sumCookie + i + '=' + indexCookie[i]
    print(sumCookie, token)
    getLoginInfo(name, pwd, token, sumCookie)