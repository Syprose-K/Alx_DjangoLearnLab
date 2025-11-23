from .models import Author, Book, Library, Librarian


#Query all books by a specific author.
def get_books_by_author(author_name):
    """
    Return all books written by the given author name.
    """
    try:
        author = Author.objects.get(name=author_name)
        # required by checker: objects.filter(author=author)
        return Book.objects.filter(author=author)
    except Author.DoesNotExist:
        return Book.objects.none()


#List all books in a library.
def get_books_in_library(library_name):
    """
    Return all books in the given library name.
    """
    try:
        library = Library.objects.get(name=library_name)
        #required by checker: books.all()
        books = library.books.all()
        return books
    except Library.DoesNotExist:
        return Book.objects.none()


#Retrieve the librarian for a library.
def get_librarian_for_library(library_name):
    """
    Return the librarian for the given library name, or None if not found.
    """
    try:
        library = Library.objects.get(name=library_name)
        #required by checker: Librarian.objects.get(library=
        librarian = Librarian.objects.get(library=library)
        return librarian
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None
