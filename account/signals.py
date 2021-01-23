from django.db.models import signals
from django.db.models.signals import post_save
from .models import User, Profile


def create_user_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        user_profile = Profile(user=user)
        user_profile.save()


post_save.connect(create_user_profile, sender=User)
