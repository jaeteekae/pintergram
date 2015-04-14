from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponseRedirect

#http://www.kelvinwong.ca/tag/media_root/ ^
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    url(r'^$', lambda r: HttpResponseRedirect('newsfeed/login')),
    url(r'^newsfeed/', include('newsfeed.urls', namespace="newsfeed")),
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
