from django.test import TestCase
from menu.models import MainCourse


class MainCourseModelTest(TestCase):
    def setUp(self):
        # Set up a new MainCourse object for each test
        self.main_course = MainCourse.objects.create(name="Spaghetti Carbonara", description="Pasta with creamy sauce and bacon")

    def test_name_label(self):
        main_course = MainCourse.objects.get(id=1)
        field_label = main_course._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_description_label(self):
        main_course = MainCourse.objects.get(id=1)
        field_label = main_course._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_name_max_length(self):
        main_course = MainCourse.objects.get(id=1)
        max_length = main_course._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)

    def test_description_max_length(self):
        main_course = MainCourse.objects.get(id=1)
        max_length = main_course._meta.get_field('description').max_length
        self.assertEqual(max_length, 500)

    def test_object_name_is_name(self):
        main_course = MainCourse.objects.get(id=1)
        expected_object_name = main_course.name
        self.assertEqual(str(main_course), expected_object_name)

# command
# python3 manage.py test tests
