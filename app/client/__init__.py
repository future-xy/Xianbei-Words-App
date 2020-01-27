#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Name    : __init__.py.py
# Time    : 2020/1/26 22:21
# Author  : Fu Yao
# Mail    : fy38607203@163.com

from flask import Blueprint

client = Blueprint('client', __name__)

from . import views
