from django.contrib import admin
from .models import Order, OrderItem
from jalali_date.admin import ModelAdminJalaliMixin


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    list_display = ['order', 'cloth', 'quantity', 'price', ]
    extra = 1


@admin.register(Order)
class OrderAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['id','user', 'first_name', 'last_name', 'datetime_created', 'is_paid','is_active','total_price']
    inlines = [
        OrderItemInline
    ]
    list_per_page = 10
    list_editable = ['is_active']
    ordering = ['-datetime_created']
    list_filter = ['datetime_created','is_paid','is_active']

    def total_price(self,order):
        return sum(item.price * item.quantity for item in order.items.all())


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'cloth', 'quantity','size','price']