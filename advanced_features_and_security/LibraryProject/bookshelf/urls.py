from django.urls import path
from .views import book_list, secure_book_form

urlpatterns = [
    path('books/', book_list, name='book_list'),
    path('books/add/', secure_book_form, name='secure_book_form'),
]
