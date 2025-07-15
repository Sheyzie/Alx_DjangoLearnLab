from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User


def admin_check(user):
    return user.is_authenticated and user.role == 'Admin'

@user_passes_test(admin_check)
def admin_view(request, id):
    admin = User.objects.get(id=id)
    context = {'admin': admin}
    render(request, 'admin_view.html', context)
    


