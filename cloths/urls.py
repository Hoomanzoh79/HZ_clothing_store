from django.urls import path
from . import views

urlpatterns = [
    path("",views.IndexView.as_view(),name="index"),
    path('list/', views.ClothsListView.as_view(), name='cloths_list'),
    path('list/female/',views.FemaleView.as_view(),name='female_list'),
    path('list/male/',views.maleView.as_view(),name='male_list'),
    path('<int:pk>/', views.ClothDetailView.as_view(), name='cloth_detail'),
    path('comment/<int:cloth_id>/', views.CommentCreateView.as_view(), name='comment_create'),
]