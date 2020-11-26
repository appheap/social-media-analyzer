from django.contrib.auth.models import AnonymousUser
from django.urls import resolve
from users import models as user_models


def full_user(request):
    try:
        if hasattr(request, 'user'):
            user = user_models.CustomUser.objects.get(pk=request.user.pk)
        else:
            user = AnonymousUser()
    except Exception as e:
        return {
            'full_user': AnonymousUser(),
        }

    return {
        'full_user': user,
    }


def current_url(request):
    try:
        lst = str(resolve(request.path_info).route).split('/')
        lst.pop()
    except Exception as e:
        lst = None
    return {
        'current_url': lst
    }
