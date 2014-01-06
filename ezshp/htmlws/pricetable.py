# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import myadmin.initdb
from django.shortcuts import render

@csrf_exempt
def index(request):
	db = myadmin.initdb.dbworker()
	substr = request.POST.get("substr")
	if (substr is None):
		sql = "select caption from (select caption FROM goods ORDER BY RAND() LIMIT 10) as main order by caption"
	else:
		sql = u"select caption FROM goods where caption like '{0}%' ORDER BY caption LIMIT 10 ".format(substr)
	print(sql)
	db.cursor.execute(sql)
	row =  db.cursor.fetchone()
	goods = []
	while row is not None:
		goods += [row[0]]
		row =  db.cursor.fetchone()
	context = {"deguging" : False,
	"goods" : goods}
	return render(request, 'pricetable.html', context)