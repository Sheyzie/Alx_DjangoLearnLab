from django.shortcuts import render
from rest_framework import generics
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import status

from django_filters import rest_framework

from .serializers import BookSerializer, AuthorSerializer
from .models import Book, Author
from .filters import BookFilter

# Create your views here.
class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AuthorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

# for list view
class BookListView(generics.ListAPIView):
    '''
    With django-filter, API calls will be;
    GET /books/?title=harry&author=rowling&publication_year=2007
    '''
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'author']
    filterset_class = BookFilter

# for detail view
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# for create view
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    permission_classes = [IsAuthenticated]

# for update view
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    permission_classes = [IsAuthenticated]


    def put(self, request):
        pk = request.data.get('pk')
        if not pk:
            return Response({"error": "pk is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({"error": "Object not found"}, status=status.HTTP_404_NOT_FOUND)

        book.title = request.data.get('name', book.title)
        book.save()
        return Response({"message": "Data updated successfully"}, status=status.HTTP_200_OK)


# for delete view
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
