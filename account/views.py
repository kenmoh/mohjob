from django.contrib.messages.api import error, success
from account.models import EmployerProfile, Profile
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import ApplicantProfileForm, ApplicantUpdateForm, CreateUserForm, EmployerProfileForm, EmployerUpdateForm
from job.models import Job
from .models import User


def sign_up(request):
    # User Registration Function
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account for "{username}" was created. You may now sign into your account.')
            return redirect('sign_in')
    context = {'form': form}
    return render(request, 'account/signup.html', context)


def sign_in(request):
    # User Login function
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.status == 'Employer':
            login(request, user)
            messages.success(request, f"You're now logged in !")
            return redirect('employer_dashboard')

        else:
            messages.error(request, f'Incorrect username or password')

        if user is not None and user.status == 'Applicant':
            login(request, user)
            messages.success(request, f"You're now logged in !")
            return redirect('applicant_dashboard')

        else:
            messages.error(request, f'Incorrect username or password')

    return render(request, 'account/signin.html')

# Fuction to logout a user


@login_required
def user_logout(request):
    logout(request)
    return redirect('index')


# Employer Dashboard function
@login_required
def employer_dashboard(request):
    jobs = Job.objects.all().filter(user=request.user)
    context = {
        'jobs': jobs
    }
    return render(request, 'account/employer_dashboard.html', context)


# Applicant/Job Seeker Dashboard function
@ login_required
def applicant_dashboard(request):
    user = request.user
    context = {'user': user}
    return render(request, 'account/applicant_dashboard.html', context)


# Function to Update an Applicant
def update_applicant(request):
    user_form = ApplicantUpdateForm(instance=request.user)
    profile_form = ApplicantProfileForm(instance=request.user.profile)

    if request.method == 'POST':
        user_form = ApplicantUpdateForm(
            request.POST or None, instance=request.user)
        profile_form = ApplicantProfileForm(
            request.POST or None, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(
                request, 'Profile Updated Successfully !')
            return redirect('applicant_dashboard')

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'account/applicant_profile.html', context)


# Function to Update an Employer
def update_employer(request):
    user_form = EmployerUpdateForm(instance=request.user)
    profile_form = EmployerProfileForm(instance=request.user.employerprofile)

    if request.method == 'POST':
        user_form = EmployerUpdateForm(
            request.POST or None, instance=request.user)
        profile_form = EmployerProfileForm(
            request.POST or None, request.FILES, instance=request.user.employerprofile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(request, 'Profile Updated Successfully !')
            return redirect('employer_dashboard')

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'account/employer_profile.html', context)
