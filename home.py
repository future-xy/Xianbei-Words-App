#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Name    : home.py
# Time    : 2019/12/11 9:34
# Author  : Fu Yao
# Mail    : fy38607203@163.com

import logging
import sys

from flask import Flask
from flask import request

import numpy as np

from sql.sillySQL import sillySQL
from utils import *
from settings import *

app = Flask(__name__, static_folder="web", static_url_path="")

if DEBUG:
    level = logging.DEBUG
else:
    level = logging.INFO

# 日志系统配置
file_handler = logging.FileHandler('app.log', encoding='UTF-8')
file_handler.setLevel(level)
stream_handler = logging.StreamHandler(sys.stderr)
stream_handler.setLevel(level)
# 设置日志文件，和字符编码
logging_format = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)d - %(message)s')
file_handler.setFormatter(logging_format)
stream_handler.setFormatter(logging_format)
# app logger
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.DEBUG)
# database logger
db_logger = logging.getLogger('Database')
db_logger.addHandler(file_handler)
db_logger.addHandler(stream_handler)
db_logger.setLevel(level)

database = sillySQL(logger=db_logger)


def newID(table, name):
    id = randID()
    while len(database.SELECTfromWHERE(table, {name: [id]})) > 1:
        app.logger.info("ID conflict!")
        id = randID()
    return id


# home page
@app.route('/')
def home():
    app.logger.debug('From {} User agent: {}'.format(request.remote_addr, request.user_agent))
    return app.send_static_file('index.html')


# Debug
# login page
@app.route('/signup', methods=['POST'])
def signup():
    app.logger.debug('From {} User agent: {}'.format(request.remote_addr, request.user_agent))
    keys = ['Uname', 'Pnumber', 'Mail', 'PW']
    if request.method == 'POST':
        try:
            form = request.json['data']
            value = [form[key] for key in keys]
        except KeyError as k:
            error_message = "KeyError: {}".format(k.args[0])
            app.logger.error(error_message)
            return ERROR(error_message)
        else:
            app.logger.debug('Post: {}'.format(value))
            for i in range(1, len(value) - 1):
                data = database.SELECTfromWHERE('USERS', {keys[i]: [value[i]]})
                if len(data) > 1:
                    return {'message': i, 'data': '{} conflict'.format(keys[i])}
            uid = newID('USERS', 'UID')
            app.logger.debug('New UID: {}'.format(uid))
            # uid,uname,pw,avatar,mail,pnumber,sex,education,garde
            database.INSERTvalues('USERS', (uid, value[0], value[3], None, value[2], value[1], 'U', None, None))
            return {'message': 0, 'data': uid}


# Debug
@app.route('/signin', methods=['POST'])
def signin():
    app.logger.debug('From {} User agent: {}'.format(request.remote_addr, request.user_agent))
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
            error_message = "KeyError: {}".format(k.args[0])
            app.logger.error(error_message)
            return ERROR(error_message)
        else:
            data = database.SELECTfromWHERE('USERS', {types[tp]: [info]})
            if len(data) != 2:
                return ERROR("Unable to find user")
            header = data[0]
            data = data[1]
            if data[header.index('pw')] != pw:
                return ERROR("PW error")
            app.logger.debug('Select data: {}'.format(data))
            index = [header.index(key.lower()) for key in keys]
            return {'message': 0, 'data': {keys[i]: data[index[i]] for i in range(len(keys))}}


# Debug
# front page
@app.route('/user/<UID>/overview', methods=['GET'])
def hello(UID):
    app.logger.debug('From {} User agent: {}'.format(request.remote_addr, request.user_agent))
    global REVIEW, LEARN
    review, learn = REVIEW, LEARN
    if request.method == 'GET':
        have_learned = database.SELECTfromWHERE('PLAN', {'UID': [UID], 'Proficiency': [1, 2, 3]})
        not_learned = database.SELECTfromWHERE('PLAN', {'UID': [UID], 'Proficiency': [0]})
        if have_learned is False or not_learned is False or len(have_learned) + len(not_learned) == 2:
            error_message = "The user({}) didn't choose any vocabulary!".format(UID)
            app.logger.error(error_message)
            return ERROR(error_message)
        review = min(review, len(have_learned) - 1)
        learn = min(learn, len(not_learned) - 1)
        t_record = database.SELECTfromWHERE('RECORD', {'UID': [UID], 'Dates': [today()]})
        # 如果今天还没由背单词
        if len(t_record) == 1:
            y_record = database.SELECTfromWHERE('RECORD', {'UID': [UID], 'Dates': [today(-1)]})
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


# Debug
@app.route('/user/<UID>/info', methods=['GET', 'POST'])
def userInfo(UID):
    app.logger.debug('From {} User agent: {}'.format(request.remote_addr, request.user_agent))
    keys = ['Uname', 'Avatar', 'Sex', 'Education', 'Grade']
    if request.method == 'POST':
        try:
            form = request.json['data']
            value = [form[key] for key in keys]
        except KeyError as k:
            error_message = "KeyError: {}".format(k.args[0])
            app.logger.error(error_message)
            return ERROR(error_message)
        else:
            for i in range(len(keys)):
                if not database.UPDATEprecise('USERS', keys[i], value[i], {"UID": [UID]}):
                    error_message = "Unable to update USER {}, item={}, value={}, i={}".format(UID, keys[i], value[i],
                                                                                               i)
                    app.logger.error(error_message)
                    return ERROR(error_message)
            return OK()
    elif request.method == 'GET':
        data = database.SELECTfromWHERE('USERS', {'UID': [UID]})
        if len(data) != 2:
            error_message = "UID {} does not exist".format(UID)
            app.logger.error(error_message)
            return ERROR(error_message)
        header = data[0]
        data = data[1]
        value = [data[header.index(key.lower())] for key in keys]
        value = [v if v != None else '' for v in value]
        return {"message": 0, "data": {
            keys[i]: value[i] for i in range(len(keys))
        }}


# Debug
@app.route('/plan', methods=['GET'])
def plan():
    app.logger.debug('From {} User agent: {}'.format(request.remote_addr, request.user_agent))
    if request.method == 'GET':
        vocab = database.SELECTfromWHERE('VOCABULARY')
        if vocab is False or len(vocab) < 2:
            error_message = "Unable to find any vocabulary"
            app.logger.error(error_message)
            return ERROR(error_message)
        return {"message": 0, "data": vocab[1:]}


# Debug
@app.route('/user/<UID>/plan', methods=['POST'])
def updateUserPlan(UID):
    app.logger.debug('From {} User agent: {}'.format(request.remote_addr, request.user_agent))
    if request.method == 'POST':
        try:
            vname = request.json['data']['Vname']
        except KeyError as k:
            error_message = "KeyError: {}".format(k.args[0])
            app.logger.error(error_message)
            return ERROR(error_message)
        else:
            vocab = database.SELECTfromWHERE('VOCABULARY', {'Vname': [vname]})
            if vocab is False or len(vocab) != 2:
                error_message = "Vocabulary {} does not exist".format(vname)
                app.logger.error(error_message)
                return ERROR(error_message)
            vid = vocab[1][vocab[0].index('vid')]
            if not database.DELETEprecise('PLAN', {'UID': [UID]}):
                error_message = "Unable to delete User {} from Plan".format(UID)
                app.logger.error(error_message)
                return ERROR(error_message)
            data = database.SELECTfromWHERE('TAKES', {'VID': [vid]})
            if data is False or len(data) < 2:
                error_message = "Unable to find any takes of {}".format(vname)
                app.logger.error(error_message)
                return ERROR(error_message)
            header = data[0]
            words = data[1:]
            for word in words:
                tid = word[header.index('tid')]
                wid = word[header.index('wid')]
                if not database.INSERTvalues('PLAN', (UID, tid, wid, 0)):
                    error_message = "Unable to insert ({})".format((UID, tid, wid, 0))
                    app.logger.error(error_message)
                    if not database.DELETEprecise('PLAN', {'UID': [UID]}):
                        error_message2 = "AND unable to delete User {} from Plan".format(UID)
                        app.logger.error(error_message)
                        error_message += ' ' + error_message2
                    return ERROR(error_message)
            return OK()


# Debug
# test page
@app.route('/plan/<UID>/<int:seed>', methods=['GET'])
def getTest(UID, seed):
    app.logger.debug('From {} User agent: {}'.format(request.remote_addr, request.user_agent))
    random.seed(seed)
    global REVIEW, LEARN
    review, learn = REVIEW, LEARN
    if request.method == 'GET':
        have_learned = database.SELECTfromWHERE('PLAN', {'UID': [UID], 'Proficiency': [1, 2, 3]})
        not_learned = database.SELECTfromWHERE('PLAN', {'UID': [UID], 'Proficiency': [0]})
        if have_learned is False or not_learned is False or len(have_learned) + len(not_learned) == 2:
            error_message = "The user({}) didn't choose any vocabulary".format(UID)
            app.logger.error(error_message)
            return ERROR(error_message)
        header = have_learned[0]
        have_learned = have_learned[1:]
        not_learned = not_learned[1:]
        if len(have_learned) + len(not_learned) < 4:
            error_message = "The vocabulary is too small".format(UID)
            app.logger.error(error_message)
            return ERROR(error_message)
        review = min(review, len(have_learned))
        learn = min(learn, len(not_learned))
        if len(have_learned) != 0:
            review_item = random.sample(have_learned, review)
        else:
            app.logger.debug("User {} hasn't learner any word yet".format(UID))
            review_item = []
        if len(not_learned) != 0:
            learn_item = random.sample(not_learned, learn)
        else:
            app.logger.debug("User {} doesn't have any new word to learn".format(UID))
            learn_item = []
        today_learn = []
        for item in learn_item:
            ops = random.sample(have_learned + not_learned, 4)
            if item not in ops:
                ops.pop(0)
                ops.append(item)
            options = [op[header.index('wid')] for op in ops]
            random.shuffle(options)
            today_learn.append((item[header.index('tid')],
                                item[header.index('wid')],
                                item[header.index('proficiency')],
                                options
                                ))
        today_review = []
        for item in review_item:
            ops = random.sample(have_learned + not_learned, 4)
            if item not in ops:
                ops.pop(0)
                ops.append(item)
            options = [op[header.index('wid')] for op in ops]
            random.shuffle(options)
            today_review.append((item[header.index('tid')],
                                 item[header.index('wid')],
                                 item[header.index('proficiency')],
                                 options
                                 ))
        return {"message": 0, "data": {
            "todayLearn": today_learn,
            "todayReview": today_review
        }}


# Debug
@app.route('/plan/<UID>', methods=['GET', 'POST'])
def updatePlan(UID):
    app.logger.debug('From {} User agent: {}'.format(request.remote_addr, request.user_agent))
    if request.method == 'GET':
        user_plan = database.SELECTfromTwoTableWHERE('PLAN', 'DICTIONARY', {"UID": [UID]})
        if user_plan is False or len(user_plan) == 1:
            error_message = "The user({}) didn't choose any vocabulary!".format(UID)
            app.logger.error(error_message)
            return ERROR(error_message)
        header = user_plan[0]
        data = user_plan[1:]
        plan = []
        for item in data:
            plan.append((
                item[header.index('tid')],
                item[header.index('wid')],
                item[header.index('english')],
                item[header.index('chinese')],
                item[header.index('proficiency')]
            ))
        return {"message": 0, "data": plan}
    elif request.method == 'POST':
        try:
            res = request.json['data']['result']
        except KeyError as k:
            error_message = "KeyError: {}".format(k.args[0])
            app.logger.error(error_message)
            return ERROR(error_message)
        else:
            for tid, wid, p in res:
                if not database.UPDATEprecise('PLAN', 'Proficiency', p, {'UID': [UID], 'TID': [tid], 'WID': [wid]}):
                    error_message = "Unable to update Plan UID: {} TID: {} WID: {}".format(UID, tid, wid)
                    app.logger.error(error_message)
                    return ERROR(error_message)
            return OK()


# Debug
@app.route('/word/<WID>', methods=['GET'])
def getWord(WID):
    app.logger.debug('From {} User agent: {}'.format(request.remote_addr, request.user_agent))
    if request.method == 'GET':
        keys = ['English', 'Chinese', 'Psymbol']
        data = database.SELECTfromWHERE('DICTIONARY', {'WID': [WID]})
        if data is False or len(data) != 2:
            error_message = "Unable to find word {}.".format(WID)
            app.logger.error(error_message)
            return ERROR(error_message)
        header = data[0]
        data = data[1]
        return {"message": 0, "data": {
            key: data[header.index(key.lower())] for key in keys
        }}


# Debug
@app.route('/record/<UID>', methods=['POST', 'GET'])
def record(UID):
    app.logger.debug('From {} User agent: {}'.format(request.remote_addr, request.user_agent))
    if request.method == 'POST':
        try:
            form = request.json['data']
            count = form['count']
            start = form['start']
            end = form['end']
        except KeyError as k:
            error_message = "KeyError: {}".format(k.args[0])
            app.logger.error(error_message)
            return ERROR(error_message)
        else:
            start_day = datetime.datetime.strptime(start, TIME_FORMAT)
            now_day = start_day.replace(minute=0, second=0)
            end_day = datetime.datetime.strptime(end, TIME_FORMAT)
            p = [0, 0, 0, 0]
            for i in range(len(p)):
                data = database.SELECTfromWHERE('PLAN', {'UID': [UID], 'Proficiency': [i]})
                if data is False:
                    error_message = "Unable to find Plan for User {}".format(UID)
                    app.logger.error(error_message)
                    return ERROR(error_message)
                p[i] = len(data) - 1
            while now_day <= end_day:
                this_day = now_day.strftime(DAY_FORMAT)
                today_record = database.SELECTfromWHERE('RECORD', {'Dates': [this_day], 'UID': [UID]})
                # record中没有这一天的记录
                if today_record is False or len(today_record) < 2:
                    last_record = database.SELECTfromWHERE('RECORD', {
                        'Dates': [(now_day - datetime.timedelta(days=1)).strftime(DAY_FORMAT)],
                        'UID': [UID]})
                    if last_record is False or len(last_record) == 1:
                        aday = 0
                    else:
                        aday = last_record[1][last_record[0].index('aday')] + 1
                    ahour = np.zeros(24).astype(np.float)
                    database.INSERTvalues('RECORD', (
                        newID('RECORD', 'SID'), UID, this_day, count, 0, p, ahour.tolist(), aday))
                # 有这一天的记录
                else:
                    ahour = np.array(today_record[1][today_record[0].index('ahour')])
                    database.UPDATEprecise('RECORD', 'Proficiency', p, {'UID': [UID], 'Dates': [this_day]})
                ahour[now_day.hour] = ahour[now_day.hour] + 60
                database.UPDATEprecise('RECORD', 'Ahour', ahour.tolist(), {'UID': [UID], 'Dates': [this_day]})
                now_day = now_day + datetime.timedelta(hours=1)
            this_day = start_day.strftime(DAY_FORMAT)
            start_record = database.SELECTfromWHERE('RECORD', {'Dates': [this_day], 'UID': [UID]})
            header = start_record[0]
            ahour = start_record[1][header.index('ahour')]
            ahour[start_day.hour] -= start_day.minute
            database.UPDATEprecise('RECORD', 'Ahour', ahour, {'UID': [UID], 'Dates': [this_day]})
            this_day = end_day.strftime(DAY_FORMAT)
            end_record = database.SELECTfromWHERE('RECORD', {'Dates': [this_day], 'UID': [UID]})
            ahour = end_record[1][header.index('ahour')]
            ahour[end_day.hour] -= (60 - end_day.minute)
            database.UPDATEprecise('RECORD', 'Ahour', ahour, {'UID': [UID], 'Dates': [this_day]})
            return OK()
    elif request.method == 'GET':
        data = database.SELECTfromWHERE('RECORD', {'UID': [UID]})
        if data is False or len(data) < 2:
            error_message = "Unable to find any record of User {}".format(UID)
            app.logger.error(error_message)
            return ERROR(error_message)
        header = data[0]
        data = data[1:]
        data.sort(key=lambda x: sort_by_time(x, header.index('dates'), DAY_FORMAT))
        records = {sort_by_time(item, header.index('dates'), DAY_FORMAT): item for item in data}
        days = 0
        last_day = datetime.datetime.strptime(today(-6), DAY_FORMAT).timestamp()
        for d in records:
            if d <= last_day:
                days = d
        app.logger.debug(data)
        for line in data:
            app.logger.debug(line)
        p_info = []
        a_time = []
        if days == 0:
            p_info.append((0, 0, 0, 0))
        else:
            p_info.append(records[days][header.index('proficiency')])
        for i in range(-6, 1):
            days = datetime.datetime.strptime(today(i), DAY_FORMAT).timestamp()
            if days in records:
                p_info.append(records[days][header.index('proficiency')])
                a_time.append(records[days][header.index('ahour')])
                # ahour += np.array(records[days][header.index('ahour')]).astype(np.float)
            else:
                p_info.append(p_info[-1])
                a_time.append(np.zeros(24))
        a_time = np.array(a_time)
        f_curve = np.random.normal(loc=5, size=7)
        return {'message': 0, 'data': {
            'proficiencyInfo': p_info[1:],
            'Ahour': a_time.sum(axis=0).tolist(),
            'Forgetting curve': f_curve.tolist(),
            'active time': a_time.sum(axis=1).tolist()
        }}


# Debug
@app.route('/feedback', methods=['POST'])
def feedback():
    app.logger.debug('From {} User agent: {}'.format(request.remote_addr, request.user_agent))
    if request.method == 'POST':
        try:
            form = request.json['data']
            uid = form['UID']
            info = form['Info']
        except KeyError as k:
            error_message = "KeyError: {}".format(k.args[0])
            app.logger.error(error_message)
            return ERROR(error_message)
        else:
            fid = newID('FEEDBACK', 'FID')
            app.logger.debug('New FID: {}'.format(fid))
            app.logger.debug('Feedback: {} from {}'.format(info, uid))
            database.INSERTvalues('FEEDBACK', (fid, uid, timestamp(), info))
        return OK()


@app.route('/test')
def test():
    app.logger.debug('From {} User agent: {}'.format(request.remote_addr, request.user_agent))
    return OK()


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
