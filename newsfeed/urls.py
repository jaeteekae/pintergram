from django.conf.urls import patterns, url, include
# from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.urlpatterns import format_suffix_patterns
from newsfeed import views


urlpatterns = patterns('',
	
    url(r'^$', views.index, name='index'),
    url(r'^$', views.base, name='base'),
    url(r'^documentation$', views.documentation, name='documentation'),
    url(r'^new_post$', views.new_post, name='new_post'),
    url(r'^offline$', views.offline, name='offline'),
    url(r'^create_post$', views.create_post, name='create_post'),
    url(r'^post/(?P<post_id>\d+)/$', views.single_post, name='single_post'),
    url(r'^(?P<tag_id>\d+)/$', views.tag, name='tag'),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^posts/$', views.PostList.as_view()),
    url(r'^posts/(?P<pk>[0-9]+)/$', views.PostDetail.as_view()),
    url(r'^tags/$', views.TagList.as_view()),
    url(r'^tags/(?P<pk>[0-9]+)/$', views.TagDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)
