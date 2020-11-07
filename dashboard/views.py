import json

from django.core import exceptions
from django.http import HttpResponse, JsonResponse
from django.urls import resolve, reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import FormView
from django.views.generic.edit import FormMixin

from telegram.client.client_utils import BaseResponse
from users import models as user_models
from telegram import models as tg_models
from django.contrib.auth.mixins import LoginRequiredMixin
from telegram import forms as tg_forms
from social_media_analyzer.globals import logger

from telegram import tasks


# Create your views here.

class JsonResponseFormMixin(FormMixin):
    def __init__(self):
        self.extra_data = {}

    def form_valid(self, form):
        if self.request.is_ajax():
            return JsonResponse(self.extra_data)
        return super(JsonResponseFormMixin, self).form_valid(form)

    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        return super(JsonResponseFormMixin, self).form_valid(form)


class MainDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/dashboard.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['current_url'] = get_url(self.request)
        return context


class AccountsView(LoginRequiredMixin, ListView):
    template_name = 'dashboard/accounts.html'
    # queryset = tg_models.TelegramChannel.objects.all()
    context_object_name = 'tg_channels'
    login_url = 'login'

    def get_queryset(self):
        self.queryset = tg_models.TelegramChannel.objects.filter(custom_user=self.request.user)
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


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
        # logger.info(form.instance.__dict__)
        form.instance.custom_user = self.request.user

        try:
            tg_models.AddChannelRequest.objects.get(done=False,
                                                    channel_username=str(form.instance.channel_username).lower(),
                                                    custom_user=self.request.user, )
        except exceptions.ObjectDoesNotExist as e:
            logger.exception(e)
            response = json.loads(
                tasks.request_add_tg_channel(
                    channel_username=form.instance.channel_username,
                    db_tg_account_admin_id=form.instance.telegram_account.pk,
                    db_userid=self.request.user.pk,
                )
            )
            self.extra_data.update(response)

            if not response['success']:
                form.add_error(None, response['message'])
                return super().form_invalid(form)
        else:
            form.add_error(None, 'You have made a request for this channel already.')
            return super().form_invalid(form)

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['telegram_accounts'] = tg_models.TelegramAccount.objects.all()
        return context


class SettingsView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/settings.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
