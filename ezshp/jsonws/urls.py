from django.conf.urls import patterns, include, url

import testjson

urlpatterns = patterns('',
    url(r'testjson/', testjson.index, name = "testjson"),
)
