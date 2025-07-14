'''
Query all books by a specific author.
List all books in a library.
Retrieve the librarian for a library.
'''

from .models import Book, Library

book = Book.objects.get(author__name='John')

book_list = Book.objects.get(library__name='Library')

librarian = Library.objects.get(librarian__name='John')
