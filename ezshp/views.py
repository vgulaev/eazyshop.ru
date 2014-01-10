# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import ez

@csrf_exempt
def index(request):
   	authorities = ez.checkauthorize(request)
   	#scripts = ["index.js"]
   	context = {"authorities": authorities,
   				"location": "home"}
   	return render(request, 'index.html', context)
    #return HttpResponse(str(authorities.login), content_type="text/plain")