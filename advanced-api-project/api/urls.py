from django.urls import path
from .views import BookListCreateAPIView, AuthorListCreateAPIView
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView


urlpatterns = [
    path('book/', BookListCreateAPIView.as_view(), name='book_view'),
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/create/', BookCreateView.as_view(), name='book_new'),
    path('books/update/', BookUpdateView.as_view(), name='book_update'),
    path('books/delete/', BookListCreateAPIView.as_view(), name='book_delete'),

    path('author/', AuthorListCreateAPIView.as_view(), name='author_view'),
]