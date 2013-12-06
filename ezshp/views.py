# Create your views here.
from django.http import HttpResponse


def index(request):
    httptext = """
<!DOCTYPE html>
<html><head>
</head><body>
<button>Press me</button>
</body></html>
"""
    return HttpResponse(httptext)