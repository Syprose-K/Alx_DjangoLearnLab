from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.detail import DetailView
from .models import Library, Book

def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

def LoginView(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("list_books")
    else:
        form = AuthenticationForm(request)
    return render(request, "relationship_app/login.html", {"form": form})


def LogoutView(request):
    if request.method == "POST":
        logout(request)
        return redirect("login")
    return render(request, "relationship_app/logout.html")


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("list_books")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def AdminView(request):
    return render(request, "relationship_app/admin_view.html")

@user_passes_test(is_librarian)
def LibrarianView(request):
    return render(request, "relationship_app/librarian_view.html")

@user_passes_test(is_member)
def MemberView(request):
    return render(request, "relationship_app/member_view.html")