# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json
import sendacceptedmail
import myadmin.initdb
import uuid
import datetime

def normalizedata(request):
    if ("1C" in request.META["HTTP_USER_AGENT"]):
        rawdata = request.read()
        jsondata = json.loads(rawdata[3:])
    else:
        jsondata = request.POST
        #jsondata = str(request)
    return jsondata

def addaccount(data):
    db = myadmin.initdb.dbworker()
    shopid = str(uuid.uuid1())
    sql = "INSERT INTO shops (id, caption, synonyms) VALUES ('%s', '%s', '%s')" % (shopid, data["shopname"], data["synonyms"])
    db.cursor.execute(sql)
    userid = str(uuid.uuid1())
    sql = "INSERT INTO users (id, login, pass, shop) VALUES ('%s', '%s', '%s', '%s')" % (userid, data["email"], data["pass"], shopid)    
    db.cursor.execute(sql)
    db.db.commit()
    return {"email" : data["email"],
            "pass" : data["pass"],
            "shopname" : data["shopname"],
            "synonyms" : data["synonyms"]}

def authorize(request, data):
    db = myadmin.initdb.dbworker()
    sql = "SELECT id FROM c9.users where login = '%s' and pass = '%s';" % (data["login"], data["pass"])
    db.cursor.execute(sql)
    userrow =  db.cursor.fetchone()
    if userrow is not None:
        sessionid = uuid.uuid1()
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql = "INSERT INTO sessions (id, login, time_start) VALUES ('%s', '%s', '%s')" % (sessionid, userrow[0], time)
        db.cursor.execute(sql)
        db.db.commit()
        s = str(sessionid)
    else:
        s = "no"
    return {"ezid" : s}

def addarticle(data):
    db = myadmin.initdb.dbworker()
    #тут есть момент что магазины могут отличаться а идентификаторы товаров нет
    sql = u"""INSERT INTO goods (id, shop, caption) VALUES ('{0}', '{1}', '{2}')
            ON DUPLICATE KEY UPDATE caption='{2}';
    """.format(data["id"], data["shop"], data["caption"])
    #sql = """INSERT INTO goods (id, shop, caption) VALUES ('%s', '%s', '%s')""" % (data["id"], data["shop"], data["caption"])
    db.cursor.execute(sql)
    db.db.commit()
    return {}

@csrf_exempt
def index(request):
    ans = {}
    isauthorize = False
    logout = False
    if request.method == 'POST':
        #need clear BOM header if it send from stupid platforms
        jsondata = normalizedata(request)
        if (jsondata["method"] == "sendacceptedmail"):
            ans = sendacceptedmail.send(request.POST)
        elif (jsondata["method"] == "addaccount"):
            ans = addaccount(request.POST)
        elif (jsondata["method"] == "authorize"):
            ans = authorize(request, jsondata)
            isauthorize = True
        elif (jsondata["method"] == "logout"):
            ans = {"try" : "try"}
            logout = True
        elif (jsondata["method"] == "addarticle"):
            ans = addarticle(jsondata)
        httptext = json.dumps(ans)
    else:
        httptext = str(request)
    #httptext = json.dumps(response_data)
    response = HttpResponse(httptext, content_type="application/json")
    if (logout):
        response.delete_cookie("ezid")
    if (isauthorize):
        if (ans["ezid"] != "no"):
            response.set_cookie("ezid", ans["ezid"])
    return response