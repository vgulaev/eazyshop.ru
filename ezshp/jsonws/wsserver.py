# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json
import sendacceptedmail
import myadmin.initdb
import uuid

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


@csrf_exempt
def index(request):
    ans = {}
    if request.method == 'POST':
        if (request.POST["method"] == "sendacceptedmail"):
            ans = sendacceptedmail.send(request.POST)
        elif (request.POST["method"] == "addaccount"):
            ans = addaccount(request.POST)
        httptext = json.dumps(ans)
    else:
        httptext = str(request)
    #httptext = json.dumps(response_data)
    return HttpResponse(httptext, content_type="application/json")