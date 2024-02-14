from django.db import models

# Create your models here.
class catedb(models.Model):
    pname=models.CharField(max_length=50,null=True,blank=True)
    pdes=models.CharField(max_length=50,null=True,blank=True)
    pimg=models.ImageField(upload_to="profile_img",null=True,blank=True)
class petdb(models.Model):
    pname=models.CharField(max_length=50,null=True,blank=True)
    breed=models.CharField(max_length=50,null=True,blank=True)
    age=models.CharField(max_length=50,null=True,blank=True)
    color=models.CharField(max_length=50,null=True,blank=True)
    gender=models.CharField(max_length=50,null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    address=models.CharField(max_length=50,null=True,blank=True)
    aname=models.CharField(max_length=50,null=True,blank=True)
    aemail=models.CharField(max_length=50,null=True,blank=True)
    amob=models.CharField(max_length=50,null=True,blank=True)

    petimg=models.ImageField(upload_to="pet_img",null=True,blank=True)
class shopdb(models.Model):
    sname=models.CharField(max_length=50,null=True,blank=True)
    simg=models.ImageField(upload_to="shop_img",null=True,blank=True)
class fooddb(models.Model):
    pname=models.CharField(max_length=50,null=True,blank=True)
    sname = models.CharField(max_length=50, null=True, blank=True)
    name=models.CharField(max_length=50,null=True,blank=True)
    des=models.CharField(max_length=100,null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    fimg=models.ImageField(upload_to="food_img",null=True,blank=True)






