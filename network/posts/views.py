from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Post, Group
from django.http import Http404


class PostView(View):
    def get(self, request):
        posts = Post.objects.order_by('-pub_date')[:10]
        context = {'posts': posts}
        return render(request, 'posts/index.html', context)


class GroupPostView(View):
    def get(self, request, slug):
        group = get_object_or_404(Group, slug=slug)
        posts = Post.objects.filter(group=group).order_by('-pub_date')
        context = {'posts': posts,
                   'group': group, }
        return render(request, 'posts/group.html', context)

# def handler404(request):
#     return render(request, '404.html', status=404)
