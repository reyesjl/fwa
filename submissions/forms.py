from django import forms
from .models import RecruitingSubmission

class RecruitingSubmissionForm(forms.ModelForm):
    class Meta:
        model = RecruitingSubmission
        exclude = ['status']
        labels = {
            'firstname': 'First Name',
            'lastname': 'Last Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'position': 'Position',
            'age': 'Age',
            'origin_country': 'Origin Country',
            'destination_country': 'Destination Country',
        }