from django.db import models
from unicodedata import name
from urllib import request


# Create your models here.

class District(models.Model):
    district=models.CharField(max_length=50)

class Place(models.Model):
    place=models.CharField(max_length=50)
    district=models.ForeignKey(District,on_delete=models.CASCADE)

class PetType(models.Model):
    pettype=models.CharField(max_length=50)

class BreedType(models.Model):
    breedtype=models.CharField(max_length=50)
    pettype=models.ForeignKey(PetType,on_delete=models.CASCADE)

class ProductType(models.Model):
    producttype=models.CharField(max_length=50)

class HospitalType(models.Model):
    hospitaltype=models.CharField(max_length=50)

class Adminlogin(models.Model):
    adminemail=models.EmailField(unique=True,max_length=50)
    adminpassword=models.CharField(max_length=50)