from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets

# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser


from newsfeed.serializers import UserSerializer, UserSerializerPut, PostSerializer, PostSerializerPut, TagSerializer, TagSerializerPut
from newsfeed.models import Post, Tag, Follower, Upvote, Preferences

from rest_framework import status
from rest_framework.decorators import api_view
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.models import User

from newsfeed.serializers import UserSerializer
from rest_framework import generics

# for auth

from rest_framework import permissions
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.hashers import make_password

# @cache_page(60 * 1)
def index(request):
    # latest_post_list = Post.objects.order_by('-timestamp')
    # tag_list = []
    # for post in latest_post_list:
    #     tag_group = Tag.objects.filter(post_id=post)
    #     tag_list.append(tag_group)
    # zipped_lists = zip(latest_post_list, tag_list)
    # context = {'zipped_lists': zipped_lists, 'latest_post_list': latest_post_list, 'test_user': request.owner.username}
    return render(request, 'newsfeed/index.html', {'self_un': request.user})

def new_post(request):
    return render(request, 'newsfeed/new_post.html')

def base(request):
    return render(request, 'newsfeed/base.html')


def offline(request):
    return render(request, 'newsfeed/offline.html')

def login(request):

    return render(request, 'newsfeed/login.html')

def signup(request):
    return render(request, 'newsfeed/signup.html')


    if request.method == 'GET':
        return render(request, 'newsfeed/login.html')

def login_user(request):
    if not request.POST['username']:
        return HttpResponseRedirect('/newsfeed/login')
    elif not request.POST['password']:
        return HttpResponseRedirect('/newsfeed/login')
    else:
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect('/newsfeed')
            else:
                return HttpResponseRedirect('/newsfeed/login')
        else:
            return HttpResponseRedirect('/newsfeed/login')

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/newsfeed/login')

def create_user(request):
    if request.method == 'GET':
        return render(request, 'newsfeed/create_user.html')
    elif request.method == 'POST':
        new_user = User(username=request.POST['username'],
                        first_name=request.POST['first_name'],
                        last_name=request.POST['last_name'],
                        email=request.POST['email'],
                        password=make_password(request.POST['password']),
                        is_staff=False,
                        is_active=True,
                        is_superuser=False)
        new_user.save()
        return HttpResponseRedirect('/newsfeed/login')


def create_post(request):
    try:
        image = request.POST['post-image']
    except MultiValueDictKeyError:
        image = None

    if not request.POST['post_title']:
        return HttpResponseRedirect('/newsfeed')
        # return HttpResponseRedirect('new_post')
    elif not request.POST['post_text'] and not image:
        return HttpResponseRedirect('/newsfeed')
        # return HttpResponseRedirect('new_post')
    else:
        new_post = Post(post_text=request.POST['post_text'], 
                        post_title=request.POST['post_title'], 
                        timestamp=timezone.now(), 
                        owner=request.user)
        if image:
            new_post.image_path = request.FILES['post-image']
        else:
            new_post.image_path = image
        new_post.save()
        tag_string = request.POST['tags']
        if tag_string:
            tag_list = [x.strip() for x in tag_string.split(',')]
            # tag_list = tag_string.split(',')
            for x in tag_list:
                new_tag = Tag(tag=x, post_id=new_post)
                new_tag.save()
        return HttpResponseRedirect('/newsfeed')

# @cache_page(60 * 10)
def single_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    tags = Tag.objects.filter(post_id=post)
    return render(request, 'newsfeed/single_post.html', {'post': post, 'tags': tags, 'self_un': request.user})

def post_tag(request):
    if request.method == 'POST':
        new_post = Post.objects.order_by('-timestamp')[0]
        try:
            tag_string = request.POST['tags']
        except MultiValueDictKeyError:
            tag_string = None
        if tag_string:
            tag_list = [x.strip() for x in tag_string.split(',')]
            # tag_list = tag_string.split(',')
            for x in tag_list:
                new_tag = Tag(tag=x, post_id=new_post)
                new_tag.save()
                old_pref = Preferences.objects.filter(owner=request.user).get(tag=x)
                if old_pref:
                    old_pref.num = old_pref.num + 1
                    old_pref.save()
                else:
                    new_pref = Preferences(owner=request.user, tag=x, num=1)
                    new_pref.save()
        return HttpResponseRedirect('/newsfeed')

def single_tag(request, tag_id):
    tag_name = Tag.objects.get(pk=tag_id)
    used_tag_list = Tag.objects.filter(tag=tag_name.tag)
    tagged_post_list = []
    tag_list = []
    for tag in used_tag_list:
        tagged_post_list.insert(0, tag.post_id)
    for post in tagged_post_list:
        tag_group = Tag.objects.filter(post_id=post)
        tag_list.append(tag_group)
    zipped_lists = zip(tagged_post_list, tag_list)
    context = {'zipped_lists': zipped_lists, 'tagged_post_list': tagged_post_list, 'self_un': request.user}
    return render(request, 'newsfeed/tag.html', context)

def tags_of_a_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    tag_group = Tag.objects.filter(post_id=post)
    JSONSerializer = serializers.get_serializer("json")
    json_serializer = JSONSerializer()
    json_serializer.serialize(tag_group)
    tags = json_serializer.getvalue()
    # tags = serializers.serializer("json", tag_group)
    return HttpResponse(tags, content_type='application/json')

def suggested(request):
    top_tags = Preferences.objects.filter(owner=request.user).order_by('-num')
    post_groups = []

    i = 0
    for top_tag in top_tags:
        if (i < 5):
            used_tags = Tag.objects.filter(tag=top_tag)
            used_text = Post.objects.filter(post_text__contains=top_tag)
            used_title = Post.objects.filter(post_title__contains=top_tag)
            tagged_post_list = []
            tag_list = []
            for tag in used_tags:
                tagged_post_list.insert(0, tag.post_id)
            for post in tagged_post_list:
                tag_group = Tag.objects.filter(post_id=post)
                tag_list.insert(0, tag_group)

            for post in used_text:
                tagged_post_list.insert(0, post)
                tag_group = Tag.objects.filter(post_id=post)
                tag_list.insert(0, tag_group)

            for post in used_title:
                tagged_post_list.insert(0, post)
                tag_group = Tag.objects.filter(post_id=post)
                tag_list.insert(0, tag_group)

            zipped_post = zip(tagged_post_list, tag_list)
            post_groups.append(zipped_post)
            i = i + 1
    zipped_groups = zip(post_groups, top_tags)
    context = {'zipped_groups': zipped_groups, 'self_un': request.user}
    return render(request, 'newsfeed/suggested.html', context)
    # JSONSerializer = serializers.get_serializer("json")
    # json_serializer = JSONSerializer()
    # json_serializer.serialize(post_groups)
    # json = json_serializer.getvalue()
    # return HttpResponse(top_tags, content_type='text')

def search(request):
    tag_name = request.POST['search_input']

    used_tag_list = Tag.objects.filter(tag=tag_name)
    used_posttext_list = Post.objects.filter(post_text__contains=tag_name)
    used_posttitle_list = Post.objects.filter(post_title__contains=tag_name)

    tagged_post_list = []

    tag_tag_list = []
    text_tag_list = []
    title_tag_list = []

    for tag in used_tag_list:
        tagged_post_list.insert(0, tag.post_id)
    for post in tagged_post_list:
        tag_group = Tag.objects.filter(post_id=post)
        tag_tag_list.append(tag_group)

    for post in used_posttext_list:
        tag_group = Tag.objects.filter(post_id=post)
        text_tag_list.append(tag_group)

    for post in used_posttitle_list:
        tag_group = Tag.objects.filter(post_id=post)
        title_tag_list.append(tag_group)

    zipped_tags = zip(tagged_post_list, tag_tag_list)
    zipped_text = zip(used_posttext_list, text_tag_list)
    zipped_title = zip(used_posttitle_list, title_tag_list)

    context = {'zipped_tags': zipped_tags, 'zipped_text': zipped_text, 'zipped_title': zipped_title, 'tagged_post_list': tagged_post_list, 'self_un': request.user}

    return render(request, 'newsfeed/search.html', context)

def documentation(request):
    return render(request, 'newsfeed/documentation.html')

def auth(request):
    return render(request, 'newsfeed/auth.html')




# API ENDPOINTS

# For POST for all of these, every field must be provided in the curl command. 
# If you don't want to fill out a field, put "" 



# Users POST, GET endpoint
# Retrieve all users
# Create a new user
# Cannot leave any fields blank
class UserList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

# User GET, PUT, DELETE endpoint
# Retrieve a user by id
# Update an existing user
# Delete an existing user
class UserDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            serializer_class = UserSerializerPut
        elif self.request.method != 'PUT':
            serializer_class = UserSerializer
        return serializer_class
    



# Posts POST, GET endpoint
# Retrieve all posts
# Create a new post
# Cannot leave any fields blank
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    # Associates this post with an owner
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        # return HttpResponse('')
        return HttpResponseRedirect('/login')

    def post(self, request, format=None):
        print 'entered here'
        print '%' * 10
        #print request.DATA
        print request.FILES
        print '%' * 10
        if serializer.is_valid():
            print 'here'
            serializer.save()
        return HttpResponseRedirect('/newsfeed')


# User GET, PUT, DELETE endpoint
# Retrieve a post by id
# Update an existing post
# Delete an existing post
class PostDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Post.objects.all()

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        if self.request.method != 'GET':
            serializer_class = PostSerializerPut
            return HttpResponseRedirect('/login')
        else:
            serializer_class = PostSerializer
            return HttpResponseRedirect('/login')
        return HttpResponseRedirect('/login')
        # return serializer_class
    


# Posts POST, GET endpoint
# Retrieve all posts
# Create a new post
# Cannot leave any fields blank
class TagList(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

# User GET, PUT, DELETE endpoint
# Retrieve a Tag by id
# Update an existing Tag
# Delete an existing Tag
class TagDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Tag.objects.all()
    
    def get_serializer_class(self):
        if self.request.method != 'GET':
            serializer_class = TagSerializerPut
        else:
            serializer_class = TagSerializer
        return serializer_class
    












