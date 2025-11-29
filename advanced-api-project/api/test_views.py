from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User

from .models import Author, Book
from .serializers import BookSerializer


class BookAPITestCase(APITestCase):
    """
    Test suite for Book API endpoints.
    Covers:
    - CRUD operations
    - Filtering, searching, ordering
    - Permissions and authentication
    """

    def setUp(self):
        # Create a user for authenticated requests
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client = APIClient()

        # Author & Books setup
        self.author = Author.objects.create(name="George Orwell")
        self.book1 = Book.objects.create(title="1984", publication_year=1949, author=self.author)
        self.book2 = Book.objects.create(title="Animal Farm", publication_year=1945, author=self.author)

        # API endpoints
        self.list_url = reverse("book-list")        # /books/
        self.create_url = reverse("book-create")    # /books/create/
        self.update_url = reverse("book-update", kwargs={"pk": self.book1.id})  # /books/<pk>/update/
        self.delete_url = reverse("book-delete", kwargs={"pk": self.book1.id})  # /books/<pk>/delete/
        self.detail_url = reverse("book-detail", kwargs={"pk": self.book1.id})  # /books/<pk>/

    # ----------------------
    # TEST LIST
    # ----------------------
    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # ----------------------
    # TEST DETAIL
    # ----------------------
    def test_retrieve_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book1.title)

    # ----------------------
    # TEST CREATE
    # ----------------------
    def test_create_book_requires_authentication(self):
        # Should fail without login
        response = self.client.post(
            self.create_url,
            {"title": "New Book", "publication_year": 2020, "author": self.author.id},
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Authenticate and try again
        self.client.login(username="testuser", password="password123")
        response = self.client.post(
            self.create_url,
            {"title": "New Book", "publication_year": 2020, "author": self.author.id},
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    # ----------------------
    # TEST UPDATE
    # ----------------------
    def test_update_book_requires_authentication(self):
        response = self.client.put(
            self.update_url, {"title": "1984 Updated", "publication_year": 1949, "author": self.author.id}
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.login(username="testuser", password="password123")
        response = self.client.put(
            self.update_url, {"title": "1984 Updated", "publication_year": 1949, "author": self.author.id}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "1984 Updated")

    # ----------------------
    # TEST DELETE
    # ----------------------
    def test_delete_book_requires_authentication(self):
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.login(username="testuser", password="password123")
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # ----------------------
    # TEST FILTERING
    # ----------------------
    def test_filter_books_by_title(self):
        response = self.client.get(f"{self.list_url}?title=1984")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "1984")

    # ----------------------
    # TEST SEARCH
    # ----------------------
    def test_search_books_by_author_name(self):
        response = self.client.get(f"{self.list_url}?search=Orwell")
        self.assertEqual(len(response.data), 2)

    # ----------------------
    # TEST ORDERING
    # ----------------------
    def test_order_books_by_publication_year_desc(self):
        response = self.client.get(f"{self.list_url}?ordering=-publication_year")
        self.assertEqual(response.data[0]["publication_year"], 1949)
        self.assertEqual(response.data[1]["publication_year"], 1945)
