from django.contrib import admin
from django.urls import path
from django.urls import include

from . import views

app_name = 'users'
urlpatterns = [
    path('signup/', views.Signup.as_view(), name='signup')
]
