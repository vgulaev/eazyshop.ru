# -*- coding: utf-8 -*-
from django.shortcuts import render
import ez
import dbconnect
import sqltables

def getdbversion():
	db = dbconnect.dbworker()
	sql = "show tables from c9 like 'sysinfo'"
	db.cursor.execute(sql)
	userrow =  db.cursor.fetchone()
	if userrow is None:
		ver = 0
	else:
		sql = "select value from sysinfo where key_name = 'versiondb'"
		db.cursor.execute(sql)
		userrow =  db.cursor.fetchone()
		if userrow is None:
			ver = 0
		else:
			ver = int(userrow[0])
	return ver
	
def runupdatedb():
	db = dbconnect.dbworker()
	dbversion = getdbversion()

	#q = ""
	for i in range(dbversion, len(sqltables.updatequeryes)):
		for q in sqltables.updatequeryes[i]:
			db.cursor.execute(q)
			db.db.commit()
	return "complate!!!"
	#return dbversion

def index(request):
    authorities = ez.checkauthorize(request)
    #scripts = ["index.js"]
    context = {"authorities": authorities}
    if ((authorities.have) and (authorities.login == "vgulaev@yandex.ru")):
    	context["dbup"] = runupdatedb()
    	return render(request, 'updatedb.html', context)
    else:
    	return render(request, 'necessaryauth.html', context)