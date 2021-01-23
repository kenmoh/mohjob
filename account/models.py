from django.db import models
from django.contrib.auth.models import AbstractUser


STATUS_CHOICES = (
    ('Applicane', 'Applicant'),
    ('Employer', 'Employer')
)


class User(AbstractUser):
    is_verified = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=35, blank=True, null=True)
    status = models.CharField(
        max_length=35, choices=STATUS_CHOICES)

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=75, null=True, blank=True)
    state = models.CharField(max_length=35)
    about = models.TextField()
    profile_photo = models.ImageField()

    def __str__(self) -> str:
        return self.user.username
