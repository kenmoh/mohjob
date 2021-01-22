from django.db import models
from account.models import User


class Job(models.Model):
    title = models.CharField(max_length=200)
    skills = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    def skills_list(self):
        return self.skills.split(',')
