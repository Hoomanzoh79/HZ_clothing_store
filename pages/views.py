from django.views.generic import TemplateView
from django.shortcuts import render


class AboutUsPageView(TemplateView):
    template_name = 'pages/about_us.html'



def handler404(request, exception):
    context = {}
    response = render(request, "pages/404.html", context=context)
    response.status_code = 404
    return response