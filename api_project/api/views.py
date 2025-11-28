# Create your views here.
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer


class BookList(generics.ListAPIView):
    """
    API endpoint that allows all books to be viewed.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    Full CRUD API for Book model.
    - list    (GET /books_all/)
    - create  (POST /books_all/)
    - retrieve (GET /books_all/<id>/)
    - update   (PUT /books_all/<id>/)
    - partial_update (PATCH /books_all/<id>/)
    - destroy  (DELETE /books_all/<id>/)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    #ModelViewSet gives one all CRUD actions automatically