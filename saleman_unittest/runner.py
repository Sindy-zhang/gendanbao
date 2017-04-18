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
            apijson_sort = json.dumps(api_json, sort_keys=True, indent=2, ensure_ascii=False)
            print apijson_sort
            print type(api_json)
            print type(apijson_sort)
            api.WritetoExcel('G:\myPython\mypro\saleman_unittest\gendanbaocase.xls', i, apijson_sort)
            #print(str(api_json).encode('gbk'))
            if api_json['status'] != "":
                self.assertEqual(code[i], api_json['status'])
                print name[i], "接口 /------------OK！api_json['status'] =", api_json['status']
            else:
                print name[i], "接口 /------------Failure！"
            #对登录接口特殊处理，获取sid，并写入到Excel中保存
            if api_json['method'] == 'loginV2' and api_json['status'] == 200:
                # oldWb = xlrd.open_workbook('G:\gendanbaocase.xls', formatting_info=True)
                # oldWb_sheet = oldWb.sheet_by_index(0)
                # newWb = copy(oldWb)
                # newWb_sheet = newWb.get_sheet(0)
                # newWb_sheet.write(1, 7, api_json['result']['sid'])
                # newWb.save('G:\gendanbaocase.xls')
                # print '写入sid成功 /------------OK！', 'sid =', api_json['result']['sid']
                # #构造cookies并写入到Excel中保存
                # login_cookies = {"sid": api_json['result']['sid']}
                # print login_cookies
                # newWb_sheet.write(1, 8, str(login_cookies))
                # newWb.save('G:\gendanbaocase.xls')
                # cookies_data = excel.getCookies
                api_cookies = api.SaveCookies('G:\myPython\mypro\saleman_unittest\gendanbaocase.xls', api_json['result']['sid'])
                print api_cookies
                #设置登录后的cookies
                cookies_data = excel.getCookies

if __name__ == "__main__":
    unittest.main()
# if __name__ == '__main__':
#     suite = unittest.TestLoader().loadTestsFromTestCase(testLoinApi)
#     unittest.TextTestRunner(verbosity=2).run(suite)
