#!c:/Python27/python.exe

from secrets import * 
import MySQLdb
print ("Content-Type: text/html; charset=utf-8")
print ("")
print ("Hello word")

db = MySQLdb.connect(host="localhost", user=mysqlusername, passwd=mysqlupsw, db="eazyshop_db", charset='utf8')

cursor = db.cursor()

def droptable(tablename):
    sql = "DROP TABLE %s" % (tablename)
    cursor.execute(sql)
    db.commit()

def dropalltable():
    names = ["prices", "pricetypes", "goods"]
    for e in names:
        if checktableexist(e):
            droptable(e)
    
def checktableexist(tablename):
    sql = """
    SHOW TABLES IN eazyshop_db
    LIKE %s
    """
    cursor.execute(sql, tablename)
    return not cursor.fetchone() is None
    
def creategoodstable():
    if checktableexist("goods"):
        droptable("goods")
    sql = """
    CREATE TABLE goods (
    id CHAR(40) PRIMARY KEY,
    caption CHAR(100)
    ) ENGINE=INNODB;
    """
    cursor.execute(sql)
    db.commit()

def createpricetypestable():
    if checktableexist("pricetypes"):
        droptable("pricetypes")
    sql = """
    CREATE TABLE goods (
    id CHAR(40) PRIMARY KEY,
    caption CHAR(100)
    ) ENGINE=INNODB;
    """
    cursor.execute(sql)
    db.commit()

def createpricestable():
    if checktableexist("prices"):
        droptable("prices")
    sql = """
    CREATE TABLE prices (
    id INTEGER PRIMARY KEY,
    good CHAR(40),
    price DECIMAL(8,2),
    
    FOREIGN KEY (good)
        REFERENCES goods(id)    
    ) ENGINE=INNODB;
    """
    cursor.execute(sql)
    db.commit()

dropalltable()
creategoodstable()
createpricestable()
db.close()