from pprint import pprint
from django.shortcuts import redirect, render
from django.contrib import messages
from listings.models import *
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from listings.models import Contact



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            pprint(request.user.username)
            messages.success(
                request, f"You are now logged in as {username}."
            )
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')

    return render(request, "accounts/login.html")

@login_required
def logout(request):
    if request.user.is_authenticated:
        auth.logout(
            request
        )
        messages.success(request, f"You have been logged out.")
    else:
        messages.error(request, f"You are not logged in.")
    return redirect("login")

@login_required
def dashboard(request):
    return render(
        request,
        "accounts/dashboard.html"
    )



def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password)
        if user:
            messages.success(request, f"Account created successfully")            
            user.save()
            return redirect('login')
        else:
            messages.error(request, f"Account creation failed")
            return redirect('register')

    return render(request, "accounts/register.html")
