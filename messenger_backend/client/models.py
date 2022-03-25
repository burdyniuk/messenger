import imp
from django.db import models
from django.contrib.auth.models import User
from django.forms import ImageField

# Create your models here.
class Client(models.Model):
    notification_token = models.CharField(max_length=400, blank=True, unique=True)
    profile_picture = models.ImageField(upload_to='images/', default='profile.png')
    last_online = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)