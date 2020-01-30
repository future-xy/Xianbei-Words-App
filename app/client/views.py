#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Name    : views.py
# Time    : 2020/1/26 22:28
# Author  : Fu Yao
# Mail    : fy38607203@163.com

from app import db
from . import client
from app.util.utils import OK, ERROR
from app.util.mail import sendMail
from config import REVIEW, LEARN, DAY_FORMAT, TIME_FORMAT
from models import Users, Vocabulary, Dictionary, Feedback, Plan, Record, Takes

from flask import request, current_app, render_template
from flask_login import current_user, login_user, login_required, logout_user
from sqlalchemy.sql import exists
from sqlalchemy import or_, func

import random
from datetime import datetime, date, timedelta
import numpy as np
from time import time


@client.route('/test')
@login_required
def test():
    print("RUNNING!")
    # print(Users.query.get('0005'))
    # print(current_user.is_authoritcated)
    # print(current_user)
    # print(current_user.uid)
    return "HELLO WORLD"


@client.route('/test/mail/<Receiver>')
@login_required
def send_mail(Receiver):
    mail_template = """
    Dear User {},
    This is a test mail!
    
    Best regards,
    先背单词
    """
    print(Receiver)
    sendMail(Receiver, mail_template.format(current_user.uid), '修改密码')
    return {}


# home page
@client.route('/')
def home():
    current_app.logger.debug('From {} User agent: {}'.format(request.remote_addr, request.user_agent))
    return render_template('index.html')


# login page
# Debug
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
            return ERROR("User doesn't exist or password error! PW:{};UID:{}".format(u.pw, u.uid))
        else:
            login_user(u, remember=True)
            print("RETURN")
            return {'message': 0,
                    'data': {'Uname': u.uname, 'Pnumber': u.pnumber, 'Mail': u.mail, 'UID': u.uid}}


@client.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return OK()


# NOT Debug
# front page
@client.route('/user/overview', methods=['GET'])
@login_required
def hello():
    current_app.logger.debug('From {} User agent: {}'.format(request.remote_addr, request.user_agent))
    UID = current_user.uid
    # if the user has chosen any vocabulary
    vid = current_user.vid
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
@client.route('/user/info', methods=['GET', 'POST'])
@login_required
def userInfo():
    current_app.logger.debug('From {} User agent: {}'.format(request.remote_addr, request.user_agent))
    UID = current_user.uid
    if request.method == 'POST':
        try:
            form = request.json['data']
        except KeyError as k:
            error_message = "KeyError: {}".format(k.args[0])
            current_app.logger.error(error_message)
            return ERROR(error_message)
        else:
            if form['Grade'] == '':
                form['Grade'] = 0
            else:
                form['Grade'] = int(form['Grade'])
            db.session.query(Users).filter(Users.uid == UID).update({k.lower(): v for k, v in form.items()})
            db.session.commit()
            return OK()
    elif request.method == 'GET':
        user = current_user
        return {"message": 0, "data": {
            "Uname": user.uname, "Avatar": user.avatar, "Sex": user.sex, "Education": user.education,
            "Grade": user.grade
        }}


# NOT Debug
@client.route('/vocabulary', methods=['GET'])
@login_required
def plan():
    current_app.logger.debug('From {} User agent: {}'.format(request.remote_addr, request.user_agent))
    vs = db.session.query(Vocabulary.vid, Vocabulary.vname, Vocabulary.count, Vocabulary.day, Vocabulary.type).all()
    print(vs)
    if len(vs) == 0:
        error_message = "Unable to find any vocabulary"
        current_app.logger.error(error_message)
        return ERROR(error_message)
    return {"message": 0, "data": vs}


# Debug
# !!!
@client.route('/user/plan', methods=['PUT', 'POST', 'GET'])
@login_required
def updateUserPlan():
    current_app.logger.debug('From {} User agent: {}'.format(request.remote_addr, request.user_agent))
    UID = current_user.uid
    if request.method == 'PUT':
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
    elif request.method == 'GET':
        vid = current_user.vid
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
# test page
@client.route('/user/plan/list', methods=['GET'])
@login_required
def getTest():
    current_app.logger.debug('From {} User agent: {}'.format(request.remote_addr, request.user_agent))
    UID = current_user.uid
    vid = current_user.vid
    if vid is None:
        error_message = "The user({}) didn't choose any vocabulary".format(UID)
        current_app.logger.error(error_message)
        return ERROR(error_message)
    # random.seed(seed)
    review, learn = REVIEW, LEARN
    start = time()
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
    # random.seed(time())
    print(time() - start)
    return {"message": 0, "data": {
        "todayLearn": today_learn,
        "todayReview": today_review
    }}


# Debug
@client.route('/word/<WID>', methods=['GET'])
@login_required
def getWord(WID):
    current_app.logger.debug('From {} User agent: {}'.format(request.remote_addr, request.user_agent))
    w = db.session.query(Dictionary).filter(Dictionary.wid == WID).one()
    return {"message": 0, "data": {"English": w.english, "Chinese": w.chinese, "Psymbol": w.psymbol}}


# Debug
@client.route('/user/record', methods=['POST', 'GET'])
@login_required
def record():
    current_app.logger.debug('From {} User agent: {}'.format(request.remote_addr, request.user_agent))
    UID = current_user.uid
    if request.method == 'POST':
        try:
            form = request.json['data']
            learned = form['count_learned']
            reviewed = form['count_reviewed']
            start = form['start']
            end = form['end']
        except KeyError as k:
            error_message = "KeyError: {}".format(k.args[0])
            current_app.logger.error(error_message)
            return ERROR(error_message)
        else:
            print(form)
            start = datetime.strptime(start, TIME_FORMAT)
            end = datetime.strptime(end, TIME_FORMAT)
            start_day = start.date()
            end_day = end.date()
            p = [db.session.query(func.count(Plan.tid)).filter(Plan.uid == '0001', Plan.proficiency == i).scalar() for i
                 in range(4)]
            # start exist?
            start_record = db.session.query(Record.learned, Record.reviewed).filter(
                Record.uid == UID, Record.dates == start_day).one_or_none()
            if start_record is None:
                cont = db.session.query(Record.aday).filter(Record.uid == UID,
                                                            Record.dates == start_day - timedelta(1)).scalar()
                if cont is None:
                    a_day = 1
                else:
                    a_day = cont + 1
                db.session.add(
                    Record(uid=UID, dates=start_day, learned=learned, reviewed=reviewed, proficiency=p, aday=a_day))
            else:
                db.session.query(Record).filter(Record.dates == start_day, Record.uid == UID).update(
                    {"learned": learned + start_record[0], "reviewed": reviewed + start_record[1], "proficiency": p})
            db.session.commit()
            if end_day != start_day:
                cont = db.session.query(Record.aday).filter(Record.uid == UID, Record.dates == start_day).scalar()
                if cont is None:
                    a_day = 1
                else:
                    a_day = cont + 1
                db.session.add(
                    Record(uid=UID, dates=end_day, learned=learned, reviewed=reviewed, proficiency=p, aday=a_day))
            db.session.commit()
            # a_hour
            now = start.replace(minute=0, second=0)
            while now < end.replace(minute=0, second=0):
                a_hour = db.session.query(Record.ahour).filter(Record.uid == UID, Record.dates == now.date()).scalar()
                a_hour[now.hour] += 60
                db.session.query(Record).filter(Record.uid == UID, Record.dates == now.date()).update({"ahour": a_hour})
                now += timedelta(hours=1)
            s_hour = db.session.query(Record.ahour).filter(Record.uid == UID, Record.dates == start_day).scalar()
            s_hour[start.hour] -= start.minute
            db.session.query(Record).filter(Record.uid == UID, Record.dates == start_day).update({"ahour": s_hour})
            e_hour = db.session.query(Record.ahour).filter(Record.uid == UID, Record.dates == end_day).scalar()
            e_hour[end.hour] += end.minute
            db.session.query(Record).filter(Record.uid == UID, Record.dates == end_day).update({"ahour": e_hour})
            db.session.commit()
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
            if init_record is None:
                record_7 = [records[-1]]
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
@client.route('/user/feedback', methods=['POST'])
@login_required
def feedback():
    current_app.logger.debug('From {} User agent: {}'.format(request.remote_addr, request.user_agent))
    try:
        form = request.json['data']
        info = form['Info']
    except KeyError as k:
        error_message = "KeyError: {}".format(k.args[0])
        current_app.logger.error(error_message)
        return ERROR(error_message)
    else:
        db.session.add(Feedback(uid=current_user.uid, info=info))
        db.session.commit()
        return OK()
