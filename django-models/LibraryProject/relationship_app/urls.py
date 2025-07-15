from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from .views import list_books, LibraryDetailView, SignUpView


urlpatterns = [
    path('books/', list_books(), name='books'),
    path('library/', LibraryDetailView.as_view(), name='library'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('login/', LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='register'),

]