# -*- coding: utf-8 -*-
import suds
from django.http import HttpResponse
import requests
from django.views.decorators.csrf import csrf_exempt
import platform
import psycopg2
import json

def cast_pickle(data, cur):
    if data is None: return None
    r = data[26:34] + "-" + data[22:26] + "-" + data[18:22] + "-" + data[2:6] + "-" + data[6:18]
    #print data
    return r

def DATETIMEtoStr(data, cur):
	return data
	
@csrf_exempt
def route(request):
	# psycopg2.extensions.register_type(
 #    	psycopg2.extensions.new_type(
 #        	psycopg2.DATETIME.values, 'Date-str', DATETIMEtoStr))
	# psycopg2.extensions.register_type(
 #    	psycopg2.extensions.new_type(
 #        	psycopg2.BINARY.values, 'BINARY-PICKLE', cast_pickle))
	# conn = psycopg2.connect("host='89.250.147.200' port='55432' dbname='USODev' user='usodev' password='usodev'")
	# curs = conn.cursor()
	# sql = request.read()
	# curs.execute(sql)
	#, _idrref, _fld3204rref, _version
	# httptext = json.dumps(curs.fetchall())
	# response = HttpResponse(httptext, content_type="application/json")
	#response = HttpResponse(httptext, content_type="text/plain")
	#response = HttpResponse(str(request), content_type="text/plain")
	httptext = "Hello word!!!"
	return response