from django.http import (
    HttpResponseServerError,
)
from django.template import TemplateDoesNotExist, loader
from django.views.decorators.csrf import requires_csrf_token

from .error_pages import ERROR_500_TEMPLATE_NAME, ERROR_PAGE_TEMPLATE


@requires_csrf_token
def server_error(request, template_name=ERROR_500_TEMPLATE_NAME):
    try:
        template = loader.get_template(template_name)
    except TemplateDoesNotExist:
        if template_name != ERROR_500_TEMPLATE_NAME:
            # Reraise if it's a missing custom template.
            raise
        return HttpResponseServerError(
            ERROR_PAGE_TEMPLATE % {'title': 'Server Error (500)', 'details': ''},
            content_type='text/html',
        )
    return HttpResponseServerError(template.render())
