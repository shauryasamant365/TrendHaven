from django.urls import path
from .api import Cart

urlpatterns = [
    path('add-to-cart/<str:product_ref>/', Cart.add, name='add-to-cart'),
    path('buy_now/<str:product_ref>/', Cart.buy_now, name='buy-now'),
    path('clear-cart/', Cart.clear, name='clear-cart'),
    path('increment/<str:product_ref>/', Cart.increment_item, name='increment-cart-item'),
    path('decrement/<str:product_ref>/', Cart.decrement_item, name='decrement-cart-item'),
    path('increment/checkout/<str:product_ref>/', Cart.increment_item_checkout, name='increment-cart-item'),
    path('decrement/checkout/<str:product_ref>/', Cart.decrement_item_checkout, name='decrement-cart-item'),
]
