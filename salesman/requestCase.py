#-*- coding:utf-8 -*-
__author__ = 'Administrator'
# 基本get请求
# import requests
# url = 'http://www.zhidaow.com'
# r = requests.get(url)
# print(r.status_code)
# print(r.text)

# 跟单宝login操作
# import requests
# headers = {"Accept": "application/json",
#                "Accept-Encoding": "gzip, deflate",
#                "Accept-Language": "zh-cn",
#                "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A456"
#             }
#
#
# def gdb_logiin(username):
#     url1 = 'http://10.0.4.71:7083/common.do?'
#     data = {"md5Pwd": "21218cca77804d2ba1922c33e0151105",
#             "method": "login",
#             "registrationId": "171976fa8a8f7f25151",
#             "subtime": "1480412138509",
#             "username": username,
#             "validCode": ""}
#     res1 = requests.post(url1, data, headers=headers)
#     print "login status_code:", res1.status_code
#     print(res1.content)
#     print "login cookies:", res1.cookies
#     print(res1.json())
#     print(username)
#     return res1.cookies
# username = raw_input('input:')
# gdb_logiin(username)
# url2 = 'http://10.0.4.71:7083/contact.do?keyword=&method=searchLoanContact&page=0&size=10&statusId=&subtime=1486632870130'
# res2 = requests.post(url2, cookies=gdb_logiin(username), headers=headers)
# print(res2.status_code)
# print(res2.content)

#使用session进行跟单宝登录并查询我的客户列表
import requests

headers = {"Accept": "application/json",
                   "Accept-Encoding": "gzip, deflate",
                   "Accept-Language": "zh-cn",
                   "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A456"
            }


def gdb_login(username):

    url1 = 'http://10.0.4.71:7083/common.do?'
    data = {"md5Pwd": "21218cca77804d2ba1922c33e0151105",
            "method": "login",
            "registrationId": "171976fa8a8f7f25151",
            "subtime": "1480412138509",
            "username": username,
            "validCode": ""}
    u_seesion = requests.session()
    res1 = u_seesion.post(url1, data, headers=headers)
    # print "login status_code:", res1.status_code
    print "res1 content:\n", res1.content
    print "login cookies:\n", res1.cookies
    #print(res1.json())
    return u_seesion


def gdb_searchloancontact():

    username = raw_input("input name:")
    url2 = 'http://10.0.4.71:7083/contact.do?keyword=&method=searchLoanContact&page=0&size=10&statusId=&subtime=1486632870130'
    res2 = gdb_login(username).get(url2, headers=headers)
    print "searchLoancontact status_code:", res2.status_code
    print "res2 content:\n", res2.content

gdb_searchloancontact()
