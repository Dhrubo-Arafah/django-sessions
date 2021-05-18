from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
 return HttpResponse("<h1>This is Home page</h1><a href='contact/'>Contact<a/><br><a href='about/'>About<a/>")

def about(request):
 return HttpResponse("<h1>This is About Page</h1><a href='/contact/'>Contact<a/><br><a href='/'>Home<a/>")

def contact(request):
 return HttpResponse("<h1>This is Contact Page</h1><a href='/about/'>About<a/><br><a href='/'>Home<a/>")

