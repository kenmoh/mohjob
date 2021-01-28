from django.db import models
from account.models import User


class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    skills = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    def skills_list(self):
        return self.skills.split(',')


class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    content = models.TextField()
    experience = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
