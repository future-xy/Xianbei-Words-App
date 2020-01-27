#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Name    : models.py
# Time    : 2020/1/23 20:35
# Author  : Fu Yao
# Mail    : fy38607203@163.com


# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from app import db, login_manager

from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float, DateTime, Text, Enum
from sqlalchemy.dialects.postgresql import ARRAY

DB_URL = 'postgresql+psycopg2://postgres:sysu_sdcs_db2019@111.231.250.160:5432/database0'

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
# app.config['SQLALCHEMY_ECHO'] = False
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
MAX_LEN = 65535


class Users(db.Model):
    __tablename__ = 'users'
    uid = Column("uid", String(32), primary_key=True, nullable=False, unique=True)
    uname = Column("uname", String(64), nullable=False)
    pw = Column("pw", String(64), nullable=False)
    avatar = Column("avatar", String, nullable=False, default='')
    mail = Column("mail", String(64), nullable=False)
    pnumber = Column("pnumber", String(32), nullable=False)
    sex = Column("sex", Enum('F', 'M', 'U'), default='U')
    education = Column("education", String(32))
    grade = Column("grade", Integer)

    def __init__(self, uid, uname, pw, avatar, mail, pnumber, sex, education, grade):
        self.uid = uid
        self.uname = uname
        self.pw = pw
        self.avatar = avatar
        self.mail = mail
        self.pnumber = pnumber
        self.sex = sex
        self.education = education
        self.grade = grade

    def __repr__(self):
        return "<Users('{}','{}','{}','{}','{}','{}','{}','{}','{}')>".format(
            self.uid, self.uname, self.pw, self.avatar, self.mail, self.pnumber, self.sex, self.education, self.grade)


class Dictionary(db.Model):
    __tablename__ = 'dictionary'
    wid = Column("wid", String(32), primary_key=True, nullable=False)
    english = Column("english", String(64), nullable=False)
    psymbol = Column("psymbol", String(32))
    chinese = Column("chinese", String)

    def __init__(self, wid, english, psymbol, chinese):
        self.wid = wid
        self.english = english
        self.psymbol = psymbol
        self.chinese = chinese

    def __repr__(self):
        return "<Dictionary('{}','{}','{}','{}')>".format(self.wid, self.english, self.psymbol, self.chinese)


class Vocabulary(db.Model):
    __tablename__ = 'vocabulary'
    cid = Column("vid", String(32), primary_key=True, nullable=False)
    vname = Column("vname", String(128), nullable=False)
    count = Column("count", Integer, nullable=False)
    day = Column("day", Integer, nullable=False)
    type = Column("type", String(64))

    def __init__(self, cid, vname, count, day, type):
        self.cid = cid
        self.vname = vname
        self.count = count
        self.day = day
        self.type = type

    def __repr__(self):
        return "<Vocabulary('{}','{}','{}','{}','{}')>".format(self.cid, self.vname, self.count, self.day, self.type)


class Takes(db.Model):
    __tablename__ = 'takes'
    tid = Column("tid", String(32), primary_key=True, nullable=False)
    vid = Column("vid", String(32), ForeignKey('vocabulary.VID'), nullable=False)
    wid = Column("wid", String(32), ForeignKey('dictionary.WID'), nullable=False)

    def __init__(self, tid, vid, wid):
        self.tid = tid
        self.vid = vid
        self.wid = wid

    def __repr__(self):
        return "<Takes('{}','{}','{}')>".format(self.tid, self.vid, self.wid)


class Plan(db.Model):
    __tablename__ = 'plan'
    uid = Column("uid", String(32), ForeignKey('users.UID'), primary_key=True)
    tid = Column("tid", String(32), ForeignKey('takes.TID'), primary_key=True)
    wid = Column("wid", String(32), ForeignKey('dictionary.WID'), nullable=False)
    proficiency = Column("proficiency", Integer)

    def __init__(self, uid, tid, wid, proficiency):
        self.uid = uid
        self.tid = tid
        self.wid = wid
        self.proficiency = proficiency

    def __repr__(self):
        return "<Plan('{}','{}','{}','{}')>".format(self.uid, self.tid, self.wid, self.proficiency)


class Record(db.Model):
    __tablename__ = 'record'
    sid = Column("sid", String(32), primary_key=True, nullable=False)
    uid = Column("uid", String(32), nullable=False)
    dates = Column("dates", String(32), nullable=False)
    learned = Column("learned", Integer, nullable=False)
    reviewed = Column("reviewed", Integer, nullable=False)
    proficiency = Column("proficiency", ARRAY(Integer))
    ahour = Column("ahour", ARRAY(Float))
    aday = Column("aday", Integer)

    def __init__(self, sid, uid, dates, learned, reviewed, proficiency, ahour, aday):
        self.sid = sid
        self.uid = uid
        self.dates = dates
        self.learned = learned
        self.reviewed = reviewed
        self.proficiency = proficiency
        self.ahour = ahour
        self.aday = aday

    def __repr__(self):
        return "<Record('{}','{}','{}','{}','{}','{}','{}','{}')>".format(
            self.sid, self.uid, self.dates, self.learned, self.reviewed, self.proficiency, self.ahour, self.aday)


class Feedback(db.Model):
    __tablename__ = 'feedback'
    fid = Column("fid", String(32), primary_key=True, nullable=False)
    uid = Column("uid", String(32), nullable=False)
    dates = Column("dates", DateTime, nullable=False)
    info = Column("info", Text(MAX_LEN))

    def __init__(self, fid, uid, dates, info):
        self.fid = fid
        self.uid = uid
        self.dates = dates
        self.info = info

    def __repr__(self):
        return "<Feedback('{}','{}','{}','{}')>".format(self.fid, self.uid, self.dates, self.info)


# @app.route('/')
# def test():
#     u = db.session.query(Users).all()
#     print("Users", u[0])
#     d = db.session.query(Dictionary).all()
#     print("Dictionary", d[0])
#     v = db.session.query(Vocabulary).all()
#     print("Vocabulary", v[0])
#     t = db.session.query(Takes).all()
#     print("Takes", t[0])
#     f = db.session.query(Feedback).all()
#     print("Feedback", f[0])
#     r = db.session.query(Record).all()
#     print("Record", r[0])
#     p = db.session.query(Plan).all()
#     print("Plan", p[0])
#
#     return {}


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=9102, debug=True)
