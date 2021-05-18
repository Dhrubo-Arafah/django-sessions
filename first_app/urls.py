from django.urls import path
from first_app import views

urlpatterns = [
    path('', views.index),
    path('home/', views.index , name="home"),
    path('about/', views.about , name="about"),
    path('contact/', views.contact , name="contact")
    ]