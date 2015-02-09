from django.contrib import admin
from newsfeed.models import User, Post, Tag

class TagInline(admin.TabularInline):
    model = Tag
    extra = 2
    

class PostInline(admin.TabularInline):
    model = Post
    extra = 3
    inlines = [TagInline]

class UserAdmin(admin.ModelAdmin):
    fields = ['username', 'first_name', 'last_name', 'upvotes']
    inlines = [PostInline]

admin.site.register(User, UserAdmin)
admin.site.register(Post)
admin.site.register(Tag)
