# Create your views here.
from django.http import HttpResponse
import sys
sys.path.append("cgi")
import htmlgen as hg

def index(request):
    t = hg.htmlgn()
    
    httptext = t.gen()
    return HttpResponse(httptext)