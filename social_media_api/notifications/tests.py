from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from posts.models import Post


User = get_user_model()

class LikeTestCase(APITestCase):
    def setUp(self):
        # create a user
        self.user = User.objects.create_user(username='testuser', password='password')
        self.author = User.objects.create_user(username='author', password='pass')

        self.client = APIClient()
        data = {
            'username': 'testuser', 
            'password': 'password'
        }
        
        # login the new user
        response = self.client.post('/api/login/', data)

        # obtain token from respopnse
        self.token = response.data['token']
        
        self.post = Post.objects.create(author=self.author, title="Test Post", content="...")

    def test_like_post(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')

        response = self.client.post(f'/api/posts/{self.post.id}/like/')
        
        self.assertEqual(response.status_code, 200)

