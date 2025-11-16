from django.urls import path
from django.views.generic import RedirectView
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import list_books, LibraryDetailView
from .views import AdminView, LibrarianView, MemberView


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
]
