# from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test, login_required
from django.views.generic import ListView

from .models import Librarian


def admin_check(user):
    return user.is_authenticated and user.role == 'Admin'

@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(admin_check), name='dispatch')
class AdminView(ListView):
    template_name = 'admin_view.html'
    model = Librarian
    context_object_name = 'librarian_list'

    
        
    
    


