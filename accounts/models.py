from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="profiles/%Y/%m/%d/")
    bio = models.TextField(blank=True)
    phone = models.CharField(max_length=20)