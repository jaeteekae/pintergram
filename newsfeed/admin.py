from django.contrib import admin
from newsfeed.models import User, Post, Tag, Follower, Upvote

# class TagInline(admin.TabularInline):
#     model = Tag
#     extra = 2
    

# class PostInline(admin.TabularInline):
#     model = Post
#     extra = 3
#     inlines = [TagInline]

# class UserAdmin(admin.ModelAdmin):
#     fields = ['username', 'first_name', 'last_name', 'password', 'email', 'avatar_path']
#     inlines = [PostInline]

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Follower)
admin.site.register(Upvote)

