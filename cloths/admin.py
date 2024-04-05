from django.contrib import admin
from .models import Cloth, Comment
from jalali_date.admin import ModelAdminJalaliMixin


@admin.register(Cloth)
class ClothAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'price', 'active', 'season', 'gender', 'sales',  ]
    list_per_page = 10
    list_editable = ['price','active']
    ordering = ['-datetime_created']



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['cloth', 'author', 'body', 'active',]
    list_per_page = 10
    list_editable = ['active']
    ordering = ['-datetime_created']