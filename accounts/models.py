from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.conf import settings

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    date_of_birth = models.DateField(default=timezone.now)
    profile_picture = models.ImageField(upload_to='static/', null=True, blank=True)
    friends = models.ManyToManyField("CustomUser", blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class FriendRequest(models.Model):
    from_user = models.ForeignKey(CustomUser, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(CustomUser, related_name='to_user', on_delete=models.CASCADE)