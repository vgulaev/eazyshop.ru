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
    names = ["prices", "pricetypes", "goods", "shops"]
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
    
def createshopstable():
    sql = """
    CREATE TABLE shops (
    id CHAR(40) PRIMARY KEY,
    caption CHAR(100)
    ) ENGINE=INNODB CHARACTER SET utf8 COLLATE utf8_bin;
    """
    cursor.execute(sql)
    db.commit()

def creategoodstable():
    sql = """
    CREATE TABLE goods (
    id CHAR(40) PRIMARY KEY,
    shop CHAR(40),
    caption CHAR(100),
    
    FOREIGN KEY (shop) REFERENCES shops(id)
    ) ENGINE=INNODB CHARACTER SET utf8 COLLATE utf8_bin;
    """
    cursor.execute(sql)
    db.commit()

def createpricetypestable():
    sql = """
    CREATE TABLE pricetypes (
    id CHAR(40) PRIMARY KEY,
    shop CHAR(40),
    caption CHAR(100),
    
    FOREIGN KEY (shop) REFERENCES shops(id)
    ) ENGINE=INNODB CHARACTER SET utf8 COLLATE utf8_bin;
    """
    cursor.execute(sql)
    db.commit()

def createpricestable():
    sql = """
    CREATE TABLE prices (
    id INTEGER PRIMARY KEY,
    pricetype CHAR(40),
    good CHAR(40),
    price DECIMAL(8,2),
    
    FOREIGN KEY (good) REFERENCES goods(id),
    FOREIGN KEY (pricetype) REFERENCES pricetypes(id)
    ) ENGINE=INNODB CHARACTER SET utf8 COLLATE utf8_bin;
    """
    cursor.execute(sql)
    db.commit()

dropalltable()
createshopstable()
creategoodstable()
createpricetypestable()
createpricestable()
db.close()