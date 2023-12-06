from cloths.models import Cloth
from django.contrib import messages
from django.utils.translation import gettext as _


class Cart:
    def __init__(self, request):
        """
        Initialize the cart
        """
        self.request = request

        self.session = request.session

        cart = self.session.get('cart')

        if not cart:
            cart = self.session['cart'] = {}

        self.cart = cart

    def add(self,cloth,size,quantity=1, replace_current_quantity=False):
        """
        Add the specified product to the cart if it exists
        """
        cloth_id = str(cloth.id)

        if cloth_id not in self.cart:
            self.cart[cloth_id] = {'quantity': 0}
        if replace_current_quantity:
            self.cart[cloth_id]['quantity'] = quantity
        else:
            self.cart[cloth_id]['quantity'] += quantity
        
        self.cart[cloth_id]['size'] = size
        messages.success(self.request, _('Product has been added successfully to the cart'))

        self.save()

    def remove(self, cloth):
        """
        Remove a product from the cart
        """
        cloth_id = str(cloth.id)

        if cloth_id in self.cart:
            del self.cart[cloth_id]
            messages.success(self.request, _('Product has been removed successfully from the cart'))
            self.save()

    def save(self):
        """
        Mark session as modified
        """
        self.session.modified = True

    def __iter__(self):
        cloth_ids = self.cart.keys()
        cloths = Cloth.objects.filter(id__in=cloth_ids)
        cart = self.cart.copy()
        for cloth in cloths:
            cart[str(cloth.id)]['cloth_obj'] = cloth
            # print(cart.values())
            # print(cart.keys())
        for item in self.cart.values():
            item['total_price'] = item['cloth_obj'].price * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session['cart']
        self.save()

    def get_total_price(self):
        return sum(item['cloth_obj'].price*item['quantity'] for item in self.cart.values())

    def is_empty(self):
        if self.cart:
            return False
        return True


