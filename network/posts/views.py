from django.shortcuts import render
from django.views import View
from .models import Post


class PostView(View):
    def get(self, request):
        posts = Post.objects.order_by('-pub_date')[:10]
        context = {'posts': posts}
        return render(request, 'posts/index.html', context)
