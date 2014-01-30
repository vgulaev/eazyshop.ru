# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json
import myadmin.dbconnect

def showtables(ans):
	ans["colums"].append("name")
	db = myadmin.dbconnect.dbworker()
	sql = u"show tables"
	db.cursor.execute(sql)
	row =  db.cursor.fetchone()
	while row is not None:
		ans["rows"].append(row[0])
		row =  db.cursor.fetchone()

def dbquery(ans, q):
	db = myadmin.dbconnect.dbworker()
	sql = q
	db.cursor.execute(sql)
	row =  db.cursor.fetchone()
	while row is not None:
		ans["rows"].append(row)
		row =  db.cursor.fetchone()

@csrf_exempt
def index(request):
	ans = {"test": "test"}

	if request.method == 'POST':
		ans = {"colums" : [],
		"rows": []}
		jsondata = request.POST
		if (jsondata["method"] == "tables"):
			showtables(ans);
		if (jsondata["method"] == "query"):
			dbquery(ans, jsondata["qtext"]);

	httptext = json.dumps(ans)
	response = HttpResponse(httptext, content_type="application/json")
	return response