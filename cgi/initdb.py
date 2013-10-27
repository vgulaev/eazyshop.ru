#!c:/Python27/python.exe

import MySQLdb
print ("Content-Type: text/html; charset=utf-8")
print ("")
print ("Hello word")

db = MySQLdb.connect(host="localhost", user="root", passwd="mysql", db="eazyshop_db", charset='utf8')

cursor = db.cursor()

sql = """
CREATE TABLE goods (
caption CHAR(100)
)
"""

cursor.execute(sql)

db.commit()

db.close()