#!/usr/local/bin/python
import cgi
import cgitb; cgitb.enable()

print ("Content-Type: text/html; charset=utf-8")
print ("")

form = cgi.FieldStorage()
print(form)
if form.has_key("dd"):
	print ("Yes I have dd = ", form["dd"].value)
#for el in form:
#    print(el)