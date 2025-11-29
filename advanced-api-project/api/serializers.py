from datetime import datetime

from rest_framework import serializers
from .models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    """
    BookSerializer
    --------------
    Serializes the Book model.

    - Includes all model fields: id, title, publication_year, author.
    - Adds custom validation to ensure publication_year is not in the future.
    """

    class Meta:
        model = Book
        fields = "__all__"

    def validate_publication_year(self, value):
        """
        Field-level validation for publication_year.

        Ensures:
        - The year is not in the future relative to the current year.

        Raises:
        - serializers.ValidationError if the year is greater than current year.
        """
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                f"Publication year cannot be in the future (current year: {current_year})."
            )
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    AuthorSerializer
    ----------------
    Serializes the Author model.

    Fields:
    - name: The author's name.
    - books: A nested representation of all Book instances related to this author.

    Relationship Handling:
    - Uses the related_name 'books' from the Book model's ForeignKey to Author.
    - The nested BookSerializer is read-only by default in this example.
      That means:
      - When you serialize an Author, you see a list of their books.
      - To create/update books, you would typically use the BookSerializer directly,
        or implement a custom create/update in this serializer to handle nested writes.
    """

    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["id", "name", "books"]
