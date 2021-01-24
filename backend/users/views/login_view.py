from django.urls import reverse_lazy
from django.views import generic

from ..forms import LoginForm
from django.contrib.auth import authenticate, login


class LoginView(generic.FormView):
    form_class = LoginForm
    success_url = reverse_lazy('dashboard:main')
    template_name = 'users/login.html'

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, 'not valid')
            return super().form_invalid(form)
