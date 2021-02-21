from account.states_status import STATE_CHOICES
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.db.models import fields
from .models import EmployerProfile, Profile, User


class CreateUserForm(UserCreationForm):
    username = forms.CharField(label='', required=True, widget=forms.TextInput(
        attrs={'class': 'focus:border-blue-600', 'Placeholder': 'Username or Company Name'}))
    email = forms.CharField(label='', required=True, widget=forms.TextInput(
        attrs={'class': 'focus:border-blue-600', 'Placeholder': 'Email'}))
    password1 = forms.CharField(label='', required=True, widget=forms.PasswordInput(
        attrs={'class': 'focus:border-blue-600', 'Placeholder': 'Password'}))
    password2 = forms.CharField(label='', required=True, widget=forms.PasswordInput(
        attrs={'class': 'focus:border-blue-600', 'Placeholder': 'Confirm Password'}))

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


class ApplicantProfileForm(forms.ModelForm):
    about = forms.CharField(label='', required=True, widget=forms.Textarea(
        attrs={'class': '', 'Placeholder': 'About', 'rows': 3}))

    class Meta:
        model = Profile
        exclude = ('user',)


class ApplicantUpdateForm(forms.ModelForm):
    username = forms.CharField(label='', required=True, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm mb-3 focus:border-blue-500', 'Placeholder': 'Username or Company Name'}))
    phone_number = forms.CharField(label='', required=True, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm mb-3 focus:border-blue-500', 'Placeholder': 'Phone Number'}))
    email = forms.CharField(label='', required=True, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm mb-3 focus:border-blue-500'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'status']


class EmployerProfileForm(forms.ModelForm):
    state = forms.ChoiceField(label='', required=True, choices=STATE_CHOICES, widget=forms.Select(
        attrs={'class': '', 'Placeholder': 'Job Type'}))
    about = forms.CharField(label='', required=True, widget=forms.Textarea(
        attrs={'class': '', 'Placeholder': 'About', 'rows': 3}))
    profile_photo = forms.FileField(label='Profile Photo or Logo')

    class Meta:
        model = EmployerProfile
        exclude = ('user',)


class EmployerUpdateForm(forms.ModelForm):
    username = forms.CharField(label='', required=True, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm mb-3 focus:border-blue-500', 'Placeholder': 'Username or Company Name'}))
    phone_number = forms.IntegerField(label='', required=True, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm mb-3 focus:border-blue-500', 'Placeholder': 'Phone Number'}))
    email = forms.CharField(label='', required=True, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm mb-3 focus:border-blue-500'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'status']
