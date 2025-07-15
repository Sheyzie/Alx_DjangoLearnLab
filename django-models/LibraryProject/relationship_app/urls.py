from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from . import views
from . import admin_view, librarian_view, member_view
from .views import list_books, LibraryDetailView


urlpatterns = [
    path('books/', list_books(), name='books'),
    path('library/', LibraryDetailView.as_view(), name='library'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('login/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('signup/', views.register, name='register'),
    path('view/admin/<int:id>', admin_view.admin_view, name='admin_view'),
    path('view/librarian/<int:id>', librarian_view.librarian_view, name='librarian_view'),
    path('view/member/<int:id>', member_view.member_view, name='member_view'),


]