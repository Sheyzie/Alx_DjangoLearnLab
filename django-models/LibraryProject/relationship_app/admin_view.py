from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.models import User
from .models import UserProfile


def admin_check(user):
    return user.is_authenticated and user.role == 'Admin'

@login_required
@user_passes_test(admin_check)
def admin_view(request, id):
    admin = UserProfile.objects.get(user=id)
    context = {'admin': admin}
    render(request, 'admin_view.html', context)
    


