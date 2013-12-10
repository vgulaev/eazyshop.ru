from django.http import HttpResponse
import htmlgen as hg

def index(request):
    t = hg.htmlgn()
    t.append(hg.htmltext("Admin page<br>"))
    
    e = hg.htmlevent()
    e.name = "onclick"
    e.function = "SayHello()"
    e.text = """function SayHello(){
        alert("Hello!");
    }
"""
    
    a = hg.a(id = "initdb")
    a.href = "/admin/initdb"
    a.caption = "Init DB"
    a.events.append(e)
    t.append(a)
    httptext = t.gen()
    return HttpResponse(httptext)