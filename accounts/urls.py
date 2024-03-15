from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>/update/",views.ProfileUpdateView.as_view(),name="profile_update"),
]