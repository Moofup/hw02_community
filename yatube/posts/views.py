from django.shortcuts import render, get_object_or_404

from .models import Group, Post


def index(request):
    title = 'Последние обновления на сайте'
    template = 'posts/index.html'
    max_posts_displayed = 10
    posts = Post.objects.select_related('author', 'group').order_by('-pub_date')[:max_posts_displayed]
    context = {
        'posts': posts,
        'title': title,
    }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    title = f'Записи сообщества {group.title}'
    template = 'posts/group_list.html'
    max_posts_displayed = 10
    posts = group.grouped_posts.all().order_by('-pub_date')[:max_posts_displayed]
    context = {
        'group': group,
        'posts': posts,
        'title': title,
    }
    return render(request, template, context)
