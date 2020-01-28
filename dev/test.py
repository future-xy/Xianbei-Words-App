#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Name    : test.py
# Time    : 2020/1/28 10:31
# Author  : Fu Yao
# Mail    : fy38607203@163.com

from requests import *

url = 'http://localhost:9102/'

data = {'data': {'type': 0, 'info': '0001', 'PW': '123456'}}
data2 = {'data': {"Vname": "高考单词闪过"}}

r = post(url + 'user/0002/plan', json=data2)
