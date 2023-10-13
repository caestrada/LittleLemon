from django.test import TestCase

from restaurant.models import Menu


class MenuViewTest(TestCase):

    def setUp(self) -> None:
        self.pizza = Menu.objects.create(title='Pizza', price=15.99, inventory=5)
        self.icecream = Menu.objects.create(title='icecream', price=9.99, inventory=10)
        self.pasta = Menu.objects.create(title='pasta', price=19.99, inventory=10)

    def test_getall(self):
        menu = Menu.objects.all()
        self.assertEqual(menu.count(), 3)
