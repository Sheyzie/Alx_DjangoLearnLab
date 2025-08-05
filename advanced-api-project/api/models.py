from django.db import models

# Create your models here.
class Author(models.Model):
    '''
    This is the model for authors
    '''
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    '''
    This is the model for Books
    - Book has a Many to One Relationship with Author model
    '''
    title = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
