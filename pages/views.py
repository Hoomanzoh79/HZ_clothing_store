from django.shortcuts import render
from django.views import generic

from cloths.models import Cloth, Comment


class AboutUsPageView(generic.TemplateView):
    template_name = 'pages/about_us.html'


def handler404(request, exception):
    context = {}
    response = render(request, "pages/404.html", context=context)
    response.status_code = 404
    return response


class IndexView(generic.ListView):
    queryset = Cloth.objects.filter(inventory__gte=1).order_by('-datetime_created')
    template_name = "index.html"
    context_object_name = 'cloths'