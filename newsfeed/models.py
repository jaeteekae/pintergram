from datetime import datetime
from django.db import models
# from pygments.lexers import get_all_lexers
# from pygments.styles import get_all_styles

class User(models.Model):
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    email = models.EmailField()
    #outdated but cool for MVP
    avatar_path = models.FilePathField("/images/avatars", blank=True)
    def __str__(self):              # __unicode__ on Python 2
        return self.username
    

#http://code.techandstartup.com/django/images/#images-templates
def generate_filename(instance, filename):
    ext = filename.split('.')[-1]
    return 'images/' + str(int(time())) + '.' + ext



class Post(models.Model):
    user_id = models.ForeignKey(User)
    post_title = models.CharField(max_length=100)
    post_text = models.TextField(max_length=5000)

    image_path = models.ImageField(upload_to=generate_filename, blank=True, null=True)

    timestamp = models.DateTimeField(default=datetime.now)

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
        return "upvote"

