from django.urls import path
from . import views

urlpatterns = [
    path("update/",views.ProfileUpdateView.as_view(), name="profile_update"),
]