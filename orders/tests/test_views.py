from django.test import TestCase
from django.urls import reverse
from django.template.defaultfilters import slugify

from accounts.models import CustomUser
from cart.cart import Cart
from cloths.models import Cloth

CLOTH_VALID_DATA =  {
            "title" : "test cloth",
            "slug" : slugify("test cloth"),
            "description" : "test description",
            "price" : 1500000,
            "sizes": "S",
            "gender": "male",
            "sales":0,
            "inventory":20,
            "category":"pants",
            "brand":"adidas",
        }

class TestOrderView(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(email="testorder@gmail.com",password="*7S^dasadDSA1")
        self.cloth = Cloth.objects.create(**CLOTH_VALID_DATA)
    
    def test_order_create_view_unauthorized(self):
        """redirects the user to login page,POST request or GET request doesn't matter"""
        url = reverse('orders:order_create')
        response = self.client.post(url)
        self.assertEquals(response.status_code,302)
        self.assertRedirects(response,reverse("account_login"))

    def test_order_create_view_authorized_empty_cart(self):
        """redirects the user to cart_detail because cart is empty,here user can only use GET request
        (we won't give away the form so they can't use POST request)"""
        self.client.force_login(user=self.user)
        url = reverse('orders:order_create')
        response = self.client.get(url)
        self.assertEquals(response.status_code,302)
        self.assertRedirects(response,reverse("cart:cart_detail"))
    
    def test_order_create_view_authorized(self):
        """cart is not empty and user is authenticated"""
        self.client.force_login(user=self.user)
        cart = Cart(self.client)
        cart.add(self.cloth,quantity=2,size="S")
        url = reverse('orders:order_create')
        response = self.client.post(url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,"orders/order_create.html")