from django.shortcuts import render
from django.contrib.auth import authenticate, login

def login_view(request):
    """Login view
    """
    if request.method == "POSTS":
        print("*" * 10)
        username = request.POST["username"]
        password = reques.POST["password"]
        print(username, ":", password)
        print("*" * 10 )
    return render(request, "users/login.html")
