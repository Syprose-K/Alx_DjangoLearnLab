# deleting a Book instance

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# or to delete directly
Book.objects.filter(author="George Orwell").delete()
