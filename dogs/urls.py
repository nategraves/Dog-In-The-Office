from django.conf.urls.defaults import *

urlpatterns = patterns('dogs.views',
    url(r'^add/$', 'add'),
    url(r'^list/(?P<office>\d+)/$', 'list'),
    url(r'^view/(?P<dog>\d+)/$', 'view'),
)
