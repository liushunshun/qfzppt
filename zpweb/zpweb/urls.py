from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from zp.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MySiteWithPython.views.home', name='home'),
    # url(r'^MySiteWithPython/', include('MySiteWithPython.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	#����
    url(r'^resume/$', 'resume.views.resume'),
	#ע��
    url(r'^register/$','zp.views.register'),
	#��¼
    url(r'^login/$','zp.views.login'),
	#��ҳ
    url(r'^','zp.views.login'),
)