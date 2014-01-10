from django.shortcuts import render
import ez

def index(request):
    authorities = ez.checkauthorize(request)
    #scripts = ["index.js"]
    context = {"authorities": authorities,
    			"location": "myadmin"}
    if (authorities.have):
        return render(request, 'myadmin.html', context)
    else:
        return render(request, 'necessaryauth.html', context)