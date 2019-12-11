#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Name    : home.py
# Time    : 2019/12/11 9:34
# Author  : Fu Yao
# Mail    : fy38607203@163.com

from flask import Flask

app = Flask(__name__)

test_file = "test.html"
with open(test_file, encoding='utf-8') as f:
    page = f.read()


@app.route('/user/<name>')
def hello(name):
    return "Hello " + str(name)


@app.route('/news')
def news():
    return page


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9102, debug=True)
