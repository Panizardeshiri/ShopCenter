
from django.urls import path,include


app_name = 'products'

urlpatterns = [
    path('api-vi/',include('products.api_vi.urls', namespace="api_products"))
]