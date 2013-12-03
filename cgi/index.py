#!c:/Python27/python.exe
import htmlgen
print ("Content-Type: text/html; charset=utf-8")
print ("")
h = htmlgen.htmlgn();

b = htmlgen.button()
b.caption = "Жми!!!";
h.items.append(b)
h.gen()