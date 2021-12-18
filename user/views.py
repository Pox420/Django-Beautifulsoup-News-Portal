from django_bs_news_portal.settings import EMAIL_HOST_USER
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
        password = request.POST.get("password1")
        password1 = request.POST.get("password2")
        if password == password1:
            user = User(email=email, password=password, email_token=generate_token(
            ), forgot_password=forgot_password_token())
            user.set_password(user.password)
            user.save()

            user.refresh_from_db()

            def send_verification_email(user):
                current_site = get_current_site(request)
                email = [user.email, ]
                subject = "Your email needs to be verified"
                email_from = EMAIL_HOST_USER
                message = f'Click in the link to verify your email {current_site}/user/verify/{user.email_token}'
                send_mail(subject, message, email_from, email)
            send_verification_email(user)

            messages.success(request, "User created successfully")
            messages.success(request, "Check your email inbox to verify your email")
            return redirect('login_user')
        else:
            messages.error(request, "Passwords do not match")
            return redirect('register')
    else:

        form = UserForm()
    return render(request, "news_app/register.html", {"form": form})


def login_user(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password1']
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_verified:
                login(request, user)
                # Redirect to index page.
                return redirect('/')
            else:
                messages.error(request, "First you need to verify your email")
                return redirect('login_user')
        else:
            messages.error(request, "Either email/password is incorrect or your email is not verified")
            return redirect('login_user')
    else:
        form = UserForm()
        return render(request, "news_app/login.html", {"form": form})

def logout_user(request):
    logout(request)
    return redirect('/')


def verify_email(request, token):
    user = get_user_model().objects.get(email_token=token)
    if user.is_verified == True:
        messages.success(request, "Email already verified")
        return redirect('/')
    else:
        user.is_verified = True
        user.save()
        messages.success(request, "Email verified successfully")
        return redirect('login_user')


def forgot_password(request):
    if request.method == "POST":
        email = request.POST['email']
        try:
            user = User.objects.get(email=email)
        except:
            user = None
         
        if user is not None:
            user.refresh_from_db()
            def send_forgot_password_email(user):
                current_site = get_current_site(request)
                email = [user.email, ]
                subject = "Your password reset link"
                email_from = EMAIL_HOST_USER
                message = f'Click in the link to reset your password {current_site}/user/reset-password/{user.forgot_password}'
                send_mail(subject, message, email_from, email)
            send_forgot_password_email(user)
            messages.success(request, "Check your email inbox to reset your password")
            return redirect('login_user')
        else:
            messages.error(request, "Email does not exist")
            return redirect('forgot_password')
    return render(request, "news_app/forgot_password.html")

def reset_password(request, token):
    user = get_user_model().objects.get(forgot_password=token)
    if request.method == "POST":
        password = request.POST['password1']
        password1 = request.POST['password2']
        if password == password1:
            user.password = password
            user.set_password(user.password)
            user.save()
            messages.success(request, "Password reset successfully")
            return redirect('login_user')
        else:
            messages.error(request, "Passwords do not match")
            return redirect('reset_password')
    return render(request, "news_app/reset_password.html")