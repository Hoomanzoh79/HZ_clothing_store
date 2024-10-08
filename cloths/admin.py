from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin
from django.utils.html import format_html
from django.utils.http import urlencode
from django.urls import reverse
from django.db.models import Count

from .models import Cloth, Comment,Color,Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['cloth','image']

class ImageInline(admin.TabularInline):
    model = Image

@admin.register(Cloth)
class ClothAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ['id','title','brand','price','category','season', 'gender', 'sales','inventory',"inventory_status","comments_count"]
    list_per_page = 10
    list_editable = ['price','inventory','category']
    ordering = ['-datetime_created']
    list_filter = ['datetime_created','gender','season','category']
    search_fields = ['title__istartswith','brand__istartswith']
    list_display_links = ['id','title']
    prepopulated_fields = {
        'slug' : ['title',]
    }
    readonly_fields = ['sales']

    def get_queryset(self, request):
        return super().get_queryset(request)\
        .prefetch_related('comments') \
        .annotate(comments_count=Count('comments'),
                  )

    def inventory_status(self,cloth):
        if cloth.inventory == 0 :
            return "sold out"
        elif cloth.inventory >= 10 :
            return "High"
        elif cloth.inventory < 10:
            return "Low"
    
    @admin.display(description='comments')
    def comments_count(self,cloth):
        url = (
            reverse('admin:cloths_comment_changelist') 
            + '?'
            + urlencode({
                'cloth__id': cloth.id,
            })
        )
        return format_html('<a href="{}">{}</a>', url, cloth.comments_count)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','cloth', 'author', 'active','body','datetime_created']
    list_per_page = 10
    list_editable = ['active']
    ordering = ['-datetime_created']
    list_filter = ['datetime_created','active']
    list_select_related = ['cloth']
    actions = ['active_comments']
    autocomplete_fields = ['cloth',]

    @admin.action(description='active comments')
    def active_comments(self,request,queryset):
        queryset.update(active=True)


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['color_name']