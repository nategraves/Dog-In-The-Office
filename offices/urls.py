from django.conf.urls.defaults import *

urlpatterns = patterns('offices.views',
    url(r'^add/$', 'add'),
    url(r'^list/$', 'list'),
)
