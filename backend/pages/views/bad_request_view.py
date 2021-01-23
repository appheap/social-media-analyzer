from django.http import HttpResponseBadRequest
from django.template import TemplateDoesNotExist, loader
from django.views.decorators.csrf import requires_csrf_token

from .error_pages import ERROR_PAGE_TEMPLATE, ERROR_400_TEMPLATE_NAME


@requires_csrf_token
def bad_request(request, exception, template_name=ERROR_400_TEMPLATE_NAME):
    try:
        template = loader.get_template(template_name)
    except TemplateDoesNotExist:
        if template_name != ERROR_400_TEMPLATE_NAME:
            # Reraise if it's a missing custom template.
            raise
        return HttpResponseBadRequest(
            ERROR_PAGE_TEMPLATE % {'title': 'Bad Request (400)', 'details': ''},
            content_type='text/html',
        )
    # No exception content is passed to the template, to not disclose any sensitive information.
    return HttpResponseBadRequest(template.render())
