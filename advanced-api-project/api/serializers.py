from rest_framework import serializers
from django.utils import timezone
from .models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    '''
    This is a serializer/deserializer for the book model.
    - All fields are serialized/deserialized.
    - Custom validation carried out on publication field
    '''
    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, data):
        if timezone.now().year < (data['publication_year']):
            raise serializers.ValidationError("Book cannot be published in the future.")
        return data

class AuthorSerializer(serializers.ModelSerializer):
    '''
    This is a serializer/deserializer for the author model
    - Book serializer is included to show 1 to Many relationship
    '''
    related_books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name','related_books']
