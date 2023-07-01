from Restaurant.models import Menu,Booking
from django.test import TestCase

#TestCase class
class MenuItemTestCase(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCrea,",price=80,inventory=10)
        self.assertEqual(item, "IceCream : 80")
