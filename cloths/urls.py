from django.urls import path
from . import views

urlpatterns = [
    path('', views.ClothsListView.as_view(), name='cloths_list'),
]