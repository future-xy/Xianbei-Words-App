#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Name    : test.py
# Time    : 2020/1/28 10:31
# Author  : Fu Yao
# Mail    : fy38607203@163.com

from requests import *

r_url = 'http://111.231.250.160:9102/'

data = {'data': {'type': 0, 'info': '0001', 'PW': '123456'}}
data2 = {'data': {"Vname": "17天搞定GRE单词"}}
data3 = {'data': {"result": [('')]}}
data4 = {
    'data': {'count_learned': 10, 'count_reviewed': 3, 'start': '2020-01-28-22-14-39', 'end': '2020-01-29-00-23-12'}}

r = post(r_url + 'signin', json=data)
