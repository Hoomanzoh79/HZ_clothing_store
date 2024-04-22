from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('add_to_cart/<int:cloth_id>/', views.add_to_cart_view, name='cart_add'),
    path('', views.cart_detail_view, name='cart_detail'),
    path('remove_from_cart/<int:cloth_id>/', views.remove_from_cart_view, name='cart_remove'),
    path('clear/', views.clear_cart, name='cart_clear'),
]