from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django import forms
from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render

from user.models import User
from .forms import UserForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
import random
import string
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site

# Create your views here.
def generate_token():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(30))

def forgot_password_token():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(30))


def register(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if password1 == password2:
            user = User(email=email, password=password1,email_token=generate_token(),forgot_password=forgot_password_token())
            user.save()
            messages.success(request, "User created successfully")
            return redirect('login_user')
        else:
            messages.error(request, "Passwords do not match")
            return redirect('register')
    else:
        
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


def verify(request,token):
    user = get_user_model().objects.get(email_token=token)
    messages.success(request, "Your email has been verified")
    return redirect('/')
