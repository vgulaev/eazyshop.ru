from django.http import HttpResponse
import htmlgen as hg

def index(request):
    httptext = str(request.COOKIES)
    
    response = HttpResponse(httptext)
    response.set_cookie("user_agreement", "fdsdsjhgfshjdfjkl")
    return response 