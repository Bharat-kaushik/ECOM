from datetime import datetime

from django.db import IntegrityError
from django.shortcuts import render
from businesslogic.domain.user import User


def add_user(first_name: str,
             password: str,
             email_id: str,
             last_name: str = "",
             is_active: bool = False,
             is_staff: bool = False,
             is_superuser: bool = False,
             ):

    """
    Create New user.
    """
    user = User()
    user.first_name = first_name
    user.last_name = last_name
    user.email = email_id
    user.is_staff = is_staff
    user.is_active = is_active
    user.is_superuser = is_superuser
    user.set_password(password)

    try:
        user.save()
    except IntegrityError as e:
        raise e
    except Exception as e:
        raise e

    return user
