from django.db import models
from Admin.models import BreedType


from Guest.models import NewShop

# Create your models here.

class NewPets(models.Model):
    breedtype=models.ForeignKey(BreedType,on_delete=models.CASCADE)
    rate=models.CharField(max_length=50)
    image=models.FileField(upload_to='Uploads/newpets/image/',null=True)
    license=models.FileField(upload_to='Uploads/newpets/license/',null=True)
    details=models.CharField(max_length=50)
    stock=models.IntegerField()
    shop=models.ForeignKey(NewShop,on_delete=models.CASCADE)
    doj=models.DateField(auto_now_add=True)


class NewProducts(models.Model):
    productname=models.CharField(max_length=50)
    breedtype=models.ForeignKey(BreedType,on_delete=models.CASCADE)
    rate=models.CharField(max_length=50)
    image=models.FileField(upload_to='Uploads/newproducts/image/',null=True)
    stock=models.IntegerField()
    productdetails=models.TextField(max_length=50,null=True)
    shop=models.ForeignKey(NewShop,on_delete=models.CASCADE)
    doj=models.DateField(auto_now_add=True)


class NewFoodItem(models.Model):
    fooditemname=models.CharField(max_length=50)
    breedtype=models.ForeignKey(BreedType,on_delete=models.CASCADE)
    rate=models.CharField(max_length=50)
    image=models.FileField(upload_to='Uploads/newfooditem/image/',null=True)
    stock=models.IntegerField()
    fooditemdetails=models.TextField(max_length=50,null=True)

    shop=models.ForeignKey(NewShop,on_delete=models.CASCADE)
    doj=models.DateField(auto_now_add=True)

class feedbackshop(models.Model):
    feedback=models.TextField(max_length=50)
    shop=models.ForeignKey(NewShop,on_delete=models.CASCADE)
    doj=models.DateField(auto_now_add=True)


class complaintshop(models.Model):
    complainttitle=models.CharField(max_length=50)
    content=models.TextField(max_length=50)
    shop=models.ForeignKey(NewShop,on_delete=models.CASCADE)
    attachment=models.FileField(null=True,upload_to='Uploads/attachmentshop/')
    reply=models.TextField(max_length=50,default="noreply")
    doj=models.DateField(auto_now_add=True)
    status=models.IntegerField(default=False)