from django.test import TestCase
from restuarant.models import Menu
from restuarant.serializers import MenuSerializer

class MenuViewTest(TestCase):

    def setUp(self) -> None:
        menu = Menu.objects.create(title="menu1", price=99.99, inventory=10)
        return super().setUp()
    
    def test_getall(self):
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        self.assertEquals(items, serializer.data)
