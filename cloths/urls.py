from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.ClothsListView.as_view(), name='cloths_list'),
    path('list/female/',views.FemaleView.as_view(),name='female_list'),
    path('list/male/',views.MaleView.as_view(),name='male_list'),
    path('list/highest-selling/',views.HighestSellingView.as_view(),name='highest_selling'),
    path('<int:pk>/', views.ClothDetailView.as_view(), name='cloth_detail'),
    path('comment/<int:cloth_id>/', views.CommentCreateView.as_view(), name='comment_create'),
]