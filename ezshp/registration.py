# -*- coding: utf-8 -*-
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
import htmlgen as hg
import json
from Crypto.Cipher import AES

def index(request):
    # t = hg.htmlgn(request)
    # t.setjsrootname(request.path)

    # n = hg.navigationblock()
    # t.append(n)
    # t.append(hg.htmltext("<br>"))
    
    # reg = hg.htmltext("""<div id = "registration-main-div">Пройдите три простых шага:
    #     <ol>
    #     <li id = "point-one"><div>Укажите свой электронный ящик<div><input id = "reg-email" placeholder = "e-mail"></input><button id = "sender" onclick = "sendregistermail()">Зарегистрироваться</button></li>
    #     <li>Подвердите свой ящик, перейдя по ссылке в письме</li>
    #     <li>Выберите версию 1С, которую Вы используете</li>
    #     </ol></div""")

    # t.append(reg)

    # t.jsmain = """function sendregistermail(){
    # var jqxhr = $.ajax({
    # "url":"/jsonws/ws/",
    # type: "POST",
    # "data": {
    #     method:"sendacceptedmail",
    #     email:$("#reg-email").val()},
    # beforeSend: function () {
    #         $("#sender").html("Идет обработка");
    #         $("#sender").attr("disabled", true);
    # }
    # } )
    #     .done(function() {
    #         //alert( "success" );
    #         alert( "На Ваш адресс " + $("#reg-email").val() + " выслано письмо с дальнейшими действиями.");
    #         $("#reg-email").attr("disabled", true);
    #         $("#point-one").css("text-decoration", "line-through");
    #     })
    #     .fail(function() {
    #         alert( "error" );
    #     })
    #     .always(function() {
    #         //alert( "На Ваш адресс " + $("#reg-email").val() + " выслано письмо с дальнейшими действиями.");
    #         $("#sender").html("Зарегистрироваться");
    #     });
    # }
    # """
    # t.cssmain = """#reg-email {
    #     width: 325px
    # }"""
    # httptext = t.gen()
    links = ["registration.css"]
    scripts = ["registration.js"]
    context = {}
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