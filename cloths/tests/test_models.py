from django.test import TestCase
from django.template.defaultfilters import slugify

from cloths.models import Cloth,Comment
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

class TestClothModel(TestCase):
    def test_create_cloth(self):
        cloth = Cloth.objects.create(**CLOTH_VALID_DATA)
        self.assertTrue(Cloth.objects.filter(pk=cloth.id).exists())
        self.assertTrue(Cloth.objects.filter(slug=cloth.slug).exists())
        self.assertEquals(Cloth.objects.count(),1)
        self.assertEquals(cloth.title,"test cloth")
        self.assertEquals(cloth.slug,slugify(cloth.title))
    
class TestCommentModel(TestCase):
    def setUp(self):
        self.cloth = Cloth.objects.create(**CLOTH_VALID_DATA)
        self.author = CustomUser.objects.create(email="testemail@email.com",password="*7S^dasadDSA1")
        self.comment = Comment.objects.create(author=self.author,cloth=self.cloth,body="test comment")
    
    def test_create_comment(self):
        self.assertEquals(Comment.objects.count(),1)
        self.assertTrue(Comment.objects.filter(pk=self.comment.id).exists())
        self.assertTrue(Comment.objects.filter(cloth=self.cloth).exists())
        self.assertEquals(self.comment.body,"test comment")
