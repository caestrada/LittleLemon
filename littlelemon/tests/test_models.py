from django.test import TestCase
from restaurant.models import Menu

class MenuModelTest(TestCase):

    def test_new_menu(self):
        menu = Menu.objects.create(title='Burger', price=10.00, inventory=10)
        self.assertEqual(menu.__str__(), "Burger : 10.0")
