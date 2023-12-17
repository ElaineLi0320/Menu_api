from django.test import TestCase
from menu.models import Drink


class DrinkModelTest(TestCase):
    def setUp(self):
        # Set up a new Drink object for each test
        self.drink = Drink.objects.create(name="Lemonade", description="Refreshing lemon flavored drink")

    def test_name_label(self):
        field_label = self.drink._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_description_label(self):
        field_label = self.drink._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_name_max_length(self):
        max_length = self.drink._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)

    def test_description_max_length(self):
        max_length = self.drink._meta.get_field('description').max_length
        self.assertEqual(max_length, 500)

    def test_object_str(self):
        expected_str = self.drink.name
        self.assertEqual(str(self.drink), expected_str)

# command
# python3 manage.py test tests
