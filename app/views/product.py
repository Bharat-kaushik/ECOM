from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from django.db import IntegrityError

from app.views.helper_method import get_image_url
from businesslogic.services.product_service import add_products
from businesslogic.repositories.product_repository import ProductRepository


@api_view(("POST", ))
def add_product(request):

    """
     Add New Product
    """
    title = request.POST.get('title')
    photo = request.FILES.get('photo')
    description = request.POST.get('description', '')
    price = request.POST.get('price')

    # try to add product in db
    try:
        product = add_products(
            title=title,
            photo=photo,
            description=description,
            price=price
        )
        return redirect('/products_list')

    # Catch integrity error
    except IntegrityError as e:
        print("here")
        return render(request, 'add_product.html', {
            "messages": [str(e)],
            "title": "Add Product"
        })

    # catch other exceptions
    except Exception as e:
        print("there")
        return render(request, 'add_product.html', {
            "messages": [str(e)],
            "title": "Add Product"
        })


@api_view(("GET", ))
def product_form(request):
    """
    render product form
    """
    return render(request, 'add_product.html', {
        "title": "Add Product"
    })


@api_view(("GET", ))
def products_list(request):
    """
     Function to get all products List
    """
    product_repo = ProductRepository()
    products = product_repo.get_all()

    product_list = []
    for product in products:
        image = product.image  # get image path from product
        image_url = get_image_url(request, str(image))  # create url to show images
        product.image = image_url  # update product image from path to url
        product_list.append(product)
    return render(request, 'products_list.html', {
        'products': product_list,
        'title': 'Products'
    })