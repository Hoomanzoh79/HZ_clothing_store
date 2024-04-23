from django.test import TestCase

from cart.forms import AddToCartForm


class TestCartForm(TestCase):
    def test_add_to_cart_form_valid_data(self):
        add_to_cart_form = AddToCartForm(data={
            'quantity' : 2,
            'size': "L",
        })
        self.assertTrue(add_to_cart_form.is_valid())
    
    def test_add_to_cart_form_invalid_data(self):
        add_to_cart_form = AddToCartForm(data={})
        self.assertFalse(add_to_cart_form.is_valid())