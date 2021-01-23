from django.contrib.auth.forms import UserChangeForm

from ..models import SiteUser


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = SiteUser
        fields = ('username', 'email', 'first_name', 'last_name', 'timezone')
