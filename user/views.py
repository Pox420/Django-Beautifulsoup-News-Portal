from django import forms
from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render
from .forms import UserForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.


def register(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        print(email, password1, password2)
        if password1 == password2:
            user = get_user_model().objects._create_user(email=email, password=password1)
            user.save()
            messages.success(request, "User created successfully")
        return redirect('login_user')
    else:
        messages.error(request, "Passwords do not match")
        form = UserForm()
    return render(request, "news_app/register.html", {"form": form})

def login_user(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password1")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('/')
    else:
        form = UserForm()
        return render(request, "news_app/login.html", {"form": form})

def logout_user(request):
    logout(request)
    print("Logged out")
    return redirect('/')

    