#-*- coding:utf-8 -*-
__author__ = 'Administrator'
import requests
import json
import urllib

headers = {"Accept": "application/json",
           "Accept-Encoding": "gzip, deflate",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A456",
            "Accept-Language": "zh-cn"}


def hd_login():
    phone = raw_input("input phone :")
    url = 'http://10.0.4.71:8085/common.do?'
    data = {"idfa": "80F1F3F7-24A0-4357-B64E-85B9A588CBBF",
            "imei": "",
            "mac": "02%3A00%3A00%3A00%3A00%3A00",
            "md5Pwd": "dc483e80a7a0bd9ef71d8cf973673924",
            "method": "loginV2",
            "subtime": "1482804770576",
            "username": phone,
            "validCode": ""
            }
    res1 = requests.post(url, data, headers=headers)
    print "hd_login status_code:", res1.status_code
    print "hd_login content:\n", res1.content
    # print "res1 cookies:", res1.cookies
    return res1.json()


def login_cookies():
    s = hd_login()
    sid = s["result"]["sid"]
    print sid
    loginCookies = {"sid": sid}
    return loginCookies


def hd_queryApplyProcess():
    #hd_login(phone)
    url2 = 'http://10.0.4.71:8085/business.do?method=queryApplyProcess&subtime=1479353084600'
    res2 = requests.get(url2, headers=headers, cookies=login_cookies())
    print "\n\nhd_queryApplyProcess status_code:", res2.status_code
    print "res2 cookies:", res2.cookies
    print "hd_queryApplyProcess content:\n", res2.content
# hd_queryApplyProcess()


def hd_applyNewLoan():
    url3 = "http://10.0.4.71:8085/business.do?"
    data3_1 = {"name": "程永", "idcard": "330722197011215918", "phone": "13536670555", "loanMoney": "99000", "loanLimit": 12, "empNo": "", "provinceId": 19,
               "cityId": 202, "gpsProvince": "", "gpsCity": "", "longitude": "114.03441325044989,65", "channelCode": "010"}
    data3 = {"loanInfoJsonStr": data3_1,
              "method": "applyNewLoan",
              "subtime": "1481092917560"}
    params = urllib.urlencode(data3)    #把整个body数据转为16进制
    res3 = requests.get(url3, params=params, cookies=login_cookies(), headers=headers)
    print "\n\nhd_applyNewLoan status_code:", res3.status_code
    print "res cookies:", res3.cookies
    print "hd_applyNewLoan content:\n", res3.content
hd_applyNewLoan()