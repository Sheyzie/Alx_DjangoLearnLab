from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import register, UserProfileView, UserProfileUpdateView


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profile/edit/', UserProfileUpdateView.as_view(), name='edit_profile'),
]