from django.shortcuts import render


from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User Not Found....")
            return redirect("home")

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Username or Password does not match...")

    return render(request, "authentication/login.html")
