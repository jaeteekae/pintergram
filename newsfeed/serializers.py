from django.forms import widgets
from datetime import datetime
from rest_framework import serializers
from django.contrib.auth.models import User
from newsfeed.models import Post, Tag, Follower, Upvote



class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'posts')


class UserSerializerPut(serializers.ModelSerializer):
    pk = serializers.IntegerField(read_only=True)
    username = serializers.CharField(required=False, allow_blank=True, max_length=30)
    first_name = serializers.CharField(required=False, allow_blank=True, max_length=30)
    last_name = serializers.CharField(required=False, allow_blank=True, max_length=50)
    
    email = serializers.EmailField(required=False)
    #avatar_path = serializers.CharField(required=False, allow_blank=True, max_length=30, default='1234')
    
    class Meta:
        model = User
        

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = Post
        fields = ('id', 'owner', 'post_title', 'post_text', 'image_path', 'timestamp')#, 'tags')


class PostSerializerPut(serializers.ModelSerializer):
    pk = serializers.IntegerField(read_only=True)
    
    owner = serializers.IntegerField(read_only=True)
    post_title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    post_text = serializers.CharField(required=False, allow_blank=True, max_length=5000)
    image_path = serializers.ImageField(required=False)
    timestamp = serializers.DateTimeField(default=datetime.now)
   
    class Meta:
        model = Post
       

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('post_id', 'tag')



class TagSerializerPut(serializers.ModelSerializer):
    pk = serializers.IntegerField(read_only=True)
    post_id = serializers.IntegerField(read_only=True)
    tag = serializers.CharField(required=True, allow_blank=True, max_length=100)
    
    class Meta:
        model = Tag
    
