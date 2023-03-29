from django.urls import path
from . import views

urlpatterns = [
    path('', views.ClothsListView.as_view(), name='cloths_list'),
    path('<int:pk>/', views.ClothDetailView.as_view(), name='cloth_detail'),
]