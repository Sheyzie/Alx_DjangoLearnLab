from django.urls import path

from .views import UserCreateAPIView, LoginView, LogoutView, UserProfileView


urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='api-login'),
    path('api/logout/', LogoutView.as_view(), name='api-logout'),
    path('api/profile/', UserProfileView.as_view(), name='profile'),
]
