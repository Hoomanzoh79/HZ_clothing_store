from django.test import TestCase


from orders.forms import OrderForm
from cloths.forms import CommentForm
from accounts.models import CustomUser


class TestOrderForm(TestCase):
    def test_order_form_valid_data(self):
        order_form = OrderForm(data={
            'first_name' : "test firstname",
            'last_name': "test lastname",
            'phone_number':"09361958721",
            'address':"test address",
        })
        self.assertTrue(order_form.is_valid())
    
    def test_order_form_invalid_phone_number(self):
        order_form = OrderForm(data={
            'first_name' : "test firstname",
            'last_name': "test lastname",
            'phone_number':"9361958721",
            'address':"test address",
        })
        self.assertFalse(order_form.is_valid())
    
    def test_order_form_invalid_data(self):
        order_form = OrderForm(data={})
        self.assertFalse(order_form.is_valid())