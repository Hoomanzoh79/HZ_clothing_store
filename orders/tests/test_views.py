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
        self.user = CustomUser.objects.create(email="testemail@email.com",password="*7S^dasadDSA1")
        self.cloth = Cloth.objects.create(**CLOTH_VALID_DATA)
    
    def test_order_create_view_unauthorized(self):
        url = reverse('orders:order_create')
        response = self.client.post(url)
        self.assertEquals(response.status_code,302)
        self.assertRedirects(response,reverse("account_login"))

    def test_order_create_view_authorized_empty_cart(self):
        self.client.force_login(user=self.user)
        url = reverse('orders:order_create')
        response = self.client.post(url)
        self.assertEquals(response.status_code,302)
        self.assertRedirects(response,reverse("cart:cart_detail"))
    
    # def test_order_create_view_authorized(self):
    #     self.client.force_login(user=self.user)
    #     cart = Cart(self.client)
    #     cart.save()
    #     cart.add(self.cloth,quantity=2,size="S")
    #     url = reverse('orders:order_create')
    #     response = self.client.post(url)
    #     self.assertEquals(response.status_code,302)
    #     self.assertRedirects(response,reverse("payment:payment_process"))