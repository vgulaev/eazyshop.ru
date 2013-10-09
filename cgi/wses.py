#!/usr/local/bin/python
#
#This is webservise for eazyshop. It doing somethink
#
import cgi
import cgitb; cgitb.enable()

print ("Content-Type: text/html; charset=utf-8")
print ("")

form = cgi.FieldStorage()
#print(form)
# o - mean "operation", cut the value name for smaller http request
if form.has_key("o"):
	if form["0"].value
	print ("Yes I have dd = ", form["dd"].value)
#for el in form:
#    print(el)