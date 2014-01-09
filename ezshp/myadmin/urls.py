from django.conf.urls import patterns, include, url

import main
import debug
import initdb
import updatedb

urlpatterns = patterns('',
    url(r'^$', main.index, name = "index"),
    url(r'debug/', debug.index, name = "debugpage"),
    url(r'initdb/', initdb.index, name = "initdb"),
    url(r'updatedb/', updatedb.index, name = "initdb"),
)
