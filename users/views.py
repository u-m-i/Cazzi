"""Users views"""

# From django

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Models

from users.models import Profile
from django.contrib.auth.models import User

# Exceptions

from django.db.utils import IntegrityError as IE


def login_view(request):
    """Login view
    """
    if request.method == "POST":
        
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user:
            login(request,user)
            return redirect("feed")
        else:
            return render(request, "users/login.html", {"error":"Invalid Username and password"})
        
    return render(request, "users/login.html")


@login_required
def logout_view(request):
    """Logout the user
    """
    logout(request)
    return redirect("login")


def signup(request):
    """ Is the Signup View
    """
    
    if request.method == "POST":

        username = request.POST["username"]
        passwd = request.POST["password"]
        passwd_confirmation = request.POST["passwd_confirm"]

        if passwd != passwd_confirmation:

            return render(request, "users/signup.html", {"error" : "Passwords does not match"})

        try:
            user = User.objects.create_user(username = username, password=passwd)
        except IE:
            return render(request, "users/login.html", {"error" : "Username is already taken"})

        user.first_name = request.POST["first_name"]
        user.last_name = request.POST["last_name"]
        user.email = request.POST["email"]
        user.save()

        profile = Profile(nickname=user)
        profile.save()

        return redirect("login")

    return render(request, "users/signup.html")

@login_required
def update_profile(request):
    """Update user view"""
    profile = request.user.profile

    return render(
        request, 
        "users/update_profile.html",
        context={
            "profile": profile,
            "user": request.user,
        }, 
    )
