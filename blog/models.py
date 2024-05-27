# models.py
from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Add created_at for posts

    def __str__(self):
        return self.title

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(default=timezone.now)  # Ensure created_at is used

    def __str__(self):
        return self.email
