from django.conf.urls import patterns, include, url
from django.http import HttpResponseRedirect

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mekavita_hu.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', lambda r : HttpResponseRedirect('blog/')),
    url(r'^blog/', include('blog.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
#    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
