from django.conf.urls import patterns, url

from newsfeed import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^newsfeed$', views.newsfeed, name='newsfeed'),
    url(r'^(?P<post_id>\d+)/$', views.single_post, name='single_post'),
)