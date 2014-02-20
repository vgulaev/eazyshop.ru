# -*- coding: utf-8 -*-
import myadmin.dbconnect

class authorities(object):
	def __init__(self, have = False, login = "", uid = "", ezid = "", uid1c = ""):
		self.have = have
		self.login = login
		self.uid = uid
		self.ezid = ezid
		self.uid1c = uid1c

def username(ezid):
    db = myadmin.dbconnect.dbworker()
    sql = """SELECT users.login, users.id, users.uid1c FROM sessions 
			join users on sessions.login = users.id
			where sessions.id = '%s';""" % ezid
    db.cursor.execute(sql)
    userrow =  db.cursor.fetchone()
    if (userrow is None):
    	r = None
    else:
    	r = userrow
    db.cursor.close()
    return {"login" : r[0], "uid" : r[1], "uid1c" : r[2]}

def  checkauthorize(request):
	ezid = request.COOKIES.get("ezid")
	if (ezid is None):
		r = authorities()
	else:
		un = username(ezid)
		r = authorities(True, un["login"], un["uid"], ezid, un["uid1c"])
	return r
