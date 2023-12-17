from django.test import TestCase
from menu.models import Appetizer


class AppetizerModelTest(TestCase):

    def setUp(self):
        # Set up non-modified objects used by all test methods
        Appetizer.objects.create(name="Bruschetta", description="Grilled bread with tomato and garlic")

    def test_name_label(self):
        appetizer = Appetizer.objects.get(id=1)
        field_label = appetizer._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_description_label(self):
        appetizer = Appetizer.objects.get(id=1)
        field_label = appetizer._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_name_max_length(self):
        appetizer = Appetizer.objects.get(id=1)
        max_length = appetizer._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)

    def test_description_max_length(self):
        appetizer = Appetizer.objects.get(id=1)
        max_length = appetizer._meta.get_field('description').max_length
        self.assertEqual(max_length, 500)

    def test_object_name_is_name(self):
        appetizer = Appetizer.objects.get(id=1)
        expected_object_name = appetizer.name
        self.assertEqual(expected_object_name, str(appetizer))

# command
# python3 manage.py test tests
