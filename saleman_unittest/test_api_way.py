#-*- coding:utf-8 -*-
__author__ = 'Administrator'
import requests
import json
from read_xl import readExcel


class testApi(object):
    def TestApi(self, method, url, data, headers, cookies):
        r = ''
        if method == 'post':
            r = requests.post(url, eval(data), headers=eval(headers))
        elif method == 'get' and data == '':
            r = requests.get(url, cookies=eval(cookies))
        elif method == 'get' and data != '':
            r = requests.get(url, params=eval(data), cookies=eval(cookies))
        jsdata = json.loads(r.content)
        return jsdata
