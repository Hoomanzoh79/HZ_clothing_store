from django.views.generic import TemplateView

class AboutUsPageView(TemplateView):
    template_name = 'pages/about_us.html'
