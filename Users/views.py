from django.shortcuts import render,redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import User


def register_user(request):
    if request.method == "POST":
        username = request.POST["username"] 
        email = request.POST["email"]
        password_one = request.POST["password_one"]
        password_two = request.POST["password_two"]

        if password_one == password_two:
            if User.objects.filter(username=username).exists():
                messages.warning(request, f"Username {username} is already exist, please give alternative")
                return redirect("register-user/")
            else:
                User.objects.create_user(username=username, password = password_one)
                messages.success(request, f"user created successfully for {username}")
                return redirect("login-user/")
        else:
            messages.warning(request, f"password and confirm password is not matched")
            return redirect("register-user/")
    return render(request, "user_registeration.html")


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Login successfully for {username}")
            return redirect("/")
    return render(request, "user_login.html")

def logout_user(request):
    logout(request)
    return redirect("/")



