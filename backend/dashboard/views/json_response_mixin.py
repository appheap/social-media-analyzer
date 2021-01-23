from django.http import JsonResponse
from django.views.generic.edit import FormMixin


class JsonResponseFormMixin(FormMixin):
    def __init__(self):
        self.extra_data = {}

    def form_valid(self, form):
        if self.request.is_ajax():
            return JsonResponse(self.extra_data)
        return super(JsonResponseFormMixin, self).form_valid(form)

    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        return super(JsonResponseFormMixin, self).form_valid(form)
