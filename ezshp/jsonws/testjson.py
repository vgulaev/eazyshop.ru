from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json
import codecs

def normalizedata(request):
    rawdata = request.read()
    if (rawdata[0:3] == codecs.BOM_UTF8):
        jsondata = json.loads(rawdata[3:])
    else:
        jsondata = request.POST
    return jsondata

@csrf_exempt
def index(request):
    #context_instance=RequestContext(request)
    response_data = {}
    response_data['result'] = 'failed'
    response_data['message'] = 'You messed up'
    
    if request.method == 'POST':
        #httptext = json.dumps(request.POST)
        
        #httptext = request.body
        rawdata = request.read()
        s = rawdata[3:]
        goodsdic = json.loads(s)
        #httptext = json.dumps(goodsdic)
        if (rawdata[0:3] == codecs.BOM_UTF8):
            httptext = "this is BOM"
        else:
            httptext = "this clear UTF" + codecs.BOM
        #httptext = json.dumps(response_data)
        #httptext = request.encoding
        #httptext = str(request)
    else:
        httptext = str(request)
    #httptext = json.dumps(response_data)
    return HttpResponse(httptext, content_type="application/json")