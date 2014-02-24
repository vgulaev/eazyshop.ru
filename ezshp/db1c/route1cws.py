# -*- coding: utf-8 -*-
import suds
from django.http import HttpResponse
import requests
from django.views.decorators.csrf import csrf_exempt
import platform

def connectionurl():
	if (platform.system() == "Windows"):
		res = "http://89.250.147.200:40080/USODev2014/ws/"
	else:
		res = "http://89.250.147.200:40080/USO/ws/"
	res = "http://89.250.147.200:40080/USO/ws/"
	#res = "http://89.250.147.200:40080/USODev2014/ws/"
	return res

@csrf_exempt
def route(request):
	url = connectionurl() + "restservice.1cws"
	if request.method == 'POST':
		rawdata = request.read()
		r = requests.post(url, data = rawdata)
		content = r.content;
	else:
		r = requests.get(url)
	response = HttpResponse(r.text, content_type="text/xml")
	return response
def routewsdl(request):
	url = connectionurl() + "restservice.1cws?wsdl"
	r = requests.get(url)
	response = HttpResponse(r.text, content_type="text/xml")
	return response
