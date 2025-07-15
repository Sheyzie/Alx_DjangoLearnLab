from django.contrib.auth.views import LogoutView
from django.urls import path, include
from .views import list_books, LibraryDetailView, SignUpView, UserLoginView


urlpatterns = [
    path('books/', list_books(), name='books'),
    path('library/', LibraryDetailView.as_view(), name='library'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('login/', LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='register'),

]