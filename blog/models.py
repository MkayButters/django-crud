from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=64)
    body = models.TextField(default="")
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
