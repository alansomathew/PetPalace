
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.conf import settings

from Admin.models import District, HospitalType, Place,Adminlogin
from Guest.models import  NewHospital, NewShop, Newuser
from Hospital.models import Newdoctor
from Shop.models import NewPets

# Create your views here.


def newuser(request):
    dis=District.objects.all()
    if request.method=="POST" and request.FILES:
        name1=request.POST.get("name")
        contact1=request.POST.get("contact")
        email1=request.POST.get("email")
        address1=request.POST.get("address")
        place1=request.POST.get("place")
        plobj=Place.objects.get(id=place1)
        photo1=request.FILES.get("photo")
        password1=request.POST.get("password")
        Newuser.objects.create(name=name1,contact=contact1,email=email1,address=address1,place=plobj,photo=photo1,password=password1)
        return render(request,'Guest/NewUser.html',{"dis":dis})
    else:
        return render(request,'Guest/NewUser.html',{"dis":dis})

def loadplace(request):
    dis=request.GET.get("disd")#district
    pla=Place.objects.filter(district=dis)#from table Place we are filtering
    return render(request,'Guest/loadplace.html',{"pla":pla})



def newshop(request):
    dis=District.objects.all()
    if request.method=="POST" and request.FILES:
        shopname1=request.POST.get("name")
        contact1=request.POST.get("contact")
        email1=request.POST.get("email")
        address1=request.POST.get("address")
        shopownername1=request.POST.get("shopownername")
        shopownercontact1=request.POST.get("shopownercontact")
        
        place1=request.POST.get("place")
        plobj=Place.objects.get(id=place1)
        proof1=request.FILES.get("proof")
        logo1=request.FILES.get("logo")

        password1=request.POST.get("password")
        NewShop.objects.create(name=shopname1,contact=contact1,email=email1,shopownername=shopownername1,shopownercontact=shopownercontact1,address=address1,place=plobj,proof=proof1,logo=logo1,password=password1)
        return render(request,'Guest/NewShop.html',{"dis":dis})
    else:
        return render(request,'Guest/NewShop.html',{"dis":dis})

def newhospital(request):
    htype=HospitalType.objects.all()
    dis=District.objects.all()
    if request.method=="POST" and request.FILES:
        name1=request.POST.get("name")
        contact1=request.POST.get("contact")
        email1=request.POST.get("email")
        address1=request.POST.get("address")
        place1=request.POST.get("place")
        plobj=Place.objects.get(id=place1)
        hospital1=request.POST.get("hospitaltype")
        plobj1=HospitalType.objects.get(id=hospital1)
        proof1=request.FILES.get("proof")
        logo1=request.FILES.get("logo")

        password1=request.POST.get("password")
        NewHospital.objects.create(name=name1,contact=contact1,email=email1,address=address1,place=plobj,hospitaltype=plobj1,proof=proof1,logo=logo1,password=password1)
        return render(request,'Guest/NewHospital.html',{"dis":dis,'htype':htype})
    else:
        return render(request,'Guest/NewHospital.html',{"dis":dis,"htype":htype})



def Login(request):
    if request.method=='POST':
        email1=request.POST.get("email")
        password1=request.POST.get("password")
        usercount=Newuser.objects.filter(email=email1,password=password1).count()
        shopcount=NewShop.objects.filter(email=email1,password=password1).count()
        hospitalcount=NewHospital.objects.filter(email=email1,password=password1).count()
        doctorcount=Newdoctor.objects.filter(email=email1,password=password1).count()
        admincount=Adminlogin.objects.filter(adminemail=email1,adminpassword=password1).count()
        

        if usercount>0:
            userobj=Newuser.objects.get(email=email1,password=password1)
            request.session["userid"]=userobj.id
            return redirect('User:home')
        
        
        elif shopcount>0:
            shopobj=NewShop.objects.get(email=email1,password=password1,vstatus=1)
            request.session["shopid"]=shopobj.id
            return redirect('Shop:home')

        
        elif hospitalcount>0:
            hospitalobj=NewHospital.objects.get(email=email1,password=password1,vstatus=1)
            request.session["hospitalid"]=hospitalobj.id
            return redirect('Hospital:home')
        
        
        elif doctorcount>0:
            doctorobj=Newdoctor.objects.get(email=email1,password=password1)
            request.session["doctorid"]=doctorobj.id
            return redirect('Doctor:home')

        elif admincount>0:
            adminobj=Adminlogin.objects.get(adminemail=email1,adminpassword=password1)
            request.session["adminid"]=adminobj.id
            return redirect('Admin:home')
    else:
        return render(request,'Guest/Login.html')

def newaccount(request):
   return render(request,'Guest/NewAccount.html')


def home(request):
    bobj=NewPets.objects.all()
    return render(request,'Guest/Home.html',{"obj":bobj})

def forgotpassword(request):
    if request.method=='POST':
        email1=request.POST.get("email")
        obj=Newuser.objects.get(email=email1)
        name=obj.name
        email2=obj.email
        password1=obj.password
        send_mail(
            'Respected Sir/Madam '+name,#subject
            "\rNo need to worry,you can relogin into your account with your previous password.\nYour previous  password is "+password1  +" and Your Username is "+email2+ " .If you didn't request a password reset feel free to delete this email.\nThank You  \r\n \r\n TheTeam Petpalace.\n ",#body
            settings.EMAIL_HOST_USER,
            [email2],
        )
        obj.save()
        return redirect('Guest:login')
    else:
        return render(request,'Guest/ForgotPassword.html')


