from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from core.global_db import db
from core.globals import logger


class TelegramChannelManagementView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/telegram_channel_management.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        channel_id = context.get('channel_id', None)
        if channel_id is not None:
            db_channel = db.telegram.get_telegram_channel_by_id(channel_id=channel_id)
            context['channel'] = db_channel
            context['profile_photo'] = db.telegram.get_latest_profile_photo(
                db_chat=db_channel.chat) if db_channel else None
        return context
