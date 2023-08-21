from django.contrib import admin
from django.urls import path,include
from .views import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.views import TokenRefreshView

app_name = 'api-user'

urlpatterns = [
    
    path('register/',UserRegisterView.as_view(),name = 'register'),
    path('login/',Login.as_view(), name='login'),
    path('refresh/',TokenRefreshView.as_view(), name='refresh'),
    path('logout/', Logout.as_view(), name='logout'),
    path('t-view/', t_view.as_view(), name='t-view'),
    path('send-sms/',csrf_exempt(SmsView.as_view()),name='send-sms'),
    path('verify-smscode/',VerifySmsView.as_view(),name='verify-smscode'),
    path('resend-code/', ResendCodeView.as_view(),name='resend-code'),
    path('forget-pass/',ForgetPassView.as_view(),name='forget-pass'),
    path('change-pass/',ChangePassView.as_view(),name='change-pass'),
    path('reset-pass/',ResetPassView.as_view(),name='reset-pass'),
    path('profile/',ProfileView.as_view(), name='profile'),
    path('address/',AddressView.as_view(), name='address'),
]