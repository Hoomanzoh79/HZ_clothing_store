from django.test import TestCase

from orders.forms import OrderForm

class TestOrderForm(TestCase):
    def test_order_form_valid_data(self):
        order_form = OrderForm(data={
            "first_name" : "test firstname",
            "last_name": "test lastname",
            "phone_number" :"09361958721",
            "address":"test address",
            "postal_code":"3149637441"
        })
        self.assertTrue(order_form.is_valid())
        self.assertIn("first_name", order_form.fields)
    
    def test_order_form_invalid_phone_number(self):
        order_form = OrderForm(data={
            'first_name' : "test firstname",
            'last_name': "test lastname",
            'phone_number':"9361958721",
            'address':"test address",
            'postal_code':'3149637441',
        })
        self.assertFalse(order_form.is_valid())
        self.assertIn('phone_number', order_form.errors.keys())
    
    def test_order_form_invalid_postal_code(self):
        order_form = OrderForm(data={
            'first_name' : "test firstname",
            'last_name': "test lastname",
            'phone_number':"09361958721",
            'address':"test address",
            'postal_code':'3149637441dsa',
        })
        self.assertFalse(order_form.is_valid())
        self.assertIn('postal_code', order_form.errors.keys())
    
    def test_order_form_invalid_data(self):
        order_form = OrderForm(data={})
        self.assertFalse(order_form.is_valid())
