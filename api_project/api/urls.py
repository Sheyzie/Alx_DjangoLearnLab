from django.urls import path, include
from .views import BookList
from rest_framework.routers import DefaultRouter
from api.views import BookViewSet
from rest_framework.authtoken.views import obtain_auth_token


# Router to handle url pattern for all CRUD functions
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')


urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
    path('', include(router.urls)),  # This includes all routes registered with the router
    path('token/', obtain_auth_token, name='api_token_auth'), # The view to generate tokens
]