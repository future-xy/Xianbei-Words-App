#!/usr/bin/env python
# -*- coding: utf-8 -*-

from email.mime.text import MIMEText
from email.header import Header
from smtplib import *


def sendMail(recv_addr, mail_content):
    server = 'smtp.sina.com'                # SMTP服务器
    send_addr = 'database_app@sina.com'     # 发送地址
    #sender = '先背单词App  '               # 发件人
    pwd = 'ac3e268ebb74985e'                # SMTP授权码

    #mail_title = '注册'
    smtp = SMTP_SSL(server)
    smtp.ehlo(server)
    smtp.login(send_addr, pwd)

    msg = MIMEText(mail_content, "plain", 'utf-8')      # 邮件内容
    # msg["Subject"] = Header(mail_title, 'utf-8')      #邮件主题
    msg["From"] = send_addr  # 发送地址
    msg["To"] = Header(recv_addr, 'utf-8')              # 收件地址

    try:
        smtp.sendmail(send_addr, recv_addr, msg.as_string())
        return 0
    except SMTPException:
        return 1
    smtp.quit()
