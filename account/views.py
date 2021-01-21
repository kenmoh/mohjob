from django.shortcuts import render



def index(request):
    name = 'Kenneth Aremoh'
    context = { 'name': name}
    return render(request, 'account/index.html', context)

def sign_up(request):
    return render(request, 'account/signup.html')

def sign_in(request):
    return render(request, 'account/signup.html')