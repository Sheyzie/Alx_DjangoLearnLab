from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Author, Librarian, Library, Book, UserProfile

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title']

class LibraryForm(forms.ModelForm):
    class Meta:
        model = Library
        fields = ['name']

class LibrarianForm(forms.ModelForm):
    class Meta:
        model = Librarian
        fields = ['name']

class CustomUserCreationForm(UserCreationForm):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )
    role = forms.ChoiceField(choices=ROLE_CHOICES)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'role']

