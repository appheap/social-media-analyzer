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
            context['channel'] = db.telegram.get_telegram_channel_by_id(channel_id=channel_id)
        return context
