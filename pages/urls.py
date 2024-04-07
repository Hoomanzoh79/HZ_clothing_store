from django.urls import path, include
from . import views

urlpatterns = [
    path('aboutus/', views.AboutUsPageView.as_view(), name='about_us'),
    path("", views.IndexView.as_view(), name="index"),
]
