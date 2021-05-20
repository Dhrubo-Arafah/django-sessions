from django import forms
from django.core import validators


# here django.core is a python tool module and validators is a library

class user_form(forms.Form):
    user_email=forms.EmailField()
    user_vmail=forms.EmailField()

    def clean(self):
        all_cleaned_data=super().clean()
        user_email=all_cleaned_data['user_email']
        user_vmail=all_cleaned_data['user_vmail']

        if user_email!=user_vmail:
            raise forms.ValidationError("Fields Don't Match")