from django.test import TestCase
from django.urls import reverse,resolve


from cart.views import (add_to_cart_view,
                        cart_detail_view,
                        clear_cart,
                        remove_from_cart_view)


class CartUrl(TestCase):
    def test_add_to_cart_url_resolve(self):
        url = reverse("cart:cart_add",args=[1])
        self.assertEquals(resolve(url).func,add_to_cart_view)
    
    def test_cart_detail_url_resolve(self):
        url = reverse("cart:cart_detail")
        self.assertEquals(resolve(url).func,cart_detail_view)
    
    def test_cart_clear_url_resolve(self):
        url = reverse("cart:cart_clear")
        self.assertEquals(resolve(url).func,clear_cart)
    
    def test_remove_from_cart_url_resolve(self):
        url = reverse("cart:cart_remove",args=[1])
        self.assertEquals(resolve(url).func,remove_from_cart_view)