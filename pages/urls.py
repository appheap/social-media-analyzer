from django.contrib import admin
from django.urls import path
from django.urls import include

from . import views

app_name = 'pages'
urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
]
