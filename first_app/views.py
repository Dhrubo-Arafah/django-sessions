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
    new_form = forms.MusicianForm()

    if request.method == 'POST':
        new_form = forms.MusicianForm(request.POST)

        if new_form.is_valid():
            new_form.save(commit=True)
            return index(request)
    context = {
        'form': new_form,
        'msg': "Add New Musician"
    }
    return render(request, 'form.html', context)
