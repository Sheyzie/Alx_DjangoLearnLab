# from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from .models import Book


def admin_check(user):
    return user.is_authenticated and user.role == 'Member'

@method_decorator(user_passes_test(admin_check), name='dispatch')
class MemberView(LoginRequiredMixin, ListView):
    template_name = 'member_view.html'
    model = Book
    context_object_name = 'book_list'

    
        
    
    


