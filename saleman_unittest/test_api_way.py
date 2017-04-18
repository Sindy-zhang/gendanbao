#-*- coding:utf-8 -*-
__author__ = 'Administrator'
import requests
import json
from read_xl import readExcel
import xlrd
from xlutils.copy import copy
import urllib


class testApi(object):
    def TestApi(self, method, url, data, headers, cookies):
        r = ''
        if method == 'post':
            r = requests.post(url, eval(data), headers=eval(headers))
        elif method == 'get' and data == '':
            r = requests.get(url, cookies=eval(cookies))
        elif method == 'get' and data != '':
            params_data = urllib.urlencode(eval(data))
            #print "\n\n", params_data
            r = requests.get(url, params=params_data, cookies=eval(cookies))
        print '----------api_code:', r.status_code
        jsdata = json.loads(r.content)
        return jsdata

    # 将apijson_sid写入Excel中保存，并构造cookies
    def SaveCookies(self, path, apijson_sid):
        oldWb = xlrd.open_workbook(path, formatting_info=True)
        oldWb_sheet = oldWb.sheet_by_index(0)
        newWb = copy(oldWb)
        newWb_sheet = newWb.get_sheet(0)
        newWb_sheet.write(1, 7, apijson_sid)
        newWb.save(path)
        print '写入sid成功 /------------OK！', 'sid =', apijson_sid
        #构造cookies并写入到Excel中保存
        login_cookies = {"sid": apijson_sid}
        print 'login cookies:', login_cookies
        newWb_sheet.write(1, 8, str(login_cookies))
        newWb.save(path)
