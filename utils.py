#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Name    : utils.py
# Time    : 2019/12/27 16:45
# Author  : Fu Yao
# Mail    : fy38607203@163.com

from settings import *
import random
import time
import datetime


def randID():
    return ''.join(random.sample(ID_SPACE, ID_LEN))


def timestamp():
    return time.strftime("%Y-%m-%d-%H-%M-%S")


def today():
    return time.strftime("%Y-%m-%d")


def yesterday():
    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
    return yesterday.strftime("%Y-%m-%d")
