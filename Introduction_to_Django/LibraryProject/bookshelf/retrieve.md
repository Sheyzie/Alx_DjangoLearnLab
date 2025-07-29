<!-- retrieving title -->
mybook = Book.objects.get(id=1)

<!-- retrieving title -->
>>> mybook.title

<!-- output -->
'1984'

<!-- retrieving author -->
>>> mybook.author

<!-- output -->
'George Orwell'

<!-- retrieving publication_year -->
>>> mybook.publication_year

<!-- output -->
1949
