from django.test import TestCase
from rest_framework.test import APIRequestFactory
from .models import Author, Book
from .views import BookListCreateAPIView, AuthorListCreateAPIView


# Create your tests here.
class APITest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name='Author Seyi')
        self.book = Book.objects.create(
            title='Micheal Bighead',
            publication_year='2025',
            author=self.author
        )
        self.factory = APIRequestFactory()
        self.view = BookListCreateAPIView.as_view()
        self.view2 = AuthorListCreateAPIView.as_view()

    def test_book_API_POST_test(self):
        # request = self.factory.post('api/v1/book/', data={'title': 'Micheal Bighead', 'publication_year': 2025, 'author': self.author})
        request = self.factory.get('api/v1/book/')
        response = self.view(request)
        # response.render()

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Micheal Bighead')


    def test_author_API_GET_test(self):
        request = self.factory.get('api/v1/author/')
        response = self.view2(request)
        # response.render()

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Author Seyi')
