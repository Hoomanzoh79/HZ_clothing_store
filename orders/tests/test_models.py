from django.test import TestCase
from django.template.defaultfilters import slugify


from orders.models import Order,OrderItem
from cloths.models import Cloth
from accounts.models import CustomUser


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

class TestOrderModel(TestCase):
    def setUp(self):
        self.cloth = Cloth.objects.create(**CLOTH_VALID_DATA)
        self.user = CustomUser.objects.create(email="testemail@email.com",password="*7S^dasadDSA1")
        self.order = Order.objects.create(user=self.user,first_name="test first name",
                                          last_name="test last name",address="test address",
                                          phone_number="09361958721"
                                          )
        self.order_item = OrderItem.objects.create(order=self.order,cloth=self.cloth,
                                                   quantity=2,size="XL",price=self.cloth.price,
                                                   )
    
    def test_create_order(self):
        self.assertEquals(Order.objects.count(),1)
        self.assertEquals(self.order.first_name,"test first name")
        self.assertTrue(Order.objects.filter(pk=self.order.id).exists())
        self.assertTrue(Order.objects.filter(user=self.user).exists())
    
    def test_create_order_item(self):
        self.assertEquals(OrderItem.objects.count(),1)
        self.assertEquals(self.order_item.order,self.order)
        self.assertEquals(self.order_item.quantity,2)
        self.assertTrue(OrderItem.objects.filter(pk=self.order_item.id).exists())
        self.assertTrue(OrderItem.objects.filter(cloth=self.cloth).exists())