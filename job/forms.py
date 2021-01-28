from django import forms
from django.forms import fields

from .models import Job, Application


class AddJobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('modified_at', 'user')


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['content', 'experience']
