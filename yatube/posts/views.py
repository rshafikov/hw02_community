from django.shortcuts import get_object_or_404, render

from .models import Group, Post


def index(request):
    posts = Post.objects.all().order_by('-pub_date')[DISPLAYED_OBJECTS_COUNT]
    template = 'posts/index.html'
    context = {
        'posts': posts,
        'title': 'Последние обновления на сайте',
    }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all().order_by('-pub_date')[DISPLAYED_OBJECTS_COUNT]
    template = 'posts/group_list.html'
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)


DISPLAYED_OBJECTS_COUNT = 10
