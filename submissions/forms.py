from django import forms
from .models import RecruitingSubmission, ToursSubmission, CanterburyKitSubmission, TeamItemSubmission

class RecruitingSubmissionForm(forms.ModelForm):
    class Meta:
        model = RecruitingSubmission
        exclude = ['status',]
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

class ToursSubmissionForm(forms.ModelForm):
    class Meta:
        model = ToursSubmission
        exclude = ['status',]
        labels = {
            'firstname': 'First Name',
            'lastname': 'Last Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'teamname': 'Team Name',
            'teamsize': 'Team Size',
        }

class CanterburyKitSubmissionForm(forms.ModelForm):
    class Meta:
        model = CanterburyKitSubmission
        exclude = ['status',]
        labels = {
            'firstname': 'First Name',
            'lastname': 'Last Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'teamname': 'Team Name',
            'teamsize': 'Team Size',
        }

class TeamItemSubmissionForm(forms.ModelForm):
    class Meta:
        model = TeamItemSubmission
        exclude = ['status']
        labels = {
            'product_name': 'Product Name',
            'firstname': 'First Name',
            'lastname': 'Last Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'teamname': 'Team Name',
            'team_primary_color', 'Team Main Color',
            'team_seconday_color', 'Team Secondary Color',
            'teamsize': 'Team Size',
        }