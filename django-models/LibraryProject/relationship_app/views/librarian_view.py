from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test, login_required

# from ..models import Librarian, library, Book, Author


def is_librarian(user):
    return user.is_authenticated and user.role == 'Librarian'


# @login_required
# @user_passes_test(is_librarian)
# def librarian_view(request):
#     books = Book.objects.all()  
#     authors = Author.objects.all()
#     librarians = Librarian.objects.all()
#     context = {
#         'books': books,
#         'authors': authors,
#         'librarians': librarians,
#     }
#     return render(request, 'librarian_view.html', context)

    
        
    
    


