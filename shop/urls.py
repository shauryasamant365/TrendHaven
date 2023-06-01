from django.urls import path
from . import views, authentication, product

urlpatterns = [
    path('', views.index, name='index'),
    
    # Auth / User account related URL patterns
    path('account/', authentication.account, name='account'),
    path('login/', authentication.login, name='login'),
    path('signup/', authentication.signup, name='signup'),
    path('logout/', authentication.signout, name='signout'),
    path('completeReg/', authentication.completeReg, name='completeReg'),
    path('delete-me/', authentication.deleteUser, name='deleteUser'),
    path('orders/', product.orders, name='orders'),
    path('update/', authentication.update, name='update'),
    path('category/', views.category, name='category'),
    path('collections/', views.collections, name='collections'),
    path('saved_products/', views.saved_product, name='saved_products'),
    path('delete-acc/', views.delete_acc, name='delete-acc'),
    path('token', authentication.token_send, name="token_send"),
    path('verify/<auth_token>', authentication.verify, name="verify"),
    
    # Product related URL patterns
    path('save_product/<str:product_ref>/',
         product.save_product, name='save_product'),
    path('remove_save_product/<str:product_ref>/',
         product.delete_saved_product, name='delete_save_product'),
    path('product/<str:product_ref>/', product.view, name='productView'),
    path('checkout/', product.checkout, name='checkout'),
]
