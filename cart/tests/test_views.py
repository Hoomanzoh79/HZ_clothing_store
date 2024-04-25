from django.test import TestCase
from django.urls import reverse
from django.template.defaultfilters import slugify

from cloths.models import Cloth


CLOTH_VALID_DATA =  {
            "title" : "test cloth",
            "slug" : slugify("test cloth"),
            "description" : "test description",
            "price" : 1500000,
            "sizes": "XL",
            "gender": "male",
            "sales":0,
            "inventory":20,
            "category":"pants",
            "brand":"adidas",
        }

class TestCartView(TestCase):
    def setUp(self):
        self.cloth = Cloth.objects.create(**CLOTH_VALID_DATA)
    
    def test_add_to_cart_view(self):
        url = reverse("cart:cart_add",args=[self.cloth.id])
        response = self.client.post(url)
        self.assertEquals(response.status_code,302)
    
    def test_cart_detail_view(self):
        url = reverse("cart:cart_detail")
        response = self.client.get(url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,"cart/cart_detail.html")
    
    def test_cart_clear_view(self):
        url = reverse("cart:cart_clear")
        response = self.client.get(url)
        self.assertEquals(response.status_code,302)
        self.assertRedirects(response,reverse("index"))
    
    def test_remove_form_cart_view(self):
        url = reverse("cart:cart_remove",args=[self.cloth.id])
        response = self.client.get(url)
        self.assertEquals(response.status_code,302)
        self.assertRedirects(response,reverse("cart:cart_detail"))