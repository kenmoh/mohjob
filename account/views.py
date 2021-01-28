from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm


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

        if user is not None and user.status == 'Applicant':
            login(request, user)
            messages.success(request, f"You're now logged in !")

            return redirect('applicant_dashboard')
    return render(request, 'account/signin.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('index')


@login_required
def employer_dashboard(request):
    user = request.user
    context = {'user': user}
    return render(request, 'account/employer_dashboard.html', context)


@login_required
def applicant_dashboard(request):
    user = request.user
    context = {'user': user}
    return render(request, 'account/applicant_dashboard.html', context)
