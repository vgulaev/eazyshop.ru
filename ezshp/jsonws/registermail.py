# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import datetime
import json
import os

from smtplib import SMTP_SSL as SMTP
from email.MIMEText import MIMEText
from Crypto.Cipher import AES

@csrf_exempt
def index(request):
    #if request.method == 'POST':
    rdata = request.POST
    ans = {}
    ans["e"] = rdata["email"]
    ans["t"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    text_for_cipher = json.dumps(ans)
    
    obj = AES.new('This is a key123', AES.MODE_CFB, 'This is an IV456')
    ciphertext = obj.encrypt(text_for_cipher)

    forurl = "".join("{0:02x}".format(ord(e)) for e in ciphertext)
    
    text_subtype = 'plain'
    
    if (os.environ.get('C9_USER') == None):
        domainname = "http://eazyshop.ru"
    else:
        domainname = "https://eazyshop_ru-c9-vgulaev.c9.io"
    
    content="""Вас проветствует, eazyshop!!!
Для завершение регистрации, перейдите пожалуйста по ссылке: %(hn)s/accept/%(uid)s
С уважением, команда eazyshop.
""" % {"hn": domainname, "uid": forurl}

    subject="Завершение регистрации на eazyshop"
    msg = MIMEText(content, text_subtype)
    msg['Subject'] = subject
    msg['From']   = "webmaster@eazyshop.ru"

    s = SMTP('smtp.yandex.ru', port = 465)
    s.login("webmaster@eazyshop.ru", "28061984")
    s.sendmail("webmaster@eazyshop.ru", "vgulaev@yandex.ru", msg.as_string())
    s.quit()  
    
    httptext = json.dumps({"ans" : "ok"})
    
    return HttpResponse(httptext, content_type="application/json")