import datetime

from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Post, Group, User
from django.http import Http404


class PostView(View):
    """
    All posts
    """
    def get(self, request):
        posts = Post.objects.order_by('-pub_date')[:10]
        context = {'posts': posts}
        return render(request, 'posts/index.html', context)


class GroupPostView(View):
    """
    Groups posts
    """
    def get(self, request, slug):
        group = get_object_or_404(Group, slug=slug)
        print(group)
        posts = Post.objects.filter(group=group).order_by('-pub_date')
        context = {'posts': posts,
                   'group': group, }
        return render(request, 'posts/group.html', context)


class PostUser(View):
    """
    Post each authors
    """
    def get(self, request):
        posts = None
        keyword = 'утро'
        start_date = datetime.date(1854, 7, 7)
        end_date = datetime.date(1854, 7, 21)
        author = User.objects.get(username='leo')
        posts = Post.objects.filter(
                                    author=author,
                                    text__contains=keyword,
                                    pub_date__range=(start_date, end_date)
                                    )
        context = {'posts': posts}
        return render(request, 'posts/posts_user.html', context)


class SearchView(View):
    """
    Simple post search
    """
    def get(self, request):
        keyword = request.GET.get('q', None)
        if keyword:
            posts = Post.objects.select_related('author', 'group').filter(text__contains=keyword)
        else:
            posts = None
        context = {'posts': posts, 'keyword': keyword}
        return render(request, 'posts/search.html', context)