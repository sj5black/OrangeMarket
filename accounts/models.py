from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)