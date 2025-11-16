from .models import Author, Book, Library, Librarian


#Query all books by a specific author
def get_books_by_author(author_name):
    """
    Return a queryset of all books written by the given author name.
    """
    return Book.objects.filter(author__name=author_name)


#List all books in a library.
def get_books_in_library(library_name):
    """
    Return a queryset of all books in the given library name.
    """
    return Book.objects.filter(libraries__name=library_name)

def get_librarian_for_library(library_name):
    """
    Return the librarian for the given library name, or None if not found.
    """
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None
