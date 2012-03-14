from django.conf import settings
from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
        url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
        url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^dogs/', include('dogs.urls')),
	url(r'^offices/', include('offices.urls')),
	url(r'^$', include('index.urls')),	
)

import os
from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': os.path.join(os.path.dirname(__file__), 'static')}),
    )
