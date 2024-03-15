from django.shortcuts import render
from django.views import generic
from .models import Profile
from .forms import ProfileChangeForm
from django.urls import reverse


class ProfileUpdateView(generic.UpdateView):
    model = Profile
    form_class = ProfileChangeForm
    template_name = "accounts/profile_update.html"

    def get_success_url(self):
        return reverse("index")
