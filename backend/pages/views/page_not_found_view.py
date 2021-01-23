from urllib.parse import quote

from django.http import (
    HttpResponseNotFound,
)
from django.template import Context, Engine, TemplateDoesNotExist, loader
from django.views.decorators.csrf import requires_csrf_token

from core.globals import logger

from .error_pages import ERROR_404_TEMPLATE_NAME, ERROR_PAGE_TEMPLATE


@requires_csrf_token
def page_not_found(request, exception, template_name=ERROR_404_TEMPLATE_NAME):
    exception_repr = exception.__class__.__name__
    # Try to get an "interesting" exception message, if any (and not the ugly
    # Resolver404 dictionary)
    try:
        message = exception.args[0]
    except (AttributeError, IndexError):
        pass
    else:
        if isinstance(message, str):
            exception_repr = message
    context = {
        'request_path': quote(request.path),
        'exception': exception_repr,
    }
    try:
        template = loader.get_template(template_name)
        body = template.render(context, request)
        content_type = None  # Django will use 'text/html'.
    except TemplateDoesNotExist as e:
        logger.exception(e)
        if template_name != ERROR_404_TEMPLATE_NAME:
            # Reraise if it's a missing custom template.
            raise
        # Render template (even though there are no substitutions) to allow
        # inspecting the context in tests.
        template = Engine().from_string(
            ERROR_PAGE_TEMPLATE % {
                'title': 'Not Found',
                'details': 'The requested resource was not found on this server.',
            },
        )
        body = template.render(Context(context))
        content_type = 'text/html'
    except Exception as e:
        logger.exception(e)
        body = ""
        content_type = 'text/html'

    return HttpResponseNotFound(body, content_type=content_type)
