from django.db import models
from django.conf import settings

class Post(models.Model):
    body = models.TextField(max_length=33000, null=True, blank=True)
    image = models.ImageField(upload_to='static/post_images/', null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"By {self.author} created at {self.created_at}"
    
class Comment(models.Model):
    comment = models.TextField(max_length=8000)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    likes = models.PositiveBigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"By {self.author} created at {self.created_at}"