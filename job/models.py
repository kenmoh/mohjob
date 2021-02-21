from django.db import models
from account.models import User
from account.states_status import STATE_CHOICES


JOB_TYPE = (
    ('Contract', 'Contract'),
    ('Full Time', 'Full Time'),
    ('Remote', 'Remote'),
)


class JobCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def clean(self):
        self.name = self.name.title()

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=300, choices=STATE_CHOICES)
    skills = models.CharField(max_length=300, blank=True, null=True)
    salary = models.PositiveIntegerField(null=True, blank=True)
    job_type = models.CharField(
        max_length=200, choices=JOB_TYPE, default='Full Time')
    category = models.ForeignKey(
        JobCategory, on_delete=models.DO_NOTHING)
    description = models.TextField()
    is_closed = models.BooleanField(default=False)
    posted_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    def skills_as_list(self):
        return self.skills.split(',')


class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    skills = models.CharField(max_length=200)
    experience = models.IntegerField()
    experience_details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.job}'

    def split_skills_as_list(self):
        return self.skills.split(',')
