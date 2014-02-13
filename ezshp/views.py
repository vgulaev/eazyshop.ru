# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import ez

def jsontester(request):
    authorities = ez.checkauthorize(request)
    scripts = ["jsontester.js", "dbadapter.js"]
    context = {"authorities": authorities,
          "location": "home",
          "scripts": scripts}
    return render(request, 'jsontester.html', context)

def demo(request):
   	authorities = ez.checkauthorize(request)
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

def orderlist(request):
    authorities = ez.checkauthorize(request)
    scripts = ["innerorderslist.js"]
    context = {"authorities": authorities,
          "location": "innerorders",
          "scripts": scripts}
    return render(request, 'innerorderslist.html', context)

def innerorder(request, uid = ""):
    authorities = ez.checkauthorize(request)
    scripts = ["innerorder.js"]
    context = {"authorities": authorities,
          "location": "innerorders",
          "orderuid" : uid,
          "scripts": scripts}
    return render(request, 'innerorder.html', context)