# -*- coding: utf-8 -*-
import documents.innerorder.main
import myadmin.dbconnect

class db1c(object):
	"""docstring for db1c"""
	def __init__(self):
		#super(db1c, self).__init__()
		#self.arg = arg
		self.db = myadmin.dbconnect.dbworker()
	def create_tables(self):
		self.db.droptable("innerorder_goods")
		self.db.droptable("innerorder")
		for q in documents.innerorder.main.sql_query_for_create_table:
			self.db.cursor.execute(q)
			self.db.db.commit()