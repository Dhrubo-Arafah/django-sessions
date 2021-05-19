from django import forms
from django.core import validators


# here django.core is a python tool module and validators is a library

class user_form(forms.Form):
    name = forms.CharField(validators=[validators.MaxLengthValidator(10),
                                       validators.MinLengthValidator(5)])

    age=forms.IntegerField(validators=[validators.MaxValueValidator(100), validators.MinValueValidator(18)])
