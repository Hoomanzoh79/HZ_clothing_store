from django.urls import path
from . import views

app_name = 'search'

urlpatterns = [
    path("results/",views.SearchResultsView.as_view(),name='search_results'),
]