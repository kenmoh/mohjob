from django.urls import path
from . import views

urlpatterns = [
    path('add_job', views.add_job, name='add_job'),
    path('job_details/<str:job_id>', views.job_details, name='job_details'),
    path('job_application/<str:job_id>',
         views.job_application, name='job_application'),
]
