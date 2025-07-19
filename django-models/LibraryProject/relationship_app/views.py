from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test, login_required

from django.views.generic import CreateView
from django.views.generic.detail import DetailView

from django.urls import reverse_lazy
from django.contrib import messages

from .forms import AuthorForm, LibrarianForm, LibraryForm, BookForm, CustomUserCreationForm
from .models import Librarian, library, Book, Author, UserProfile
from .views import member_view, admin_view, librarian_view


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
            user = form.save(commit=False)
            username = form.cleaned_data.get('username')

            form.save()

            # Manually set role (instead of letting the signal do it)
            role = form.cleaned_data['role']
            UserProfile.objects.filter(user=user).update(role=role)

            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect(reverse_lazy('login')) # Redirect to your login page
    else:
        form = UserCreationForm()
    return render(request, 'myapp/signup.html', {'form': form})


@login_required
@user_passes_test(admin_view.is_admin)
def admin_view(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    librarians = Librarian.objects.all()
    context = {
        'books': books,
        'authors': authors,
        'librarians': librarians,
    }
    return render(request, 'relationship_app/admin_view.html', context)
 
@login_required
@user_passes_test(librarian_view.is_librarian)
def librarian_view(request):
    books = Book.objects.all()  
    authors = Author.objects.all()
    librarians = Librarian.objects.all()
    context = {
        'books': books,
        'authors': authors,
        'librarians': librarians,
    }
    return render(request, 'relationship_app/librarian_view.html', context)

@login_required
@user_passes_test(member_view.is_member)
def member_view(request):
    books = Book.objects.all()  
    authors = Author.objects.all()
    librarians = Librarian.objects.all()
    context = {
        'books': books,
        'authors': authors,
        'librarians': librarians,
    }
    return render(request, 'relationship_app/member_view.html', context) 