from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=15)
    context = models.TextField(max_length=500)
    time = models.DateTimeField(blank=True,null=True)
    author = models.EmailField(blank=True,null=True)


    def __str__(self):
        return self.title
