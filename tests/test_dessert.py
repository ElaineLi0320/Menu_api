from django.test import TestCase
from menu.models import Dessert


class DessertModelTest(TestCase):
    def setUp(self):
        # Set up a new Dessert object for each test
        self.dessert = Dessert.objects.create(name="Tiramisu", description="Coffee-flavored Italian dessert")

    def test_name_label(self):
        field_label = self.dessert._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_description_label(self):
        field_label = self.dessert._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_name_max_length(self):
        max_length = self.dessert._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)

    def test_description_max_length(self):
        max_length = self.dessert._meta.get_field('description').max_length
        self.assertEqual(max_length, 500)

    def test_object_name_is_name(self):
        expected_object_name = self.dessert.name
        self.assertEqual(str(self.dessert), expected_object_name)

# command
# python3 manage.py test tests
