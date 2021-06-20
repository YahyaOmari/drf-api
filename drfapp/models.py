from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 64)
    name = models.CharField(max_length = 64)
    body = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)