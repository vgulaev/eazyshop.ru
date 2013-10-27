#!c:/Python27/python.exe
# -*- coding: utf-8 -*-
# This Python file uses the following encoding: utf-8

from secrets import *
from htmlgenerator import * 
import MySQLdb
from tarfile import version
print ("Content-Type: text/html; charset=utf-8")
print ("")

db = MySQLdb.connect(host="localhost", user=mysqlusername, passwd=mysqlupsw, db="eazyshop_db", charset='utf8')

cursor = db.cursor()

sql = """
SELECT goods.caption, pricetypes.caption, prices.price FROM prices
    LEFT JOIN (goods, pricetypes) ON (prices.good = goods.id AND prices.pricetype = pricetypes.id)
"""
cursor.execute(sql)

rd = u""
row = cursor.fetchone()
#printtablehead(len(row))
while not row is None:
    #print type(str(row[0]))
    rd = rd + wh(u"".join(wh(unicode(e), "tr") for e in row), "td")
    row = cursor.fetchone()

db.close()

rd = wh(wh(rd, "tbody"), "table", 'id = "price-table" cellspacing = "0px"')

print rd.encode("utf8")