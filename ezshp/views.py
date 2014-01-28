# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import ez

def demo(request):
   	authorities = ez.checkauthorize(request)
   	#scripts = ["index.js"]
   	context = {"authorities": authorities,
   				"location": "home"}
   	return render(request, 'demo.html', context)
    #return HttpResponse(str(authorities.login), content_type="text/plain")

def index(request):
   	authorities = ez.checkauthorize(request)
   	#scripts = ["index.js"]
   	context = {"authorities": authorities,
   				"location": "home"}
   	return render(request, 'index.html', context)
    #return HttpResponse(str(authorities.login), content_type="text/plain")