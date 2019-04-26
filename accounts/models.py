from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
# Create your models here.
    
class Follower(AbstractUser):
    pass

class Following(AbstractUser):
    pass

class Link(models.Model):
    folloewing = models.ForeignKey(Following, on_delete=models.CASCADE)
    folloewer = models.ForeignKey(Follower, on_delete=models.CASCADE)