#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Name    : manage.py
# Time    : 2020/1/27 10:10
# Author  : Fu Yao
# Mail    : fy38607203@163.com

import os

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import create_app, db

app = create_app(os.getenv('CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
