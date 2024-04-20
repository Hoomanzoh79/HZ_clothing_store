from django.test import TestCase
from django.test import Client
from django.template.defaultfilters import slugify
from django.urls import reverse

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

class TestClothView(TestCase):
    def setUp(self):
        self.cloth = Cloth.objects.create(**CLOTH_VALID_DATA)

    def test_cloths_list_view(self):
        url = reverse("cloths_list")
        response = self.client.get(url)
        self.assertEquals(response.status_code,200)
        self.assertContains(response,self.cloth.title)
        self.assertTemplateUsed("cloths/cloths_list.html")
    
    def test_cloth_detail_view_valid_slug(self):
        url = reverse("cloth_detail",kwargs={"slug":self.cloth.slug})
        response = self.client.get(url)
        self.assertEquals(response.status_code,200)
        self.assertContains(response,self.cloth.title)
        self.assertTemplateUsed("cloths/cloths_detail.html")

    def test_cloth_detail_view_invalid_slug(self):
        url = reverse("cloth_detail",kwargs={"slug":"-invalid-slug"})
        response = self.client.get(url)
        self.assertEquals(response.status_code,404)
    
    def test_female_list_view(self):
        url = reverse("female_list")
        response = self.client.get(url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed("cloths/female_list.html")
    
    def test_male_list_view(self):
        url = reverse("male_list")
        response = self.client.get(url)
        self.assertEquals(response.status_code,200)
        self.assertContains(response,self.cloth.title)
        self.assertTemplateUsed("cloths/male_list.html")
    
    def test_highest_selling_view(self):
        url = reverse("highest_selling")
        response = self.client.get(url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed("cloths/highest_selling.html")


class CommentView(TestCase):
    def setUp(self):
        self.author = CustomUser.objects.create(email="testemail@email.com",password="*7S^dasadDSA1")
        self.cloth = Cloth.objects.create(**CLOTH_VALID_DATA)
        self.comment = Comment.objects.create(cloth=self.cloth,
                                              author=self.author,
                                              body="test comment",
                                              active=True,
                                              )
        
    def test_comment_create_view_unauthorized(self):
        """user is not logged in therefore we get 302 status code and redirect to login"""
        url = reverse("comment_create",kwargs={"slug":self.cloth.slug})
        response = self.client.post(url,data={"body":"test comment"})
        self.assertEquals(response.status_code,302)
        self.assertRedirects(response,reverse("account_login"))
    
    def test_comment_create_view_authorized(self):
        """user is logged in therefore we get 302 status code and redirect to cloth_detail"""
        author = self.author
        url = reverse("comment_create",kwargs={"slug":self.cloth.slug})
        self.client.force_login(user=author)
        response = self.client.post(url,data={"body":"test comment"})
        self.assertTrue(author.is_authenticated)
        self.assertEquals(response.status_code,302)
        self.assertRedirects(response,reverse("cloth_detail",kwargs={"slug":self.cloth.slug}))
    
    def test_comment_exists_in_cloth_detail(self):
        url = reverse("cloth_detail",kwargs={"slug":self.cloth.slug})
        response = self.client.get(url)
        self.assertContains(response,self.comment.body)