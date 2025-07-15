from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User


def member_check(user):
    return user.is_authenticated and user.role == 'Member'

@user_passes_test(member_check)
def member_view(request, id):
    member = User.objects.get(id=id)
    context = {'member': member}
    render(request, 'member_view.html', context)

