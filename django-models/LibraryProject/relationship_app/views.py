from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library, Book

# Create your views here.
def all_books(request):
    books = Book.objects.all()
    context = {'books': books}
    render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    template_name = 'relationship_app/library_detail.html'
    model = Library

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        books = Library.books.all()
        context['book_list'] = books
