from django.db import models

from Admin.models import Place
from Guest.models import NewHospital

# Create your models here.

class Newdoctor(models.Model):
    name=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    email=models.EmailField(unique=True, max_length=50)
    address=models.TextField(max_length=50)
    place=models.ForeignKey(Place,on_delete=models.CASCADE)
    photo=models.FileField(upload_to='Uploads/newdoctorphotos/')
    proof=models.FileField(upload_to='Uploads/newdoctorphotos/')
    qualification=models.CharField(max_length=50,null=True)
    password=models.CharField(max_length=50)
    doj=models.DateField(auto_now_add=True)
    hospital=models.ForeignKey(NewHospital,on_delete=models.CASCADE)

class feedbackhospital(models.Model):
    feedback=models.TextField(max_length=50)
    hospital=models.ForeignKey(NewHospital,on_delete=models.CASCADE)
    doj=models.DateField(auto_now_add=True)


class complainthospital(models.Model):
    complainttitle=models.CharField(max_length=50)
    content=models.TextField(max_length=50)
    hospital=models.ForeignKey(NewHospital,on_delete=models.CASCADE)
    attachment=models.FileField(null=True,upload_to='Uploads/attachmenthospital/')
    reply=models.TextField(null=True,max_length=50,default="noreply")
    doj=models.DateField(auto_now_add=True)
    status=models.IntegerField(default=False)
    


