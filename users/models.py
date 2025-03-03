from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    is_eating_healthy = models.BooleanField(default=False)
    is_playing_sport = models.BooleanField(default=False)
    is_intellectually_stimulated = models.BooleanField(default=False)
    
    