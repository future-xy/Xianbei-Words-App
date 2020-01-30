#!/usr/bin/env python
# -*- coding: utf-8 -*-

from email.mime.text import MIMEText
from email.header import Header
from smtplib import *


def sendMail(recv_addr, mail_content, mail_title):

    server = 'smtp.sina.com'                            # SMTP服务器
    send_addr = 'database_app@sina.com'                 # 发送地址
    pwd = 'ac3e268ebb74985e'                            # SMTP授权码

    msg = MIMEText(mail_content, "plain", 'utf-8')      # 邮件内容

    # 邮件头部
    msg['Subject'] = Header(mail_title, 'utf-8')        # 邮件主题
    msg['From'] = send_addr                             # 发件人(因sina策略，发件人与发件邮箱必须保持一致)
    msg['To'] = Header(recv_addr, 'utf-8')              # 收件人

    smtp = SMTP_SSL(server)
    smtp.ehlo(server)
    smtp.login(send_addr, pwd)

    try:
        smtp.sendmail(send_addr, recv_addr, msg.as_string())
        smtp.quit()
        return 0
    except SMTPException:
        smtp.quit()
        return 1

