# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json
import sendacceptedmail
import myadmin.dbconnect
import uuid
import datetime
import db1c.server1c
import xml.etree.cElementTree as et

def normalizedata(request):
    if ("1C" in request.META["HTTP_USER_AGENT"]):
        rawdata = request.read()
        jsondata = json.loads(rawdata[3:])
    else:
        jsondata = request.POST
        #jsondata = str(request)
    return jsondata

def addaccount(data):
    db = myadmin.dbconnect.dbworker()
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
    db = myadmin.dbconnect.dbworker()
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
    db = myadmin.dbconnect.dbworker()
    #тут есть момент что магазины могут отличаться а идентификаторы товаров нет
    sql = u"""INSERT INTO goods (id, shop, caption) VALUES ('{0}', '{1}', '{2}')
            ON DUPLICATE KEY UPDATE caption='{2}';
    """.format(data["id"], data["shop"], data["caption"])
    #sql = """INSERT INTO goods (id, shop, caption) VALUES ('%s', '%s', '%s')""" % (data["id"], data["shop"], data["caption"])
    db.cursor.execute(sql)
    db.db.commit()
    return {}

def get_shop_id_by_ezid(data):
    db = myadmin.dbconnect.dbworker()
    sql = u"select users.shop from sessions join users on sessions.login = users.id where sessions.id = '{0}'".format(data["session_uid"])
    db.cursor.execute(sql)
    userrow =  db.cursor.fetchone()
    if userrow is not None:
        s = userrow[0]
    else:
        s = "no"
    return {"shop_uid" : s}

def getorder(data):
    # srv1c = db1c.server1c.remoteserver()
    # sxml = srv1c.getobj(data["uid"], u"ВнутреннийЗаказ", "own")
    # root = et.fromstring(sxml.encode("utf-8"))
    # ans = {child.tag : child.text for child in root if (child.tag in ['Date', 'Number', u'Комментарий'])}
    # el = root.find(u"Ответственный")
    # ans[u"Ответственный"] = {"uid" : el.attrib["uid"], u"наименование" : el.attrib[u"наименование"]}
    # el = root.find(u"Исполнитель")
    # ans[u"Исполнитель"] = {"uid" : el.attrib["uid"], u"наименование" : el.attrib[u"наименование"]}
    # ans["row"] = [];
    ans = {"re": "sxml"}
    return ans

def getorderlist(data):
    srv1c = db1c.server1c.remoteserver()
    q = u"""
ВЫБРАТЬ
    ВнутреннийЗаказ.Ссылка
ИЗ
    Документ.ВнутреннийЗаказ КАК ВнутреннийЗаказ

УПОРЯДОЧИТЬ ПО
    ВнутреннийЗаказ.Дата УБЫВ    
    """
    count = "0";
    sxml = srv1c.gettable(q, u"дата, номер, ответственный, исполнитель", "0", count)
    root = et.fromstring(sxml.encode("utf-8"))
    ans = {"colums" : [],
        "rows": []}
    for row in root.findall("row"):
        r = {u"дата" : row.attrib[u"дата"],
                u"номер" : row.attrib[u"номер"],
                u"ответственный" : row.attrib[u"ответственный"],
                u"исполнитель" : row.attrib[u"исполнитель"],
                u"uid" : row.attrib[u"uid"]}
        ans["rows"].append(r)
        #ans["rows"][
        #ans["rows"][]
    ans["count"] = root.attrib["count"]
    #ans = json.dumps(sxml)
    return ans

def testserver():
    return {"ans" : "ok"}

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
        elif (jsondata["method"] == "get_shop_id_by_ezid"):
            ans = get_shop_id_by_ezid(jsondata)
        elif (jsondata["method"] == "testserver"):
            ans = testserver()
        elif (jsondata["method"] == "getorderlist"):
            ans = getorderlist(jsondata)
        elif (jsondata["method"] == "getorder"):
            ans = getorder(jsondata)
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