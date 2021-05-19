from django.shortcuts import render
from first_app.models import Musician, Album
from first_app import forms


# Create your views here.

def index(request):
    # SELECT * FROM MUSICIAN ORDER BY first_name
    musician_list = Musician.objects.order_by('first_name')
    context = {
        'text': "List of Musicians",
        'musician': musician_list
    }
    return render(request, 'index.html', context)


def about(request):
    context = {
        'text': "Hello From About page"
    }
    return render(request, 'about.html', context)


def contact(request):
    context = {
        'text': "Hello From Contact page"
    }
    return render(request, 'contact.html', context)


def form(request):
    new_form = forms.user_form
    context = {
        'form': new_form,
        'msg': "this form is created using django library"
    }
    if request.method == "POST":
        new_form = forms.user_form(request.POST)
        if new_form.is_valid():
            user_name = new_form.cleaned_data['user_name']
            user_dob = new_form.cleaned_data['user_dob']
            user_email = new_form.cleaned_data['user_email']

            context.update({'user_name': user_name,
                            'user_dob': user_dob,
                            'user_email': user_email
                            })
            # we can use context.update() dedicatedly for a key
            context.update({'form_submitted': "Yes"})

    return render(request, 'form.html', context)
