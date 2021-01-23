from django.urls import reverse_lazy
from django.views import generic

from ..forms import CustomUserCreationForm


# Create your views here.

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('users:login')
