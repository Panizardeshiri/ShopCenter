from django.contrib import admin
from django.urls import path,include
from .views import *

app_name = 'accounts'

urlpatterns = [
    
    path('api-vi/',include('accounts.api_vi.urls'),name = 'api-user'),
    
]