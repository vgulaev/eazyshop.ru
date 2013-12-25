# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json
import sendacceptedmail
import myadmin.initdb
import uuid
import datetime

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

@csrf_exempt
def index(request):
    ans = {}
    isauthorize = False
    logout = False
    if request.method == 'POST':
        if (request.POST["method"] == "sendacceptedmail"):
            ans = sendacceptedmail.send(request.POST)
        elif (request.POST["method"] == "addaccount"):
            ans = addaccount(request.POST)
        elif (request.POST["method"] == "authorize"):
            ans = authorize(request, request.POST)
            isauthorize = True
        elif (request.POST["method"] == "logout"):
            ans = {"try" : "try"}
            logout = True
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