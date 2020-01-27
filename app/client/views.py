#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Name    : views.py
# Time    : 2020/1/26 22:28
# Author  : Fu Yao
# Mail    : fy38607203@163.com

from app import db
from . import client

from flask import request, current_app

from models import Users, Vocabulary, Dictionary, Feedback, Plan, Record, Takes
from flask_login import current_user, login_user, login_required

import random


@client.route('/test')
def test():
    print("RUNNING!")
    info = "LOG INFO"
    current_app.logger.debug(info)
    current_app.logger.info(info)
    current_app.logger.warning(info)
    current_app.logger.error(info)
    current_app.logger.critical(info)
    return "HELLO WORLD"
#
# # home page
# @client.route('/')
# def home():
#     client.logger.debug('From {} User agent: {}'.format(request.remote_addr, request.user_agent))
#     return client.send_static_file('index.html')
#
#
# # Debug
# # login page
# @client.route('/signup', methods=['POST'])
# def signup():
#     client.logger.debug('From {} User agent: {}'.format(request.remote_addr, request.user_agent))
#     keys = ['Uname', 'Pnumber', 'Mail', 'PW']
#     if request.method == 'POST':
#         try:
#             form = request.json['data']
#             value = [form[key] for key in keys]
#         except KeyError as k:
#             error_message = "KeyError: {}".format(k.args[0])
#             client.logger.error(error_message)
#             return ERROR(error_message)
#         else:
#             client.logger.debug('Post: {}'.format(value))
#             for i in range(1, len(value) - 1):
#                 data = database.SELECTfromWHERE('USERS', {keys[i]: [value[i]]})
#                 if len(data) > 1:
#                     return {'message': i, 'data': '{} conflict'.format(keys[i])}
#             uid = newID('USERS', 'UID')
#             client.logger.debug('New UID: {}'.format(uid))
#             # uid,uname,pw,avatar,mail,pnumber,sex,education,garde
#             database.INSERTvalues('USERS', (uid, value[0], value[3], None, value[2], value[1], 'U', None, None))
#             return {'message': 0, 'data': uid}
#
#
# # Debug
# @client.route('/signin', methods=['POST'])
# def signin():
#     client.logger.debug('From {} User agent: {}'.format(request.remote_addr, request.user_agent))
#     types = ['UID', 'Pnumber', 'Mail']
#     keys = ['Uname', 'Pnumber', 'Mail', 'UID']
#     if request.method == 'POST':
#         try:
#             form = request.json['data']
#             client.logger.debug('Post: {}'.format(form))
#             tp = form['type']
#             info = form['info']
#             pw = form['PW']
#         except KeyError as k:
#             error_message = "KeyError: {}".format(k.args[0])
#             client.logger.error(error_message)
#             return ERROR(error_message)
#         else:
#             data = database.SELECTfromWHERE('USERS', {types[tp]: [info]})
#             if len(data) != 2:
#                 return ERROR("Unable to find user")
#             header = data[0]
#             data = data[1]
#             if data[header.index('pw')] != pw:
#                 return ERROR("PW error")
#             client.logger.debug('Select data: {}'.format(data))
#             index = [header.index(key.lower()) for key in keys]
#             return {'message': 0, 'data': {keys[i]: data[index[i]] for i in range(len(keys))}}
#
#
# # Debug
# # front page
# @client.route('/user/<UID>/overview', methods=['GET'])
# def hello(UID):
#     client.logger.debug('From {} User agent: {}'.format(request.remote_addr, request.user_agent))
#     global REVIEW, LEARN
#     review, learn = REVIEW, LEARN
#     if request.method == 'GET':
#         have_learned = database.SELECTfromWHERE('PLAN', {'UID': [UID], 'Proficiency': [1, 2, 3]})
#         not_learned = database.SELECTfromWHERE('PLAN', {'UID': [UID], 'Proficiency': [0]})
#         if have_learned is False or not_learned is False or len(have_learned) + len(not_learned) == 2:
#             error_message = "The user({}) didn't choose any vocabulary!".format(UID)
#             client.logger.error(error_message)
#             return ERROR(error_message)
#         review = min(review, len(have_learned) - 1)
#         learn = min(learn, len(not_learned) - 1)
#         t_record = database.SELECTfromWHERE('RECORD', {'UID': [UID], 'Dates': [today()]})
#         # 如果今天还没由背单词
#         if len(t_record) == 1:
#             y_record = database.SELECTfromWHERE('RECORD', {'UID': [UID], 'Dates': [today(-1)]})
#             # 如果昨天没有背单词
#             if len(y_record) == 1:
#                 cont = 0
#             else:
#                 cont = y_record[1][y_record[0].index('aday')]
#         else:
#             cont = t_record[1][t_record[0].index('aday')]
#             today_learned = t_record[1][t_record[0].index('learned')]
#             today_reviewed = t_record[1][t_record[0].index('review')]
#             learn = max(0, learn - today_learned)
#             review = max(0, review - today_reviewed)
#         if len(not_learned) > 1:
#             tid = not_learned[1][not_learned[0].index('tid')]
#         else:
#             tid = have_learned[1][have_learned[0].index('tid')]
#         data = database.SELECTfromTwoTableWHERE('VOCABULARY', 'TAKES', {'TID': [tid]})
#         vname = data[1][data[0].index('vname')]
#         return {"message": 0, "data": {
#             "Vname": vname,
#             "alreadyRecite": len(have_learned) - 1,
#             "remained": len(not_learned) - 1,
#             "today learn": learn,
#             "today review": review,
#             "continuous": cont,
#         }}
#
#
# # Debug
# @client.route('/user/<UID>/info', methods=['GET', 'POST'])
# def userInfo(UID):
#     client.logger.debug('From {} User agent: {}'.format(request.remote_addr, request.user_agent))
#     keys = ['Uname', 'Avatar', 'Sex', 'Education', 'Grade']
#     if request.method == 'POST':
#         try:
#             form = request.json['data']
#             value = [form[key] for key in keys]
#         except KeyError as k:
#             error_message = "KeyError: {}".format(k.args[0])
#             client.logger.error(error_message)
#             return ERROR(error_message)
#         else:
#             if value[keys.index('Grade')] is '':
#                 value[keys.index('Grade')] = None
#             else:
#                 value[keys.index('Grade')] = int(value[keys.index('Grade')])
#             for i in range(len(keys)):
#                 if not database.UPDATEprecise('USERS', keys[i], value[i], {"UID": [UID]}):
#                     error_message = "Unable to update USER {}, item={}, value={}, i={}".format(UID, keys[i], value[i],
#                                                                                                i)
#                     client.logger.error(error_message)
#                     return ERROR(error_message)
#             return OK()
#     elif request.method == 'GET':
#         data = database.SELECTfromWHERE('USERS', {'UID': [UID]})
#         if len(data) != 2:
#             error_message = "UID {} does not exist".format(UID)
#             client.logger.error(error_message)
#             return ERROR(error_message)
#         header = data[0]
#         data = data[1]
#         value = [data[header.index(key.lower())] for key in keys]
#         value = [v if v != None else '' for v in value]
#         return {"message": 0, "data": {
#             keys[i]: value[i] for i in range(len(keys))
#         }}
#
#
# # Debug
# @client.route('/plan', methods=['GET'])
# def plan():
#     client.logger.debug('From {} User agent: {}'.format(request.remote_addr, request.user_agent))
#     if request.method == 'GET':
#         vocab = database.SELECTfromWHERE('VOCABULARY')
#         if vocab is False or len(vocab) < 2:
#             error_message = "Unable to find any vocabulary"
#             client.logger.error(error_message)
#             return ERROR(error_message)
#         return {"message": 0, "data": vocab[1:]}
#
#
# # Debug
# @client.route('/user/<UID>/plan', methods=['POST'])
# def updateUserPlan(UID):
#     client.logger.debug('From {} User agent: {}'.format(request.remote_addr, request.user_agent))
#     if request.method == 'POST':
#         try:
#             vname = request.json['data']['Vname']
#         except KeyError as k:
#             error_message = "KeyError: {}".format(k.args[0])
#             client.logger.error(error_message)
#             return ERROR(error_message)
#         else:
#             vocab = database.SELECTfromWHERE('VOCABULARY', {'Vname': [vname]})
#             if vocab is False or len(vocab) != 2:
#                 error_message = "Vocabulary {} does not exist".format(vname)
#                 client.logger.error(error_message)
#                 return ERROR(error_message)
#             vid = vocab[1][vocab[0].index('vid')]
#             if not database.DELETEprecise('PLAN', {'UID': [UID]}):
#                 error_message = "Unable to delete User {} from Plan".format(UID)
#                 client.logger.error(error_message)
#                 return ERROR(error_message)
#             data = database.SELECTfromWHERE('TAKES', {'VID': [vid]})
#             if data is False or len(data) < 2:
#                 error_message = "Unable to find any takes of {}".format(vname)
#                 client.logger.error(error_message)
#                 return ERROR(error_message)
#             header = data[0]
#             words = data[1:]
#             for word in words:
#                 tid = word[header.index('tid')]
#                 wid = word[header.index('wid')]
#                 if not database.INSERTvalues('PLAN', (UID, tid, wid, 0)):
#                     error_message = "Unable to insert ({})".format((UID, tid, wid, 0))
#                     client.logger.error(error_message)
#                     if not database.DELETEprecise('PLAN', {'UID': [UID]}):
#                         error_message2 = "AND unable to delete User {} from Plan".format(UID)
#                         client.logger.error(error_message)
#                         error_message += ' ' + error_message2
#                     return ERROR(error_message)
#             return OK()
#
#
# # Debug
# # test page
# @client.route('/plan/<UID>/<int:seed>', methods=['GET'])
# def getTest(UID, seed):
#     client.logger.debug('From {} User agent: {}'.format(request.remote_addr, request.user_agent))
#     random.seed(seed)
#     global REVIEW, LEARN
#     review, learn = REVIEW, LEARN
#     if request.method == 'GET':
#         have_learned = database.SELECTfromWHERE('PLAN', {'UID': [UID], 'Proficiency': [1, 2, 3]})
#         not_learned = database.SELECTfromWHERE('PLAN', {'UID': [UID], 'Proficiency': [0]})
#         if have_learned is False or not_learned is False or len(have_learned) + len(not_learned) == 2:
#             error_message = "The user({}) didn't choose any vocabulary".format(UID)
#             client.logger.error(error_message)
#             return ERROR(error_message)
#         header = have_learned[0]
#         have_learned = have_learned[1:]
#         not_learned = not_learned[1:]
#         if len(have_learned) + len(not_learned) < 4:
#             error_message = "The vocabulary is too small".format(UID)
#             client.logger.error(error_message)
#             return ERROR(error_message)
#         review = min(review, len(have_learned))
#         learn = min(learn, len(not_learned))
#         if len(have_learned) != 0:
#             review_item = random.sample(have_learned, review)
#         else:
#             client.logger.debug("User {} hasn't learner any word yet".format(UID))
#             review_item = []
#         if len(not_learned) != 0:
#             learn_item = random.sample(not_learned, learn)
#         else:
#             client.logger.debug("User {} doesn't have any new word to learn".format(UID))
#             learn_item = []
#         today_learn = []
#         for item in learn_item:
#             ops = random.sample(have_learned + not_learned, 4)
#             if item not in ops:
#                 ops.pop(0)
#                 ops.append(item)
#             options = [op[header.index('wid')] for op in ops]
#             random.shuffle(options)
#             today_learn.append((item[header.index('tid')],
#                                 item[header.index('wid')],
#                                 item[header.index('proficiency')],
#                                 options
#                                 ))
#         today_review = []
#         for item in review_item:
#             ops = random.sample(have_learned + not_learned, 4)
#             if item not in ops:
#                 ops.pop(0)
#                 ops.append(item)
#             options = [op[header.index('wid')] for op in ops]
#             random.shuffle(options)
#             today_review.append((item[header.index('tid')],
#                                  item[header.index('wid')],
#                                  item[header.index('proficiency')],
#                                  options
#                                  ))
#         return {"message": 0, "data": {
#             "todayLearn": today_learn,
#             "todayReview": today_review
#         }}
#
#
# # Debug
# @client.route('/plan/<UID>', methods=['GET', 'POST'])
# def updatePlan(UID):
#     client.logger.debug('From {} User agent: {}'.format(request.remote_addr, request.user_agent))
#     if request.method == 'GET':
#         user_plan = database.SELECTfromTwoTableWHERE('PLAN', 'DICTIONARY', {"UID": [UID]})
#         if user_plan is False or len(user_plan) == 1:
#             error_message = "The user({}) didn't choose any vocabulary!".format(UID)
#             client.logger.error(error_message)
#             return ERROR(error_message)
#         header = user_plan[0]
#         data = user_plan[1:]
#         plan = []
#         for item in data:
#             plan.append((
#                 item[header.index('tid')],
#                 item[header.index('wid')],
#                 item[header.index('english')],
#                 item[header.index('chinese')],
#                 item[header.index('proficiency')]
#             ))
#         return {"message": 0, "data": plan}
#     elif request.method == 'POST':
#         try:
#             res = request.json['data']['result']
#         except KeyError as k:
#             error_message = "KeyError: {}".format(k.args[0])
#             client.logger.error(error_message)
#             return ERROR(error_message)
#         else:
#             for tid, wid, p in res:
#                 if not database.UPDATEprecise('PLAN', 'Proficiency', p, {'UID': [UID], 'TID': [tid], 'WID': [wid]}):
#                     error_message = "Unable to update Plan UID: {} TID: {} WID: {}".format(UID, tid, wid)
#                     client.logger.error(error_message)
#                     return ERROR(error_message)
#             return OK()
#
#
# # Debug
# @client.route('/word/<WID>', methods=['GET'])
# def getWord(WID):
#     client.logger.debug('From {} User agent: {}'.format(request.remote_addr, request.user_agent))
#     if request.method == 'GET':
#         keys = ['English', 'Chinese', 'Psymbol']
#         data = database.SELECTfromWHERE('DICTIONARY', {'WID': [WID]})
#         if data is False or len(data) != 2:
#             error_message = "Unable to find word {}.".format(WID)
#             client.logger.error(error_message)
#             return ERROR(error_message)
#         header = data[0]
#         data = data[1]
#         return {"message": 0, "data": {
#             key: data[header.index(key.lower())] for key in keys
#         }}
#
#
# # Debug
# @client.route('/record/<UID>', methods=['POST', 'GET'])
# def record(UID):
#     client.logger.debug('From {} User agent: {}'.format(request.remote_addr, request.user_agent))
#     if request.method == 'POST':
#         try:
#             form = request.json['data']
#             learned = form['count_learned']
#             reviewed = form['count_reviewed']
#             start = form['start']
#             end = form['end']
#         except KeyError as k:
#             error_message = "KeyError: {}".format(k.args[0])
#             client.logger.error(error_message)
#             return ERROR(error_message)
#         else:
#             start_day = datetime.datetime.strptime(start, TIME_FORMAT)
#             now_day = start_day.replace(minute=0, second=0)
#             end_day = datetime.datetime.strptime(end, TIME_FORMAT)
#             p = [0, 0, 0, 0]
#             for i in range(len(p)):
#                 data = database.SELECTfromWHERE('PLAN', {'UID': [UID], 'Proficiency': [i]})
#                 if data is False:
#                     error_message = "Unable to find Plan for User {}".format(UID)
#                     client.logger.error(error_message)
#                     return ERROR(error_message)
#                 p[i] = len(data) - 1
#             while now_day <= end_day:
#                 this_day = now_day.strftime(DAY_FORMAT)
#                 today_record = database.SELECTfromWHERE('RECORD', {'Dates': [this_day], 'UID': [UID]})
#                 # record中没有这一天的记录
#                 if today_record is False or len(today_record) < 2:
#                     last_record = database.SELECTfromWHERE('RECORD', {
#                         'Dates': [(now_day - datetime.timedelta(days=1)).strftime(DAY_FORMAT)],
#                         'UID': [UID]})
#                     if last_record is False or len(last_record) == 1:
#                         aday = 0
#                     else:
#                         aday = last_record[1][last_record[0].index('aday')] + 1
#                     ahour = np.zeros(24).astype(np.float)
#                     database.INSERTvalues('RECORD', (
#                         newID('RECORD', 'SID'), UID, this_day, learned, reviewed, 0, 0, p, ahour.tolist(), aday))
#                 # 有这一天的记录
#                 else:
#                     ahour = np.array(today_record[1][today_record[0].index('ahour')], dtype=np.float)
#                     database.UPDATEprecise('RECORD', 'Proficiency', p, {'UID': [UID], 'Dates': [this_day]})
#                 ahour[now_day.hour] = ahour[now_day.hour] + 60
#                 database.UPDATEprecise('RECORD', 'Ahour', ahour.tolist(), {'UID': [UID], 'Dates': [this_day]})
#                 now_day = now_day + datetime.timedelta(hours=1)
#             this_day = start_day.strftime(DAY_FORMAT)
#             start_record = database.SELECTfromWHERE('RECORD', {'Dates': [this_day], 'UID': [UID]})
#             header = start_record[0]
#             ahour = start_record[1][header.index('ahour')]
#             ahour[start_day.hour] -= start_day.minute
#             database.UPDATEprecise('RECORD', 'Ahour', ahour, {'UID': [UID], 'Dates': [this_day]})
#             this_day = end_day.strftime(DAY_FORMAT)
#             end_record = database.SELECTfromWHERE('RECORD', {'Dates': [this_day], 'UID': [UID]})
#             ahour = end_record[1][header.index('ahour')]
#             ahour[end_day.hour] -= (60 - end_day.minute)
#             database.UPDATEprecise('RECORD', 'Ahour', ahour, {'UID': [UID], 'Dates': [this_day]})
#             return OK()
#     elif request.method == 'GET':
#         data = database.SELECTfromWHERE('RECORD', {'UID': [UID]})
#         if data is False or len(data) < 2:
#             error_message = "Unable to find any record of User {}".format(UID)
#             client.logger.error(error_message)
#             return ERROR(error_message)
#         header = data[0]
#         data = data[1:]
#         data.sort(key=lambda x: sort_by_time(x, header.index('dates'), DAY_FORMAT))
#         records = {sort_by_time(item, header.index('dates'), DAY_FORMAT): item for item in data}
#         days = 0
#         last_day = datetime.datetime.strptime(today(-6), DAY_FORMAT).timestamp()
#         for d in records:
#             if d <= last_day:
#                 days = d
#         for line in data:
#             client.logger.debug(line)
#         p_info = []
#         a_time = []
#         if days == 0:
#             p_info.append((0, 0, 0, 0))
#         else:
#             p_info.append(records[days][header.index('proficiency')])
#         for i in range(-6, 1):
#             days = datetime.datetime.strptime(today(i), DAY_FORMAT).timestamp()
#             if days in records:
#                 p_info.append(records[days][header.index('proficiency')])
#                 a_time.append(records[days][header.index('ahour')])
#                 # ahour += np.array(records[days][header.index('ahour')]).astype(np.float)
#             else:
#                 p_info.append(p_info[-1])
#                 a_time.append(np.zeros(24))
#         a_time = np.array(a_time, dtype=np.float)
#         f_curve = np.random.normal(loc=5, size=7)
#         return {'message': 0, 'data': {
#             'proficiencyInfo': p_info[1:],
#             'Ahour': a_time.sum(axis=0).tolist(),
#             'Forgetting curve': f_curve.tolist(),
#             'active time': a_time.sum(axis=1).tolist()
#         }}
#
#
# # Debug
# @client.route('/feedback', methods=['POST'])
# def feedback():
#     client.logger.debug('From {} User agent: {}'.format(request.remote_addr, request.user_agent))
#     if request.method == 'POST':
#         try:
#             form = request.json['data']
#             uid = form['UID']
#             info = form['Info']
#         except KeyError as k:
#             error_message = "KeyError: {}".format(k.args[0])
#             client.logger.error(error_message)
#             return ERROR(error_message)
#         else:
#             fid = newID('FEEDBACK', 'FID')
#             client.logger.debug('New FID: {}'.format(fid))
#             client.logger.debug('Feedback: {} from {}'.format(info, uid))
#             database.INSERTvalues('FEEDBACK', (fid, uid, timestamp(), info))
#         return OK()
#
#
# @client.route('/test')
# def test():
#     client.logger.debug('From {} User agent: {}'.format(request.remote_addr, request.user_agent))
#     return OK()
