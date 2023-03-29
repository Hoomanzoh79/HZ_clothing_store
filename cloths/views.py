from django.shortcuts import render
from django.views import generic
from .models import Cloth


class ClothsListView(generic.ListView):
    queryset = Cloth.objects.filter(active=True)
    template_name = 'cloths/cloths_list.html'
    context_object_name = 'cloths'


class ClothDetailView(generic.DetailView):
    model = Cloth
    template_name = 'cloths/cloth_detail.html'
    context_object_name = 'cloth'
