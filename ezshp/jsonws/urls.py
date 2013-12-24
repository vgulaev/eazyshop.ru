from django.conf.urls import patterns, include, url

import testjson
import registermail
import wsserver

urlpatterns = patterns('',
    url(r'testjson/', testjson.index, name = "testjson"),
    url(r'registermail/', registermail.index, name = "registermail"),
    url(r'ws/', wsserver.index, name = "registermail"),
)
