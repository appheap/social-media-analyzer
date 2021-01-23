from django.http import JsonResponse

from users.models import SiteUser


# todo: remove this code
def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': SiteUser.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'

    return JsonResponse(data)
