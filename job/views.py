from django.shortcuts import render, get_object_or_404
from .models import Job


def job_details(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    context = {'job': job}
    return render(request, 'job/job_details.html', context)
