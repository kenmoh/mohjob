from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_verified = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=35, blank=True, null=True)
    
    def __str__(self):
        return self.username
