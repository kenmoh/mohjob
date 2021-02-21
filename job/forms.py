from django import forms
from django.core.exceptions import ValidationError
from django.forms import fields
from account.states_status import STATE_CHOICES

from .models import JOB_TYPE, Job, Application, JobCategory


class AddJobForm(forms.ModelForm):
    title = forms.CharField(label='', required=True, widget=forms.TextInput(
        attrs={'class': '', 'Placeholder': 'Job Title'}))
    skills = forms.CharField(label='', required=True, widget=forms.TextInput(
        attrs={'class': ' mt-2', 'Placeholder': 'Skills (Seperate each skill with a comma e.g Python, Java)'}))
    location = forms.ChoiceField(label='', choices=STATE_CHOICES, widget=forms.Select(
        attrs={'class': 'form control form-control-sm mb-2', 'Placeholde': 'Location'}))
    salary = forms.IntegerField(label='', required=False, widget=forms.TextInput(
        attrs={'class': '', 'Placeholder': 'Salary'}))
    job_type = forms.ChoiceField(label='', required=True, choices=JOB_TYPE, widget=forms.Select(
        attrs={'class': '', 'Placeholder': 'Job Type'}))
    description = forms.CharField(label='', required=True, widget=forms.Textarea(
        attrs={'class': '', 'Placeholder': 'Description', 'rows': 3}))
    is_closed = forms.BooleanField(label='Application Closed ?', required=False, widget=forms.CheckboxInput(
        attrs={'class': ''}))

    class Meta:
        model = Job
        exclude = ('modified_at', 'user')

    def __init__(self, *args, **kwargs):
        super(AddJobForm, self).__init__(*args, **kwargs)
        self.fields['location'].initial = 'Abuja'


class AddCategoryForm(forms.ModelForm):

    name = forms.CharField(label='', required=True, widget=forms.TextInput(
        attrs={'class': 'py-1 ', 'Placeholder': 'Add New Category'}))

    class Meta:
        model = JobCategory
        fields = ['name']

    def clean_name(self):
        name = self.cleaned_data['name']
        if JobCategory.objects.filter(name=name).exists():
            raise ValidationError(
                f'The Category "{name}" already exist, Please select it from the Category field dropdown !')
        return name


class ApplicationForm(forms.ModelForm):
    skills = forms.CharField(label='', required=True, widget=forms.TextInput(
        attrs={'class': '', 'Placeholder': 'Skills'}))
    experience = forms.IntegerField(label='', required=True, widget=forms.TextInput(
        attrs={'class': '', 'Placeholder': 'Year(s) of Experience'}))
    experience_details = forms.CharField(label='', required=True, widget=forms.Textarea(
        attrs={'class': '', 'Placeholder': 'Experience Details', 'rows': 3}))

    class Meta:
        model = Application
        exclude = ['user', 'created_at', 'job']
