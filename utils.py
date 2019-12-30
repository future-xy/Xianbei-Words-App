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
    return time.strftime(TIME_FORMAT)


# def today():
#     return time.strftime("%Y-%m-%d")


def today(d=0):
    yesterday = datetime.datetime.now() + datetime.timedelta(days=d)
    return yesterday.strftime(DAY_FORMAT)


def sort_by_time(x, i, f):
    return datetime.datetime.strptime(x[i], f).timestamp()


def ERROR(info=''):
    return {'message': 1,
            'data': info}


def OK():
    return {"message": 0,
            'data': ''}
