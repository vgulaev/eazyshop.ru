from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()
import os
import sys
sys.path.append(settings.SITE_ROOT + "/ezshp")

import views
import jsonresponse
import showrequest
#import myadmin.main
import myadmin.urls
import principles
import registration
import jsonws.urls

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.index, name='index'),
    url(r'^json/$', jsonresponse.index, name='index'),
    url(r'^sr/$', showrequest.index, name='index'),
    url(r'^principles/', principles.index, name = 'principles'),
    url(r'^registration/', registration.index, name = 'registration'),
    url(r'^myadmin/', include(myadmin.urls)),
    url(r'^jsonws/', include(jsonws.urls)),
    #url(r'^myadmin/', myadmin.main.index, name = 'index'),
    # url(r'^$', 'ezshp.views.home', name='home'),
    # url(r'^ezshp/', include('ezshp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
