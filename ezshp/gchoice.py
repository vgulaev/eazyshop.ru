# -*- coding: utf-8 -*-
"""Like Goods choice"""
from django.shortcuts import render
import ez

def index(request):
   	authorities = ez.checkauthorize(request)
   	scripts = ["gchoice.js"]
   	context = {"authorities": authorities,
   				"location"	: "choice",
   				"scripts"	: scripts}
   	return render(request, 'choice.html', context)
    #return HttpResponse(str(authorities.login), content_type="text/plain")