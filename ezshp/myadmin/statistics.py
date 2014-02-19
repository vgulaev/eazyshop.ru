# -*- coding: utf-8 -*-
from django.http import HttpResponse
import os

def index(request):
	path = __file__.split("\\")
	rootdir = "\\".join(path[0:-3])
	httptext = ""
	stat = {}
	for root, subFolders, files in os.walk(rootdir):
		for fl in files:
			fileName, fileExtension = os.path.splitext(fl)
			if ((fileExtension in stat) == True):
				stat[fileExtension] = stat[fileExtension] + 1
			else:
				stat[fileExtension] = 0
	for e in stat:
		httptext = httptext + "<br>" + e + " " + str(stat[e])
	return HttpResponse(httptext)