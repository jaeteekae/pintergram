from newsfeed.models import User, Post, Tag, Follower, Upvote
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password', 'email', 'avatar_path')


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('user_id', 'post_title', 'post_text', 'image_path', 'timestamp')

class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('post_id', 'tag')

class FollowerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Follower
        fields = ('follower_id', 'followee_id')

class UpvoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Upvote
        fields = ('post_id', 'original_poster', 'voter_set')



# class UserSerializer(serializers.Serializer):
#     pk = serializers.IntegerField(read_only=True)
#     username = serializers.CharField(required=True, allow_blank=False, max_length=30)
#     first_name = serializers.CharField(required=True, allow_blank=False, max_length=30)
#     last_name = serializers.CharField(required=True, allow_blank=False, max_length=50)
#     password = serializers.CharField(required=True, allow_blank=False, max_length=30, default='1234')
#     email = serializers.EmailField(required=True)
    
    

#     def create(self, validated_data):
#         """
#         Create and return a new `User` instance, given the validated data.
#         """
#         return User.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `User` instance, given the validated data.
#         """
#         instance.username = validated_data.get('username', instance.username)
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.password = validated_data.get('password', instance.password)
#         instance.email = validated_data.get('email', instance.email)

#         instance.save()
#         return instance