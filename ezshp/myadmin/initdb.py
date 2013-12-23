#!c:/Python27/python.exe
# -*- coding: utf-8 -*-
import os
import MySQLdb
import secrets
import sqltables
#print ("Content-Type: text/html; charset=utf-8")
#print ("")
#print ("Hello word")
mysql_pass = ""

class dbworker:
    def __init__(self, dbuser):
        self.db = MySQLdb.connect(host = os.environ['IP'], user=dbuser, passwd=mysql_pass, db="c9", charset='utf8')
        self.cursor = self.db.cursor()
    def droptable(self, tablename):
        sql = "DROP TABLE %s" % (tablename)
        self.cursor.execute(sql)
        self.db.commit()
    def dropalltable(self):
        names = ["prices", "pricetypes", "goods", "users", "shops"]
        for e in names:
            if self.checktableexist(e):
                self.droptable(e)
    def checktableexist(self, tablename):
        sql = """
        SHOW TABLES IN c9
        LIKE %s
        """
        self.cursor.execute(sql, tablename)
        return not self.cursor.fetchone() is None
    def loadexampledata(self):
        slq = "INSERT INTO shops (id, caption) VALUES('1', 'МПК')"
        self.cursor.execute(slq)
        slq = "INSERT INTO pricetypes (id, shop, caption) VALUES ('1', '1', 'Цена1'), ('2', '1', 'Цена2')"
        self.cursor.execute(slq)
        slq = """
        INSERT INTO goods (id, shop, caption) VALUES ('1', '1', 'Арматура а400/а500'),
        ('2', '1', 'Балка 40Б1'),
        ('3', '1', 'Профнастил НС 50'),
        ('4', '1', 'Колбаса докторская'),
        ('5', '1', 'Yokohama 225x35')
        """
        self.cursor.execute(slq)
        slq = """
        INSERT INTO prices (pricetype, good, price) VALUES ('1', '1', 23500),
        ('2', '1', 23400),
        ('1', '2', 36000),
        ('2', '2', 35500)
        """
        self.cursor.execute(slq)
        self.db.commit()
    def createtables(self):
        for e in sqltables.sqlqueryes:
            self.cursor.execute(e)
            self.db.commit()
    def doinitdb(self):
        self.dropalltable()
        #self.createshopstable()
        #self.creategoodstable()
        #self.createpricetypestable()
        #self.createpricestable()
        self.createtables()
        self.loadexampledata()
        self.db.close()
    
from django.http import HttpResponse
import htmlgen as hg

def loadmysqlcredential():
    global mysql_pass
    if (os.environ.get('C9_USER') == None):
        os.environ['C9_USER'] = "root"
        mysql_pass = secrets.mysql_pass
    if (os.environ.get('IP') == None):
        os.environ['IP'] = "localhost"

#loadmysqlcredential()
#print("*********=", mysql_pass)
#d = dbworker(dbuser="root")
#d.doinitdb()
#print("Verry Good!!!")

def index(request):
    loadmysqlcredential()
    d = dbworker(dbuser=os.environ['C9_USER'])
    d.doinitdb()
    t = hg.htmlgn(request)
    t.setjsrootname(request.path)
    t.append(hg.htmltext("Initialization complete!!!"))

    httptext = t.gen()
    return HttpResponse(httptext)