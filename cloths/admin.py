from django.contrib import admin
from .models import Cloths


@admin.register(Cloths)
class ClothAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'active', 'season', 'gender', ]