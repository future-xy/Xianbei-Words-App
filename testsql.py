#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Name    : testsql.py
# Time    : 2020/1/26 11:16
# Author  : Fu Yao
# Mail    : fy38607203@163.com

from sqlalchemy import Column, String, create_engine
from sqlalchemy.types import CHAR, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func, desc, distinct, asc

Base = declarative_base()

MAX_LEN = 65535
DB_URL = 'postgresql+psycopg2://postgres:sysu_sdcs_db2019@111.231.250.160:5432/database0'


# class Catalog(Base):
#     """
#     目录结构
#     """
#     __tablename__ = "t_app_market_catalog"  # 关联的数据库中的表名
#
#     id = Column("id", Integer, primary_key=True, nullable=False, autoincrement=True)  # 类成员变量关联表字段
#     catalog = Column('catalog', Text, nullable=False)  # 类成员变量关联表字段
#
#     def __init__(self, id=None, catalog=None):  # (可有可无,看需求)
#         self.id = id
#         self.catalog = catalog


class FEEDBACK(Base):
    __tablename__ = 'feedback'
    FID = Column("fid", String(32), primary_key=True, nullable=False)
    UID = Column("uid", String(32), nullable=False)
    Dates = Column("dates", String(32), nullable=False)
    INFO = Column("info", Text(MAX_LEN))

    def __init__(self, FID, UID, Dates, INFO):
        self.FID = FID
        self.UID = UID
        self.Dates = Dates
        self.INFO = INFO


# "postgresql://postgres:36o%Situation2018@192.168.232.188:52432/situation"
# '数据库类型://用户名:口令@机器地址:端口号/数据库名
engine = create_engine(DB_URL, echo=True)

DBsession = sessionmaker(bind=engine)
session = DBsession()
query = session.query(FEEDBACK)
# print(session.query(func.count(FEEDBACK.FID)).all())
