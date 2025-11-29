from django_filters import rest_framework
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    """
    BookListView
    ------------
    Read-only endpoint to list all Book instances.

    - Uses DRF's ListAPIView to provide GET /books/ endpoint.
    - Accessible to everyone (authenticated or not) thanks to
      IsAuthenticatedOrReadOnly permission class.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    filterset_fields = ['title', 'author__name', 'publication_year']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title'] 

class BookDetailView(generics.RetrieveAPIView):
    """
    BookDetailView
    --------------
    Read-only endpoint to retrieve a single Book by its primary key (id).

    - Uses DRF's RetrieveAPIView to provide GET /books/<pk>/ endpoint.
    - Accessible to everyone (authenticated or not).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookCreateView(generics.CreateAPIView):
    """
    BookCreateView
    --------------
    Handles creation of new Book instances.

    - Uses DRF's CreateAPIView to provide POST /books/create/ endpoint.
    - Only authenticated users can create books, enforced by
      IsAuthenticated permission class.
    - Validation is handled by BookSerializer, including custom
      publication_year validation.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Hook to customize creation behavior.

        Currently, it just saves the instance, but this is where you could:
        - associate the book with request.user
        - log creation activity
        - apply custom business logic
        """
        serializer.save()


class BookUpdateView(generics.UpdateAPIView):
    """
    BookUpdateView
    --------------
    Handles updating existing Book instances.

    - Uses DRF's UpdateAPIView to provide:
      - PUT /books/<pk>/update/
      - PATCH /books/<pk>/update/
    - Only authenticated users can update books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        """
        Hook to customize update behavior.

        You can add logging, additional validation, or side effects here.
        """
        serializer.save()


class BookDeleteView(generics.DestroyAPIView):
    """
    BookDeleteView
    --------------
    Handles deletion of Book instances.

    - Uses DRF's DestroyAPIView to provide DELETE /books/<pk>/delete/
    - Only authenticated users can delete books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
