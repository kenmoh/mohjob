from django.urls import path
from . import views

urlpatterns = [
    path('sign_up', views.sign_up, name='sign_up'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('employer_dashboard', views.employer_dashboard, name='employer_dashboard'),
    path('applicant_dashboard', views.applicant_dashboard,
         name='applicant_dashboard'),
    path('update_applicant/',
         views.update_applicant, name='update_applicant'),
    path('update_employer/', views.update_employer, name='update_employer'),
]
