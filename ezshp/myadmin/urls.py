from django.conf.urls import patterns, include, url

import main
import debug
import initdb

urlpatterns = patterns('',
    url(r'^$', main.index, name = "index"),
    url(r'debug/', debug.index, name = "debugpage"),
    url(r'initdb/', initdb.index, name = "initdb"),
)
