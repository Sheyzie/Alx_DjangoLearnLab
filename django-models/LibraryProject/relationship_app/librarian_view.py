from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User


def librarian_check(user):
    return user.role == 'Librarian'

@user_passes_test(librarian_check)
def librarian_view(request):
    librarian = User.objects.get(id=id)
    context = {'librarian': librarian}
    render(request, 'librarian_view.html', context)

