from django.test import TestCase
from django.urls import reverse,resolve

from pages.views import AboutUsPageView,IndexView


class TestPagesUrl(TestCase):
    def test_about_us_url_resolve(self):
        url = reverse("about_us")
        self.assertEquals(resolve(url).func.view_class,AboutUsPageView)
    
    def test_index_url_resolve(self):
        url = reverse("index")
        self.assertEquals(resolve(url).func.view_class,IndexView)