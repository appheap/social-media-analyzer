from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class MainDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/dashboard.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['current_url'] = get_url(self.request)
        return context
