from rest_framework import serializers
from ..models import *
from django.conf import settings
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenBlacklistSerializer
from django.core.exceptions import ObjectDoesNotExist
from phonenumber_field.validators import validate_international_phonenumber
from datetime import datetime, timedelta,timezone
import random
from .utils import send_sms_code
from django.utils import timezone
from datetime import *
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
import re




# Define UserRegisterSerializer class
class UserRegisterSerializer(serializers.ModelSerializer):
    # phone = serializers.CharField(max_length=15, validators=[validate_international_phonenumber])
    phone = serializers.CharField(max_length=15)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('phone','password','password2')


  
    
    def validate(self,attrs):
        phone_regex = "^([0]{1}[0-9]{3}[0-9]{3}[0-9]{4})|([\+]{1}[0-9]{1,3}[0-9]{3}[0-9]{4,6})"
        is_phone=re.search(phone_regex, attrs['phone']) 
        if  is_phone==None:
            raise serializers.ValidationError ({'phone':'please enter valid phone number'})
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password':'password does not matched'})
        
        return attrs
    
    


    def create(self,validated_data):
        sms_code = random.randint(100000,999999)
        sms_code_expiry = datetime.now()+ timedelta(minutes=5)
        user = User(
            phone=validated_data['phone'],
            sms_code=sms_code,
            sms_code_expiry = sms_code_expiry,
            max_sms_code_try=settings.MAX_SMS_CODE_TRY,
            )
        user.set_password(validated_data['password'])
        user.save()
        #call send sms_code function
        send_sms_code(sms_code,user.phone)
        return user
    


class UserLoginSerializer(TokenObtainPairSerializer):
    
    def validate(self, attrs):
        data = super().validate(attrs)
        access_token=data['access']
        refresh_token=data['refresh']

        user = User.objects.get(phone=attrs['phone'])
        if user.is_logged_in:
            raise serializers.ValidationError({'error':'User is logged in before'})
        user.is_logged_in =True
        user.access_token=access_token
        user.refresh_token=refresh_token
        user.save()
        return data




# Define UserLogoutSerializer class
class UserLogoutSerializer(TokenBlacklistSerializer):
    def validate(self, attrs):
        data = super(UserLogoutSerializer, self).validate(attrs)
        data['detail'] = "User Successfully Logged Out"
        return data
    



class UserVerifySerializer(serializers.ModelSerializer):
    phone = serializers.CharField(max_length=15, validators=[validate_international_phonenumber])
    sms_code = serializers.CharField(max_length=6)

    class Meta:
        model = User
        fields = ('phone','sms_code')



# Define ResendCodeSerializer Class
class ResendCodeSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(max_length=15, validators=[validate_international_phonenumber])

    class Meta:
        model =User
        fields =('phone',)


class ForgetPassSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(max_length=15, validators=[validate_international_phonenumber])

    class Meta:
        model = User
        fields = ('phone',)

class ResetPassSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=15, validators=[validate_international_phonenumber])
    pass_code = serializers.CharField(max_length=6)
    new_pass = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    new_pass_confirm = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    
    def validate(self, attrs):
        if attrs['new_pass'] != attrs['new_pass_confirm']:
            raise serializers.ValidationError({'password':'Password does not match'})
        return attrs


class ChangePassSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=15, validators=[validate_international_phonenumber])
    old_pass = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    new_pass = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    new_pass_confirm = serializers.CharField(write_only=True, required=True, validators=[validate_password])



    def validate(self, attrs):
        if attrs['old_pass'] == attrs['new_pass']:
            raise serializers.ValidationError({'password': 'New Pass Must be Different from the Old Pass'})
        return attrs    
    
class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = '__all__'
        

