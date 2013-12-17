# -*- coding: utf-8 -*-
from django.http import HttpResponse
import htmlgen as hg

def index(request):
    t = hg.htmlgn(request)
    t.setjsrootname(request.path)

    n = hg.navigationblock()
    t.append(n)
    t.append(hg.htmltext("<br>"))    
    
    t.append(hg.htmltext("""
    <ul>
    <li>На первом месте функциональность</li>
    <li>Аскетичный дизайн или его отсутсивие (возможен пересмотр)</li>
    <li>Реализуеться функционал и публикуеться, дизайна может и не быть</li>
    <li>Абсолютная открытость проекта: ваши данные абсолютно открытна, практически любой может их получить и как то использовать</li>
    </ul>
    """))
    httptext = t.gen()
    return HttpResponse(httptext)
    
def who_we_are(request):
    t = hg.htmlgn(request)
    t.setjsrootname(request.path)

    n = hg.navigationblock()
    t.append(n)
    t.append(hg.htmltext("<br>"))    
    
    t.append(hg.htmltext("""Мы амбициозный проект, у которого есть несколько целей
    <ul>
    <li>Дать возможность каждому попробывать on-line торговлю</li>
    <li>Стать лучшей интернет витриной</li>
    <li>Предоставить всем сервис личных кабинетов как b2b так и b2c</li>
    <li>Организовать удобный сервис формирование любых заказов</li>
    </ul>
    """))
    httptext = t.gen()
    return HttpResponse(httptext)