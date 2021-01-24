import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView

from core.global_db import db
from telegram import forms as tg_forms
from telegram import tasks
from .json_response_mixin import JsonResponseFormMixin


class TelegramChannelAddView(LoginRequiredMixin, JsonResponseFormMixin, FormView, ):
    template_name = 'dashboard/add_telegram_channel.html'
    # model = tg_models.AddChannelRequest
    form_class = tg_forms.AddChannelRequestForm
    context_object_name = 'tg_channel'
    # fields = ('username', 'telegram_account', 'chat',)
    login_url = 'login'
    # success_url = reverse_lazy('dashboard:accounts')
    success_url = '.'

    def form_invalid(self, form):
        return super().form_invalid(form)

    def form_valid(self, form):
        form.instance.user = self.request.user

        if db.telegram.undone_add_channel_request_exists(
                db_site_user=self.request.user,
                channel_username=str(form.instance.channel_username).lower()
        ):
            form.add_error(None, 'You have made a request for this channel already.')
            return super().form_invalid(form)

        response = json.loads(
            tasks.request_add_tg_channel(
                channel_username=form.instance.channel_username,
                db_tg_account_admin_id=form.instance.admin.pk,
                db_userid=self.request.user.pk,
            )
        )
        self.extra_data.update(response)

        if not response['success']:
            form.add_error(None, response['message'])
            return super().form_invalid(form)

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['telegram_accounts'] = db.telegram.get_all_available_telegram_accounts()
        return context
