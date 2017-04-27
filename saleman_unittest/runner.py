#-*- coding:utf-8 -*-
__author__ = 'Administrator'
from read_xl import readExcel
from test_api_way import testApi
import unittest
import json
import requests
import xlrd
from xlutils.copy import copy



class testLoinApi(unittest.TestCase):
    def setUp(self):
        print "start:"

    def tearDown(self):
        print "test over!"

    def test_LoginApi(self):
        excel = readExcel()
        excel.path = 'G:\myPython\mypro\saleman_unittest\gendanbaocase.xls'
        name = excel.getName
        data = excel.getData
        url = excel.getUrl
        method = excel.getMethod
        code = excel.getCode
        headers_data = excel.getHeaders
        cookies_data = ''
        row = excel.getRows
        for i in range(0, row-1):
            api = testApi()
            api_json = api.TestApi(method[i], url[i], data[i], headers_data[i], cookies_data)
            print("-------------->>>>>>>>>>>>>>")
            #指定json格式数据的参数缩进indent，ensure_ascii=FALSE保留中文字符
            apijson_sort = json.dumps(api_json, sort_keys=True, indent=2, ensure_ascii=False)
            print apijson_sort
            api.WritetoExcel('G:\myPython\mypro\saleman_unittest\gendanbaocase.xls', i, apijson_sort)
            if api_json['status'] != "":
                self.assertEqual(code[i], api_json['status'])
                print name[i], "接口 /------------OK！api_json['status'] =", api_json['status']
            else:
                print name[i], "接口 /------------Failure！"
            #对登录接口特殊处理，获取sid，并写入到Excel中保存
            if api_json['method'] == 'loginV2' and api_json['status'] == 200:
                api_cookies = api.SaveCookies('G:\myPython\mypro\saleman_unittest\gendanbaocase.xls', api_json['result']['sid'])
                print api_cookies
                #设置登录后的cookies
                cookies_data = excel.getCookies

# if __name__ == "__main__":
#     unittest.main()
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(testLoinApi)
    unittest.TextTestRunner(verbosity=2).run(suite)
