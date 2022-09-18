from django.conf import settings
from django.shortcuts import redirect, render
from Admin.models import District, Place

from Guest.models import NewHospital, Newuser
import Hospital
from Hospital.models import Newdoctor, complainthospital, feedbackhospital
from django.core.mail import send_mail

from User.models import BookDoctor


# Create your views here.

def homepage(request):
    if 'hospitalid' in request.session:

        return render(request,'Hospital/Home.html')
    else:
        return redirect('Guest:login')




def editprofile(request):
    if 'hospitalid' in request.session:
        
        editobj=NewHospital.objects.get(id=request.session["hospitalid"])
        
        if request.method=='POST' and request.FILES:
            name=request.POST.get("name")
            contact=request.POST.get("contact")
            address=request.POST.get("address")
            logo=request.FILES.get("logo")
            
            editobj.name=name
            editobj.contact=contact
            editobj.address=address
            editobj.logo=logo
            

            editobj.save()
            return redirect('/Hospital/Home/')
        else:
            return render(request,'Hospital/EditProfile.html',{"editobj":editobj})
    else:
        return redirect('Guest:login')
        

def changepassword(request):
    if 'hospitalid' in request.session:
        
        editobj=NewHospital.objects.get(id=request.session["hospitalid"])
        if request.method=='POST':
            curpass=request.POST.get("currentpassword")
            alpass=editobj.password
            if curpass==alpass:
                newpass=request.POST.get("newpassword")
                editobj.password=newpass
                editobj.save()
                return redirect('Guest:login')
        else:
            return render(request,'Hospital/ChangePassword.html')
    else:
        return redirect('Guest:login')
        

def myprofile(request):
    if 'hospitalid' in request.session:

        obj1=NewHospital.objects.get(id=request.session["hospitalid"])
        return render(request,'Hospital/MyProfile.html',{"obj1":obj1})
    else:
        return redirect('Guest:login')




def newdoctor(request):
    if 'hospitalid' in request.session:

        dis2=NewHospital.objects.all()
        dis=District.objects.all()
        if request.method=="POST" and request.FILES:
            name1=request.POST.get("name")
            contact1=request.POST.get("contact")
            email1=request.POST.get("email")
            address1=request.POST.get("address")
            place1=request.POST.get("place")
            plobj=Place.objects.get(id=place1)
            photo1=request.FILES.get("photo")
            proof1=request.FILES.get("proof")
            qualification=request.POST.get("qualification")
            hosobj=NewHospital.objects.get(id=request.session["hospitalid"])
            hosname=hosobj.name

            password1=request.POST.get("password")
            Newdoctor.objects.create(qualification=qualification,name=name1,contact=contact1,email=email1,address=address1,hospital=hosobj,place=plobj,photo=photo1,proof=proof1,password=password1)
            send_mail(
            'Respected Sir/Madam '+name1,#subject
            "\rHappy to announce that you are added to"+hosname+" webbased consultation team.\nYour password is " + password1+"and Your Username is "+email1+ ".\n This is from Petpalace Team thank you for joining for our services. \r\n If you have any questions and if there is anything we can improve please reply to this email. \r\n We were always happy to help!. \r\n \r\nTeam Petpalace.\n Thank You.",#body
            settings.EMAIL_HOST_USER,
            [email1],
        )
            return render(request,'Hospital/Doctor.html',{"dis":dis})
        else:
            return render(request,'Hospital/Doctor.html',{"dis":dis})
    else:
        return redirect('Guest:login')


def viewdoctors(request):
    if 'hospitalid' in request.session:

        hosobj=NewHospital.objects.get(id=request.session["hospitalid"])
        viewobj1=Newdoctor.objects.filter(hospital=hosobj)
        return render(request,'Hospital/ViewDoctors.html',{"dis":viewobj1})
    else:
        return redirect('Guest:login')

        



def delete_doctor(request,did):
    if 'hospitalid' in request.session:

        disobj=Newdoctor.objects.get(id=did)

        disobj.delete()
        return redirect('/Hospital/viewdoctors/')
    else:
        return redirect('Guest:login')



def feedback(request):
    if 'hospitalid' in request.session:

        editobj=NewHospital.objects.get(id=request.session["hospitalid"])
        if request.method=="POST":
            feedback=request.POST.get("feedback")
            feedbackhospital.objects.create(feedback=feedback,hospital=editobj)
            return redirect('/Hospital/Home/')


        else:
            return render(request,'Hospital/FeedbackHospital.html')
    else:
        return redirect('Guest:login')



def complaint(request):
    if 'hospitalid' in request.session:

        editobj=NewHospital.objects.get(id=request.session["hospitalid"])
        if request.method=="POST" and request.FILES:
            complainttitle=request.POST.get("complainttitle")
            content=request.POST.get("content")
            attachment=request.FILES.get("attachment")
            complainthospital.objects.create(attachment=attachment,complainttitle=complainttitle,hospital=editobj,content=content)
            return redirect('/Hospital/Home/')
        else:
            return render(request,'Hospital/HospitalComplaint.html')
    else:
        return redirect('Guest:login')

def logout(request):
    del request.session['hospitalid']
    return redirect('Guest:login')


def viewadminfeedbacks(request):
    if 'hospitalid' in request.session:
        obj1=feedbackhospital.objects.all()
        return render(request,'Hospital/ViewAdminFeedbacks.html',{"obj1":obj1}) 
    else:
        return redirect('Guest:login')


def viewadmincomplaints(request):
    if 'hospitalid' in request.session:
        obj1=complainthospital.objects.all()
        return render(request,'Hospital/ViewAdminComplaints.html',{"obj1":obj1}) 
    else:
        return redirect('Guest:login')

def viewdoctorbookings(request):
    if 'hospitalid' in request.session:
        obj2=NewHospital.objects.get(id=request.session["hospitalid"])
        obj1=BookDoctor.objects.filter(doctor_hospital=obj2)
        return render(request,'Hospital/ViewDoctorBookings.html',{"obj1":obj1})
    else:
        return redirect('Guest:login')