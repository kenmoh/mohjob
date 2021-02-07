from django import forms
from django.forms import fields

from .models import Job, Application


class AddJobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('modified_at', 'user')


class ApplicationForm(forms.ModelForm):
    content = forms.CharField(
        max_length=650,
        widget=forms.Textarea(attrs={
            'class': 'mb-5 h-14 shadow-md focus:ring-red-500 focus:border-red-500 mt-1  sm:text-sm border-green-300 rounded-md',
            'Placeholder': 'Something'})

    )

    class Meta:
        model = Application
        fields = ['content', 'experience']
