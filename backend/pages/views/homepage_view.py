from django.views.generic import TemplateView


# Create your views here.


class HomePageView(TemplateView):
    # extra_context = {'test': "it's a test"}
    template_name = 'pages/home.html'
