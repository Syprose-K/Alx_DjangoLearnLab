# updating a Book instance
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.author = "George Orwell"
book.save()

# or to update directly
Book.objects.filter(title="1984").update(title="Nineteen Eighty-Four")
