# -*- coding: utf-8 -*-
from django.shortcuts import render
import xml.sax

import ez
import dbconnect

class InkscapeSvgHandler(xml.sax.ContentHandler):
	def __init__(self):
		self.db = dbconnect.dbworker()
		self.sql = u"""INSERT INTO goods (id, shop, caption, unit) VALUES ('{0}', '{1}', '{2}', '{3}')
            ON DUPLICATE KEY UPDATE caption='{2}', unit='{3}';"""
	def startElement(self, name, attrs):
		if name == "root":
			self.shop = attrs["shop"]
		if name == "goods":
			#for (k,v) in attrs.items():
			sql = self.sql.format(attrs["id"], self.shop, attrs["caption"], attrs["unit"])
			self.db.cursor.execute(sql)
			self.db.db.commit()
			pass

def index(request):
	authorities = ez.checkauthorize(request)
	#scripts = ["index.js"]
	context = {"authorities": authorities,
		"location": "myadmin",
		"dbup": "loaded"}
	if ((authorities.have) and (authorities.login == "vgulaev@yandex.ru")):
		parser = xml.sax.make_parser()
		parser.setContentHandler(InkscapeSvgHandler())
		parser.parse(open("d:/forsite.xml","r"))
		return render(request, 'updatedb.html', context)
	else:
		return render(request, 'necessaryauth.html', context)
