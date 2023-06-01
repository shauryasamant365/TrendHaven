from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    products = Product.objects.all()
    testimonials = Testimonial.objects.all()
    cart_items = []

    if request.user.is_authenticated:
        cart = Cart.objects.get(belongs_to=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
        products_list = []
        for product in products:
            products_list.append(product)
            for cart_item in cart_items:
                if product == cart_item.product:
                    products_list.remove(product)

        params = {'products': products_list,
                  'cart_items': cart_items, 'testimonials': testimonials}
    else:
        params = {'products': products, 'testimonials': testimonials}

    return render(request, 'shop/index.html', params)


def category(request):
    messages.success(
        request, 'This page that features `Product by Category` is under development and will be available soon.')
    return redirect('index')


def collections(request):
    messages.success(
        request, 'This page that features `Our Preminum Collection` is under development and will be available soon.')
    return redirect('index')


@login_required
def saved_product(request):
    products = SavedProduct.objects.filter(user=request.user)
    if len(products) == 0:
        messages.success(
            request, 'You have not saved any products yet. Add some products and try again.')
        return redirect('index')
    else:
        return render(request, 'shop/saved_prod.html', {'products': products})


@login_required
def delete_acc(request):
    request.user.delete()
    messages.success(
        request, 'Your account was deleted successfully. See you soon 😕')
    return redirect('index')
