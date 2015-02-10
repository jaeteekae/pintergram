from django.db import models


class User(models.Model):
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=30, default="0000")
    email = models.EmailField()
    avatar_path = models.FilePathField("/images/avatars")
    def __str__(self):              # __unicode__ on Python 2
        return self.username



class Post(models.Model):
    user_id = models.ForeignKey(User)
    #post_id = models.CharField(max_length=10)
    post_title = models.CharField(max_length=100)
    post_text = models.TextField(max_length=5000)
    image_path = models.FilePathField("/images/posts")
    timestamp = models.DateTimeField('date published')
    def __str__(self):              # __unicode__ on Python 2
        return self.post_title

class Tag(models.Model):
    post_id = models.ForeignKey(Post)
    tag = models.CharField(max_length=100)
    def __str__(self):              # __unicode__ on Python 2
        return self.tag


class Follower(models.Model):
    follower_id = models.ForeignKey(User, related_name='follower_set')
    followee_id = models.ForeignKey(User, related_name='followee_set')
    def __str__(self):              # __unicode__ on Python 2
        return self.followee_id

class Upvote(models.Model):
    post_id = models.ForeignKey(Post)
    original_poster = models.ForeignKey(User, related_name='op_set')
    voter_set       = models.ForeignKey(User, related_name='voter_set')
    def __str__(self):              # __unicode__ on Python 2
        return self.post_id.post_title
