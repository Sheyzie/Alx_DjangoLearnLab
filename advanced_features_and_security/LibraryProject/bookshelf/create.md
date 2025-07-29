<!-- creating a new book -->
>>> newbook = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

<!-- saving into database -->
>>> newbook.save()

<!-- expected result -->
<QuerySet [<Book: Book object (1)>]>