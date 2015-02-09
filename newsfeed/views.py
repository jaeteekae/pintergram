from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.utils import timezone

from newsfeed.models import User, Post



# def index(request):
#     latest_post_list = Post.objects.order_by('-timestamp')[:5]
#     context = {'latest_post_list': latest_post_list}
#     return render(request, 'newsfeed/index.html', context)

def index(request):
    latest_post_list = Post.objects.order_by('-timestamp')[:5]
    context = {'latest_post_list': latest_post_list}

    if request.POST:
    	new_post = Post(post_text="request.POST['post_text']", post_title="request.POST['post_title']", timestamp=timezone.now(), upvotes=0, )
    	new_post.save()
    	latest_post_list = Post.objects.order_by('-timestamp')[:5]
    	context = {'latest_post_list': latest_post_list}
    	# return HttpResponseRedirect(reverse('newsfeed:index'))
    	render(request, 'newsfeed/index.html', context)
    else:
    	return render(request, 'newsfeed/index.html', context)



def newsfeed(request):
    latest_post_list = Post.objects.order_by('-timestamp')[:5]
    context = {'latest_post_list': latest_post_list}

    if request.POST:
    	new_post = Post(post_text="request.POST['post_text']", post_title="request.POST['post_title']", timestamp=timezone.now(), upvotes=0, user_id=User.objects.get(pk=1))
    	new_post.save()
    	latest_post_list = Post.objects.order_by('-timestamp')[:5]
    	context = {'latest_post_list': latest_post_list}
    	# return HttpResponseRedirect(reverse('newsfeed:index'))
    	render(request, 'newsfeed/newsfeed.html', context)
    else:
    	return render(request, 'newsfeed/newsfeed.html', context)





def single_post(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'newsfeed/single_post.html', {'post': post})




