"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('backend.users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('telegram/', include('backend.telegram.urls')),
    path('dashboard/', include('backend.dashboard.urls')),
    path('', include('backend.pages.urls')),
]

import django.conf.urls as urls

urls.handler403 = 'pages.views.bad_request'
urls.handler403 = 'pages.views.permission_denied'
urls.handler404 = 'pages.views.page_not_found'
urls.handler500 = 'pages.views.server_error'
