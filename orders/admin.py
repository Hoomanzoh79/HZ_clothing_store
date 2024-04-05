from django.contrib import admin
from .models import Order, OrderItem
from jalali_date.admin import ModelAdminJalaliMixin


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    list_display = ['order', 'cloth', 'quantity', 'price', ]
    extra = 1


@admin.register(Order)
class OrderAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'datetime_created', 'is_paid','is_active',]
    inlines = [
        OrderItemInline
    ]
    list_per_page = 10
    list_editable = ['is_active']
    ordering = ['-datetime_created']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'cloth', 'quantity', 'price', ]