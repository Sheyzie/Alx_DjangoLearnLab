from django.views.generic import DetailView
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User


def admin_check(user):
    return user.role == 'Admin'

@user_passes_test(admin_check)
class Admin(DetailView):
    model = User
    template_name = 'admin_view.html'
    


