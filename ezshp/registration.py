# -*- coding: utf-8 -*-
# Create your views here.
from django.http import HttpResponse
import htmlgen as hg
import json
from Crypto.Cipher import AES

def index(request):
    t = hg.htmlgn(request)
    t.setjsrootname(request.path)

    n = hg.navigationblock()
    t.append(n)
    t.append(hg.htmltext("<br>"))
    
    reg = hg.htmltext("""<div id = "registration-main-div">Пройдите три простых шага:
        <ol>
        <li id = "point-one"><div>Укажите свой электронный ящик<div><input id = "reg-email" placeholder = "e-mail"></input><button id = "sender" onclick = "sendregistermail()">Зарегистрироваться</button></li>
        <li>Подвердите свой ящик, перейдя по ссылке в письме</li>
        <li>Выберите версию 1С, которую Вы используете</li>
        </ol></div""")

    t.append(reg)

    t.jsmain = """function sendregistermail(){
    var jqxhr = $.ajax({
    "url":"/jsonws/registermail/",
    type: "POST",
    "data": {
        email:$("#reg-email").val()},
    beforeSend: function () {
            $("#sender").html("Идет обработка");
            $("#sender").attr("disabled", true);
    }
    } )
        .done(function() {
            //alert( "success" );
            alert( "На Ваш адресс " + $("#reg-email").val() + " выслано письмо с дальнейшими действиями.");
            $("#reg-email").attr("disabled", true);
            $("#point-one").css("text-decoration", "line-through");
        })
        .fail(function() {
            alert( "error" );
        })
        .always(function() {
            //alert( "На Ваш адресс " + $("#reg-email").val() + " выслано письмо с дальнейшими действиями.");
            $("#sender").html("Зарегистрироваться");
        });
    }
    """
    t.cssmain = """#reg-email {
        width: 325px
    }"""
    httptext = t.gen()
    return HttpResponse(httptext)

def accept(request, uid = ""):
    obj2 = AES.new('This is a key123', AES.MODE_CFB, 'This is an IV456')
    cred = json.loads(obj2.decrypt(str(uid).decode("hex")))

    t = hg.htmlgn(request)
    t.setjsrootname(request.path)

    n = hg.navigationblock()
    t.append(n)
    t.append(hg.htmltext("""<br>"""))
    
    i = hg.input(id="email")
    i.placeholder = "e-mail"
    i.value = str(cred["e"])
    t.append(i)
    t.append(hg.htmltext("<br>"))
    
    i = hg.input(id="pass")
    i.placeholder = "пароль"
    t.append(i)
    t.append(hg.htmltext("<br>"))

    i = hg.input(id="passcopy")
    i.placeholder = "повторите пароль"
    t.append(i)
    t.append(hg.htmltext("<br>"))


    i = hg.input(id="shopname")
    i.placeholder = "имя магазина"
    t.append(i)
    t.append(hg.htmltext("<br>"))
    
    i = hg.input(id="synonyms")
    i.placeholder = "английский синоним"
    t.append(i)
    t.append(hg.htmltext(", желательно короткий"))
    t.append(hg.htmltext("<br>"))
    
    e = hg.htmlevent()
    e.name = "onclick"
    e.function = "sendform()"
    e.text = "sendform"
    b = hg.button(id = "sendform")
    b.caption = "Завершить регистрацию"
    b.events.append(e)
    t.append(b)
    

    #t.append(hg.htmltext(str("Hello" + uid)))
    t.cssmain = """
    input {
    width: 250px
    }
    button {
    width: 250px
    }
    """
    t.jsmain = """
    """
    
    httptext = t.gen()
    return HttpResponse(httptext)