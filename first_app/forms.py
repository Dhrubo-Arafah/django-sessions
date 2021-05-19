from django import forms

# we use widget to place arguments that django doesn't provide
class user_form(forms.Form):
    #boolean_field=forms.BooleanField(required=False)
    #field=forms.CharField(max_length=15, min_length=5)
    # choices = (('', 'SELECT OPTION'), ('1', 'First'), ('2', 'Second'), ('3', 'Third'))
    # field=forms.ChoiceField(choices=choices, widget=forms.RadioSelect)
    choices = (('A', 'A'), ('B', 'B'), ('C', 'C'))
    field=forms.MultipleChoiceField(choices=choices,
                                    widget=forms.CheckboxSelectMultiple,
                                    required=False)