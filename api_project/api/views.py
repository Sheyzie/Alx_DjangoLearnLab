from rest_framework import generics
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Book
from .serializers import BookSerializer

# Book list view for the serializer
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# View for the Serializer to Perform the CRUD functions
class BookViewSet(viewsets.ModelViewSet):
    # Token Authentication to ensure that users can be authenticated via token
    authentication_classes = [TokenAuthentication]

    # Permission to ensure that only permitted users can have access
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer