from django import forms
from django.forms import fields
from account.states_status import STATE_CHOICES

from .models import Job, Application


class AddJobForm(forms.ModelForm):
    title = forms.CharField(label='', required=True, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm mb-2', 'Placeholder': 'Job Title'}))
    skills = forms.CharField(label='', required=True, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm mb-2 mt-2', 'Placeholder': 'Skills (Seperate each skill with a comma e.g Python, Java)'}))
    location = forms.ChoiceField(label='', choices=STATE_CHOICES, widget=forms.Select(
        attrs={'class': 'form control form-control-sm mb-2', 'Placeholde': 'Location'}))
    salary_from = forms.IntegerField(label='', required=True, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm mb-2', 'Placeholder': 'Salary From'}))
    salary_to = forms.IntegerField(label='', required=True, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm mb-2', 'Placeholder': 'Salary To'}))
    description = forms.CharField(label='', required=True, widget=forms.Textarea(
        attrs={'class': 'form-control form-control-sm mb-2', 'Placeholder': 'Description', 'rows': 3}))

    class Meta:
        model = Job
        exclude = ('modified_at', 'user')

    def __init__(self, *args, **kwargs):
        super(AddJobForm, self).__init__(*args, **kwargs)
        self.fields['location'].initial = 'Abuja'


class ApplicationForm(forms.ModelForm):
    content = forms.CharField(label='', required=True, widget=forms.Textarea(
        attrs={'class': 'form-control form-control-sm mb-2', 'Placeholder': 'Description', 'rows': 3}))
    experience = forms.CharField(label='', required=True, widget=forms.Textarea(
        attrs={'class': 'form-control form-control-sm mb-2', 'Placeholder': 'Experience', 'rows': 3}))

    class Meta:
        model = Application
        fields = ['content', 'experience']
