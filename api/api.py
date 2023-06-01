from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from shop.models import Cart as UserCart
from shop.models import CartItem, Product
from django.contrib import messages
# Create your views here.


class Cart:
    @login_required
    def add(request, product_ref):
        product = Product.objects.get(title=product_ref)
        users_cart = UserCart.objects.get(belongs_to=request.user)
        try:
            already_added_item = CartItem.objects.get(
                cart=users_cart, product=product)
        except CartItem.DoesNotExist:
            already_added_item = None
        print(already_added_item)
        if already_added_item != None:
            already_added_item.quantity += 1
            already_added_item.save()
        else:
            item = CartItem.objects.create(cart=users_cart, product=product)
            item.save()
        return redirect('index')

    def buy_now(request, product_ref):
        product = Product.objects.get(title=product_ref)
        users_cart = UserCart.objects.get(belongs_to=request.user)
        try:
            already_added_item = CartItem.objects.get(
                cart=users_cart, product=product)
        except CartItem.DoesNotExist:
            already_added_item = None
        if already_added_item != None:
            already_added_item.quantity += 1
            already_added_item.save()
        else:
            item = CartItem.objects.create(cart=users_cart, product=product)
            item.save()
        return redirect('checkout')


    def add(request, product_ref):
        product = Product.objects.get(title=product_ref)
        users_cart = UserCart.objects.get(belongs_to=request.user)
        try:
            already_added_item = CartItem.objects.get(
                cart=users_cart, product=product)
        except CartItem.DoesNotExist:
            already_added_item = None
        print(already_added_item)
        if already_added_item != None:
            already_added_item.quantity += 1
            already_added_item.save()
        else:
            item = CartItem.objects.create(cart=users_cart, product=product)
            item.save()
        return redirect('index')

    @login_required
    def clear(request):
        users_cart = UserCart.objects.get(belongs_to=request.user)
        CartItem.objects.filter(cart=users_cart).delete()
        return redirect('index')

    @login_required
    def increment_item(request, product_ref):
        product = Product.objects.get(title=product_ref)
        users_cart = UserCart.objects.get(belongs_to=request.user)
        item = CartItem.objects.get(cart=users_cart, product=product)
        if item.quantity < 10:
            item.quantity += 1
            item.save()
        else:
            messages.success(
                request, 'You have reached to the maximum quantity of each item, that is restricted to 10😖')
        return redirect('index')

    @login_required
    def decrement_item(request, product_ref):
        product = Product.objects.get(title=product_ref)
        users_cart = UserCart.objects.get(belongs_to=request.user)
        item = CartItem.objects.get(cart=users_cart, product=product)
        if item.quantity > 1:
            item.quantity -= 1
            item.save()
        else:
            item.delete()
        return redirect('index')

    @login_required
    def increment_item_checkout(request, product_ref):
        product = Product.objects.get(title=product_ref)
        users_cart = UserCart.objects.get(belongs_to=request.user)
        item = CartItem.objects.get(cart=users_cart, product=product)
        if item.quantity < 10:
            item.quantity += 1
            item.save()
        else:
            messages.success(
                request, 'You have reached to the maximum quantity of each item, that is restricted to 10😖')
        return redirect('checkout')

    @login_required
    def decrement_item_checkout(request, product_ref):
        product = Product.objects.get(title=product_ref)
        users_cart = UserCart.objects.get(belongs_to=request.user)
        item = CartItem.objects.get(cart=users_cart, product=product)
        if item.quantity > 1:
            item.quantity -= 1
            item.save()
        else:
            item.delete()
        return redirect('checkout')
