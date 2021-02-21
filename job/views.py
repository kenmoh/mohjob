from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Job
from .forms import AddCategoryForm, AddJobForm, ApplicationForm


@login_required
def job_details(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    context = {'job': job}
    return render(request, 'job/job_details.html', context)


@login_required
def add_job(request):
    form = AddJobForm()
    if request.method == 'POST':

        form = AddJobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user
            job.save()
            messages.success(request, f'Job posted successfully !')
            return redirect('employer_dashboard')

    context = {'form': form}
    return render(request, 'job/add_job.html', context)


def add_category(request):
    form = AddCategoryForm()
    if request.method == 'POST':
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Category Created Successfully !')
            return redirect('add_job')
    context = {'form': form}
    return render(request, 'job/add_category.html', context)


def job_application(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    form = ApplicationForm()
    if request.method == 'POST':
        form = ApplicationForm(request.POST)

        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.job = job
            application.save()
            messages.success(request, "Application sent successfully !")
            return redirect('applicant_dashboard')

    context = {'form': form}
    return render(request, 'job/job_application.html', context)
