from django.http import HttpResponseForbidden
from django.template import TemplateDoesNotExist, loader
from django.views.decorators.csrf import requires_csrf_token

from .error_pages import ERROR_403_TEMPLATE_NAME, ERROR_PAGE_TEMPLATE


@requires_csrf_token
def permission_denied(request, exception, template_name=ERROR_403_TEMPLATE_NAME):
    try:
        template = loader.get_template(template_name)
    except TemplateDoesNotExist:
        if template_name != ERROR_403_TEMPLATE_NAME:
            # Reraise if it's a missing custom template.
            raise
        return HttpResponseForbidden(
            ERROR_PAGE_TEMPLATE % {'title': '403 Forbidden', 'details': ''},
            content_type='text/html',
        )
    return HttpResponseForbidden(
        template.render(request=request, context={'exception': str(exception)})
    )
