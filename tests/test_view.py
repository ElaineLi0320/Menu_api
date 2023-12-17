from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from menu.models import Appetizer
from menu.serializers import AppetizerSerializer


class AppetizerAPITestCase(APITestCase):

    def setUp(self):
        self.appetizer = Appetizer.objects.create(name="Bruschetta", description="Grilled bread with tomatoes and garlic")
        self.list_url = reverse('appetizer_list')
        self.detail_url = reverse('appetizer_detail', kwargs={'id': self.appetizer.id}) 

    def test_get_appetizer_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_appetizer(self):
        data = {"name": "Spring Rolls", "description": "Fried rolls with vegetables and meat"}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Appetizer.objects.count(), 2)

    def test_get_appetizer_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.appetizer.name)

    def test_update_appetizer(self):
        data = {"name": "Updated Bruschetta", "description": "Updated description"}
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.appetizer.refresh_from_db()
        self.assertEqual(self.appetizer.name, "Updated Bruschetta")

    def test_delete_appetizer(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Appetizer.objects.count(), 0)

# command
# python3 manage.py test tests
