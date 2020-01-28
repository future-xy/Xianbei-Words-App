#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Name    : test.py
# Time    : 2020/1/28 10:31
# Author  : Fu Yao
# Mail    : fy38607203@163.com

from requests import *

url = 'http://111.231.250.160:9102/'

data = {'data': {'type': 0, 'info': '0001', 'PW': '123456'}}
data2 = {'data': {"Vname": "17天搞定GRE单词"}}
data3 = {'data': {"result":[('')]}}

r = post(url + 'user/0002/plan', json=data2)
