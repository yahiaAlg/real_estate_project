from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    photo_profile = models.ImageField(upload_to='users_photos', blank=True, null=True)
    

    def __str__(self):
        return f"{self.owner.username} profile"

