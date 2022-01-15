from django.shortcuts import render, get_object_or_404
from .models import Group, Post


MAX_POST_DISPLAYED = 10


def index(request):
    title = 'Последние обновления на сайте'
    template = 'posts/index.html'
    posts = Post.objects.select_related(
        'author',
        'group'
    )[:MAX_POST_DISPLAYED]
    context = {
        'posts': posts,
        'title': title,
    }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    title = f'Записи сообщества {group.title}'
    template = 'posts/group_list.html'
    posts = group.posts.all(
    )[:MAX_POST_DISPLAYED]
    context = {
        'group': group,
        'posts': posts,
        'title': title,
    }
    return render(request, template, context)
