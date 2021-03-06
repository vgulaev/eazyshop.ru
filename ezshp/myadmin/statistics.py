# -*- coding: utf-8 -*-
from django.http import HttpResponse
import os
import platform

def index(request):
	if (platform.system() == "Windows"):
		dirsym = "\\"
	else:
		dirsym = "/"
	path = __file__.split(dirsym)
	rootdir = dirsym.join(path[0:-3])

	httptext = """<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.0.3/css/bootstrap.min.css">
<link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.0.3/css/bootstrap-theme.min.css">
</head>
<body>
	"""
	#stat = {}
	stat = {".css" : {}, ".js" : {}, ".django" : {}, ".py" : {}, ".html" : {}}
	for e in stat:
		stat[e] = {"items" : 0, "lines" : 0}
	totallines = 0
	for root, subFolders, files in os.walk(rootdir):
		for fl in files:
			fileName, fileExtension = os.path.splitext(fl)
			
			f = open(root + dirsym + fl)
			if ((fileExtension in stat) == True):
				stat[fileExtension]["items"] = stat[fileExtension]["items"] + 1
				lines = len(f.readlines())
				stat[fileExtension]["lines"] = stat[fileExtension]["lines"] + lines
				totallines = totallines + lines
			#else:
			#	stat[fileExtension] = {"items" : 1, "lines" : len(f.readlines())}
			f.close()			
	for e in stat:
		httptext += "<br>" + e + " " + str(stat[e]["items"]) + " lines " + str(stat[e]["lines"])
	httptext += "<br>" + "Total lines: " + str(totallines) + " cost: "+ str(totallines * 12) + " $"
	httptext += "</body></html>"
	return HttpResponse(httptext)