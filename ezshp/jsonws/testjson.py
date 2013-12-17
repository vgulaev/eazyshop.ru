from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json

@csrf_exempt
def index(request):
    #context_instance=RequestContext(request)
    response_data = {}
    response_data['result'] = 'failed'
    response_data['message'] = 'You messed up'
    
    if request.method == 'POST':
        #httptext = json.dumps(request.POST)
        httptext = str(request)
    else:
        httptext = json.dumps(response_data)
    #httptext = json.dumps(response_data)
    return HttpResponse(httptext, content_type="application/json")