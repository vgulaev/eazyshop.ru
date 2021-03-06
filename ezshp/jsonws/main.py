from django.http import HttpResponse
import htmlgen as hg

def index(request):
    t = hg.htmlgn(request)
    t.setjsrootname(request.path)

    n = hg.navigationblock()
    t.append(n)
    t.append(hg.htmltext("<br>"))    

    t.append(hg.htmltext("Admin page<br>"))
    
    e = hg.htmlevent()
    e.name = "onclick"
    e.function = "SayHello()"
    e.text = """function SayHello(){
        alert("Hello!");
    }
"""
    
    a = hg.a(id = "initdb")
    a.href = "/myadmin/initdb"
    a.caption = "Init DB"
    a.events.append(e)
    t.append(a)
    t.append(hg.htmltext("<br>"))

    a = hg.a(id = "debug")
    a.href = "/myadmin/debug"
    a.caption = "Debuging page"
    t.append(a)
    t.append(hg.htmltext("<br>"))

    a = hg.a(id = "sa")
    a.caption = "JSON Example"
    a.href = "/json/"
    t.append(a)
    t.append(hg.htmltext("<br>"))

    a = hg.a(id = "sb")
    a.caption = "Show request"
    a.href = "/sr/"
    t.append(a)

    httptext = t.gen()
    return HttpResponse(httptext)