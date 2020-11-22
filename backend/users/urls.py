from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.urls import include

from . import views

app_name = 'users'
urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    url(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),
]
