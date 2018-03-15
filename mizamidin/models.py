from django.db import models
import uuid
import datetime
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from datetime import date

# Create your models here.
class Type(models.Model):

    name = models.CharField(max_length=200, help_text="Enter a car type ")
    
    def __str__(self):

        return self.name

from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Car(models.Model):

    car_title = models.CharField(max_length=200)
    seller = models.ForeignKey('Seller', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the car")
    isbn = models.CharField('ISBN',max_length=13, help_text='Gost Nomer')
    type = models.ManyToManyField(Type, help_text="Select a type for this car")
    price_car = models.CharField(max_length=20)
    standart = models.CharField(max_length=20)
    date_vp = models.DateField(null=True, blank=True)
    car_ava = models.ImageField(upload_to='car_avas/', null=True, blank=True)
    


    def display_type(self):

        return ', '.join([ type.name for type in self.type.all()[:3] ])
    display_type.short_description = 'Type'
    
    def __str__(self):

        return self.car_title
    
    
    def get_absolute_url(self):

        return reverse('car-detail', args=[str(self.id)])
    def display_type(self):

        return ', '.join([ type.name for type in self.type.all()[:3] ])
    display_type.short_description = 'Type'
import uuid # Required for unique book instances

class MarkInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular book across whole library")
    car = models.ForeignKey('Car', on_delete=models.SET_NULL, null=True) 
    imprint = models.CharField(max_length=200)
    mark = models.CharField(max_length=20)
    made_in = models.CharField(max_length=20)
    crooked = models.CharField(max_length=20)
    due_back = models.DateField(null=True, blank=True)


    LOAN_STATUS = (
        ('m', 'Cridit'),
        ('o', 'Satyldy'),
        ('a', 'Satylady'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='d', help_text='Car Satylymda')
   

    class Meta:
        ordering = ["due_back"]



        

    def __str__(self):

        return '%s (%s)' % (self.id,self.car.car_title)


class Seller(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    

    
    def get_absolute_url(self):

        return reverse('seller-detail', args=[str(self.id)])
    

    def __str__(self):

        return '{0}, {1}'.format(self.last_name,self.first_name)
   
