from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

User = get_user_model()


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        title = self.text.split('.')[0]
        return title

    # def get_absolute_url(self):
    #     return reverse('post.index', kwargs={'id': self.id})




