from django.test import TestCase
from django.template.defaultfilters import slugify


from cloths.models import Cloth,Comment


class TestCommentModel(TestCase):
    def setUp(self):
        self.valid_data = {
            "title" : "test cloth",
            "description" : "test description",
            "slug" : slugify("title"),
            "price" : 1500000,
            "sizes": (('S', 'S')),
            "gender": "male",
            "sales":0,
            "inventory":20,
            "category":"pants",
            "brand":"adidas",
        }

    def test_create_cloth_valid_data(self):
        cloth = Cloth.objects.create(self.valid_data)
        self.assertTrue(Cloth.objects.filter(pk=cloth.id).exists())
        self.assertEquals(cloth.title,'test cloth')
        self.assertEquals(cloth.objects.count(),1)
