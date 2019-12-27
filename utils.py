#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Name    : utils.py
# Time    : 2019/12/27 16:45
# Author  : Fu Yao
# Mail    : fy38607203@163.com

from settings import *
import random


def newID():
    return ''.join(random.sample(ID_SPACE, ID_LEN))
