from django.test import TestCase
from django.template.defaultfilters import slugify

from cart.forms import AddToCartForm
from cloths.models import Cloth

CLOTH_VALID_DATA = {
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

class TestCartForm(TestCase):
    def setUp(self):
        self.cloth = Cloth.objects.create(**CLOTH_VALID_DATA)

    def test_add_to_cart_form_valid_data(self):
        add_to_cart_form = AddToCartForm(pk=self.cloth.id,data={
            'quantity' : 2,
            'sizes': "XL",
        })
        self.assertTrue(add_to_cart_form.is_valid())
    
    def test_add_to_cart_form_invalid_size(self):
        add_to_cart_form = AddToCartForm(pk=self.cloth.id,data={
            'quantity' : 2,
            'sizes': "S",
        })
        self.assertFalse(add_to_cart_form.is_valid())
    
    def test_add_to_cart_form_invalid_data(self):
        add_to_cart_form = AddToCartForm(pk=self.cloth.id,data={})
        self.assertFalse(add_to_cart_form.is_valid())