from django.db import models


class User(models.Model):
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=30, default="0000")
    email = models.CharField(max_length=254)
    upvotes = models.IntegerField()
    avatar_path = models.CharField(max_length=100)
    def __str__(self):              # __unicode__ on Python 2
        return self.username



class Post(models.Model):
    user_id = models.ForeignKey(User)
    #post_id = models.CharField(max_length=10)
    post_title = models.CharField(max_length=100)
    post_text = models.CharField(max_length=5000)
    image_path = models.CharField(max_length=100)
    timestamp = models.DateTimeField('date published')
    upvotes = models.IntegerField()
    def __str__(self):              # __unicode__ on Python 2
        return self.title

class Tag(models.Model):
	post_id = models.ForeignKey(Post)
	tag = models.CharField(max_length=100)


class Follower(models.Model):
	follower_id = models.ForeignKey(User, related_name='+')
	followee_id = models.ForeignKey(User, related_name='+')

class Upvote(models.Model):
	post_id = models.ForeignKey(Post)
	original_poster = models.ForeignKey(User, related_name='+')
	voter = models.ForeignKey(User, related_name='+')
