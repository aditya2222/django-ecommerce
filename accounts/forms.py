from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=120)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    


class GuestForm(forms.Form):
    email = forms.EmailField()

class LoginForm(forms.Form):
    username = forms.CharField(max_length=120)
    password = forms.CharField(widget=forms.PasswordInput)