# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import myadmin.dbconnect
from django.shortcuts import render
from collections import namedtuple

@csrf_exempt
def index(request):
	db = myadmin.dbconnect.dbworker()
	substr = request.POST.get("substr")
	if ((substr is None) or (substr == "")):
		sql = "select caption, id from (select caption, id FROM goods ORDER BY RAND() LIMIT 10) as main order by caption"
	else:
		sql = u"select caption, id FROM goods where caption like '%{0}%' ORDER BY caption LIMIT 10".format(substr)
	#print(sql)
	db.cursor.execute(sql)
	row =  db.cursor.fetchone()
	goods = []
	Good = namedtuple('Good', ['caption', 'id'])
	while row is not None:
		goods += [Good(row[0], row[1])]
		row =  db.cursor.fetchone()
	context = {"deguging" : False,
	"goods" : goods}
	return render(request, 'pricetable.html', context)