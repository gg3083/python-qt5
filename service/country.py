import datetime
import json

import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup


def getCountryInfo(cookie):
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

    url = "https://vip.lsmaps.com/api/RestBusinessData"

    resBody = requests.get(url, headers=headers)
    countryList = []
    try:
        jsonTxt = json.loads(resBody.text)
        for item in jsonTxt:
            countrys = item['CountryEn'] + '—' + item['CountryCn'] + '—' + item['CountryCode']
            countryList.append(countrys)
        return countryList
    except Exception:
        return countryList




if __name__ == '__main__':
    cookie = '__RequestVerificationToken=r3C7PlD_eIf0-QzESJyJM4C3hlScMIM5Dp0VA0jNIdy14D8MbsZ3ye7nNeWy5DnGsym20A2; _safe_token_=49E6D91D60E8B75893028E43A2B7DB77D68106626E9ED6FAF1401B99A03AB7F266EC5802FF2EC3AA24BF97CEEA50A1EFEF7CFEF51A55645F18286944C678935B; lsxx=01B8515C797DA1B830BCC72BF7D47613F33DAAC25177BB040150C5982FB8156F9BD023A3F6CFE043C0B24B8AFFFAB770A53B63A65AF77B73926D0BF5EF5F1266FB4445EBB5324AE929670A26A04F4FB366DF0AC1F9851C38A375B9A44DF1396DC5EE4482633088D8C6FBD55FE2794646272E9DEF67CF4C3FA57AB4E38FD01C15B912AF0EE88AF720767AFF3F'
    getCountryInfo(cookie)