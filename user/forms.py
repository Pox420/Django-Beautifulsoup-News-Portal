from .models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')