from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
    chat_id = models.IntegerField(default=0)
    from_user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    time = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to = 'images/', blank=True)
    file = models.FileField(upload_to='uploads/', blank=True)

class Chat(models.Model):
    name = models.CharField(max_length=150)
    users = models.ManyToManyField(User)
    chat_picture = models.ImageField(upload_to='images/', default='profile.png')
    type = models.CharField(max_length=30)
    messages = models.ManyToManyField(Message, blank=True)
