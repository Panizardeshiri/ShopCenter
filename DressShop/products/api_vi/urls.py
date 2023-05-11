from django.urls import path,include
from .views import *


app_name = 'api_products'

urlpatterns = [

    path('products-list/',ProductListView.as_view(),name='products-list'),
    path('product-detail/<int:id>',ProductDetailView.as_view(),name='product-detail')
    
]