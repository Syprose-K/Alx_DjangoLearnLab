# retrieving a Book instance
Book.objects.all()
Book.objects.get(title="1984")
Book.objects.filter(author="George Orwell")
