from django.conf.urls import patterns, url, include
# from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.urlpatterns import format_suffix_patterns
from newsfeed import views


urlpatterns = patterns('',
	
    url(r'^$', views.index, name='index'),
    url(r'^$', views.base, name='base'),
    url(r'^documentation$', views.documentation, name='documentation'),
    url(r'^auth$', views.auth, name='auth'),
    url(r'^login$', views.login, name='login'),
    url(r'^signup$', views.signup, name='signup'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^new_post$', views.new_post, name='new_post'),
    url(r'^offline$', views.offline, name='offline'),
    url(r'^create_post$', views.create_post, name='create_post'),
    url(r'^login_user$', views.login_user, name='login_user'),
    url(r'^create_user$', views.create_user, name='create_user'),
    url(r'^post/(?P<post_id>\d+)/$', views.single_post, name='single_post'),
    url(r'^post/(?P<post_id>\d+)/$', views.single_tag, name='single_tag'),
    url(r'^tag/(?P<tag_id>\d+)/$', views.single_tag, name='single_tag'),
    url(r'^tags_of_a_post/(?P<post_id>\d+)/$', views.tags_of_a_post, name='tags_of_a_post'),
    url(r'^search$', views.search, name='search'),
    url(r'^suggested$', views.suggested, name='suggested'),
    url(r'^post_tag$', views.post_tag, name='post_tag'),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^posts/$', views.PostList.as_view()),
    url(r'^posts/(?P<pk>[0-9]+)/$', views.PostDetail.as_view()),
    url(r'^tags/$', views.TagList.as_view()),
    url(r'^tags/(?P<pk>[0-9]+)/$', views.TagDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)

#urls for login not sure if needed

#urlpatterns += [
#    url(r'^api-auth/', include('rest_framework.urls',
#                               namespace='rest_framework')),
#]
