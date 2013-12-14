import json

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

@csrf_exempt
def index(request):
    response_data = {}
    response_data['result'] = 'failed'
    response_data['message'] = 'You messed up'
    httptext = json.dumps(response_data)
    return HttpResponse(httptext, content_type="application/json")
    #return httptext
    
#print(index("ddd"))