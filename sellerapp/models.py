from django.db import models

# Create your models here.
class sellpetdb(models.Model):
    pname = models.CharField(max_length=50, null=True, blank=True)
    breed = models.CharField(max_length=50, null=True, blank=True)
    age = models.CharField(max_length=50, null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    address = models.TextField(max_length=50, null=True, blank=True)
    phone = models.IntegerField(null=True,blank=True)
    name=models.CharField(max_length=50,null=True,blank=True)
    petimg = models.ImageField(upload_to="pet_img", null=True, blank=True)


class sellersigndb(models.Model):
    sname=models.CharField(max_length=50,null=True,blank=True)
    paswrd=models.CharField(max_length=50,null=True,blank=True)
    re_pswrd=models.CharField(max_length=50,null=True,blank=True)
    email=models.CharField(max_length=50,null=True,blank=True)
    phone=models.IntegerField(null=True,blank=True)



