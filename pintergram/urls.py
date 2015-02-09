from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^newsfeed/', include('newsfeed.urls', namespace="newsfeed")),
    url(r'^admin/', include(admin.site.urls)),
)