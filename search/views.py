from django.views.generic import ListView
from cloths.models import Cloth

class SearchResultsView(ListView):
    model = Cloth
    template_name = "search/search_results.html"
    context_object_name = 'cloths'

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = self.model.objects.filter(
            title__icontains=query
        ) | self.model.objects.filter(
            description__icontains=query
        ) 
        return object_list
