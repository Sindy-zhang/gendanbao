#-*- coding:utf-8 -*-
__author__ = 'Administrator'
import requests
import json
from read_xl import readExcel


class testApi(object):
    def TestApi(self, method, url, data, headers):
        r = ''
        if method == 'post':
            r = requests.post(url, eval(data), headers=eval(headers))
        elif method == 'get':
            r = requests.get(url, params=eval(data))
        jsdata = json.loads(r.text)
        return jsdata

    # def getCode(self):
    #     code = self.TestApi.json()['status']
    #     return code
    #
    # def getJson(self):
    #     json_data = self.TestApi.json()
    #     return json_data