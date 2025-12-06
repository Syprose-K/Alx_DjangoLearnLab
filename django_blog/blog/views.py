from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import RegisterForm

class UserLoginView(LoginView):
    template_name = 'blog/login.html'

class UserLogoutView(LogoutView):
    template_name = 'blog/logout.html'

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = RegisterForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == "POST":
        request.user.email = request.POST.get("email")
        request.user.save()
        return render(request, "blog/profile.html", {"success": True})
    return render(request, "blog/profile.html")
