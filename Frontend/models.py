from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class signupdb(models.Model):
    uname=models.CharField(max_length=50,null=True,blank=True)
    pswrd=models.CharField(max_length=50,null=True,blank=True)
    re_pswrd=models.CharField(max_length=50,null=True,blank=True)
    email=models.CharField(max_length=50,null=True,blank=True)
    mob=models.IntegerField(null=True,blank=True)
class cartdb(models.Model):
    quantity=models.IntegerField(null=True,blank=True)
    uname=models.CharField(max_length=50,null=True,blank=True)
    name=models.CharField(max_length=50,null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    total_price=models.IntegerField(null=True,blank=True)

class adrsdb(models.Model):
    name=models.CharField(max_length=50,null=True,blank=True)
    email=models.CharField(max_length=50,null=True,blank=True)
    mob=models.IntegerField(null=True,blank=True)
    houseno=models.CharField(max_length=50,null=True,blank=True)
    area=models.CharField(max_length=50,null=True,blank=True)
    landmark=models.CharField(max_length=50,null=True,blank=True)
    pincode=models.IntegerField(null=True,blank=True)
class wishlistdb(models.Model):

    uname=models.CharField(max_length=50,null=True,blank=True)
    name=models.CharField(max_length=50,null=True,blank=True)
    des=models.CharField(max_length=50,null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    wishimg=models.ImageField(upload_to="food_img",null=True,blank=True)
class reviewdb(models.Model):
    uname=models.CharField(max_length=50,null=True,blank=True)
    name=models.CharField(max_length=50,null=True,blank=True)
    review_des=models.CharField(max_length=100,blank=True,null=True)
    rating=models.IntegerField(blank=True,null=True)
class sellerpetdb(models.Model):
    pname = models.CharField(max_length=50, null=True, blank=True)
    selleremail=models.CharField(max_length=50,null=True,blank=True)
    breed = models.CharField(max_length=50, null=True, blank=True)
    age = models.CharField(max_length=50, null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    address = models.TextField(max_length=50, null=True, blank=True)
    phone = models.IntegerField(null=True,blank=True)
    name=models.CharField(max_length=50,null=True,blank=True)
    petimg = models.ImageField(upload_to="pet_img", null=True, blank=True)

class buypagedb(models.Model):
    uname = models.CharField(max_length=50, null=True, blank=True)
    total_price = models.IntegerField(null=True, blank=True)
class notificationdb(models.Model):
    selleremail = models.CharField(max_length=50, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    breed = models.CharField(max_length=50, null=True, blank=True)
    age = models.CharField(max_length=50, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    uname = models.CharField(max_length=50, null=True, blank=True)
    mob=models.IntegerField(null=True,blank=True)
class adminnotificationdb(models.Model):
    aemail=models.CharField(max_length=50,null=True,blank=True)
    amob=models.IntegerField(null=True,blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    breed = models.CharField(max_length=50, null=True, blank=True)
    age = models.CharField(max_length=50, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    uname = models.CharField(max_length=50, null=True, blank=True)
    mob = models.IntegerField(null=True, blank=True)
class contactdb(models.Model):
    name=models.CharField(max_length=50,null=True,blank=True)
    email=models.CharField(max_length=50,null=True,blank=True)
    msg=models.CharField(max_length=100,null=True,blank=True)











