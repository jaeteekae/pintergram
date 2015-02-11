from django.conf.urls import patterns, url

from newsfeed import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^create_post$', views.create_post, name='create_post'),
    url(r'^(?P<post_id>\d+)/$', views.single_post, name='single_post'),
)