from django.shortcuts import render, redirect
from job.models import Job


def index(request):

    jobs = Job.objects.all()
    context = {'jobs': jobs}
    return render(request, 'pages/index.html', context)
