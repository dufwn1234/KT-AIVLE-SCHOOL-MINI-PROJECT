# accounts/urls.py
from django.urls import path
from django.shortcuts import render
from . import views


def home(request):
    return render(request,'home.html')

# app_name = 'accounts'

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
]