# Create your views here.
from django.http import HttpResponse
from django.conf import settings
import htmlgen as hg

def index(request):
    t = hg.htmlgn()
    
    a = hg.a(id = "reftoadmin")
    a.caption = "Admin page"
    a.href = "/myadmin/"
    t.append(a)
    t.append(hg.htmltext("<br>"))    

    a = hg.a(id = "sa")
    a.caption = "Not bad"
    a.href = "/json/"
    t.append(a)
    t.append(hg.htmltext("<br>"))

    a = hg.a(id = "sb")
    a.caption = "Show request"
    a.href = "/sr/"
    t.append(a)

    b = hg.button(id = "sb1")
    b.caption = "Press me!"
    t.append(b)
    
    b = hg.button(id = "sb2")
    b.caption = "Check me!"
    t.append(b)

    httptext = t.gen()
    return HttpResponse(httptext)
    #return httptext
    
#print(index("ddd"))