'''
Query all books by a specific author.
List all books in a library.
Retrieve the librarian for a library.
'''

from .models import Book, Library

book = Book.objects.get(author__name='John')

book_list = Library.objects.get(name=library_name)

librarian = Library.objects.get(librarian__name='John')
