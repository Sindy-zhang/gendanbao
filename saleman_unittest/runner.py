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
        excel.path = 'G:\gendanbaocase.xls'
        name = excel.getName
        data = excel.getData
        url = excel.getUrl
        method = excel.getMethod
        code = excel.getCode
        headers_data = excel.getHeaders
        row = excel.getRows
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
            if api_json['method'] == 'loginV2' and api_json['status'] == 200:
                oldWb = xlrd.open_workbook('G:\gendanbaocase.xls', formatting_info=True)
                oldWb_sheet = oldWb.sheet_by_index(0)
                newWb = copy(oldWb)
                newWb_sheet = newWb.get_sheet(0)
                newWb_sheet.write(1, 7, api_json['result']['sid'])
                newWb.save('G:\gendanbaocase.xls')
                if oldWb_sheet.cell_value(1, 7) == api_json['result']['sid']:
                    print '写入sid成功 /------------', 'sid =', api_json['result']['sid']
if __name__ == "__main__":
    unittest.main()
# if __name__ == '__main__':
#     suite = unittest.TestLoader().loadTestsFromTestCase(testLoinApi)
#     unittest.TextTestRunner(verbosity=2).run(suite)
