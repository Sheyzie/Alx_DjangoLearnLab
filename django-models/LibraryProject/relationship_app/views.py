from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from .models import Library, Book

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    template_name = 'relationship_app/library_detail.html'
    model = Library

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'