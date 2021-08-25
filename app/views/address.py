from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

from businesslogic.services.address_service import add_address
from businesslogic.repositories.address_repository import AddressRepository


@login_required(login_url='/login')
@api_view(("POST", ))
def register_address(request):
    """
        Function to save address for user
    """
    user = request.user     # Getting user from request
    # Fetching input fields data from request
    address = request.POST.get("address")
    state = request.POST.get("state")
    city = request.POST.get("city")
    zip = request.POST.get("zip")
    product_id = request.POST.get('prod_info')

    # Try to register address user
    try:
        address = add_address(
            user=user,
            local_address=address,
            city=city,
            state=state,
            zip=zip
        )
        return redirect(f'/address_list/{product_id}')

    # Catch Integrity error
    except IntegrityError as e:
        return render(request, 'add_address.html', {
            "messages": [str(e)],
            "title": "Add Address"
        })

    # catch other exceptions
    except Exception as e:
        return render(request, 'add_address.html', {
            "messages": [str(e)],
            "title": "Add Address"
        })


@login_required(login_url='/login')
@api_view(("GET", ))
def address_form(request, p_id):
    """
        Method to render the address form
    """
    return render(request, 'add_address.html', {
        "product_id": p_id,
        "title": "Add Address"

    })


@login_required(login_url='/login')
@api_view(("GET", ))
def address_list(request, p_id):
    """
    Method to get all the address for current user
    """
    user = request.user
    address_repo = AddressRepository()

    # try to fetch address for current user
    try:
        address = address_repo.get_address_for_user(user)

    # catch exception
    except Exception as e:
        return render(request, 'products_list.html', {
            "messages": [str(e)],
            "title": "Products"
        })

    # check if there is any address available or not
    if len(address):
        return render(request, 'address.html', {
            "addresses": address,
            "product_id": p_id,
            "title": "Address"
        })

    # if address is not present render this block
    else:
        return render(request, 'address_not_found.html', {
            "product_id": p_id,
            "title": "Address Not Found"
        })