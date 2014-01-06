from django.conf.urls import patterns, include, url

import pricetable

urlpatterns = patterns('',
    url(r'pricetable/', pricetable.index, name = "testjson"),
)
