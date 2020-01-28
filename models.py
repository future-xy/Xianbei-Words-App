#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Name    : models.py
# Time    : 2020/1/23 20:35
# Author  : Fu Yao
# Mail    : fy38607203@163.com


from app import db, login_manager
from app.util.utils import newID

from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float, Text, Enum, TIMESTAMP, CHAR
from sqlalchemy.dialects.postgresql import ARRAY

from datetime import datetime, date


class Users(db.Model):
    __tablename__ = 'users'
    uid = Column("uid", String(32), primary_key=True, nullable=False, unique=True, default=lambda: newID(prefix='U'))
    uname = Column("uname", String(64), nullable=False)
    pw = Column("pw", String(64), nullable=False)
    avatar = Column("avatar", String(4194304), nullable=False, default='')
    mail = Column("mail", String(64), nullable=False)
    pnumber = Column("pnumber", String(32), nullable=False)
    sex = Column("sex", CHAR, nullable=False, default='U')
    education = Column("education", String(32), nullable=False, default='')
    grade = Column("grade", Integer, nullable=False, default=0)
    vid = Column("vid", String(32), ForeignKey('vocabulary.vid'), nullable=True)

    def __repr__(self):
        return "<Users('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')>".format(
            self.uid, self.uname, self.pw, self.avatar, self.mail, self.pnumber, self.sex, self.education, self.grade,
            self.vid)


class Dictionary(db.Model):
    __tablename__ = 'dictionary'
    wid = Column("wid", String(32), primary_key=True, nullable=False, default=lambda: newID(prefix='W'))
    english = Column("english", String(64), nullable=False, default='')
    psymbol = Column("psymbol", String(32), nullable=False, default='')
    chinese = Column("chinese", Text, nullable=False, default='')

    def __repr__(self):
        return "<Dictionary('{}','{}','{}','{}')>".format(self.wid, self.english, self.psymbol, self.chinese)


class Vocabulary(db.Model):
    __tablename__ = 'vocabulary'
    vid = Column("vid", String(32), primary_key=True, nullable=False, default=lambda: newID(prefix='V'))
    vname = Column("vname", String(128), nullable=False, default='')
    count = Column("count", Integer, nullable=False, default=0)
    day = Column("day", Integer, nullable=False, default=0)
    type = Column("type", String(64), nullable=False, default='')

    def __repr__(self):
        return "<Vocabulary('{}','{}','{}','{}','{}')>".format(self.vid, self.vname, self.count, self.day, self.type)


class Takes(db.Model):
    __tablename__ = 'takes'
    tid = Column("tid", String(32), primary_key=True, nullable=False, default=lambda: newID('T'))
    vid = Column("vid", String(32), ForeignKey('vocabulary.vid'), nullable=False)
    wid = Column("wid", String(32), ForeignKey('dictionary.wid'), nullable=False)

    def __repr__(self):
        return "<Takes('{}','{}','{}')>".format(self.tid, self.vid, self.wid)


class Plan(db.Model):
    __tablename__ = 'plan'
    uid = Column("uid", String(32), ForeignKey('users.uid'), primary_key=True, nullable=False)
    tid = Column("tid", String(32), ForeignKey('takes.tid'), primary_key=True, nullable=False)
    proficiency = Column("proficiency", Integer, nullable=False, default=0)
    dates = Column("dates", Date, nullable=True)

    def __repr__(self):
        return "<Plan('{}','{}','{}','{}')>".format(self.uid, self.tid, self.proficiency, self.dates)


class Record(db.Model):
    __tablename__ = 'record'
    sid = Column("sid", String(32), primary_key=True, nullable=False, default=lambda: newID('S'))
    uid = Column("uid", String(32), ForeignKey('users.uid'), nullable=False)
    dates = Column("dates", Date, nullable=False, default=date.today)
    learned = Column("learned", Integer, nullable=False, default=0)
    reviewed = Column("reviewed", Integer, nullable=False, default=0)
    proficiency = Column("proficiency", ARRAY(Integer), nullable=False)
    ahour = Column("ahour", ARRAY(Float), nullable=False)
    aday = Column("aday", Integer, nullable=False, default=0)

    def __repr__(self):
        return "<Record('{}','{}','{}','{}','{}','{}','{}','{}')>".format(
            self.sid, self.uid, self.dates, self.learned, self.reviewed, self.proficiency, self.ahour, self.aday)


class Feedback(db.Model):
    __tablename__ = 'feedback'
    fid = Column("fid", String(32), primary_key=True, nullable=False, default=lambda: newID('F'))
    uid = Column("uid", String(32), ForeignKey('users.uid'), nullable=False)
    dates = Column("dates", TIMESTAMP, nullable=False, default=datetime.now)
    info = Column("info", Text, nullable=False, default='')

    def __repr__(self):
        return "<Feedback('{}','{}','{}','{}')>".format(self.fid, self.uid, self.dates, self.info)
