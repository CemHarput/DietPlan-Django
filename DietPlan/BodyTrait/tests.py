from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import BodyTrait


class BodyTraitAPITestCase(APITestCase):
    def setUp(self):
        self.body_trait = BodyTrait.objects.create(gender='M', weight=70, height=175, age=30)

    def test_get_bodytrait(self):
        url = reverse('bodytrait-detail', args=[self.body_trait.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_bodytrait(self):
        url = reverse('bodytrait-list')
        data = {'gender': 'F', 'weight': 65, 'height': 165, 'age': 28}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Add more tests for update, delete, etc.
