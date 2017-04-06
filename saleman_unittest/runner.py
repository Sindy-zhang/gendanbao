#-*- coding:utf-8 -*-
__author__ = 'Administrator'
from read_xl import readExcel
from test_api_way import testApi
import unittest
import json
import requests
import xlrd


class testLoinApi(unittest.TestCase):
    def test_LoginApi(self):
        excel = readExcel()
        excel.path = 'G:\gendanbaocase.xls'
        name = excel.getName
        data = excel.getData
        url = excel.getUrl
        method = excel.getMethod
        code = excel.getCode
        headers_data = excel.getHeaders
        row = excel.getRows
        headers = {"Accept": "application/json",
                   "Accept-Encoding": "gzip, deflate",
                   "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A456",
                   "Accept-Language": "zh-cn"}
        for i in range(0, row-1):
            api = testApi()
            api_json = api.TestApi(method[i], url[i], data[i], headers_data[i])
            print("-------------->>>>>>>>>>>>>>")
            print(api_json)
            if api_json['status'] != "":
                self.assertEqual(code[i], api_json['status'])
                print name[i], "接口 /------------OK！api_json['status'] =", api_json['status']
            else:
                print name[i], "接口 /------------Failure！"

if __name__ == "__main__":
    unittest.main()
# if __name__ == '__main__':
#     suite = unittest.TestLoader().loadTestsFromTestCase(testLoinApi)
#     unittest.TextTestRunner(verbosity=2).run(suite)
