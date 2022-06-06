from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.conf import settings


# Create your models here.
class CustomAccountManager(BaseUserManager):

    def create_superuser(self,email,user_name,first_name,password,**other_fields):

        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active',True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True'
            )
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True'
            )
        return self.create_user(email,user_name,first_name,password,**other_fields)

    def create_user(self,email,user_name,first_name,password,**other_fields):

        if not email:
            raise ValueError(_('You must provide an email adress'))
        
        email = self.normalize_email(email)
        user = self.model(email=email,user_name=user_name,first_name=first_name,**other_fields)
        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(_('email adress'),unique=True)
    user_name = models.CharField(max_length=120,unique=True)
    first_name = models.CharField(max_length=120,blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name','first_name']

    def __str__(self):
        return self.user_name


class Car(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=30)
    brand = models.CharField(max_length=30,default='mercedes')
    price = models.CharField(max_length=10)
    luggage = models.CharField(max_length=20)
    doors = models.CharField(max_length=10)
    passengers = models.CharField(max_length=10)
    transmission = models.CharField(max_length=30)
    gas = models.CharField(max_length=30)
    interior1 = models.ImageField(upload_to='images/')
    interior2 = models.ImageField(upload_to='images/')
    interior3 = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

class Featured(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=30)
    price = models.CharField(max_length=10)
    luggage = models.CharField(max_length=20)
    doors = models.CharField(max_length=10)
    passengers = models.CharField(max_length=10)
    transmission = models.CharField(max_length=30)
    gas = models.CharField(max_length=30)
    interior1 = models.ImageField(upload_to='images/')
    interior2 = models.ImageField(upload_to='images/')
    interior3 = models.ImageField(upload_to='images/')