from django.contrib.auth import login, authenticate,get_user_model
from django.shortcuts import render, redirect
from .forms import GuestForm,RegisterForm,LoginForm 
from django.utils.http import is_safe_url
from .models import GuestEmail

# Instance of the current user
User = get_user_model()

# Create your views here.

# The form below is applicable for login and register and other auth forms  also

def login_view(request):
    form =  LoginForm(request.POST or None)
    context = {"form":form}
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect("/")
        else:
            print("Error")
    return render(request,"accounts/login.html",context)




def guest_register_view(request):
    form =  GuestForm(request.POST or None)
    context = {"form":form}
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():

        email = form.cleaned_data.get("email")
        new_guest_email = GuestEmail.objects.create(email=email)
        request.session['guest_email_id']=new_guest_email.id
        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect("accounts:register")
        
    return redirect("accounts:register")


# Register View

def register_view(request):
    form = RegisterForm(request.POST or None)
    context = {"form":form}

    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
    return render(request,"accounts/register.html",context)

