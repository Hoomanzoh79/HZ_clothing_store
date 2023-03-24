from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.HomePageView.as_view(), name='home'),
    path('aboutus/', views.AboutUsPageView.as_view(), name='about_us'),
]
