#!/usr/bin/env python
# -*- coding: utf-8 -*-

from email.mime.text import MIMEText
from email.header import Header
from smtplib import *


class Mail:
    def __init__(self, server, send_addr, pwd, header):
        self.server = server
        self.send_addr = send_addr
        self.pwd = pwd
        self.header = header

    def send(self, recv_addr, content, title):
        h = Header(self.header, 'utf-8')
        h.append('<{}>'.format(self.send_addr), 'ascii')

        msg = MIMEText(content, "plain", 'utf-8')  # 邮件内容

        # 邮件头部
        msg['Subject'] = Header(title, 'utf-8')  # 邮件主题
        msg['From'] = h  # 发件人
        msg['To'] = Header(recv_addr, 'utf-8')  # 收件人

        smtp = SMTP_SSL(self.server)
        smtp.ehlo(self.server)
        smtp.login(self.send_addr, self.pwd)

        try:
            smtp.sendmail(self.send_addr, recv_addr, msg.as_string())
            smtp.quit()
            return 0
        except SMTPException:
            smtp.quit()
            return 1
