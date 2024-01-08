from django import forms
from .models import PlayerEntry, School

class PlayerEntryForm(forms.ModelForm):
    school_of_interest = forms.ModelChoiceField(queryset=School.objects.all())

    class Meta:
        model = PlayerEntry
        exclude = ['status']  # This is for staff usage only

    def __init__(self, *args, **kwargs):
        super(PlayerEntryForm, self).__init__(*args, **kwargs)

