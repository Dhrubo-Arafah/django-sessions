from django import forms
from first_app.models import *


class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        # fields="__all__"
        #fields=['first_name', 'last_name']
        exclude=['first_name', 'instrument']