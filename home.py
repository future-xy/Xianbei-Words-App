#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Name    : home.py
# Time    : 2019/12/11 9:34
# Author  : Fu Yao
# Mail    : fy38607203@163.com

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "Welcome"
