from django.urls import path
from django.views.generic import RedirectView
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import (
    list_books, 
    LibraryDetailView, 
    AdminView, 
    LibrarianView, 
    MemberView, 
    add_book, 
    edit_book, 
    delete_book
)

urlpatterns = [
    path("", RedirectView.as_view(url="/relationship/books/")),  
    path("books/", list_books, name="list_books"),
    path("libraries/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("register/", views.register, name="register"),
    path("admin-view/", AdminView, name="AdminView"),
    path("librarian-view/", LibrarianView, name="LibrarianView"),
    path("member-view/", MemberView, name="MemberView"),
    path('books/add/', add_book, name='add_book'),
    path('books/<int:pk>/edit/', edit_book, name='edit_book'),
    path('books/<int:pk>/delete/', delete_book, name='delete_book'),
]
