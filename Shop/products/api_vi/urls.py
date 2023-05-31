from django.urls import path,include
from .views import *


app_name='api-products'

urlpatterns = [
    path('products-list/',ProductListView.as_view(),name='products-list'),
    path('product-detail/<int:id>',ProductDetailView.as_view(),name='product-detail'),
    # path('cart/',CartView.as_view(),name='cart'),
    # path('cart-detail/<int:id>',CartItemDetailView.as_view(),name='cart-detail'),
    # path('add-cart/',AddCartView.as_view(),name='add-cart'),
    path('cartitem',CartItemView.as_view(),name='cart-item')
]