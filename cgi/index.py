#!c:/Python27/python.exe
# -*- coding: utf-8 -*-
# This Python file uses the following encoding: utf-8

import htmlgen
print ("Content-Type: text/html; charset=utf-8")
print ("")
h = htmlgen.htmlgn();

b = htmlgen.input()
h.items.append(b)

b = htmlgen.button()
b.id = "fb"
b.caption = "Жми!!!";
h.items.append(b)

b = htmlgen.button()
b._class = "btcl"
b.caption = "Вторая кнопка";
h.items.append(b)

h.gen()