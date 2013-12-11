# -*- coding: utf-8 -*-
from django.http import HttpResponse
import htmlgen as hg

def index(request):
    t = hg.htmlgn(request)
    t.setjsrootname(request.path)
    t.append(hg.htmltext("""
    <ul>
    <li>На первом месте функциональность</li>
    <li>Аскетичный дизайн или его отсутсивие (возможен пересмотр)</li>
    <li>Реализуеться функционал и публикуеться, дизайна может и не быть</li>
    </ul>
    """))
    httptext = t.gen()
    return HttpResponse(httptext)