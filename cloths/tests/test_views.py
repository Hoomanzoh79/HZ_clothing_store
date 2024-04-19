from django.test import TestCase
from django.template.defaultfilters import slugify
from django.urls import reverse

from cloths.models import Cloth
from accounts.models import CustomUser

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

class TestClothView(TestCase):
    def setUp(self):
        self.cloth = Cloth.objects.create(**CLOTH_VALID_DATA)

    def test_cloths_list_view(self):
        url = reverse("cloths_list")
        response = self.client.get(url)
        self.assertEquals(response.status_code,200)
        self.assertNotEquals(response.status_code,404)
        self.assertContains(response,self.cloth.title)
        self.assertTemplateUsed("cloths/cloths_list.html")
    
    def test_cloth_detail_view_valid_slug(self):
        url = reverse("cloth_detail",kwargs={"slug":self.cloth.slug})
        response = self.client.get(url)
        self.assertEquals(response.status_code,200)
        self.assertNotEquals(response.status_code,404)
        self.assertContains(response,self.cloth.title)
        self.assertTemplateUsed("cloths/cloths_detail.html")

    def test_cloth_detail_view_invalid_slug(self):
        url = reverse("cloth_detail",kwargs={"slug":"-invalid-slug"})
        response = self.client.get(url)
        self.assertEquals(response.status_code,404)
        self.assertNotEquals(response.status_code,200)
