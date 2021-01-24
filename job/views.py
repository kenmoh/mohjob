from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from .models import Job
from .forms import AddJobForm


def job_details(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    context = {'job': job}
    return render(request, 'job/job_details.html', context)


def add_job(request):
    form = AddJobForm()
    if request.method == 'POST':
        form = AddJobForm(request.POST)

        if form.is_valid():
            job = form.save(commit=False)
            job.posted_by = request.user
            job.save()
            messages.success(request, f'Job posted successfully !')
            return redirect('employer_dashboard')
    return redirect(request, 'job/add_job.html')
