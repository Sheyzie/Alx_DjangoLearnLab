from rest_framework import serializers
from .models import Book

# class to handle serialization and deserialization of the Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author']