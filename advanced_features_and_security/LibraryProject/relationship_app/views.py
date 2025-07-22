from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import Permission
from django.contrib.auth.decorators import permission_required, user_passes_test, login_required

from django.views.generic import CreateView
from django.views.generic.detail import DetailView

from django.urls import reverse_lazy
from django.contrib import messages

from .models import Library, Librarian, Book, Author, UserProfile
from .view import members_view, admins_view, librarians_view

from bookshelf.group_permissions import create_group_permission


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

            # giving permisions to user
            if role == 'Admin':
                group = create_group_permission('Admins')
            elif role == 'Librarian':
                group = create_group_permission('Editors')
            elif role == 'Member':
                group = create_group_permission('Viewers')             
            user.group.add(group)
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect(reverse_lazy('login')) # Redirect to your login page
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


@login_required
@user_passes_test(admins_view.is_admin)
@permission_required('bookshelf.can_delete', raise_exception=True)
@permission_required('bookshelf.can_create', raise_exception=True)
@permission_required('bookshelf.can_edit', raise_exception=True)
@permission_required('bookshelf.can_view', raise_exception=True)
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
@user_passes_test(librarians_view.is_librarian)
@permission_required('bookshelf.can_create', raise_exception=True)
@permission_required('bookshelf.can_edit', raise_exception=True)
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
@user_passes_test(members_view.is_member)
@permission_required('bookshelf.can_view', raise_exception=True)
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

@permission_required('bookshelf.can_create', raise_exception=True)
@permission_required('bookshelf.can_edit', raise_exception=True)
def add_book(request):
    return render(request, 'relationship_app/add_book.html')

@permission_required('bookshelf.can_create', raise_exception=True)
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request):
    return render(request, 'relationship_app/edit_book.html')

@permission_required('bookshelf.can_delete', raise_exception=True)
@permission_required('bookshelf.can_create', raise_exception=True)
@permission_required('bookshelf.can_edit', raise_exception=True)
@permission_required('bookshelf.can_view', raise_exception=True)
def delete_book(request):
    return render(request, 'relationship_app/delete_book.html')