from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import register, UserProfileView, UserProfileUpdateView, PostCreateView, PostListView, PostDetailView, PostUpdateView, PostDeleteView, add_comment, CommentCreateView, CommentUpdateView, CommentDeleteView, PostsByTagListView, SearchPostListView


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profile/edit/', UserProfileUpdateView.as_view(), name='edit_profile'),
    
    path('posts/', PostListView.as_view(), name='post_list'),
    path('post/new/ ', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

    path('post/<int:pk>/comments/new/', add_comment, name='add_comment'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='edit_comment'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete_comment'),
    path('tags/<slug:tag_slug>/', PostsByTagListView.as_view(), name='posts_by_tag'),
    path('search/', SearchPostListView.as_view(), name='post_search'),
]
