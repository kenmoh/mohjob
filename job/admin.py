from django.contrib import admin
from .models import Application, Job, JobCategory

admin.site.register(Application)
admin.site.register(JobCategory)
admin.site.register(Job)
