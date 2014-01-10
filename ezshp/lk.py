# -*- coding: utf-8 -*-
from django.shortcuts import render
import ez

def index(request):
    authorities = ez.checkauthorize(request)
    scripts = ["lk.js"]
    context = {"authorities": authorities,
    			"location": "lk",
    			"scripts": scripts}
    if (authorities.have):
    	return render(request, 'lk.html', context)
    else:
    	return render(request, 'necessaryauth.html', context)
    #return HttpResponse(str(authorities.login), content_type="text/plain")