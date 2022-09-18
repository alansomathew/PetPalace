from django.db import models

from Hospital.models import Newdoctor

# Create your models here.
class feedbackdoctor(models.Model):
    feedback=models.TextField(max_length=50)
    doctor=models.ForeignKey(Newdoctor,on_delete=models.CASCADE)
    doj=models.DateField(auto_now_add=True)

class complaintdoctor(models.Model):
    complainttitle=models.CharField(max_length=50)
    content=models.TextField(max_length=50)
    doctor=models.ForeignKey(Newdoctor,on_delete=models.CASCADE)
    attachment=models.FileField(null=True,upload_to='Uploads/attachmentdoctor/')
    reply=models.TextField(null=True,max_length=50,default="noreply")
    doj=models.DateField(auto_now_add=True)
    status=models.IntegerField(default=False)