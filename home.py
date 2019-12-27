#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Name    : home.py
# Time    : 2019/12/11 9:34
# Author  : Fu Yao
# Mail    : fy38607203@163.com

import logging

from flask import Flask
from flask import request

from sql.sillySQL import sillySQL
from utils import *

app = Flask(__name__, static_folder="web", static_url_path="")

database = sillySQL()

# 日志系统配置
handler = logging.FileHandler('app.log', encoding='UTF-8')
# 设置日志文件，和字符编码
logging_format = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
handler.setFormatter(logging_format)
app.logger.addHandler(handler)


# home page
@app.route('/')
def home():
    return app.send_static_file('index.html')


# login page
@app.route('/signup', methods=['POST'])
def signup():
    keys = ['Uname', 'Pnumber', 'Mail', 'PW']
    if request.method == 'POST':
        form = request.json['data']
        value = [form[key] for key in keys]
        if DEBUG:
            app.logger.debug('Post in Signup: {}'.format(value))
        for i in range(1, len(value) - 1):
            data = database.SELECTfromWHERE('USERS', {keys[i]: [value[i]]})
            if len(data) > 1:
                return {'message': i, 'data': ''}
        uid = newID()
        if DEBUG:
            app.logger.debug('New UID: {}'.format(uid))
        while len(database.SELECTfromWHERE('USERS', {'UID': [uid]})) > 1:
            app.logger.info("UID conflict!")
            uid = newID()
        # uid,uname,pw,avatar,mail,pnumber,sex,education,garde
        database.INSERTvalues('USERS', (uid, value[0], value[3], None, value[2], value[1], 'U', None, None))
        return {'message': 0, 'data': uid}
    else:
        app.logger.warning("Not supported method in Signup: {}".format(request.method))


@app.route('/signin', methods=['POST'])
def signin():
    types = ['UID', 'Pnumber', 'Mail']
    keys = ['Uname', 'Pnumber', 'Mail', 'UID']
    if request.method == 'POST':
        form = request.json['data']
        if DEBUG:
            app.logger.debug('Post in Signup: {}'.format(form))
        tp = form['type']
        info = form['info']
        data = database.SELECTfromWHERE('USERS', {types[tp]: [info]})
        if len(data) != 2:
            return {'message': 1, 'data': ''}
        header = data[0]
        data = data[1]
        if data[header.index('pw')] != form['PW']:
            return {'message': 1, 'data': ''}
        if DEBUG:
            app.logger.debug('Header: {}'.format(header))
            app.logger.debug('Select data: {}'.format(data))
        index = [header.index(key.lower()) for key in keys]
        return {'message': 0, 'data': {keys[i]: data[index[i]] for i in range(len(keys))}}
    else:
        app.logger.warning("Not supported method in Signin: {}".format(request.method))


# front page
@app.route('/user/<UID>/overview', methods=['GET'])
def hello(UID):
    res = {"message": 1, "data": {}}
    data = database.SELECTfromWHERE("PLAN", "UID=" + UID)
    header = data[0]
    t = header.index["TID"]
    data = database.SELECTfromTwoTableWHERE("")
    # print(type(UID))
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
    # app.logger.error("FEEDBACK")
    # app.logger.info("FEEDBACK")
    # app.logger.warning("WARNING")
    pass
    # return "FEEDBACK"


@app.route("/test/<UID>", methods=['POST', 'GET'])
def test(UID):
    print(UID)
    if request.method == 'POST':
        # print(request.headers)
        # print(request.json['data'])
        # print(request.json['data']['username'])
        # print(request.json['data']['password'])
        # print(request.json['data']['phone'])
        # print(request.form['data'])
        return {"data": str(UID)}
        # return "USER:{} pw:{} phone:{}".format(request.form['username'], request.form['password'],
        #                                        request.form['phone'])
    else:
        # json.dump()
        # d = json.encoder()
        return {"data": str(UID)}


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
    print("!")
    app.run(host='0.0.0.0', port=9102, debug=True)
