from django.conf.urls import patterns, url

from newsfeed import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^$', views.base, name='base'),
    url(r'^new_post$', views.new_post, name='new_post'),
    url(r'^create_post$', views.create_post, name='create_post'),
    url(r'^(?P<post_id>\d+)/$', views.single_post, name='single_post'),
    url(r'^(?P<tag_id>\d+)/$', views.tag, name='tag'),
)