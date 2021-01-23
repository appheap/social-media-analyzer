from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class SettingsView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/settings.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
