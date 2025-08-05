from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate
from django.contrib.auth import get_user_model
from .models import Author, Book
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView


# Create your tests here.
class BookAPITest(APITestCase):
    def setUp(self):
        self.username = 'SampleUser'
        self.email = 'sample_user@mail.com'
        self.password = 'sample_password'

        self.user = get_user_model().objects.create_superuser(
            username=self.username,
            email= self.email,
            password = self.password
        )
        # Attempt to log in
        login_successful = self.client.login(username=self.username, password=self.password)

        self.author = Author.objects.create(name='Sample Author')
        self.factory = APIRequestFactory()

    # def test_user_login(self):
    #     # Attempt to log in
    #     login_successful = self.client.login(username=self.username, password=self.password)
    #     self.assertTrue(login_successful)

    def test_BookCreateView(self):
        self.view = BookCreateView.as_view()
       
        request = self.factory.post('api/v1/book/create/', {'title': 'Micheal Bighead', 'publication_year': 2025, 'author': self.author.id}, format='json')
        
        # Force authenticate the request with the user
        force_authenticate(request, user=self.user)

        response = self.view(request)
        # response.render()

        self.assertEqual(response.status_code, 201)

    def test_BookListView(self):
        self.view = BookListView.as_view()

        request = self.factory.get('api/v1/books/')
        response = self.view(request)

        self.assertEqual(response.status_code, 200)

    def test_BookUpdateView(self):
        self.view = BookUpdateView.as_view()
        self.view2 = BookListView.as_view()
        book = Book.objects.create(
            title='Micheal Bighead',
            publication_year=2024,
            author=self.author
        )
        request = self.factory.put('api/v1/books/update', {'title': 'Micheal Bigger head', 'publication_year': 2025, 'author': self.author.id}, format='json')
        request2 = self.factory.get('api/v1/books/')
        # Force authenticate the request with the user
        force_authenticate(request, user=self.user)

        response = self.view(request, pk='1')
        response2 = self.view2(request2)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response2, 'Micheal Bigger head')

    def test_DeleteView(self):
        self.view = BookDeleteView.as_view()
        self.view2 = BookListView.as_view()
        book = Book.objects.create(
            title='Micheal Bighead',
            publication_year=2024,
            author=self.author
        )
        request = self.factory.delete('api/v1/books/delete')
        request2 = self.factory.get('api/v1/books/')
        # Force authenticate the request with the user
        force_authenticate(request, user=self.user)

        response = self.view(request, pk='1')
        response2 = self.view2(request2)
        # response.render()

        self.assertEqual(response.status_code, 204)
        self.assertContains(response2, [])




