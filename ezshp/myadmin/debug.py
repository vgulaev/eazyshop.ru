from django.http import HttpResponse
import htmlgen as hg

def index(request):
    #httptext = str(request.COOKIES)
    #httptext = str(request.path)
    t = hg.htmlgn()
    t.setjsrootname(request.path)
    httptext = t.jsrootname
    response = HttpResponse(httptext)
    response.set_cookie("user_agreement", "fdsdsjhgfshjdfjkl")
    return response 