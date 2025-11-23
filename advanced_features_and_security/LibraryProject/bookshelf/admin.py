from django.contrib import admin

# Register your models here.
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Columns displayed in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add filters on the right sidebar
    list_filter = ('author', 'publication_year')
    
    # Enable search bar
    search_fields = ('title', 'author')

# Register the model with the custom admin
admin.site.register(Book, BookAdmin)