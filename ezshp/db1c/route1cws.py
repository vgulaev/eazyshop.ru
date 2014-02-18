# -*- coding: utf-8 -*-
import suds
from django.http import HttpResponse
import requests
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def route(request):
	rawdata = request.read()
	url = "http://127.0.0.1/USODev2014/ws/restservice.1cws"
	r = requests.post(url, data = rawdata)
	response = HttpResponse(r.text, content_type="text/xml")
	#response = HttpResponse(str(request), content_type="text/plain")
	return response
def routewsdl(request):
	url = "http://127.0.0.1/USODev2014/ws/restservice.1cws?wsdl"
	r = requests.get(url)
	response = HttpResponse(r.text, content_type="text/xml")
	return response
