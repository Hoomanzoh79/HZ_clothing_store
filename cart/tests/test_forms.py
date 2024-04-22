from django.test import TestCase

from cart.forms import AddToCartForm


class TestCommentForm(TestCase):
    def test_add_to_cart_form_valid_data(self):
        comment_form = AddToCartForm(data={
            'quantity' : 2,
            'size': "L",
        })
        self.assertTrue(comment_form.is_valid())
    
    def test_add_to_cart_form_invalid_data(self):
        comment_form = AddToCartForm(data={})
        self.assertFalse(comment_form.is_valid())