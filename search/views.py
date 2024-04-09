from django.views.generic import ListView
from cloths.models import Cloth


class SearchResultsView(ListView):
    model = Cloth
    template_name = "search/search_results.html"
    context_object_name = 'cloths'

    def get_queryset(self):  # new
        search_query = self.request.GET.get("q")
        if not search_query:
            search_query = ""
        object_list = self.model.objects.filter(
            title__icontains=search_query
        ) | self.model.objects.filter(
            description__icontains=search_query
        )
        return object_list

    def get_context_data(self, **kwargs):
        context = super(SearchResultsView, self).get_context_data(**kwargs)
        context.update({
            'search_query': self.request.GET.get("q"),
        })
        return context


class FilterResultsView(ListView):
    model = Cloth
    template_name = "search/filter_results.html"
    context_object_name = 'cloths'

    def get_queryset(self):  # new
        filter_query = self.request.GET.get("q")
        if not filter_query:
            filter_query = ""
        object_list = self.model.objects.filter(
            category=filter_query
        )
        print(filter_query)
        return object_list
