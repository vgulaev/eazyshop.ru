# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json
import myadmin.dbconnect
import ez

def showtables(ans):
	ans["colums"].append("name")
	db = myadmin.dbconnect.dbworker()
	sql = u"show tables"
	db.cursor.execute(sql)
	row =  db.cursor.fetchone()
	while row is not None:
		ans["rows"].append(row[0])
		row =  db.cursor.fetchone()

def dbquery(ans, q, ifcommit = False):
	db = myadmin.dbconnect.dbworker()
	sql = q
	db.cursor.execute(sql)
	#ans["q"] = q
	if (ifcommit == "True"):
		db.db.commit()
		ans.clear()
		ans["result"] = "ok"
	else:
		row =  db.cursor.fetchone()
		while row is not None:
			ans["rows"].append(row)
			row =  db.cursor.fetchone()
	db.cursor.close()

@csrf_exempt
def index(request):
	authorities = ez.checkauthorize(request)
	ans = {"test": "test"}
	if request.method == 'POST':
		ans = {"colums" : [],
		"rows": []}
		jsondata = request.POST
		if (jsondata["method"] == "tables"):
			showtables(ans);
		if (jsondata["method"] == "query"):
			if jsondata["query_text"] == "select_from_goods":
				cond = jsondata["qtext"]
				if authorities.have:
					if len(cond) > 0:
						cond += " and "
					cond += u" shop = '{0}'".format(authorities.shopid) 
				sql = u"select * from goods where {0} limit 10".format(cond)
				dbquery(ans, sql, jsondata.get("commit"))
			else:
				if (authorities.have) and (authorities.login != "demo@demo.ru"):
					dbquery(ans, jsondata["qtext"], jsondata.get("commit"))
		if (jsondata["method"] == "queries"):
			if (authorities.have) and (authorities.login != "demo@demo.ru"):
				ans = {"results" : []}
				qs = json.loads(jsondata["qtext"])
				for q in qs:
					a = {"colums" : [],
					"rows": []}
					dbquery(a, q);
					ans["results"].append(a)
	httptext = json.dumps(ans)
	response = HttpResponse(httptext, content_type="application/json")
	return response