from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import register, UserProfileView, UserProfileUpdateView, PostCreateView, PostListView, PostDetailView, PostUpdateView, PostDeleteView


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profile/edit/', UserProfileUpdateView.as_view(), name='edit_profile'),
    
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/new/ ', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]