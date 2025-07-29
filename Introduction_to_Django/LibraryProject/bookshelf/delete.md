<!-- deleting book -->
>>> newbook.delete()

<!-- output -->
(1, {'bookshelf.Book': 1})

<!-- import book -->
>>> from bookshelf.models import Book

<!-- trying to retrieve book -->
>>> Book.objects.all()

<!-- output -->
<QuerySet []>
