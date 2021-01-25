from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.MainDashboardView.as_view(), name='main'),
    path('accounts/', views.AccountsView.as_view(), name='accounts'),
    path('accounts/add_telegram_channel/', views.TelegramChannelAddView.as_view(), name='add_telegram_channel'),
    path(
        'accounts/telegram/<str:channel_id>/',
        views.TelegramChannelManagementView.as_view(),
        name='telegram_account_management'
    ),
    path('settings/', views.SettingsView.as_view(), name='settings'),
]
