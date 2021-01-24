from django import forms
from django.forms import fields

from .models import Job


class AddJobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('modified_at',)