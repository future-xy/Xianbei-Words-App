#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Name    : home.py
# Time    : 2019/12/11 9:34
# Author  : Fu Yao
# Mail    : fy38607203@163.com

from flask import Flask
from flask import request

app = Flask(__name__, static_folder="web", static_url_path="")

test_file = "test.html"
with open(test_file, encoding='utf-8') as f:
    page = f.read()


@app.route('/user/<name>')
def hello(name):
    return "Hello " + str(name)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post {}'.format(post_id)


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return 'Subpath {}'.format(subpath)


@app.route('/news')
def news():
    return page


@app.route('/')
def home():
    return app.send_static_file('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "USERNAME:" + request.form['username'] + "    " + "PASSWORD:" + request.form['password']
    else:
        print(request.args.get('name'))
        return str(dir(request))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9102, debug=True)
