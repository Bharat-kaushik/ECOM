from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from rest_framework.decorators import api_view


@api_view(("POST",))
def login_user(request):
    """
    Method to Login the user.
    """
    # Get email and password from request.
    username = request.POST.get('username')
    password = request.POST.get('password')

    # Authenticate whether username or password is correct
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user) #login user
        user.save()
        return redirect('/products_list')
    else:
        return render(request, "login.html", {
            "messages": ["Email or Password is incorrect."],
            "title": "Login"
        })


@api_view(("GET", ))
def login_get(request):
    """
     Function to render login form/ if already logged in then redirect to products list.
    """
    if request.user.is_authenticated:
        return redirect('/products_list')
    return render(request, 'login.html', {'title': 'login'})


@login_required(login_url='login')
def logoutuser(request):
    """
     Logout user
    """
    logout(request)
    return redirect('/products_list')

