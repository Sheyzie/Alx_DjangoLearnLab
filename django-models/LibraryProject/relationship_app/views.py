from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from django.contrib import messages
from .models import Library, Book

from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User

# Create your views here.
def list_books(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        books = Book.objects.all()
        context = {'books': books}
    else:
        context = {'Error': 'User not logged in'}
    render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    template_name = 'relationship_app/library_detail.html'
    model = Library

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect(reverse_lazy('login')) # Redirect to your login page
    else:
        form = UserCreationForm()
    return render(request, 'myapp/signup.html', {'form': form})

# class SignUpView(CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'relationship_app/register.html'


def admin_check(user):
    return user.role == 'Admin'

@user_passes_test(admin_check)
class Admin(DetailView):
    model = User
    template_name = 'admin_view.html'
    



