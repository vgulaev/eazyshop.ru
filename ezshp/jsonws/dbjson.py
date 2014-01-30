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
#	while row is not None:
#		ans["rows"] += [row[0]]

@csrf_exempt
def index(request):
	ans = {"test": "test"}

	if request.method == 'POST':
		ans = {"colums" : [],
		"rows": []}
		jsondata = request.POST
		if (jsondata["method"] == "tables"):
			showtables(ans);

	httptext = json.dumps(ans)
	response = HttpResponse(httptext, content_type="application/json")
	return response