# Create your views here.
from django.http import HttpResponse
from django.conf import settings
import htmlgen as hg

def index(request):
    t = hg.htmlgn()
    
    a = hg.a()
    a.id = "sa"
    #a.caption = str(settings.STATICFILES_DIRS)
    a.caption = "Not bad"
    a.href = "/json/"
    t.items.append(a)
    
    a = hg.a(id = "sb")
    a.caption = "Show request"
    a.href = "/sr/"
    t.items.append(a)

    b = hg.button(id = "sb1")
    b.caption = "Press me!"
    t.items.append(b)
    
    b = hg.button(id = "sb2")
    b.caption = "Check me!"
    t.items.append(b)

    httptext = t.gen()
    return HttpResponse(httptext)
    #return httptext
    
#print(index("ddd"))