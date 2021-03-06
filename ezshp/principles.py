# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
import ez
import htmlgen as hg

def index(request):
    authorities = ez.checkauthorize(request)
    context = {"authorities": authorities}
    return render(request, 'principles.html', context)
    
def who_we_are(request):
    authorities = ez.checkauthorize(request)
    context = {"authorities": authorities}
    return render(request, 'who-we-are.html', context)

def welcome(request):
    authorities = ez.checkauthorize(request)
    scripts = ["welcome.js"]
    context = {"authorities"	: authorities,
                "location": "welcome",
				"scripts"		: scripts}
    return render(request, 'welcome.html', context)