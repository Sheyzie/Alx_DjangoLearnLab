from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# Create your views here.
def all_books(request):
    books = Book.objects.all()
    context = {'books': books}
    render(request, 'list_book.html', context)

class LibraryDetailView(DetailView):
    template_name = 'llibrary_detail.html'
    model = Library

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        books = Library.books.all()
        context['book_list'] = books
