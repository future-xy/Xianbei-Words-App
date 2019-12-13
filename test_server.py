#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Name    : test_server.py
# Time    : 2019/12/13 22:57
# Author  : Fu Yao
# Mail    : fy38607203@163.com

import requests

url = "http://localhost:9102/"
usertest1 = "user/0/overview"
plantest1 = "plan/0001/0"
res = requests.post(url + "feedback")
print(res.text)
