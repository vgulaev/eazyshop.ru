# -*- coding: utf-8 -*-
# Create your views here.
from django.http import HttpResponse
from django.conf import settings
import htmlgen as hg

def index(request):
    t = hg.htmlgn()
    
    a = hg.a(id = "reftoadmin")
    a.caption = "Admin page"
    a.href = "/myadmin/"
    t.append(a)
    t.append(hg.htmltext("<br>"))    

    a = hg.a(id = "sa")
    a.caption = "Not bad"
    a.href = "/json/"
    t.append(a)
    t.append(hg.htmltext("<br>"))

    a = hg.a(id = "sb")
    a.caption = "Show request"
    a.href = "/sr/"
    t.append(a)
    
    i = hg.input(id = "username")
    i.placeholder = "Логин"
    t.append(i)

    i = hg.input(id = "passw")
    i.placeholder = "Пароль"
    t.append(i)

    b = hg.button(id = "button-signin")
    b.caption = "Войти"
    t.append(b)
    
    b = hg.button(id = "button-signup")
    b.caption = "Зарегистрироваться"
    t.append(b)

    httptext = t.gen()
    return HttpResponse(httptext)
    #return httptext
    
#print(index("ddd"))