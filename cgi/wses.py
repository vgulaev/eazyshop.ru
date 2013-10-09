#!/usr/local/bin/python
import cgi
import cgitb; cgitb.enable()
import os

#======================================================
#This is webservise for eazyshop. It doing somethink
#

print ("Content-Type: text/html; charset=utf-8")
print ("")

form = cgi.FieldStorage()
# o - mean "operation", cut the value name for smaller http request
if form.has_key("o"):
	# cn - mean "check name"
	if (form["o"].value == "cn"):
		if (os.path.isdir("/home/eazyshop/eazyshop.ru/doc/" + form["n"].value)):
			print("exist")
		else:
			print ("free")