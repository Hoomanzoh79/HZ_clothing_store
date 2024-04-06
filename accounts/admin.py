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
    list_display = ('id','user','first_name','last_name','phone_number','datetime_created')
    ordering = ['-id']
    list_per_page = 10
    search_fields = ['user']
    list_select_related = ['user']
    list_filter = ['datetime_created']