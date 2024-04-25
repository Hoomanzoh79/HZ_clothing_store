from django.test import TestCase
from django.urls import reverse



class TestPagesView(TestCase):
    def test_about_us_view(self):
        url = reverse("about_us")
        response = self.client.get(url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,"pages/about_us.html")
    
    def test_index_view(self):
        url = reverse("index")
        response = self.client.get(url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,"index.html")