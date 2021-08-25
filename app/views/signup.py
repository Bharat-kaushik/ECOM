from django.shortcuts import render, HttpResponse, redirect
from rest_framework.decorators import api_view
from django.db import IntegrityError

from businesslogic.services.user_service import add_user


@api_view(("POST",))
def do_signup(request):
    """
    Creating a new user.
    """
    password = request.POST.get('password')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email_id = request.POST.get('email')

    # try to create new user
    try:
        user = add_user(
            first_name=first_name,
            last_name=last_name,
            password=password,
            email_id=email_id,
            is_active=True
        )
        return render(request, 'login.html', {
            "messages": ["Successfully Registered Please login."],
            "title": "Register"
        })

    # catch integrity error
    except IntegrityError as e:
        return render(request, 'signup.html', {
            "messages": ["User with this email exists."],
            "title": "Register"

        })

    # catch other exception
    except Exception as e:
        return render(request, 'signup.html', {
            "messages": [str(e)],
            "title": "Register"
        })


@api_view(("GET", ))
def signup_form(request):
    """
     render a signup form
    """
    return render(request, 'signup.html', {
        "title": "Register"
    })
