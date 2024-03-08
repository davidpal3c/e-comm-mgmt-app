from django.shortcuts import render
from userauths.forms import UserRegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.shortcuts import redirect
from django.conf import settings



User = settings.AUTH_USER_MODEL


def register_view(request):
    
    if request.method == "POST":
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Hey {username}, Your account was created successfully!")
            new_user = authenticate(username=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1'])
            login(request, new_user)
            return redirect("core:index")

    else:
        print("User cannot be registered")
        form = UserRegisterForm()

    context = {
        'form': form,
    }

    return render(request, "userauths/sign-up.html", context)


def login_view(request):           
    if request.user.is_authenticated:           # check if user is already authenticated
        messages.warning(request, f"You are already Logged In!")
        return redirect("core:index")
        # return render(request, "userauths/sign-in.html")

    if request.method == "POST":              #check if method used is POST
        email = request.POST.get("email") 
        password = request.POST.get("password")
        
        try:
            user = User.objects.get(email=email)       # check credentials match
        except: 
            messages.warning(request, f"User with {email} does not exist")

        user = authenticate(request, email=email, password=password)        # login functionality / redirect

        if user is not None:
            login(request, user)
            messages.success(request, "You are logged in.")
            return redirect("core:index")

        else: 
            messages.warning(request, "User Does Not Exist.")

    context = {}

    return render(request, "userauths/sign-in.html", context)


def logout_view(request):       # a string URL will be passed later on
    logout(request)
    messages.success(request, "You've been Logged-out.")
    return redirect("userauths:sign-in")







