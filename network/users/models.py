from django.db import models


class Contact(models.Model):
    """
    Сontact form with admin
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    body = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    is_answered = models.BooleanField(default=False)

    def __str__(self):
        return self.subject



