#!c:/Python27/python.exe
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import ez
import htmlgen as hg
import dbconnect

def index(request):
    #loadmysqlcredential()
    authorities = ez.checkauthorize(request)

    context = {"authorities": authorities,
                "location": "myadmin"}

    if (authorities.have):
        d = dbconnect.dbworker()
        d.doinitdb()
        t = hg.htmlgn(request)
        t.setjsrootname(request.path)
        t.append(hg.htmltext("Initialization complete!!!"))

        httptext = t.gen()
        return HttpResponse(httptext)
    else:
        return render(request, 'necessaryauth.html', context)