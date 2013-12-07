#!c:/Python27/python.exe
# -*- coding: utf-8 -*-
import htmlgenerator as hg

class htmltag:
    def __init__(self, id, _class):
        self.id = id
        self._class = _class
    def idtext(self):
	    return hg.at("id", self.id) + hg.at("class", self._class)

class a(htmltag):
    def __init__(self, id = "", _class = ""):
        htmltag.__init__(self, id, _class)
        self.href = ""
        self.caption = ""
    def text(self):
        return "<a " + self.idtext() + hg.at("href", self.href) + ">"+ self.caption + "</a>"

class button(htmltag):
    def __init__(self, id = "", _class = ""):
        htmltag.__init__(self, id, _class)
        self.caption = ""
    def text(self):
		return '<button' +  self.idtext() + '>' + self.caption + '</button>'

class input(htmltag):
    def __init__(self, id = "", _class = ""):
        htmltag.__init__(self, id, _class)
	def text(self):
		return '<input' + self.idtext() + '></input>'
		
class registerblock(htmltag):
    def __init__(self, id = "", _class = ""):
        htmltag.__init__(self, id, _class)
        self.items = []
        t = input(id = "UserNameEmail")
        self.items.append(t)
    def text(self):
        r = ""
        for i in self.items:
            r += i.text
        r = hg.wh("", "<div>", self.idtext())
        return r
    
class htmlgn:
    def __init__(self):
        self.items = []
    def gen(self):
		r =  "<!DOCTYPE html><html><head><title>Торгуй - легко!!!</title>"
		r += '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
		r += hg.wh("", "script", hg.at("src", "//code.jquery.com/jquery-1.10.2.min.js"))
		r += "</head><body>"
		r += "Hello word"
		for i in self.items:
			r += i.text();
		r += "</body></html>"
		return r
		
#t = htmlgn()
#print(t.gen())