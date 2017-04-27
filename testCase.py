#coding: utf-8
__author__ = 'Administrator'
# def cap_upper(S):
#     return str.capitalize(S)
# L = ['adam', 'LISA', 'barT']
# R = list(map(cap_upper,L))
# print(R)
#
# def is_odd(n):
#     return n % 2 == 1
# L =[1, 2, 4, 5, 6, 9, 10, 15]
# R = list(filter(is_odd,L))
# print(R)
#
# L = [36, 5, 12, 9, 21]
# S = sorted(L)
# print(S)
#
# def print_name():
#     name = input('what is your name?')
#     if name.endswith("tank"):
#         print( 'hello tank')
#     elif name.endswith('xiao'):
#         print('hello xiao')
#     else:
#         print('hello strange')
# print_name()
#
# from selenium import webdriver
# browser = webdriver.Firefox()
# browser.get("https://www.baidu.com/")
# browser.find_element_by_id("kw").send_keys("you")
# browser.find_element_by_id("su").click()
# 在chrome打开网站，并进行搜索
# import os
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
# os.environ["webdriver.chrome.driver"] = chromedriver
# print("start program: ")
# driver = webdriver.Chrome(chromedriver)
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.send_keys("selenium")
# elem.send_keys(Keys.RETURN)
# # su = driver.find_element_by_id("submit")
# # su.click()
# assert "Python" in driver.title
# driver.close()
# driver.quit()
#lambda  函数应用
# f = lambda x: x * x
# print(f(5))
# L = list(map(f, [y for y in range(11)]))
# print(L)
#定义一个函数返回一个另一个函数
# def build(x, y):
#     return lambda: x+y
# S = build(1, 2)
# print(S())
#定义一个class，包含属性和方法;__name和__score属性的值不允许外部修改
# class Student:
#     def __init__(self, name, score):
#         self.__name = name
#         self.__score = score
#     def print_score(self):
#         print('%s:%s' % (self.__name, self.__score))
#     def set_score(self, score):
#         if 0 <= score <= 100:
#             self.__score = score
#         else:
#             self.__score = 'wrong data'
#             # raise ValueError("bad score")
# bart = Student("lili", 98)
# bart.print_score()
# bart.score = 78
# bart.print_score()
# bart.set_score(-10)
# bart.print_score()
#
#
#
# class Students(object):
#     def get_score(self):
#         return self._score
#
#     def set_score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('bad score')
#         if value < 0 or value > 100:
#             raise ValueError('bad score')
#         self._score = value
# e = Students()
# e.set_score(50)
# print(e.get_score())
#查看系统环境变量
# import os
# print(os.name)
# print(os.environ)
# print(os.getenv('path'))
#

# 构造一个装饰器
# def log(func):
#     def f1(*k, **q):
#         print('call %s():' % func.__name__)
#         return func(*k, **q)
#     return f1
#
#
# @log
# def now():
#     print('2016-11-25')
# print(now())

# md5转格式并大写输出
# import hashlib
# def md5Encode(Str):
#     md5 = hashlib.md5()
#     md5.update(Str)
#     print(md5.hexdigest().upper())
# md5Encode("ni你里wj4456")
# md5Encode(raw_input("input:"))


# from urllib import parse, request
# postdata = parse.urlencode(
#     {
#         'username': 'lili',
#         'password': 'lili',
#         'continuURI': 'http://www.verycd.com/',
#         'fk': fk,
#         'login_submit': '登录'
#
#     }
# )
#判断一个字符串是否为整数
# def str_is_num():
#     str = raw_input("please input a string:")
#     try:
#         if str[0] == '0':
#             #print '0'
#             return 0
#         else:
#             str1 = int(str)
#             print type(str1)
#             if isinstance(str1, int):
#                 print str1
#             else:
#                 #print '0'
#                 return 0
#     except:
#         #print '0'
#         return 0
# str_is_num()
#
def str_is_real():
    str = raw_input("please input a string:")
    arr = []
    for i in str:
        try:
            if i == '(':
                arr.append(i)
                #print(arr)
            elif i == ')' and len(arr) != 0:
                arr.pop()
            else:
                print 'false'
                return 'false'
        except:
            print 'false'
    if len(arr) == 0:
        print 'true'
        return 'true'
    else:
        print "false"
        return 'false'
str_is_real()