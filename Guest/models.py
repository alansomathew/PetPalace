from django.db import models

from Admin.models import District, HospitalType, Place

# Create your models here.
class Newuser(models.Model):
    name=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    email=models.EmailField(unique=True, max_length=50)
    address=models.TextField(max_length=50)
    place=models.ForeignKey(Place,on_delete=models.CASCADE)
    photo=models.FileField(upload_to='Uploads/newuserphotos/')
    password=models.CharField(max_length=50)
    doj=models.DateField(auto_now_add=True)
    
class NewShop(models.Model):
    name=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    email=models.EmailField(unique=True, max_length=50)
    address=models.TextField(max_length=50)
    shopownername=models.CharField(max_length=50,null=True)
    shopownercontact=models.CharField(max_length=50,null=True)

    place=models.ForeignKey(Place,on_delete=models.CASCADE)
    proof=models.FileField(upload_to='Uploads/newshopphotos/proofphotos/')
    logo=models.ImageField(upload_to='Uploads/newshopphotos/logophotos/')
    password=models.CharField(max_length=50)
    doj=models.DateField(auto_now_add=True)
    vstatus=models.IntegerField(default=False)


class NewHospital(models.Model):
    name=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    email=models.EmailField(unique=True, max_length=50)
    address=models.TextField(max_length=50)
    place=models.ForeignKey(Place,on_delete=models.CASCADE)
    hospitaltype=models.ForeignKey(HospitalType,on_delete=models.CASCADE,null=True)
    proof=models.FileField(upload_to='Uploads/newhospitalphotos/proofphotos/')
    logo=models.FileField(upload_to='Uploads/newhospitalphotos/logophotos/')
    password=models.CharField(max_length=50)
    doj=models.DateField(auto_now_add=True)
    vstatus=models.IntegerField(default=False)

