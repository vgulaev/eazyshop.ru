# -*- coding: utf-8 -*-
import smtplib

from smtplib import SMTP_SSL as SMTP

from email.MIMEText import MIMEText

text_subtype = 'plain'
content="""\
Пробуем отправить русский текст
"""
subject="Sent from Python"

msg = MIMEText(content, text_subtype)

msg['Subject'] = subject
msg['From']   = "webmaster@eazyshop.ru"

s = SMTP('smtp.yandex.ru', port = 465)
s.login("webmaster@eazyshop.ru", "28061984")
s.sendmail("webmaster@eazyshop.ru", "vgulaev@yandex.ru", msg.as_string())
s.quit()

import datetime
print(datetime.datetime.now())
print("Ok!!!")