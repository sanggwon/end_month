from django.db import models
from django.conf import settings
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=30)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = "post_like", blank = True)
