#!c:/Python27/python.exe
# -*- coding: utf-8 -*-
from secrets import * 
import MySQLdb
print ("Content-Type: text/html; charset=utf-8")
print ("")
print ("Hello word")

db = MySQLdb.connect(host="localhost", user=mysqlusername, passwd=mysqlupsw, db="c9", charset='utf8')

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
    pricetype CHAR(40),
    good CHAR(40),
    price DECIMAL(8,2),
    
    PRIMARY KEY(pricetype, good),
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

def loadexampledata():
    slq = "INSERT INTO shops (id, caption) VALUES('1', 'МПК')"
    cursor.execute(slq)
    slq = "INSERT INTO pricetypes (id, shop, caption) VALUES ('1', '1', 'Цена1'), ('2', '1', 'Цена2')"
    cursor.execute(slq)
    slq = """
    INSERT INTO goods (id, shop, caption) VALUES ('1', '1', 'Арматура а400/а500'),
     ('2', '1', 'Балка 40Б1'),
     ('3', '1', 'Профнастил НС 50'),
     ('4', '1', 'Колбаса докторская'),
     ('5', '1', 'Yokohama 225x35')
    """
    cursor.execute(slq)
    slq = """
    INSERT INTO prices (pricetype, good, price) VALUES ('1', '1', 23500),
    ('2', '1', 23400),
    ('1', '2', 36000),
    ('2', '2', 35500)
    """
    cursor.execute(slq)
    db.commit()

loadexampledata()

db.close()