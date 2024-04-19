from django.test import TestCase
from django.urls import reverse,resolve

from cloths.views import (ClothsListView,
                          ClothDetailView,
                          FemaleView,
                          MaleView,
                          HighestSellingView,
                          CommentCreateView)

class TestClothUrl(TestCase):
    def test_cloths_list_url_resolve(self):
        url = reverse("cloths_list")
        self.assertEquals(resolve(url).func.view_class,ClothsListView)
    
    def test_cloth_detail_url_resolve(self):
        url = (r'/cloths/list/cloth-title[0-9]+/')
        self.assertEquals(resolve(url).func.view_class,ClothDetailView)

    def test_female_list_url_resolve(self):
        url = reverse("female_list")
        self.assertEquals(resolve(url).func.view_class,FemaleView)

    def test_male_list_url_resolve(self):
        url = reverse("male_list")
        self.assertEquals(resolve(url).func.view_class,MaleView)

    def test_highest_selling_list_url_resolve(self):
        url = reverse("highest_selling")
        self.assertEquals(resolve(url).func.view_class,HighestSellingView)
    
class TestCommentUrl(TestCase):
    def test_comment_create_url_resolve(self):
        url = (r'/cloths/list/comment/cloth-title[0-9]+/')
        self.assertEquals(resolve(url).func.view_class,CommentCreateView)
    