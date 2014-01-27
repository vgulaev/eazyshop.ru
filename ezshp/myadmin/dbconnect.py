# -*- coding: utf-8 -*-
import os
import MySQLdb
import secrets
import sqltables
import socket

def loadmysqlcredential():
    passwd = ""
    if (os.environ.get('C9_USER') == None):
        os.environ['C9_USER'] = "root"
        mysql_pass = secrets.mysql_pass
    if (os.environ.get('IP') == None):
        os.environ['IP'] = "localhost"
    if (socket.gethostname() == "eazyshop.ru"):
        os.environ['C9_USER'] = "root"
        os.environ['IP'] = "localhost"
        passwd = secrets.mysql_pass
    r = {   "host" : os.environ['IP'],
            "user" : os.environ['C9_USER'],
            "passwd" : passwd}
    return r

class dbworker:
    def __init__(self):
        cred = loadmysqlcredential()
        self.db = MySQLdb.connect(host = cred["host"], user = cred["user"], passwd = cred["passwd"], db = "c9", charset = 'utf8')
        self.cursor = self.db.cursor()
    def droptable(self, tablename):
        sql = "DROP TABLE %s" % (tablename)
        self.cursor.execute(sql)
        self.db.commit()
    def dropalltable(self):
        names = ["prices", "pricetypes", "goods", "sessions","users", "shops"]
        for e in names:
            if self.checktableexist(e):
                self.droptable(e)
    def checktableexist(self, tablename):
        sql = u"""
        SHOW TABLES IN c9
        LIKE '{0}'
        """.format(tablename)
        self.cursor.execute(sql)
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