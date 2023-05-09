from .views import *
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.views.decorators.csrf import csrf_exempt

app_name= 'api_user'
urlpatterns = [
    path('register/',UserRegisterView.as_view(),name='register'),
    path('login/', UserLoginView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', UserLogoutView.as_view(),name='logout'),
    path('send-sms/',csrf_exempt(SmsView.as_view()),name='send-sms'),
    path('verify-smscode/',VerifySmsView.as_view(),name='verify-smscode'),
    path('resend-code/', ResendCodeView.as_view(),name='resend-code'),
    path('forget-pass/',ForgetPassView.as_view(),name='forget-pass'),
    path('change-pass/',ChangePassView.as_view(),name='change-pass'),
    # path('n/',NewRView.as_view(),)
    # path('validation-sms/<code:int>/')

]