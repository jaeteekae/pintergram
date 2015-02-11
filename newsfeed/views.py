from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.utils import timezone

from newsfeed.models import Post, User

def index(request):
    latest_post_list = Post.objects.order_by('-timestamp')
    context = {'latest_post_list': latest_post_list}
    return render(request, 'newsfeed/index.html', context)

def new_post(request):
    return render(request, 'newsfeed/new_post.html')

def create_post(request):
    new_post = Post(post_text=request.POST['post_text'], post_title=request.POST['post_title'], timestamp=timezone.now(), user_id=User.objects.get(pk=1))
    new_post.save()
    return HttpResponseRedirect('/newsfeed')

def single_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'newsfeed/single_post.html', {'post': post})
