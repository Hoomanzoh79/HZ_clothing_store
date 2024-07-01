from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from django.utils.translation import gettext as _


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="orders")
    is_paid = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    first_name = models.CharField(max_length=50,verbose_name=_('First name'))
    last_name = models.CharField(max_length=50,verbose_name=_('Last name'))
    address = models.TextField(verbose_name=_('Address'))
    postal_code = models.CharField(max_length=10,
                                   validators=[RegexValidator(regex="^(?!(\d)\1{3})[13-9]{4}[1346-9][ -]?[013-9]{5}$|^$")],
                                   verbose_name=_("Postal code"),null=True
                                   )
    phone_number = models.CharField(max_length=12,
                                    validators=[RegexValidator(regex="^[0][9][0-9][0-9]{8,8}$")],
                                    verbose_name=_('Phone number')
                                    )

    order_notes = models.CharField(max_length=700, blank=True,verbose_name=_('Order notes'))

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Order : {self.id}'

    def get_total_price(self):
        return sum(item.price * item.quantity for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    cloth = models.ForeignKey('cloths.Cloth', on_delete=models.CASCADE, related_name='order_items')
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(default=1)
    size = models.CharField(max_length=10)
    color = models.CharField(max_length=25,null=True)

    def __str__(self):
        return f'OrderItem {self.id}: {self.cloth} x {self.quantity} (price:{self.price})'

