from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.views.generic.edit import FormMixin
from django.shortcuts import render

from cloths.models import Cloth
from .forms import ClothFilterForm


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


class CategoryFilterResultsView(ListView):
    model = Cloth
    template_name = "search/category_filter_results.html"
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

    def get_context_data(self, **kwargs):
        context = super(CategoryFilterResultsView, self).get_context_data(**kwargs)
        context.update({
            'filter_query': self.request.GET.get("q"),
        })
        return context


class FilterResultsView(FormMixin,ListView):
    model = Cloth
    template_name = "search/filter_results.html"

    def get(self, request, *args, **kwargs):
        form_class = ClothFilterForm
        self.form = self.get_form(form_class)
        self.category = self.request.GET.get("category")
        self.season = self.request.GET.get("season")
        self.gender = self.request.GET.get("gender")
        print(self.category)
        cloths = self.model.objects.filter(category=self.category)
        return render(request,template_name=self.template_name,context={'cloths':cloths})

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)