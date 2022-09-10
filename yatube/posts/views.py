from django.conf import settings
from django.shortcuts import get_object_or_404, render

from .models import Group, Post


def index(request):
    posts = Post.objects.all()[:settings.POSTS_PER_PAGE]
    return render(request, 'posts/index.html', {
        'posts': posts,
    })


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:settings.POSTS_PER_PAGE]
    return render(request, 'posts/group_list.html', {
        'group': group,
        'posts': posts,
    })
