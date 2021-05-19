from django import forms

# we use widget to place arguments that django doesn't provide
class user_form(forms.Form):
    user_name = forms.CharField(
        required=False,
        label="Username",
        # initial="Dhrubo", value of input
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter your full name',
                'style': 'width:300px; border:none'
            }))

    user_dob = forms.DateField(
        label="Date of Birth",
        widget=forms.TextInput(
            attrs={
                'type': 'date'
            }))

    user_email = forms.EmailField(
        required=False,
        label="email",
    )
