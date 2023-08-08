from rest_framework.generics import GenericAPIView
from .serializers import *
from django.contrib.auth import get_user_model
from rest_framework import status
from .utils import send_sms_code,get_tokens_for_user
from rest_framework.response import Response
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView
)
from .utils import send_sms_code
from rest_framework.views import APIView
import ghasedakpack
from datetime import timezone
from datetime import datetime, timedelta
import random
from django.conf import settings
from django.utils import timezone
from datetime import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication,BasicAuthentication,TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken , OutstandingToken
import environ
env = environ.Env()
User = get_user_model()

# UserRegistrationView
class UserRegisterView(GenericAPIView):
    serializer_class = UserRegisterSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:serializer.save()
        except: raise serializers.ValidationError({'phone':'phone alredy exist'})
        user = User.objects.get(phone=serializer.validated_data['phone'])
        refresh_token, access_token = get_tokens_for_user(user)
        return Response(
            {'message':'User Successfully Registered',
             'refresh_token': refresh_token,
             'access_token': access_token
            },status= status.HTTP_201_CREATED)

# Create your views here.


# USerLogoutView


class Logout(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        tokens = OutstandingToken.objects.filter(user_id=request.user.id)

        for token in tokens:
            t,_ = BlacklistedToken.objects.get_or_create(token= token)
            
         
        tokens.delete()
        return Response({'detail':'logout seccuesfully'},status=status.HTTP_200_OK)   

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
class Login(TokenObtainPairView):
    serializer_class = UserLoginSerializer



class VerifySmsView(GenericAPIView):
    serializer_class= UserVerifySerializer

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        # print(serializer.data)
        user = User.objects.get(phone=serializer.validated_data.get('phone'))
        if (not user.is_verified
            and user.sms_code == serializer.validated_data.get('sms_code')
            and user.sms_code_expiry
        ):
            user.is_verified = True
            user.sms_code_expiry = None
            user.save()
            return Response({
                'status':status.HTTP_200_OK,
                'message': 'Seccessfully Verified User'

            })
        else:
            return Response({
                'status':status.HTTP_400_BAD_REQUEST,
                'message': 'User is verified before Or Please Enter the Correct Code'
            })










class ResendCodeView(GenericAPIView):
    serializer_class = ResendCodeSerializer

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user  = User.objects.get(phone=serializer.validated_data.get('phone'))

        if int(user.max_sms_code_try)==0 and datetime.now()<user.sms_code_max_out.replace(tzinfo=None):
            return Response('max sms_code try reached, try after an hour')

        sms_code = random.randint(100000, 999999)
        sms_code_expiry = datetime.now() + timedelta(minutes=5)
        max_sms_code_try = int(user.max_sms_code_try) -1

        user.sms_code = sms_code
        user.sms_code_expiry = sms_code_expiry
        user.max_sms_code_try = max_sms_code_try
        if max_sms_code_try == 0:
            user.sms_code_max_out = datetime.now() + timedelta(hours=1)
        elif max_sms_code_try == -1:
            user.max_sms_code_try = settings.MAX_SMS_CODE_TRY
        else:
            user.sms_code_max_out =None
            user.max_sms_code_try= max_sms_code_try

        user.save()
        send_sms_code(sms_code,user.phone)
        return Response('resend successfully')


class ForgetPassView(GenericAPIView):
    serializer_class = ForgetPassSerializer

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        # print(serializer.data)
        user = User.objects.get(phone=serializer.validated_data.get('phone'))
        pass_code = random.randint(100000, 999999)
        user.pass_code = pass_code
        user.save()
        send_sms_code(pass_code, user.phone)
        return Response('Code sent')

class ChangePassView(GenericAPIView):
    serializer_class = ChangePassSerializer

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(phone=serializer.validated_data.get('phone'))
        if user.pass_code == serializer.validated_data.get('pass_code'):
            user.set_password(serializer.validated_data.get('new_pass'))
            user.save()
            return Response('the pass changed successfully')
        else:
            return Response('please enter the correct code')




class SmsView(APIView):
    def get(self, request):
        sms = ghasedakpack.Ghasedak(env('Ghasedak_api_key'))
        code = 123
        # sms.send({"message":f'hello {code}', 'receptor':'09232905208','linenumber':'300002525'})
        send_sms_code(code,'phone')
        return Response('ok')
    
class t_view(APIView):
    # permission_classes=[IsAuthenticated]
    def get(self, request):
        # user = User.objects.get(phone='+989017963636')
        print(request.user.is_logged_in)
        return Response({'detail':'ok'})

# ghasedakpack_api =d8cf3910d2c2bbb0d048fb53799e64f014b50021dc263168b28501697f17f138
# 5.114.182.131