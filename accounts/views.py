from django.shortcuts import render
from .forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
# Create your views here.
# This view will handle all our authentication stuff such as registeration while the login and logout are being done by Django itself

class CreateUserView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'