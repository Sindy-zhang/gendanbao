#-*- coding:utf-8 -*-
import requests
import json
import urllib
import unittest


class LoginSuit(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        print 'test over'

    def test_login(self):
        # self.phone = raw_input("input phone :")
        headers = {"Accept": "application/json",
                   "Accept-Encoding": "gzip, deflate",
                   "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A456",
                   "Accept-Language": "zh-cn"}
        url = 'http://10.0.4.71:8085/common.do?'
        data = {"idfa": "80F1F3F7-24A0-4357-B64E-85B9A588CBBF",
                "imei": "",
                "mac": "02%3A00%3A00%3A00%3A00%3A00",
                "md5Pwd": "dc483e80a7a0bd9ef71d8cf973673924",
                "method": "loginV2",
                "subtime": "1482804770576",
                "username": "13536670555",
                "validCode": ""
                }
        res1 = requests.post(url, data, headers=headers)
        self.assertTrue(res1.status_code == 200, 'code is error!')
        # print "hd_login status_code:", res1.status_code
        # print "hd_login content:\n", res1.content
        return res1.json()

    def test_cookies(self):
        s = LoginSuit.test_login(self)
        status = s["status"]
        if status == 200:
            sid = s["result"]["sid"]
            loginCookies = {"sid": sid}
            print loginCookies
            return loginCookies
        else:
            print'\nlogin failed'


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginSuit)
    unittest.TextTestRunner(verbosity=2).run(suite)
    # unittest.main(verbosity=2)


class QueryApplyProcess(LoginSuit):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_queryApplyProcess(self):
        headers = {"Accept": "application/json",
                   "Accept-Encoding": "gzip, deflate",
                   "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A456",
                   "Accept-Language": "zh-cn"}
        url2 = 'http://10.0.4.71:8085/business.do?method=queryApplyProcess&subtime=1479353084600'
        res2 = requests.get(url2, headers=headers, cookies=LoginSuit.test_cookies(self))
        print "\n\nhd_queryApplyProcess status_code:", res2.status_code
        print "res2 cookies:", res2.cookies
        print "hd_queryApplyProcess content:\n", res2.content



    #
    # # hd_queryApplyProcess()
    #
    # def hd_applyNewLoan():
    #     phone = raw_input("input phone :")
    #     url3 = "http://10.0.4.71:8085/business.do?"
    #     name = urllib.quote("程永")   #先对中文进行编码
    #     data3_1 = {"name": name, "idcard": "330722197011215918", "phone": "13536670555", "loanMoney": "99000", "loanLimit": 12, "empNo": "", "provinceId": 19,
    #                "cityId": 202, "gpsProvince": "", "gpsCity": "", "longitude": "114.03441325044989,65", "channelCode": "010"}
    #     data3 = {"loanInfoJsonStr": data3_1,
    #               "method": "applyNewLoan",
    #               "subtime": "1481092917560"}
    #     params = urllib.urlencode(data3)    #把整个body数据转为16进制
    #     res3 = requests.get(url3, params=params, cookies=hd_login(phone), headers=headers)
    #     print "\n\nhd_applyNewLoan status_code:", res3.status_code
    #     print "res cookies:", res3.cookies
    #     print "hd_applyNewLoan content:\n", res3.content
    # hd_applyNewLoan()

