from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

from businesslogic.repositories.address_repository import AddressRepository
from businesslogic.repositories.product_repository import ProductRepository
from businesslogic.services.order_service import add_order


@login_required(login_url="/login")
@api_view(("POST", ))
def create_order(request):

    """
    creating order
    """

    # getting data from request
    user = request.user
    product_id = request.POST.get('productId')
    address_id = request.POST.get('addressId')

    # check if product id and address id is available
    if product_id and address_id:
        product_repo = ProductRepository()
        address_repo = AddressRepository()

        # try to fetch product and address
        try:
            product = product_repo.get_by_pk(pk=product_id)
            address = address_repo.get_by_pk(pk=address_id)

            # try to create order
            try:
                order = add_order(product=product, address=address)
                return render(request, 'order_placed.html', {
                    "order": order,
                    "title": "Order Placed"
                })

            # catch Integrity Error
            except IntegrityError as e:
                messages.error(request, str(e))
                return redirect('/products_list')\

            # catch other exceptions
            except Exception as e:
                messages.error(request, str(e))
                return redirect('/products_list')

        # catch exception if address or product is not available in db
        except ObjectDoesNotExist as e:
            messages.error(request, str(e))
            return redirect('/products_list')

        # catch other exception
        except Exception as e:
            messages.error(request, str(e))
            return redirect('/products_list')

    # if product id or address id is not available
    else:
        return messages.error(request, "Product and Address is must to Order.")
