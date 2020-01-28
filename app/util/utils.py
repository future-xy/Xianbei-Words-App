#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Name    : utils.py
# Time    : 2019/12/27 16:45
# Author  : Fu Yao
# Mail    : fy38607203@163.com

from config import ID_SPACE, TIME_FORMAT, DAY_FORMAT, ID_LEN
import random
import time
import datetime

from flask import current_app, request


def newID(prefix='', length=ID_LEN):
    l = length - 1 - len(prefix)
    return prefix + '_' + ''.join(random.sample(ID_SPACE, l))


# def timestamp():
#     return time.strftime(TIME_FORMAT)


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
