#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Name    : __init__.py.py
# Time    : 2020/1/26 22:16
# Author  : Fu Yao
# Mail    : fy38607203@163.com


import logging
import sys
import os

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from config import config
from app.util.logger import logger_init

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'


def create_app(config_name):
    app = Flask(__name__, static_url_path='')
    app.config.from_object(config[config_name])

    # initialize
    db.init_app(app)
    login_manager.init_app(app)

    # log settings
    app.logger = logging.getLogger('App')
    app.logger.setLevel(logging.DEBUG)
    app.logger.addHandler(logger_init(os.path.join(app.config.get('BASE_DIR'), 'logs/critical.log'), logging.CRITICAL))
    app.logger.addHandler(logger_init(os.path.join(app.config.get('BASE_DIR'), 'logs/error.log'), logging.ERROR))
    app.logger.addHandler(logger_init(os.path.join(app.config.get('BASE_DIR'), 'logs/warning.log'), logging.WARNING))
    app.logger.addHandler(logger_init(os.path.join(app.config.get('BASE_DIR'), 'logs/info.log'), logging.INFO))
    app.logger.addHandler(logger_init(os.path.join(app.config.get('BASE_DIR'), 'logs/debug.log'), logging.DEBUG))

    from .client import client as client_blueprint
    app.register_blueprint(client_blueprint)

    return app
