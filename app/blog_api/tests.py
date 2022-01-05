from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.
from blog.models import Category


class PostTests(APITestCase):

    def test_view_posts(self):
        url = reverse('blog_api/v1/:list_post')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def create_post(self):
        self.test_category = Category.objects.create(name='django')

        self.testuser1 = User.objects.create_user(
            username='test_user1', password='123456789'
        )

        data = {'title': 'new', 'author': 1, 'except': 'new', 'content': 'new'}
        url = reverse('blog_api/v1/:list_post')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
