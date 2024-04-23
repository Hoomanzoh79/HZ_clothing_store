from django.test import TestCase
from django.urls import reverse,resolve

from orders.views import order_create_view


class TestOrderUrl(TestCase):
    def test_order_create_url_resolve(self):
        url = reverse("orders:order_create")
        self.assertEquals(resolve(url).func,order_create_view)