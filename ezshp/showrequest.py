import json

from django.http import HttpResponse
import sys
from django.conf import settings

def index(request):
    httptext = json.dumps(request.COOKIES)
    return HttpResponse(httptext, content_type="text/plain")