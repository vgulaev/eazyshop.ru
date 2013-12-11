from django.http import HttpResponse
import htmlgen as hg

def index(request):
    #httptext = str(request.COOKIES)
    #httptext = str(request.path)
    t = hg.htmlgn(request)
    #t.setjsrootname(request.path)
    #httptext = str(request)
    httptext = str(t.ismobile)
    response = HttpResponse(httptext, content_type="application/json")
    #response.set_cookie("user_agreement", "fdsdsjhgfshjdfjkl")
    return response 