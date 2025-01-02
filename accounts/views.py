from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', "")
        password = request.POST.get('password', "")
        if username and password:
            current_user = auth.authenticate(request, username=username, password=password)
            # current_user = User.objects.filter(username=username, password=password)[0]
            if current_user:
                auth.login(request, current_user) 
                # request.session["user"] = current_user
                # request.session.set_expiry(0)
                
                messages.success(
                    request, "Login Successfull"
                )
                return redirect('dashboard')
            else:
                messages.error(
                    request, "Invalid username or password"
                )
                return redirect("login")
    else:
        return render(request, "accounts/login.html")
          
            
    
    return render(request, "accounts/login.html")

@login_required
def logout(request):
    auth.logout(request)
    # del request.user
    # del request.session["user"]

    return redirect("home")


def register(request):
    if request.method == "POST":
        username = request.POST.get('username', "")
        first_name = request.POST.get('first_name', "")
        last_name = request.POST.get('last_name', "")
        email = request.POST.get('email', "")
        password = request.POST.get('password', "")
        password2 = request.POST.get('password2', "")
        if password != password2:
            messages.warning(request, "Passwords do not match")
            return render(request, "accounts/register.html")
        else:
                        
            current_user = User.objects.create_user(
                username=username, 
                first_name=first_name, 
                last_name=last_name, 
                email=email, 
                password=password
            )
            
            if current_user:
                messages.success(request, "User created successfully")
                return redirect('login')
            else:
                messages.error(request, "Failed to create user")
                return render(request, "accounts/register.html")
            
    return render(request, "accounts/register.html")

@login_required
def dashboard(request):
    return render(request, "accounts/dashboard.html")