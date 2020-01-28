#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Name    : views.py
# Time    : 2020/1/26 22:28
# Author  : Fu Yao
# Mail    : fy38607203@163.com

from app import db
from . import client
from app.util.utils import OK, ERROR
from config import REVIEW, LEARN, DAY_FORMAT, TIME_FORMAT
from models import Users, Vocabulary, Dictionary, Feedback, Plan, Record, Takes

from flask import request, current_app, render_template
from flask_login import current_user, login_user, login_required
from sqlalchemy.sql import exists
from sqlalchemy import or_, func

import random
from datetime import datetime, date, timedelta
import numpy as np
from time import time


@client.route('/test')
def test():
    print("RUNNING!")
    # print("_______________________________")
    # user = Users(uname='test1', pw='123456', mail='1@1', pnumber='123')
    # db.session.add(user)
    # print("Input: {}".format(user))
    # print("Output: {}".format(db.session.query(Users).all()))
    # print("_______________________________")
    # print("Output: {}".format(db.session.query(Dictionary).all()))
    # print("_______________________________")
    # print("Output: {}".format(db.session.query(Vocabulary).all()))
    # print("_______________________________")
    # take = Takes(vid='0001', wid='0001')
    # print("Input: {}".format(take))
    # db.session.add(take)
    # print("Output: {}".format(db.session.query(Takes).all()))
    # print("_______________________________")
    # plan1 = Plan(uid='0001', tid='0001', proficiency=1, dates=datetime.now())
    # print("Input: {}".format(plan1))
    # p2 = Plan(uid='0001', tid='0002')
    # print("Input: {}".format(p2))
    # db.session.add(plan1)
    # db.session.add(p2)
    # print("Output: {}".format(db.session.query(Plan).all()))
    # print("_______________________________")
    # r1 = Record(uid='0001', learned=1, reviewed=2, proficiency=[1, 0, 0, 0], ahour=np.zeros(24).tolist(), aday=2)
    # r2 = Record(uid='0002', learned=2, reviewed=2, proficiency=[1, 0, 0, 0], ahour=np.ones(24).tolist(), aday=2)
    # print("Input: {}".format(r1))
    # print("Input: {}".format(r2))
    # db.session.add(r1)
    # db.session.add(r2)
    # print("Output: {}".format(db.session.query(Record).all()))
    # print("_______________________________")
    # f1 = Feedback(uid='0002', info='hi')
    # print("Input: {}".format(f1))
    # db.session.add(f1)
    # print("Output: {}".format(db.session.query(Feedback).all()))
    # do = db.session.query(Record.dates).filter(
    #     and_(Record.uid == '0001', Record.dates == date.today() - timedelta(58))).scalar()
    # print(type(do))
    # print(do)
    # have_learned = db.session.query(func.count(Plan.tid)).filter(Plan.uid == '0001', Plan.proficiency == 0).scalar()
    # print(have_learned)
    # db.session.query(Users).filter(Users.uid == '0001').update({'uname': 'hahahaha'})
    # data = db.session.query(Plan.tid, Takes.wid, Dictionary.english, Dictionary.chinese, Plan.proficiency).filter(
    #     Plan.tid == Takes.tid, Takes.wid == Dictionary.wid, Plan.uid == '0001').all()
    today_record = db.session.query(Record.ahour).filter(Record.dates == date.fromisoformat('2020-01-28'),
                                                         Record.uid == '0001').scalar()

    print(today_record)
    return "HELLO WORLD"


# home page
@client.route('/')
def home():
    current_app.logger.debug('From {} User agent: {}'.format(request.remote_addr, request.user_agent))
    return render_template('index.html')


# Debug
# login page
@client.route('/signup', methods=['POST'])
def signup():
    current_app.logger.info('From {} User agent: {}'.format(request.remote_addr, request.user_agent))
    try:
        form = request.json['data']
    except KeyError as k:
        error_message = "KeyError: {}".format(k.args[0])
        current_app.logger.error(error_message)
        return ERROR(error_message)
    else:
        current_app.logger.debug('Post: {}'.format(form))
        # 查重
        if db.session.query(exists().where(Users.pnumber == form['Pnumber'])).scalar():
            return {'message': 1, 'data': '{} conflict'.format(form['Pnumber'])}
        elif db.session.query(exists().where(Users.mail == form['Mail'])).scalar():
            return {'message': 2, 'data': '{} conflict'.format(form['Mail'])}
        new_user = Users(uname=form['Uname'], pw=form['PW'], mail=form['Mail'], pnumber=form['Pnumber'])
        db.session.add(new_user)
        db.session.commit()
        current_app.logger.debug('Uid: {}'.format(new_user.uid))
        return {'message': 0, 'data': new_user.uid}


# Debug
@client.route('/signin', methods=['POST'])
def signin():
    current_app.logger.info('From {} User agent: {}'.format(request.remote_addr, request.user_agent))
    try:
        form = request.json['data']
        current_app.logger.debug('Post: {}'.format(form))
        tp = form['type']
        info = form['info']
        pw = form['PW']
    except KeyError as k:
        error_message = "KeyError: {}".format(k.args[0])
        current_app.logger.error(error_message)
        return ERROR(error_message)
    else:
        # uid
        if tp == 0:
            u = db.session.query(Users).filter(Users.uid == info).one_or_none()
        # pnumber
        elif tp == 1:
            u = db.session.query(Users).filter(Users.pnumber == info).one_or_none()
        # mail
        else:
            u = db.session.query(Users).filter(Users.mail == info).one_or_none()
        if u is None or u.pw != pw:
            return ERROR()
        else:
            return {'message': 0,
                    'data': {'Uname': u.uname, 'Pnumber': u.pnumber, 'Mail': u.mail, 'UID': u.uid}}


# NOT Debug
# front page
@client.route('/user/<UID>/overview', methods=['GET'])
def hello(UID):
    current_app.logger.debug('From {} User agent: {}'.format(request.remote_addr, request.user_agent))
    # if the user has chosen any vocabulary
    vid = db.session.query(Users.vid).filter(Users.uid == UID).scalar()
    if vid is None:
        error_message = "The user({}) didn't choose any vocabulary!".format(UID)
        current_app.logger.error(error_message)
        return ERROR(error_message)
    # vname
    v = db.session.query(Vocabulary).filter(Vocabulary.vid == vid).one()
    vname = v.vname

    review, learn = REVIEW, LEARN
    have_learned = db.session.query(func.count(Plan.tid)).filter(Plan.uid == UID, Plan.proficiency != 0).scalar()
    not_learned = db.session.query(func.count(Plan.tid)).filter(Plan.uid == UID, Plan.proficiency == 0).scalar()
    review = min(review, have_learned)
    learn = min(learn, not_learned)

    t_record = db.session.query(Record).filter(Record.dates == date.today(), Record.uid == UID).one_or_none()
    # 如果今天还没有背单词
    if t_record is None:
        y_record = db.session.query(Record.aday).filter(
            Record.dates == date.today() - timedelta(days=1), Record.uid == UID).scalar()
        # 如果昨天没有背单词
        if y_record is None:
            cont = 0
        else:
            cont = y_record
    else:
        cont = t_record.aday
        today_learned = t_record.learned
        today_reviewed = t_record.reviewed
        learn = max(0, learn - today_learned)
        review = max(0, review - today_reviewed)
    return {"message": 0, "data": {
        "Vname": vname,
        "alreadyRecite": have_learned,
        "remained": not_learned,
        "today learn": learn,
        "today review": review,
        "continuous": cont,
    }}


# NOT Debug
@client.route('/user/<UID>/info', methods=['GET', 'POST'])
def userInfo(UID):
    current_app.logger.debug('From {} User agent: {}'.format(request.remote_addr, request.user_agent))
    if request.method == 'POST':
        try:
            form = request.json['data']
        except KeyError as k:
            error_message = "KeyError: {}".format(k.args[0])
            current_app.logger.error(error_message)
            return ERROR(error_message)
        else:
            db.session.query(Users).filter(Users.uid == UID).update({k.lower(): v for k, v in form.item()})
            db.commit()
            return OK()
    elif request.method == 'GET':
        user = db.session.query(Users).filter(Users.uid == UID).one_or_none()
        if user is None:
            error_message = "UID {} does not exist".format(UID)
            current_app.logger.error(error_message)
            return ERROR(error_message)
        return {"message": 0, "data": {
            "Uname": user.uname, "Avatar": user.avatar, "Sex": user.sex, "Education": user.education,
            "Grade": user.grade
        }}


# NOT Debug
@client.route('/plan', methods=['GET'])
def plan():
    current_app.logger.debug('From {} User agent: {}'.format(request.remote_addr, request.user_agent))
    vs = db.session.query(Vocabulary).all()
    if len(vs) == 0:
        error_message = "Unable to find any vocabulary"
        current_app.logger.error(error_message)
        return ERROR(error_message)
    return {"message": 0, "data": [(v.vid, v.vname, v.count, v.day, v.type) for v in vs]}


# Debug
@client.route('/user/<UID>/plan', methods=['POST'])
def updateUserPlan(UID):
    current_app.logger.debug('From {} User agent: {}'.format(request.remote_addr, request.user_agent))
    try:
        vname = request.json['data']['Vname']
    except KeyError as k:
        error_message = "KeyError: {}".format(k.args[0])
        current_app.logger.error(error_message)
        return ERROR(error_message)
    else:
        vocab = db.session.query(Vocabulary).filter(Vocabulary.vname == vname).one()
        vid = vocab.vid
        db.session.query(Users).filter(Users.uid == UID).update({"vid": vid})
        # Delte old
        db.session.query(Plan).filter(Plan.uid == UID).delete()
        # Add new
        db.session.execute("""INSERT INTO plan
        (SELECT uid,tid AS tid, 0 AS proficiency, NULL AS dates
        FROM users u, takes t
        WHERE u.vid=t.vid AND uid='{}');""".format(UID))
        db.session.commit()
        return OK()


# Debug
# test page
@client.route('/plan/<UID>/<int:seed>', methods=['GET'])
def getTest(UID, seed):
    current_app.logger.debug('From {} User agent: {}'.format(request.remote_addr, request.user_agent))
    #
    vid = db.session.query(Users.vid).filter(Users.uid == UID).scalar()
    if vid is None:
        error_message = "The user({}) didn't choose any vocabulary".format(UID)
        current_app.logger.error(error_message)
        return ERROR(error_message)
    random.seed(seed)
    review, learn = REVIEW, LEARN
    have_learned = db.session.query(Plan.tid, Takes.wid, Plan.proficiency).filter(Plan.tid == Takes.tid,
                                                                                  Plan.uid == UID,
                                                                                  Plan.proficiency != 0).all()
    not_learned = db.session.query(Plan.tid, Takes.wid, Plan.proficiency).filter(Plan.tid == Takes.tid,
                                                                                 Plan.uid == UID,
                                                                                 Plan.proficiency == 0).all()
    if len(have_learned) + len(not_learned) < 4:
        error_message = "The vocabulary is too small".format(UID)
        current_app.logger.error(error_message)
        return ERROR(error_message)
    review = min(review, len(have_learned))
    learn = min(learn, len(not_learned))
    if len(have_learned) != 0:
        review_item = random.sample(have_learned, review)
    else:
        current_app.logger.debug("User {} hasn't learner any word yet".format(UID))
        review_item = []
    if len(not_learned) != 0:
        learn_item = random.sample(not_learned, learn)
    else:
        current_app.logger.debug("User {} doesn't have any new word to learn".format(UID))
        learn_item = []
    today_learn = []
    for item in learn_item:
        ops = random.sample(have_learned + not_learned, 4)
        if item not in ops:
            ops.pop(0)
            ops.append(item)
        options = [op[1] for op in ops]
        random.shuffle(options)
        today_learn.append(item + (options,))
    today_review = []
    for item in review_item:
        ops = random.sample(have_learned + not_learned, 4)
        if item not in ops:
            ops.pop(0)
            ops.append(item)
        options = [op[1] for op in ops]
        random.shuffle(options)
        today_review.append(item + (options,))
    return {"message": 0, "data": {
        "todayLearn": today_learn,
        "todayReview": today_review
    }}


# Debug
@client.route('/plan/<UID>', methods=['GET', 'POST'])
def updatePlan(UID):
    current_app.logger.debug('From {} User agent: {}'.format(request.remote_addr, request.user_agent))
    if request.method == 'GET':
        #
        vid = db.session.query(Users.vid).filter(Users.uid == UID).scalar()
        if vid is None:
            error_message = "The user({}) didn't choose any vocabulary".format(UID)
            current_app.logger.error(error_message)
            return ERROR(error_message)
        data = db.session.query(Plan.tid, Takes.wid, Dictionary.english, Dictionary.chinese, Plan.proficiency).filter(
            Plan.tid == Takes.tid, Takes.wid == Dictionary.wid, Plan.uid == UID).all()
        return {"message": 0, "data": data}
    elif request.method == 'POST':
        try:
            res = request.json['data']['result']
        except KeyError as k:
            error_message = "KeyError: {}".format(k.args[0])
            current_app.logger.error(error_message)
            return ERROR(error_message)
        else:
            for tid, wid, p in res:
                db.session.query(Plan).filter(Plan.uid == UID, Plan.tid == tid).upate({'proficiency': p})
            db.session.commit()
            return OK()


# Debug
@client.route('/word/<WID>', methods=['GET'])
def getWord(WID):
    current_app.logger.debug('From {} User agent: {}'.format(request.remote_addr, request.user_agent))
    w = db.session.query(Dictionary).filter(Dictionary.wid == WID).one()
    return {"message": 0, "data": {"English": w.english, "Chinese": w.chinese, "Psymbol": w.psymbol}}


# Debug
@client.route('/record/<UID>', methods=['POST', 'GET'])
def record(UID):
    current_app.logger.debug('From {} User agent: {}'.format(request.remote_addr, request.user_agent))
    # 换一种方法，update,insert等
    if request.method == 'POST':
        try:
            form = request.json['data']
            # 没有更新进去
            learned = form['count_learned']
            reviewed = form['count_reviewed']
            start = form['start']
            end = form['end']
        except KeyError as k:
            error_message = "KeyError: {}".format(k.args[0])
            current_app.logger.error(error_message)
            return ERROR(error_message)
        else:
            start_day = datetime.strptime(start, TIME_FORMAT)
            now_day = start_day.replace(minute=0, second=0)
            end_day = datetime.strptime(end, TIME_FORMAT)
            p = [db.session.query(func.count(Plan.tid)).filter(Plan.uid == UID, Plan.proficiency == i).scalar() for i in
                 range(4)]
            while now_day <= end_day:
                this_day = now_day.strftime(DAY_FORMAT)
                # today_record = database.SELECTfromWHERE('RECORD', {'Dates': [this_day], 'UID': [UID]})
                today_record = db.session.query(Record.ahour).filter(Record.dates == date.fromisoformat(this_day),
                                                                     Record.uid == UID).scalar()
                # record中没有这一天的记录
                if today_record is None:
                    last_record = db.session.query(Record.aday).filter(
                        Record.dates == date.fromisoformat(this_day) - timedelta(days=1), Record.uid == UID).scalar()
                    if last_record is None:
                        aday = 0
                    else:
                        aday = last_record + 1
                    ahour = np.zeros(24).astype(np.float)
                    db.session.add(
                        Record(uid=UID, dates=date.fromisoformat(this_day), learned=learned, reviewed=reviewed,
                               proficiency=p, ahour=ahour.tolist(), aday=aday))
                # 有这一天的记录
                else:
                    ahour = np.array(today_record)
                    # database.UPDATEprecise('RECORD', 'Proficiency', p, {'UID': [UID], 'Dates': [this_day]})
                    db.session.query(Record).filter(
                        Record.uid == UID, Record.dates == date.fromisoformat(this_day)).update({'proficiency': p})
                ahour[now_day.hour] = ahour[now_day.hour] + 60
                # database.UPDATEprecise('RECORD', 'Ahour', ahour.tolist(), {'UID': [UID], 'Dates': [this_day]})
                db.session.query(Record).filter(Record.uid == UID, Record.dates == date.fromisoformat(this_day)).update(
                    {'ahour': ahour.tolist()})
                now_day = now_day + timedelta(hours=1)
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
        init_record = Record.query.order_by(Record.dates.desc()).filter(
            Record.uid == UID, Record.dates <= date.today() - timedelta(7)).first()
        records = Record.query.order_by(Record.dates.desc()).filter(Record.uid == UID,
                                                                    Record.dates > date.today() - timedelta(7)).all()
        if init_record is None and len(records) == 0:
            error_message = "Unable to find any record of User {}".format(UID)
            current_app.logger.error(error_message)
            return ERROR(error_message)
        f_curve = np.zeros(7).tolist()
        if len(records) == 0:
            p_info = [init_record.proficiency] * 7
            a_hour = np.zeros(24).tolist()
            a_time = np.zeros(7).tolist()
        else:
            record_7 = [init_record]
            for d in range(-6, 1):
                if records[-1].dates == date.today() + timedelta(d):
                    record_7.append(records.pop())
                else:
                    record_7.append(record_7[-1])
            record_7.pop(0)
            p_info = [r.proficiency for r in record_7]
            a = np.array([r.ahour for r in record_7])
            a_hour = a.mean(axis=0).tolist()
            a_time = a.sum(axis=1).tolist()
        return {'message': 0, 'data': {
            'proficiencyInfo': p_info,
            'Ahour': a_hour,
            'Forgetting curve': f_curve,
            'active time': a_time
        }}


# Debug
@client.route('/feedback', methods=['POST'])
def feedback():
    current_app.logger.debug('From {} User agent: {}'.format(request.remote_addr, request.user_agent))
    try:
        form = request.json['data']
        uid = form['UID']
        info = form['Info']
    except KeyError as k:
        error_message = "KeyError: {}".format(k.args[0])
        current_app.logger.error(error_message)
        return ERROR(error_message)
    else:
        db.session.add(Feedback(uid=uid, info=info))
        db.session.commit()
        return OK()
