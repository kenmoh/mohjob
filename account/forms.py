from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import User


class CreateUserForm(UserCreationForm):
    username = forms.CharField(label='', required=True, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm mb-3 focus:border-blue-500', 'Placeholder': 'Username'}))
    email = forms.CharField(label='', required=True, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm mb-3 focus:border-blue-500', 'Placeholder': 'Email'}))
    password1 = forms.CharField(label='', required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-sm mb-3 focus:border-blue-500', 'Placeholder': 'Password'}))
    password2 = forms.CharField(label='', required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-sm mb-3 focus:border-blue-500', 'Placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'status']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError(
                f'A user with "{email}" already exist !')
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if User.objects.filter(phone_number=phone_number).exists():
            raise ValidationError(
                f'The phone number "{phone_number}" is already in use !')
        return phone_number

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['status'].widget.attrs.update(
            {'class': 'form-control form-control-sm mb-3'})
