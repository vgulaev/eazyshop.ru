# -*- coding: utf-8 -*-
from django.shortcuts import render

def index(request):
    scripts = ["index.js"]
    context = {"scripts" : scripts}
    return render(request, 'index.html', context)