from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import UserRegistrationForm, UserLoginForm
from .models import Profile


# Create your views here.
def sign_up(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create a profile for the user
            Profile.objects.create(user=user)
            login(request, user)
            return redirect("home")
    else:
        form = UserRegistrationForm()
    return render(request, "accounts/register.html", {"form": form})


def sign_in(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
    else:
        form = UserLoginForm()
    return render(request, "accounts/login.html", {"form": form})


def sign_out(request):
    logout(request)
    return redirect("home")


def profile(request):
    user = request.user
    if request.method == "POST":
        # Update profile picture if provided
        if request.FILES.get("avatar"):
            user.profile.image = request.FILES["avatar"]
            user.profile.save()

        # Update user information
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.save()

        return redirect("profile")
    else:
        return render(request, "accounts/profile.html", {"user": user})
