<!-- creating a new book -->
>>> newbook = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

<!-- saving into database -->
>>> newbook.save()

<!-- expected result -->
<QuerySet [<Book: Book object (1)>]>

<!-- retrieving title -->
>>> newbook.title

<!-- output -->
'1984'

<!-- retrieving author -->
>>> newbook.author

<!-- output -->
'George Orwell'

<!-- retrieving publication_year -->
>>> newbook.publication_year

<!-- output -->
1949

<!-- updating title -->
>>> newbook.title = "Nineteen Eighty-Four"

<!-- saving changes to database -->
>>> newbook.save()

<!-- checking if changes was implemented -->
>>> newbook.title

<!-- output -->
'Nine

<!-- deleting book -->
>>> newbook.delete()

<!-- output -->
(1, {'bookshelf.Book': 1})

<!-- trying to retrieve book -->
>>> Book.objects.all()

<!-- output -->
<QuerySet []>
