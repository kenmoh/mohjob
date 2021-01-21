from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from .models import User

class CreateUserForm(UserCreationForm):
    username = forms.CharField(label='Username', required=True)
    email = forms.EmailField(label='Username', required=True)
    password1 = forms.PasswordInput(label='Username', required=True)
    password2 = forms.PasswordInput(label='Username', required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(f'The email "{self.email} is already in use !')
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if User.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError(f'The phone number "{self.phone_number}" is already in use !')
        return phone_number