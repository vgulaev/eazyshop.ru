# -*- coding: utf-8 -*-
# Create your views here.
from django.http import HttpResponse
from django.conf import settings
from django.template import RequestContext, loader
import htmlgen as hg

def indexfromtemplate(request):
    template = loader.get_template('index.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def index(request):
    t = hg.htmlgn(request)
    t.setjsrootname(request.path)
    
    n = hg.navigationblock()
    t.append(n)
    t.append(hg.htmltext("<br>"))    
    
    i = hg.input(id = "username")
    i.placeholder = "Логин"
    t.append(i)

    i = hg.input(id = "passw")
    i.placeholder = "Пароль"
    t.append(i)

    b = hg.button(id = "button-signin")
    b.caption = "Войти"
    t.append(b)
    
    a = hg.a(id = "button-signup")
    a.href = "/registration/"
    a.caption = "Зарегистрироваться"
    t.append(a)
    t.append(hg.htmltext("<br>"))
    
    a = hg.a(id = "whoweare")
    a.caption = "Кто мы такие и какие наши планы"
    a.href = "/who-we-are/"
    t.append(a)
    t.append(hg.htmltext("<br>"))

    a = hg.a(id = "pr")
    a.caption = "Узнайте наши принципы, что бы остаться с нами"
    a.href = "/principles/"
    t.append(a)
    
    t.jsmain = """
    $(function () {
    //$("#username").val($(window).width());
    //$("#passw").val($(window).height());
    //$("#button-signup").button();
    //$("#button-signin").button();
    });
    """;

    httptext = t.gen()
    return HttpResponse(httptext)
    #return httptext
    
#print(index("ddd"))