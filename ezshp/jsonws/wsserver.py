# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json
import sendacceptedmail

@csrf_exempt
def index(request):
    #context_instance=RequestContext(request)
    #response_data = {}
    #response_data['result'] = 'failed'
    #response_data['message'] = 'You messed up'
    ans = {}
    if request.method == 'POST':
        if (request.POST["method"] == "sendacceptedmail"):
            ans = sendacceptedmail.send(request.POST)
        elif (request.POST["method"] == "addaccount"):
            ans = addaccount(request.POST)
        httptext = json.dumps(ans)
        #httptext = str(request)
    else:
        httptext = str(request)
    #httptext = json.dumps(response_data)
    return HttpResponse(httptext, content_type="application/json")