from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class UserTest(TestCase):
    def setup(self):
        self.user = self.client.post(reverse('register'), {
            'username': 'sample user',
            'email': 'sample_user@mail.com',
            'password1': 'sampleuser123',
            'password2': 'sampleuser123'
        })

    def test_user_login(self):
        login_successful = self.client.login(username='sample user', password='sampleuser123')

        response = self.client.get('/profile/')

        self.assertTrue(login_successful)
        self.assertEqual(response.status_code, 200)

    def test_edit_profile(self):
        login_successful = self.client.login(username='sample user', password='sampleuser123')
        response = self.client.put('/profile/edit/', {'username': 'sample_user'})

        user = User.objects.get(username='sample_user')

        self.assertEqual(user.username, 'sample_user')

