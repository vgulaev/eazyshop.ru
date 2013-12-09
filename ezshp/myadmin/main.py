from django.http import HttpResponse
import htmlgen as hg

def index(request):
    t = hg.htmlgn()
    t.append(hg.htmltext("Admin page"))
    a = hg.a(id = "initdb")
    a.href = "/initdb"
    t.append(a)
    httptext = t.gen()
    return HttpResponse(httptext)