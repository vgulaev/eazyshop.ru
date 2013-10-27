#!c:/Python27/python.exe

from secrets import * 
import MySQLdb
print ("Content-Type: text/html; charset=utf-8")
print ("")
print ("Hello word")

db = MySQLdb.connect(host="localhost", user=mysqlusername, passwd=mysqlupsw, db="eazyshop_db", charset='utf8')

cursor = db.cursor()

def checktableexist(tablename):
    sql = """
    SHOW TABLES IN eazyshop_db
    LIKE %s
    """
    cursor.execute(sql, tablename)
    return not cursor.fetchone() is None
    
print(checktableexist("goods"))
    
def creategoodstable():
    sql = """
    DROP TABLE goods
    """
#cursor.execute(sql)

#db.commit()

sql = """
CREATE TABLE goods (
caption CHAR(100)
)
"""
#cursor.execute(sql)
#db.commit()

sql = """
CREATE TABLE pricetype (
caption CHAR(100)
)
"""
#cursor.execute(sql)
#db.commit()

sql = """
SHOW TABLES IN eazyshop_db
LIKE "dfdffer"
"""
cursor.execute(sql)

print(cursor.fetchone())
row = cursor.fetchone()
while row is not None:
    print(row)
    row = cursor.fetchone()
#print(cursor.fetchall())

db.close()