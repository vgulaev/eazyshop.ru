from django.conf.urls import patterns, include, url

import main
import debug
import initdb
import updatedb
import xmltodb
import db1c
import statistics

urlpatterns = patterns('',
    url(r'^$', main.index, name = "index"),
    url(r'debug/', debug.index, name = "debugpage"),
    url(r'initdb/', initdb.index, name = "initdb"),
    url(r'updatedb/', updatedb.index, name = "initdb"),
    url(r'xmltodb/', xmltodb.index, name = "xmltodb"),
    url(r'db1c_create/', updatedb.db1c_create, name = "updatedb.db1c_create"),
	url(r'statistics/', statistics.index, name = "updatedb.db1c_create"),
)
