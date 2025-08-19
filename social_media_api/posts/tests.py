from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from .models import Post


User = get_user_model()

class PostAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client = APIClient()
        data = {
            'username': 'testuser', 
            'password': 'password'
        }

        # create a new user
        response = self.client.post('/api/register/', data)
        
        # login the new user
        response = self.client.post('/api/login/', data)

        # obtain token from respopnse
        self.token = response.data['token']

    def test_create_post(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')
        
        response = self.client.post('/api/posts/', {'title': 'Test', 'content': 'Testing'})
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Post.objects.count(), 1)

