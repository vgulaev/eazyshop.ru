# -*- coding: utf-8 -*-
import myadmin.dbconnect

class authorities(object):
	def __init__(self, have = False, login = "", ezid = ""):
		self.have = have
		self.login = login
		self.ezid = ezid

def username(ezid):
    db = myadmin.dbconnect.dbworker()
    sql = """SELECT users.login FROM sessions 
			join users on sessions.login = users.id
			where sessions.id = '%s';""" % ezid
    db.cursor.execute(sql)
    userrow =  db.cursor.fetchone()
    if (userrow is None):
    	r = None
    else:
    	r = userrow[0]
    db.cursor.close()
    return r

def  checkauthorize(request):
	ezid = request.COOKIES.get("ezid")
	if (ezid is None):
		r = authorities()
	else:
		r = authorities(True, username(ezid), ezid)
	return r
