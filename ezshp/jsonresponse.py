import json

from django.http import HttpResponse
import sys
sys.path.append("cgi")
from django.conf import settings

def index(request):
    response_data = {}
    response_data['result'] = 'failed'
    response_data['message'] = 'You messed up'
    httptext = json.dumps(response_data)
    return HttpResponse(httptext, content_type="application/json")
    #return httptext
    
#print(index("ddd"))