from django.db import models

class Author(models.Model):
    """
    Author model
    -----------
    Represents a single author.

    Fields:
    - name: The full name of the author.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        # Helpful for debugging and admin display
        return self.name


class Book(models.Model):
    """
    Book model
    ----------
    Represents a book written by an author.

    Fields:
    - title: The title of the book.
    - publication_year: The year the book was published.
    - author: ForeignKey to Author, indicating who wrote the book.
              This creates a one-to-many relationship:
              One Author → Many Books.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="books",  # allows author.books.all() to get all books
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
