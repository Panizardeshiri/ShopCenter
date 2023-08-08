from django.urls import path,include
from .views import *


app_name='api-products'

urlpatterns = [
    path('products-list/',ProductListView.as_view(),name='products-list'),
    path('product-detail/<int:id>',ProductDetailView.as_view(),name='product-detail'),
    path('favorit-list',FavoritListView.as_view(),name= 'favorit-list'),
     path('addto-favorit-list/<int:id>',AddToFavoritListView.as_view(),name= 'addto-favorit-list'),
    path('cart/',CartView.as_view(),name='cart'),
    path('cart-detail/<int:id>',CartDetailView.as_view(),name='cart-detail'),
    path('shopping-cart/',ShoppingCartView.as_view(),name='shopping-cart'),
  
    # path('request/', SendRequestView.as_view(), name='send-request'),
    # path('verify/', VerifyView.as_view() , name='verify'),
   
 
    
]