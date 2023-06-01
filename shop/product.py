from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def view(request, product_ref):
    product = Product.objects.get(title=product_ref)
    return render(request, 'shop/product/view.html', {'product': product})


@login_required
def checkout(request):
    cart = Cart.objects.get(belongs_to=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    if len(cart_items) == 0:
        messages.success(
            request, 'Your cart seems to be empty. Please add some product and try again.')
        return redirect('index')
    else:
        if request.method == "POST":
            order = Order.objects.create(
                user=request.user,
                card_holder=request.POST['card-holder'],
                card_number=request.POST['card-number'],
                validity=request.POST['validity'],
                cvv=request.POST['credit-cvv'],
                street_address=request.POST['street-address'],
                state=request.POST['state'],
                zip=request.POST['zip'],
            )

            for cart_item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=cart_item.product,
                    quantity=cart_item.quantity,
                )
            cart_items.delete()
            messages.success(request, 'Your order is sent successfully!')
            return redirect("index")
        else:
            total = 0
            for cart_item in cart_items:
                total += cart_item.product.price * cart_item.quantity

            grand_total = total + 50
            return render(request, 'shop/product/checkout.html', {'cart_items': cart_items, 'total': total, 'grand_total': grand_total})


@login_required
def orders(request):
    order = Order.objects.filter(user=request.user)
    order_items = OrderItem.objects.filter(order__in=order)
    if len(order_items) == 0:
        messages.success(
            request, 'You have no order history. Place an order and try again.')
        return redirect('index')
    else:
        return render(request, 'shop/orders.html', {'orders': order_items})


@login_required
def save_product(request, product_ref):
    product = Product.objects.get(title=product_ref)
    SavedProduct.objects.create(user=request.user, product=product)

    return redirect('index')


@login_required
def delete_saved_product(request, product_ref):
    SavedProduct.objects.get(
        user=request.user, product=Product.objects.get(title=product_ref)).delete()
    messages.success(request, 'The product was removed successfully!')
    return redirect('index')

