from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth import get_user_model
from django import forms
from django.utils.translation import gettext as _

from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email',)


class ProfileChangeForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("first_name", "last_name",
                  "address", "phone_number",
                  )
        widgets = {
            'phone_number': forms.Textarea(attrs={'rows': 0, 'placeholder': _('Example : 09121111111 ')}),
            'address': forms.Textarea(attrs={'rows': 3}),
        }
