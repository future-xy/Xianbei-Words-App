#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Name    : logger.py
# Time    : 2020/1/26 22:21
# Author  : Fu Yao
# Mail    : fy38607203@163.com

import logging
from logging.handlers import TimedRotatingFileHandler


# 日志过滤器，根据不同等级（DEBUG, INFO等）进行过滤
class LogLevelFilter(logging.Filter):
    def __init__(self, name='', level=logging.DEBUG):
        super(LogLevelFilter, self).__init__(name)
        self.level = level

    def filter(self, record):
        return record.levelno == self.level


# 日志记录器初始化
def logger_init(log_file_path, log_level):
    logger = TimedRotatingFileHandler(filename=log_file_path, when="W6", interval=1, )
    logger.setLevel(log_level)
    logger.addFilter(LogLevelFilter(level=log_level))
    logger.setFormatter(
        logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'))
    return logger
