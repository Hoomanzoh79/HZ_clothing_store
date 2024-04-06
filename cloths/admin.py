from django.contrib import admin
from .models import Cloth, Comment
from jalali_date.admin import ModelAdminJalaliMixin


@admin.register(Cloth)
class ClothAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['id','title', 'price', 'season', 'gender', 'sales','inventory',"inventory_status"]
    list_per_page = 10
    list_editable = ['price','inventory']
    ordering = ['-datetime_created']
    list_filter = ['datetime_created','gender','season']

    def inventory_status(self,cloth):
        if cloth.inventory == 0 :
            return "sold out"
        elif cloth.inventory >= 10 :
            return "High"
        elif cloth.inventory < 10:
            return "Low"



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','cloth', 'author', 'body', 'active',]
    list_per_page = 10
    list_editable = ['active']
    ordering = ['-datetime_created']
    list_filter = ['datetime_created','active']
    list_select_related = ['cloth']