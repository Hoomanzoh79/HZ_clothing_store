from django.contrib import admin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser,Profile
from django.contrib.auth.admin import UserAdmin


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ('id','email', 'username',
                    'is_staff','is_superuser',
                    'is_active',
                    )
    ordering = ['-id']
    list_editable = ['is_active']
    list_per_page = 10


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ('id','user','first_name','last_name','phone_number',)
    ordering = ['-id']
    list_per_page = 10
    list_select_related = ['user']