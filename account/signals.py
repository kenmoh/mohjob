from django.db.models import signals
from django.db.models.signals import post_save
from .models import User, Profile, EmployerProfile


def create_user_profile(sender, instance, created, **kwargs):
    user = instance
    if created and user.status == 'Applicant':
        user_profile = Profile(user=user)
        user_profile.save()
        print('Applicant Profile')
    else:
        if created and user.status == 'Employer':
            user_profile = EmployerProfile(user=user)
            user_profile.save()
            print('Employer profile')


post_save.connect(create_user_profile, sender=User)
