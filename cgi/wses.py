#!/usr/local/bin/python
import cgi
import cgitb; cgitb.enable()
import os
import shutil

#======================================================
#This is webservise for eazyshop. It doing somethink
#

print ("Content-Type: text/html; charset=utf-8")
print ("")

def createnewshop(shopname):
	pt = "/home/eazyshop/eazyshop.ru/docs/" + shopname
	if (os.path.isdir(pt)):
		print("already exist")
		return None
	os.makedirs(pt)
	print("complete")

form = cgi.FieldStorage()
# o - mean "operation", cut the value name for smaller http request
if form.has_key("o"):
	# cn - mean "check name"
	operation = form["o"].value 
	if (operation == "cn"):
		if (os.path.isdir("/home/eazyshop/eazyshop.ru/docs/" + form["n"].value)):
			print ("exist")
		else:
			print ("free")
	# c - mean "create"
	elif (operation == "c"):
		print (createnewshop(form["n"].value))
	# d - mean "delete shop"
	elif (operation == "d"):
		shutil.rmtree("/home/eazyshop/eazyshop.ru/docs/" + form["n"].value)
		print ("complete")		