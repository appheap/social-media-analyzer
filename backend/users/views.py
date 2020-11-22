from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm, LoginForm
from backend.users.models import CustomUser
from django.http import JsonResponse


# Create your views here.

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('users:login')


class LoginView(generic.FormView):
    form_class = LoginForm
    success_url = reverse_lazy('dashboard:main')
    template_name = 'users/login.html'

    def form_valid(self, form):
        from django.contrib.auth import authenticate, login
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, 'not valid')
            return super().form_invalid(form)


# todo: remove this code
def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': CustomUser.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'

    return JsonResponse(data)
