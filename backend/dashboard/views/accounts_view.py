from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from core.global_db import db


class AccountsView(LoginRequiredMixin, ListView):
    template_name = 'dashboard/accounts.html'
    context_object_name = 'tg_channels'
    login_url = 'login'

    def get_queryset(self):
        self.queryset = db.telegram.get_user_telegram_channels(
            db_site_user=self.request.user
        )
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
