from django.urls import path

from .views import UserCreateAPIView, LoginView, LogoutView, UserProfileView, follow_user, unfollow_user


urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='api_login'),
    path('logout/', LogoutView.as_view(), name='api_logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('follow/<int:user_id>/', follow_user, name='follow_user'),
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow_user'),
]
