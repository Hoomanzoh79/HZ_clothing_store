from django.contrib import admin
from .models import Cloth, Comment
from jalali_date.admin import ModelAdminJalaliMixin


@admin.register(Cloth)
class ClothAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'price', 'active', 'season', 'gender', 'sales',  ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['cloth', 'author', 'body', 'active',]