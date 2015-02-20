from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.utils.datastructures import MultiValueDictKeyError


from newsfeed.models import Post, User, Tag

def index(request):
    latest_post_list = Post.objects.order_by('-timestamp')
    tag_list = []
    for post in latest_post_list:
        tag_group = Tag.objects.filter(post_id=post)
        tag_list.append(tag_group)
    zipped_lists = zip(latest_post_list, tag_list)
    context = {'zipped_lists': zipped_lists, 'latest_post_list': latest_post_list}
    return render(request, 'newsfeed/index.html', context)

def new_post(request):
    return render(request, 'newsfeed/new_post.html')

def base(request):
    return render(request, 'newsfeed/base.html')


def create_post(request):
    try:
        image = request.POST['post-image']
    except MultiValueDictKeyError:
        image = request.FILES['post-image']

    if not request.POST['post_title']:
        return HttpResponseRedirect('/newsfeed')
        # return HttpResponseRedirect('new_post')
    elif not request.POST['post_text'] and not image:
        return HttpResponseRedirect('/newsfeed')
        # return HttpResponseRedirect('new_post')
    else:
        new_post = Post(post_text=request.POST['post_text'], 
                        post_title=request.POST['post_title'], 
                        timestamp=timezone.now(), 
                        user_id=User.objects.get(pk=1))
        if image:
            new_post.image_path = request.FILES['post-image']
        new_post.save()
        tag_string = request.POST['tags']
        if tag_string:
            tag_list = [x.strip() for x in tag_string.split(',')]
            # tag_list = tag_string.split(',')
            for x in tag_list:
                new_tag = Tag(tag=x, post_id=new_post)
                new_tag.save()
        return HttpResponseRedirect('/newsfeed')

def single_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    tags = Tag.objects.filter(post_id=post)
    return render(request, 'newsfeed/single_post.html', {'post': post, 'tags': tags})

def tag(request, tag_id):
    tagged_post_list = Post.objects.order_by('-timestamp')
    context = {'tagged_post_list': tagged_post_list}
    return render(request, 'newsfeed/tag.html', context)
