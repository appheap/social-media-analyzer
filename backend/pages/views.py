from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
from backend.core.globals import logger


class HomePageView(TemplateView):
    # extra_context = {'test': "it's a test"}
    template_name = 'pages/home.html'


# def home(request):
#     return HttpResponse(loader.get_template('pages/home.html').render({}, request))


from urllib.parse import quote

from django.http import (
    HttpResponseBadRequest, HttpResponseForbidden, HttpResponseNotFound,
    HttpResponseServerError,
)
from django.template import Context, Engine, TemplateDoesNotExist, loader
from django.views.decorators.csrf import requires_csrf_token

ERROR_400_TEMPLATE_NAME = 'pages/page-400.html'
ERROR_403_TEMPLATE_NAME = 'pages/page-403.html'
ERROR_404_TEMPLATE_NAME = 'pages/page-404.html'
ERROR_500_TEMPLATE_NAME = 'pages/page-500.html'
ERROR_PAGE_TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
  <title>%(title)s</title>
</head>
<body>
  <h1>%(title)s</h1><p>%(details)s</p>
</body>
</html>
"""


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
