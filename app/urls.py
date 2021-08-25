from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth import settings
from app.views import (
    login,
    signup,
    product,
    address,
    order,
    validatemail_api
)

urlpatterns = [
    path('', product.products_list),
    path('login', login.login_get),
    path('dologin', login.login_user),
    path('dosignup', signup.do_signup),
    path('logout', login.logoutuser),
    path('signup', signup.signup_form),
    path('product_form', product.product_form),
    path('products_list', product.products_list),
    path('add_product', product.add_product),
    path('add_order', order.create_order),
    path('address_form/<int:p_id>', address.address_form),
    path('add_address', address.register_address),
    path('address_list/<int:p_id>', address.address_list),
    path('api/validatemail', validatemail_api.validate_email),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
