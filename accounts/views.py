from django.shortcuts import redirect
from django.views import generic
from .models import Profile
from .forms import ProfileChangeForm
from django.urls import reverse
from django.contrib import messages
from django.utils.translation import gettext as _
from django.contrib.auth.mixins import LoginRequiredMixin


class ProfileUpdateView(LoginRequiredMixin, generic.UpdateView):
    form_class = ProfileChangeForm
    template_name = "accounts/profile_update.html"

    def get_success_url(self):
        messages.success(self.request, _('Your profile has been updated successfully'))
        return reverse("profile_update")

    def get_object(self):
        user = self.request.user
        try:
            profile = Profile.objects.get(user_id=user.id)
        except Profile.DoesNotExist:
            profile = Profile.objects.create(user=user)
        return profile
