from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()
import os
import sys
sys.path.append(settings.SITE_ROOT + "/ezshp")
sys.path.append(settings.SITE_ROOT + "/cgi")

import views
import lk
import jsonresponse
import showrequest
#import myadmin.main
import myadmin.urls
import principles
import registration
import jsonws.urls
import htmlws.urls
import gchoice
import db1c.route1cws
import db1c.routesql

urlpatterns = patterns('',
    # Index page
    url(r'^$', views.index, name='home'),
    url(r'^lk/$', lk.index, name='lk'),
    url(r'^choice/$', gchoice.index, name='choice'),
    url(r'^orderlist/$', views.orderlist, name='choice'),
    url(r'^ws/restservice.1cws', db1c.route1cws.route, name='ws'),
    url(r'^ws/restservice.wsdl', db1c.route1cws.routewsdl, name='ws'),
    url(r'^sql.connect', db1c.routesql.route, name='ws'),
    url(r'^innerorder/(?P<uid>[-\w]+)', views.innerorder, name = 'registration'),
    # For ajax and other json servises
    url(r'^jsonws/', include(jsonws.urls)),
    # For ajax and other json servises
    url(r'^htmlws/', include(htmlws.urls)),
    #Admin page
    url(r'^myadmin/', include(myadmin.urls)),
    #Who we are
    url(r'^who-we-are/', principles.who_we_are, name = 'who-we-are'),
    #Our princeples
    url(r'^principles/', principles.index, name = 'principles'),
    #Welcome page
    url(r'^welcome/', principles.welcome, name = 'welcome'),
    #Bussines logic
    #registration page
    url(r'^registration/', registration.index, name = 'registration'),
    #aceptedpage
    url(r'^accept/(?P<uid>\w+)', registration.accept, name = 'registration'),
    #End bussines logic
    ########################################
    #####For fun
    ########################################
    url(r'^demohtml/$', views.demo, name='demo'),
    url(r'^jsontester/$', views.jsontester, name='demo'),
    url(r'^json/$', jsonresponse.index, name='index'),
    url(r'^sr/$', showrequest.index, name='index'),
    url(r'^readme.txt', registration.index, name = 'registration'),
    # url(r'^$', 'ezshp.views.home', name='home'),
    # url(r'^ezshp/', include('ezshp.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
