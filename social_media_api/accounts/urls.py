from django.urls import path

from .views import UserCreateAPIView, LoginView, LogoutView, UserProfileView


urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='api-login'),
    path('logout/', LogoutView.as_view(), name='api-logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
]
