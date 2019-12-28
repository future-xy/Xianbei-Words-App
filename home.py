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


def newID(table, name):
    id = randID()
    while len(database.SELECTfromWHERE(table, {name: [id]})) > 1:
        app.logger.info("ID conflict!")
        id = randID()
    return id


# home page
@app.route('/')
def home():
    return app.send_static_file('index.html')


# login page
@app.route('/signup', methods=['POST'])
def signup():
    keys = ['Uname', 'Pnumber', 'Mail', 'PW']
    if request.method == 'POST':
        try:
            form = request.json['data']
            value = [form[key] for key in keys]
        except KeyError as k:
            app.logger.error("KeyError: {}".format(k.args[0]))
            return STD_ERROR
        else:
            app.logger.debug('Post: {}'.format(value))
            for i in range(1, len(value) - 1):
                data = database.SELECTfromWHERE('USERS', {keys[i]: [value[i]]})
                if len(data) > 1:
                    return {'message': i, 'data': ''}
            uid = newID('USERS', 'UID')
            app.logger.debug('New UID: {}'.format(uid))
            # uid,uname,pw,avatar,mail,pnumber,sex,education,garde
            database.INSERTvalues('USERS', (uid, value[0], value[3], None, value[2], value[1], 'U', None, None))
            return {'message': 0, 'data': uid}
    else:
        app.logger.warning("Not supported method: {}".format(request.method))


@app.route('/signin', methods=['POST'])
def signin():
    types = ['UID', 'Pnumber', 'Mail']
    keys = ['Uname', 'Pnumber', 'Mail', 'UID']
    if request.method == 'POST':
        try:
            form = request.json['data']
            app.logger.debug('Post: {}'.format(form))
            tp = form['type']
            info = form['info']
            pw = form['PW']
        except KeyError as k:
            app.logger.error("KeyError: {}".format(k.args[0]))
            return STD_ERROR
        else:
            data = database.SELECTfromWHERE('USERS', {types[tp]: [info]})
            if len(data) != 2:
                return STD_ERROR
            header = data[0]
            data = data[1]
            if data[header.index('pw')] != pw:
                return STD_ERROR
            if DEBUG:
                app.logger.debug('Header: {}'.format(header))
                app.logger.debug('Select data: {}'.format(data))
            index = [header.index(key.lower()) for key in keys]
            return {'message': 0, 'data': {keys[i]: data[index[i]] for i in range(len(keys))}}
    else:
        app.logger.warning("Not supported method: {}".format(request.method))


# front page
@app.route('/user/<UID>/overview', methods=['GET'])
def hello(UID):
    if request.method == 'GET':
        learn = 100
        review = 150
        have_learned = database.SELECTfromWHERE('PLAN', {'UID': [UID], 'Proficiency': [1, 2, 3]})
        not_learned = database.SELECTfromWHERE('PLAN', {'UID': [UID], 'Proficiency': [0]})
        if len(have_learned) + len(not_learned) == 2:
            app.logger.info("The user({}) didn't choose any vocabulary!")
            return STD_ERROR
        review = min(review, len(have_learned) - 1)
        learn = max(learn, len(not_learned) - 1)
        t_record = database.SELECTfromWHERE('RECORD', {'UID': [UID], 'Dates': [today()]})
        # 如果今天还没由背单词
        if len(t_record) == 1:
            y_record = database.SELECTfromWHERE('RECORD', {'UID': [UID], 'Dates': [yesterday()]})
            # 如果昨天没有背单词
            if len(y_record) == 1:
                cont = 0
            else:
                cont = y_record[1][y_record[0].index('aday')]
        else:
            cont = t_record[1][t_record[0].index('aday')]
        if len(not_learned) > 1:
            tid = not_learned[1][not_learned[0].index('tid')]
        else:
            tid = have_learned[1][have_learned[0].index('tid')]
        data = database.SELECTfromTwoTableWHERE('VOCABULARY', 'TAKES', {'TID': [tid]})
        vname = data[1][data[0].index('vname')]
        return {"message": 0, "data": {
            "Vname": vname,
            "alreadyRecite": len(have_learned) - 1,
            "remained": len(not_learned) - 1,
            "today learn": learn,
            "today review": review,
            "continuous": cont,
        }}
    else:
        app.logger.warning("Not supported method: {}".format(request.method))


@app.route('/user/<UID>/info', methods=['GET', 'POST'])
def userInfo(UID):
    keys = ['Uname', 'Avatar', 'Sex', 'Education', 'Grade']
    if request.method == 'POST':
        try:
            form = request.json['data']
            value = [form[key] for key in keys]
        except KeyError as k:
            app.logger.error("KeyError: {}".format(k.args[0]))
            return STD_ERROR
        else:
            for i in range(len(keys)):
                database.UPDATEprecise('USERS', keys[i], value[i], "UID='{}'".format(UID))
            return STD_OK
    elif request.method == 'GET':
        data = database.SELECTfromWHERE('USERS', {'UID': [UID]})
        if len(data) != 2:
            app.logger.warning("UID {} does not exist".format(UID))
            return STD_ERROR
        header = data[0]
        data = data[1]
        value = [data[header.index(key.lower())] for key in keys]
        value = [v if v != None else '' for v in value]
        return {"message": 0, "data": {
            keys[i]: value[i] for i in range(len(keys))
        }}
    else:
        app.logger.warning("Not supported method: {}".format(request.method))


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
    if request.method == 'POST':
        try:
            form = request.json['data']
            uid = form['UID']
            info = form['Info']
        except KeyError as k:
            app.logger.error("KeyError: {}".format(k.args[0]))
            return STD_ERROR
        else:
            fid = newID('FEEDBACK', 'FID')
            app.logger.debug('New FID: {}'.format(fid))
            app.logger.debug('Feedback: {} from {}'.format(info, uid))
            database.INSERTvalues('FEEDBACK', (fid, uid, timestamp(), info))
        return STD_OK
    else:
        app.logger.warning("Not supported method: {}".format(request.method))


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
    app.run(host='0.0.0.0', port=9102, debug=True)
