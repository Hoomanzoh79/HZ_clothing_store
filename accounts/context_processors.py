from .models import Profile
from django.shortcuts import get_object_or_404


def profile(request):
    user = request.user
    return {
        'profile': get_object_or_404(Profile, user_id=user.id),
    }
