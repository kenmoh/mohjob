from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CreateUserForm


def index(request):
    name = 'Kenneth Aremoh'
    context = {'name': name}
    return render(request, 'account/index.html', context)


def sign_up(request):
    # User Registration Function
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account for "{username}" was created')
            return redirect('index')
    context = {'form': form}
    return render(request, 'account/signup.html', context)


def sign_in(request):
    return render(request, 'account/signup.html')
