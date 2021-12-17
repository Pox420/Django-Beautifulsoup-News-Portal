from django.db.models.signals import post_save
from django.dispatch import receiver
# from django.contrib.auth.models import User
from .models import User
from django.contrib.auth import get_user_model
from user.models import User, UserProfile
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site

# ......EMAIL VARIABLES.....
subject = "Your email needs to be verified"
from django_bs_news_portal.settings import EMAIL_HOST_USER
email_from = EMAIL_HOST_USER


@receiver(post_save, sender=User)
def send_email_verification_mail(sender, instance, created,**kwargs):  

    if created:
        email_token = instance.email_token
        # current_site = get_current_site(request)
        email = [instance.email,]
        message = f'Click in the link to verify your email http://127.0.0.1:8000/user/verify/{email_token}'
        send_mail(subject, message, email_from, email)
        print("email sent")