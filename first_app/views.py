from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
 context={
  'msg':"Hello From Homepage"
 }
 return render(request, 'index.html', context)

def about(request):
 context={
  'msg':"Hello From About page"
 }
 return render(request, 'about.html', context)

def contact(request):
 context={
  'msg':"Hello From Contact page"
 }
 return render(request, 'contact.html', context)

