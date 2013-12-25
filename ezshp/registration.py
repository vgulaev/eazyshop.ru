# -*- coding: utf-8 -*-
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
import htmlgen as hg
import json
from Crypto.Cipher import AES

def index(request):
    links = ["registration.css"]
    scripts = ["registration.js"]
    context = { "scripts": scripts,
                "links": links}
    return render(request, 'registration.html', context)

def accept(request, uid = ""):
    obj2 = AES.new('This is a key123', AES.MODE_CFB, 'This is an IV456')
    cred = json.loads(obj2.decrypt(str(uid).decode("hex")))

    links = ["accept.css"]
    scripts = ["accept.js"]
    context = { "email": cred["e"],
                "scripts": scripts,
                "links": links}

    return render(request, 'accept.html', context)