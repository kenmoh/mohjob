from django.shortcuts import render, redirect
from job.models import Job
from account.models import User


def index(request):
    users = User.objects.all()
    jobs = Job.objects.all().order_by('posted_at')
    context = {
        'jobs': jobs,
        'users': users
    }
    return render(request, 'pages/indext2.html', context)
