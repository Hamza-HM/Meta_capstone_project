from django.test import TestCase
from restaurant.models import MenuItem
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.item1 = MenuItem.objects.create(
            title='IceCream',
            price=80,
            inventory=100
        )
        self.item2 = MenuItem.objects.create(
            title='Chocolate Cake',
            price=100,
            inventory=200
        )

    def test_getall(self):
        # Serialize the retrieved items.
        serializer1 = MenuSerializer(self.item1)
        serializer2 = MenuSerializer(self.item2)

        # Assert the HTTP response status code.
        # response = self.client.post('http://127.0.0.1:8000/restaurant/menu/1',{
        #     'bearer': 'af76bf0d3368a38e4c2177b25177f7bdabd00ca0' 
        # })
        # self.assertEqual(response.status_code, 200)

        # Now, you can assert the serialized data.
        self.assertEqual(serializer1.data['title'], 'IceCream')
        self.assertAlmostEqual(serializer1.data['price'], '80.00')
        self.assertEqual(serializer1.data['inventory'], 100)
        self.assertIsInstance(self.item1, MenuItem)

        self.assertEqual(serializer2.data['title'], 'Chocolate Cake')
        self.assertAlmostEqual(serializer2.data['price'], '100.00')
        self.assertEqual(serializer2.data['inventory'], 200)
