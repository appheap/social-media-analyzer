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
        db_telegram_channels = db.telegram.get_user_telegram_channels(
            db_site_user=self.request.user
        )
        context['tg_channels'] = db_telegram_channels
        db_profile_photos = [db.telegram.get_latest_profile_photo(db_chat=db_channel.chat) for db_channel in
                             db_telegram_channels]
        context['profile_photos'] = db_profile_photos
        context['objects'] = list(zip(db_telegram_channels, db_profile_photos))

        return context
