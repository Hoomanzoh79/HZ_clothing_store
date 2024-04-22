from django.test import TestCase
from django.template.defaultfilters import slugify
from django.test import TestCase, RequestFactory, Client
from django.contrib.auth.models import User, AnonymousUser
from django.urls import reverse

from cloths.models import Cloth
from cart.cart import Cart


CLOTH_VALID_DATA1 = {
            "title" : "test cloth 1",
            "slug" : slugify("test cloth 1"),
            "description" : "test description 1",
            "price" : 1500000,
            "sizes": "XL",
            "gender": "male",
            "sales":0,
            "inventory":20,
            "category":"pants",
            "brand":"adidas",
        }

CLOTH_VALID_DATA2 = {
            "title" : "test cloth 2",
            "slug" : slugify("test cloth 2"),
            "description" : "test description 2",
            "price" : 1500000,
            "sizes": "L",
            "gender": "female",
            "sales":0,
            "inventory":20,
            "category":"pants",
            "brand":"adidas",
        }


class TestCart(TestCase):
    def setUp(self):
        self.cloth1 = Cloth.objects.create(**CLOTH_VALID_DATA1)
        self.cloth2 = Cloth.objects.create(**CLOTH_VALID_DATA2)
        self.factory = RequestFactory()
    
    def test_add_cloth_to_cart(self):
        cart = Cart(self.client)
        cart.add(self.cloth1,quantity=1,size="XL")
        for item in cart:
            quantity = item["quantity"]
            size = item["size"]
        self.assertEquals(len(cart), 1)
        self.assertEquals(quantity, 1)
        self.assertEquals(size, "XL")
    
    def test_add_multiple_cloths_to_cart(self):
        cart = Cart(self.client)
        cart.add(self.cloth1,quantity=1,size="XL")
        cart.add(self.cloth2, quantity=2,size="L")
        self.assertEquals(len(cart), 3)
    
    def test_remove_cloth_from_cart(self):
        cart = Cart(self.client)
        cart.add(self.cloth1,quantity=2,size="XL")
        cart.remove(self.cloth1)
        self.assertEquals(len(cart), 0)
    
    # def test_clear_cart(self):
    #     url = reverse("cart:cart_detail")
    #     cart = Cart(self.client.get(url))
    #     cart.add(self.cloth1,quantity=1,size="XL")
    #     cart.add(self.cloth2, quantity=2,size="L")
    #     cart.clear()
    #     self.assertEquals(len(cart),0)