from django.urls import path
from . import views

urlpatterns = [
    path('job_details/<str:job_id>', views.job_details, name='job_details'),
]
