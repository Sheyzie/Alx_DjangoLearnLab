from django.urls import path
from .views import BookListCreateAPIView, AuthorListCreateAPIView


urlpatterns = [
    path('book/', BookListCreateAPIView.as_view(), name='book_view'),
    path('author/', AuthorListCreateAPIView.as_view(), name='author_view'),
]