from django.http import HttpResponse
import htmlgen as hg

def index(request):
    t = hg.htmlgn()
    t.append(hg.htmltext("Admin page<br>"))
    a = hg.a(id = "initdb")
    a.href = "/admin/initdb"
    a.caption = "Init DB"
    t.append(a)
    httptext = t.gen()
    return HttpResponse(httptext)