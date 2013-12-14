# -*- coding: utf-8 -*-
# Create your views here.
from django.http import HttpResponse
import htmlgen as hg

def index(request):
    t = hg.htmlgn(request)
    t.setjsrootname(request.path)

    n = hg.navigationblock()
    t.append(n)
    t.append(hg.htmltext("<br>"))
    
    reg = hg.htmltext("""<div id = "registration-main-div">Пройдите три простых шага:
        <ol>
        <li><div>Укажите свой электронный ящик<div><input id = "reg-email" placeholder = "e-mail"></input><button onclick = "sendregistermail()">Зарегистрироваться</button></li>
        <li>Подвердите свой ящик, перейдя по ссылке в письме</li>
        <li>Выберите версию 1С, которую Вы используете</li>
        </ol></div""")

    t.append(reg)

    t.jsmain = """function sendregistermail(){
    var jqxhr = $.ajax({
    "url":"/jsonws/testjson/",
    type: "POST",
    "data": {
        mail:"it is simple string for sendin",
        enother: "dsfsdfdsfsdfsd",
        fgffdg: "fsfdfsdsfsdf",
        hthth: "fgdfgdg"}
    } )
        .done(function() {
            alert( "success" );
        })
        .fail(function() {
            alert( "error" );
        })
        .always(function() {
            alert( "complete" );
        });
    }
    """
    t.cssmain = """#reg-email {
        width: 325px
    }"""
    httptext = t.gen()
    return HttpResponse(httptext)
    #return httptext
    
#print(index("ddd"))