
from django.db import models
from Admin.models import PetType

from Guest.models import NewShop, Newuser

from Hospital.models import Newdoctor
from Shop.models import NewFoodItem, NewPets, NewProducts

# Create your models here.


class BookPet(models.Model):
    bookeddate = models.DateField(auto_now_add=True)
    user = models.ForeignKey(Newuser, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50)
    totalprice = models.CharField(max_length=50)
    pet = models.ForeignKey(NewPets, on_delete=models.CASCADE)
    vstatus = models.IntegerField(default=False)
    pstatus = models.IntegerField(default=False)
    deliverydate=models.CharField(max_length=50,default="Not Declared")



class BookProduct(models.Model):
    bookeddate = models.DateField(auto_now_add=True)
    user = models.ForeignKey(Newuser, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50)
    totalprice = models.CharField(max_length=50)
    product = models.ForeignKey(NewProducts, on_delete=models.CASCADE)
    vstatus = models.IntegerField(default=False)
    pstatus = models.IntegerField(default=False)
    deliverydate=models.CharField(max_length=50,default="Not Declared")



class BookFood(models.Model):
    bookeddate = models.DateField(auto_now_add=True)
    user = models.ForeignKey(Newuser, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50)
    totalprice = models.CharField(max_length=50)
    fooditem = models.ForeignKey(NewFoodItem, on_delete=models.CASCADE)
    vstatus = models.IntegerField(default=False)
    pstatus = models.IntegerField(default=False)
    deliverydate=models.CharField(max_length=50,default="Not Declared")


class feedbackuser(models.Model):
    feedback = models.TextField(max_length=50)
    user = models.ForeignKey(Newuser, on_delete=models.CASCADE)
    doj = models.DateField(auto_now_add=True)


class complaintuser(models.Model):
    complainttitle = models.CharField(max_length=50)
    content = models.TextField(max_length=50)
    user = models.ForeignKey(Newuser, on_delete=models.CASCADE)
    reply = models.TextField(max_length=50, default="noreply")
    attachment = models.FileField(upload_to='Uploads/attachmentuser/')
    doj = models.DateField(auto_now_add=True)
    status = models.IntegerField(default=False)


class BookDoctor(models.Model):
    doj = models.DateField(auto_now_add=True)
    bookingdate = models.CharField(max_length=50)
    bookingtime = models.CharField(max_length=50, null=True)
    user = models.ForeignKey(Newuser, on_delete=models.CASCADE)
    reason = models.CharField(max_length=50)
    consultationfee = models.CharField(max_length=50)
    doctor = models.ForeignKey(Newdoctor, on_delete=models.CASCADE)
    vstatus = models.IntegerField(default=False)
    pstatus = models.IntegerField(default=False)


class complainttoshop1(models.Model):
    complainttitle = models.CharField(max_length=50)
    content = models.TextField(max_length=50)
    user = models.ForeignKey(Newuser, on_delete=models.CASCADE)
    reply = models.TextField(max_length=50, default="noreply")
    attachment = models.FileField(upload_to='Uploads/attachmenttoshop/')
    doj = models.DateField(auto_now_add=True)
    status = models.IntegerField(default=False)
    shop = models.ForeignKey(NewShop, on_delete=models.CASCADE, null=True)


class returnpet(models.Model):
    doj = models.DateField(auto_now_add=True)
    status = models.IntegerField(default=False)
    bookeddate = models.DateField(auto_now_add=True)
    user = models.ForeignKey(Newuser, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50)
    totalprice = models.CharField(max_length=50)
    pet = models.ForeignKey(NewProducts, on_delete=models.CASCADE)
    reply = models.TextField(max_length=50, default="noreply")
    shop = models.ForeignKey(NewShop, on_delete=models.CASCADE)
    reason = models.CharField(max_length=50)
    attachment = models.FileField(upload_to='Uploads/returnpet/')


class feedbackusertoshop(models.Model):
    feedback = models.TextField(max_length=50)
    user = models.ForeignKey(Newuser, on_delete=models.CASCADE)
    doj = models.DateField(auto_now_add=True)
    shop = models.ForeignKey(NewShop, on_delete=models.CASCADE)


class Chat(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    from_user = models.ForeignKey(
        Newuser, on_delete=models.SET_NULL, default=False, null=True, related_name="from_user")
    to_user = models.ForeignKey(
        Newuser, on_delete=models.SET_NULL, default=False, null=True, related_name="to_user")
    from_doctor = models.ForeignKey(
        Newdoctor, on_delete=models.SET_NULL, default=False, null=True, related_name="from_doctor")
    to_doctor = models.ForeignKey(
        Newdoctor, on_delete=models.SET_NULL, default=False, null=True, related_name="to_doctor")
    content = models.TextField()
