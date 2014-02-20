# -*- coding: utf-8 -*-
from django.http import HttpResponse
import os

def index(request):
	path = __file__.split("\\")
	rootdir = "\\".join(path[0:-3])
	httptext = ""
	#stat = {}
	stat = {".css" : {}, ".js" : {}, ".django" : {}, ".py" : {}, ".html" : {}}
	for e in stat:
		stat[e] = {"items" : 0, "lines" : 0}
	totallines = 0
	for root, subFolders, files in os.walk(rootdir):
		for fl in files:
			fileName, fileExtension = os.path.splitext(fl)
			f = open(root + "\\" + fl)
			if ((fileExtension in stat) == True):
				stat[fileExtension]["items"] = stat[fileExtension]["items"] + 1
				lines = len(f.readlines())
				stat[fileExtension]["lines"] = stat[fileExtension]["lines"] + lines
				totallines = totallines + lines
			#else:
			#	stat[fileExtension] = {"items" : 1, "lines" : len(f.readlines())}
			f.close()			
	for e in stat:
		httptext = httptext + "<br>" + e + " " + str(stat[e]["items"]) + " lines " + str(stat[e]["lines"])
	httptext = httptext + "<br>" + "Total lines: " + str(totallines) + " cost: "+ str(totallines * 12) + " $"
	return HttpResponse(httptext)