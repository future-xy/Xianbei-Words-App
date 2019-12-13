#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Name    : home.py
# Time    : 2019/12/11 9:34
# Author  : Fu Yao
# Mail    : fy38607203@163.com

from flask import Flask
from flask import request

app = Flask(__name__, static_folder="web", static_url_path="")


# home page
@app.route('/')
def home():
    return app.send_static_file('index.html')


# login page
@app.route('/signup', methods=['POST'])
def signup():
    pass
    # return "UP"


@app.route('/signin', methods=['POST'])
def signin():
    pass
    # return "IN"


# front page
@app.route('/user/<UID>/overview', methods=['GET'])
def hello(UID):
    # return str(UID)
    pass


@app.route('/user/<UID>/info', methods=['GET', 'POST'])
def userInfo(UID):
    pass
    # if request.method == 'POST':
    #     return str(UID) + "POST"
    # else:
    #     return str(UID) + "GET"


@app.route('/user/<UID>/plan', methods=['POST'])
def updateUserPlan(UID):
    pass
    # return UID


# test page
@app.route('/plan/<UID>/<index>', methods=['GET'])
def getTest(UID, index):
    # print(UID)
    # print(index)
    # return "Hello" + str(UID) + str(index)
    pass


@app.route('/plan/<UID>', methods=['GET', 'POST'])
def updatePlan(UID):
    pass
    # if request.method == 'GET':
    #     return "GET" + str(UID)
    # else:
    #     return "POST" + str(UID)
    # return UID


@app.route('/word/<WID>', methods=['GET'])
def getWord(WID):
    pass
    # return WID


@app.route('/info/<UID>', methods=['GET'])
def getInfo(UID):
    pass
    # return UID


@app.route('/feedback', methods=['POST'])
def feedback():
    pass
    # return "FEEDBACK"


# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     return 'Post {}'.format(post_id)
#
#
# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     return 'Subpath {}'.format(subpath)
#
#
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return "USERNAME:" + request.form['username'] + "    " + "PASSWORD:" + request.form['password']
#     else:
#         print(request.args.get('name'))
#         return str(dir(request))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9102, debug=True)
