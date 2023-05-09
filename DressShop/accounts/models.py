from django.db import models
from django.contrib.auth.models import PermissionsMixin, BaseUserManager, AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings
from datetime import timedelta

# Create your models here.
# Create UserManager
class UserManager(BaseUserManager):
    def create_user(self,phone , password, **extra_fields):
        if not phone:
            raise ValueError(_("The phone must be set"))
        print(50 * "*", phone)
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Superuser must have is_staff=True"))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("Superuser must have is_superuser=True"))
        return self.create_user(phone, password, **extra_fields)

# Create User Model
class User(AbstractBaseUser, PermissionsMixin):
    phone = PhoneNumberField(blank=True,unique=True)
    sms_code = models.CharField(max_length=6,null=True)
    sms_code_expiry = models.DateTimeField(blank=True, null=True)
    max_sms_code_try = models.CharField(max_length=2,default=settings.MAX_SMS_CODE_TRY)
    sms_code_max_out = models.DateTimeField(blank=True,null=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    pass_code = models.CharField(max_length=6,null=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    user_name = models.CharField(max_length=250, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    objects = UserManager()

    def __str__(self):
        return str(self.phone)


# Create Profile Model
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=255)
    image = models.ImageField(blank=True, null=True)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user.phone)


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


