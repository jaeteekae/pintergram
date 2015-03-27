from django.forms import widgets
from rest_framework import serializers
from newsfeed.models import User, Post, Tag, Follower, Upvote



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'first_name', 'last_name', 'email', 'avatar_path')


class UserSerializerPut(serializers.ModelSerializer):
    pk = serializers.IntegerField(read_only=True)
    username = serializers.CharField(required=False, allow_blank=True, max_length=30)
    first_name = serializers.CharField(required=False, allow_blank=True, max_length=30)
    last_name = serializers.CharField(required=False, allow_blank=True, max_length=50)
    
    email = serializers.EmailField(required=False)
    avatar_path = serializers.CharField(required=False, allow_blank=True, max_length=30, default='1234')
    
    class Meta:
        model = User
        

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'user_id', 'post_title', 'post_text', 'image_path', 'timestamp')


class PostSerializerPut(serializers.ModelSerializer):
    pk = serializers.IntegerField(read_only=True)
    
    user_id = serializers.IntegerField(read_only=True)
    post_title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    post_text = serializers.CharField(required=False, allow_blank=True, max_length=5000)
    image_path = serializers.CharField(required=False, allow_blank=True, max_length=30, default='1234')
    
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
    
