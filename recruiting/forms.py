from django import forms
from .models import PlayerEntry

class PlayerEntryForm(forms.ModelForm):
    class Meta:
        model = PlayerEntry
        exlude = ['status'] # This is for staff usage only
