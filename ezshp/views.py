# Create your views here.
from django.http import HttpResponse
import sys
sys.path.append("cgi")
import htmlgen as hg

def index(request):
    t = hg.htmlgn()
    
    a = hg.a()
    a.id = "sa"
    a.caption = "Reprezent json"
    a.href = "/json/"
    t.items.append(a)
    
    a = hg.a()
    a.id = "sb"
    a.caption = "Show request"
    a.href = "/sr/"
    t.items.append(a)

    b = hg.button()
    b.id = "sb1"
    b.caption = "Press me!"
    t.items.append(b)
    
    b = hg.button()
    b.id = "sb2"
    b.caption = "Check me!"
    t.items.append(b)

    httptext = t.gen()
    return HttpResponse(httptext)
    #return httptext
    
#print(index("ddd"))