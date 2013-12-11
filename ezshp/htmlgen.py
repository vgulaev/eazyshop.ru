# -*- coding: utf-8 -*-
import htmlgenerator as hg
from django.conf import settings

class htmlevent:
    def __init__(self):
        name = ""
        function = ""
        text = ""

class htmltag:
    def __init__(self, id = "", _class = ""):
        self.id = id
        self._class = _class
        self.events = []
    def idtext(self):
	    return hg.at("id", self.id) + hg.at("class", self._class)
    def evtext(self):
        r = ""
        for e in self.events:
            r += e.name + " = " + '"' + e.function + '"'
        return r

class htmltext(htmltag):
    def __init__(self, content = ""):
        htmltag.__init__(self)
        self.content = content
    def text(self):
        return self.content

class a(htmltag):
    def __init__(self, id = "", _class = ""):
        htmltag.__init__(self, id, _class)
        self.href = ""
        self.caption = ""
    def text(self):
        return "<a " + self.idtext() + hg.at("href", self.href) + self.evtext() +">"+ self.caption + "</a>"

class button(htmltag):
    def __init__(self, id = "", _class = ""):
        htmltag.__init__(self, id, _class)
        self.caption = ""
    def text(self):
		return '<button' +  self.idtext() + '>' + self.caption + '</button>'

class input(htmltag):
    def __init__(self, id = "", _class = ""):
        htmltag.__init__(self, id, _class)
        self.placeholder = ""
    def text(self):
        return '<input' + self.idtext() + hg.at("placeholder", self.placeholder) + '></input>'
		
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
        self.scripts = []
        self.jsrootname = ""
        self.jsmain = ""
    def setjsrootname(self, path):
        self.jsrootname = path[1:].replace("/", "-")
    def append(self, htmlel):
        self.items.append(htmlel)
    def generatejsfiles(self):
        filename =  "/static/js/" + str(self.jsrootname) + "first.js"
        #filename =  "/static/js/" + "myadmin-debug-" + "first.js"
        self.scripts.append(filename)
        f = open(settings.SITE_ROOT + filename, "w+")
        for t in self.items:
            for e in t.events:
                f.write(e.text)
        f.close()
        filename =  "/static/js/" + str(self.jsrootname) + "main.js"
        self.scripts.append(filename)
        f = open(settings.SITE_ROOT + filename, "w+")
        f.write(self.jsmain)
        f.close()
    def gen(self):
        self.generatejsfiles()
        r =  "<!DOCTYPE html><html><head><title>Торгуй - легко!!!</title>"
        r += '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
        r += hg.wh("", "link", hg.at("src", "//code.jquery.com/ui/1.10.3/themes/smoothness/jquery-ui.css"))
        r += hg.wh("", "script", hg.at("src", "//code.jquery.com/jquery-1.9.1.js"))
        r += hg.wh("", "script", hg.at("src", "//code.jquery.com/ui/1.10.3/jquery-ui.js"))
        for s in self.scripts:
            r += hg.wh("", "script", hg.at("src", s))
        r += "</head><body>"
		#r += "Hello word"
        for i in self.items:
            r += i.text();
        r += "</body></html>"
        return r
		
#t = htmlgn()
#print(t.gen())