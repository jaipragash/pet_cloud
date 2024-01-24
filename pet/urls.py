from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('login1/', views.login1, name='login1'),
    path('register', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'), 
    path('collections/', views.collections, name='collections'), 
    path('collections/<str:name>', views.collectionsview, name='collections'), 
    path('collections/<str:cname>/<str:pname>', views.product_detail, name='product_detail'),
    path('addtocart', views.add_to_cart, name='addtocart'),
    path('cart', views.cart_page, name='cart'),
    path('remove_cart/<str:cid>', views.remove_cart, name='remove_cart'),
]
