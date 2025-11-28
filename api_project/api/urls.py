from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

#Create a router and register the ViewSet with it
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

#Route for the BookList view ListAPIView - read-only
urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)), #router URLs for BookViewSet all CRUD operations
]
