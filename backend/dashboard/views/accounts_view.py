from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from telegram import models as tg_models


class AccountsView(LoginRequiredMixin, ListView):
    template_name = 'dashboard/accounts.html'
    # queryset = tg_models.TelegramChannel.objects.all()
    context_object_name = 'tg_channels'
    login_url = 'login'

    def get_queryset(self):
        self.queryset = tg_models.TelegramChannel.objects.filter(site_user=self.request.user)
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
