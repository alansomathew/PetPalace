

from django.conf import settings
from django.shortcuts import render,redirect
from django.core.mail import send_mail
from Admin.models import BreedType, District, HospitalType, PetType,Place, ProductType
from Doctor.models import complaintdoctor, feedbackdoctor
from Guest.models import NewHospital, NewShop, Newuser
from Hospital.models import complainthospital, feedbackhospital
from Shop.models import complaintshop, feedbackshop
from User.models import complaintuser, feedbackuser
# Create your views here.

def district(request):
    if 'adminid' in request.session:
        disobj=District.objects.all()
        if request.method=="POST":
            district1=request.POST.get("district")
            District.objects.create(district=district1)
            return render(request,'Admin/District.html',{"dis":disobj})
        else:
            return render(request,'Admin/District.html',{"dis":disobj})
    else:
        return redirect('Guest:login')
    
def delete_district(request,did):
    if 'adminid' in request.session:
        disobj=District.objects.get(id=did)
        disobj.delete()
        return redirect('/Admin/district/')
    else:
        return redirect('Guest:login')
def edit_district(request,eid):
    if 'adminid' in request.session:
        editobj=District.objects.get(id=eid)
        disobj=District.objects.all()
        if request.method=='POST':
            district2=request.POST.get("district")
            editobj.district=district2
            editobj.save()
            return redirect('/Admin/district/')
        else:
            return render(request,'Admin/District.html',{"dis":disobj,"editobj":editobj})
    else:
        return redirect('Guest:login')

def place(request):
    if 'adminid' in request.session:
        placeobj=Place.objects.all()
        districtobj=District.objects.all()
        if request.method=="POST":
            distobj1=request.POST.get("district")
            dist=District.objects.get(id=distobj1)
            placeobj1=request.POST.get("place")
            Place.objects.create(district=dist,place=placeobj1)
            return render(request,'Admin/Place.html',{"dis":districtobj,"pla":placeobj})
        else:
            return render(request,'Admin/Place.html',{"dis":districtobj,"pla":placeobj})
    else:
        return redirect('Guest:login')

def delete_place(request,pid):
    if 'adminid' in request.session:
        placeobj=Place.objects.get(id=pid)
        placeobj.delete()
        return redirect('/Admin/place/')
    else:
        return redirect('Guest:login')

def pettype(request):
    if 'adminid' in request.session:
        pettypeobj=PetType.objects.all()
        if request.method=="POST":
            pettype1=request.POST.get("pettype")
            PetType.objects.create(pettype=pettype1)
            return render(request,'Admin/PetType.html',{"pet":pettypeobj})
        else:
            return render(request,'Admin/PetType.html',{"pet":pettypeobj})
    else:
        return redirect('Guest:login')

def edit_pettype(request,eid):
    if 'adminid' in request.session:
        editobj=PetType.objects.get(id=eid)
        disobj=PetType.objects.all()
        if request.method=='POST':
            pettype=request.POST.get("pettype")
            editobj.pettype=pettype
            editobj.save()
            return redirect('/Admin/pettype/')
        else:
            return render(request,'Admin/PetType.html',{"pet":disobj,"editobj":editobj})
    else:
        return redirect('Guest:login')

def delete_pettype(request,pid):
    if 'adminid' in request.session:
        placeobj=PetType.objects.get(id=pid)
        placeobj.delete()
        return redirect('/Admin/pettype/')
    else:
        return redirect('Guest:login')

def breedtype(request):
    if 'adminid' in request.session:
        petobj=PetType.objects.all()
        breedobj=BreedType.objects.all()
        if request.method=="POST":
            petypeobj1=request.POST.get("pettype")
            petypeobj2=PetType.objects.get(id=petypeobj1)
            breedobj1=request.POST.get("breedtype")
            BreedType.objects.create(breedtype=breedobj1,pettype=petypeobj2)
            return render(request,'Admin/BreedType.html',{"dis":petobj,"pla":breedobj})
        else:
            return render(request,'Admin/BreedType.html',{"dis":petobj,"pla":breedobj})
    else:
        return redirect('Guest:login')

def delete_breedtype(request,pid):
    if 'adminid' in request.session:
        breedobj3=BreedType.objects.get(id=pid)
        breedobj3.delete()
        return redirect('/Admin/breedtype/')
    else:
        return redirect('Guest:login')

def producttype(request):
    if 'adminid' in request.session:
        disobj=ProductType.objects.all()
        if request.method=="POST":
            producttype1=request.POST.get("producttype")
            ProductType.objects.create(producttype=producttype1)
            return render(request,'Admin/ProductType.html',{"dis":disobj})
        else:
            return render(request,'Admin/ProductType.html',{"dis":disobj})
    else:
        return redirect('Guest:login')

def delete_producttype(request,did):
    if 'adminid' in request.session:
        disobj=ProductType.objects.get(id=did)
        disobj.delete()
        return redirect('/Admin/producttype/')
    else:
        return redirect('Guest:login')

def edit_producttype(request,eid):
    if 'adminid' in request.session:
        editobj=ProductType.objects.get(id=eid)
        disobj=ProductType.objects.all()
        if request.method=='POST':
            producttype2=request.POST.get("producttype")
            editobj.producttype=producttype2
            editobj.save()
            return redirect('/Admin/producttype/')
        else:
            return render(request,'Admin/ProductType.html',{"dis":disobj,"editobj":editobj})
    else:
        return redirect('Guest:login')

def hospitaltype(request):
    if 'adminid' in request.session:
        disobj=HospitalType.objects.all()
        if request.method=="POST":
            hospitaltype1=request.POST.get("hospitaltype")
            HospitalType.objects.create(hospitaltype=hospitaltype1)
            return render(request,'Admin/HospitalType.html',{"dis":disobj})
        else:
            return render(request,'Admin/HospitalType.html',{"dis":disobj})
    else:
        return redirect('Guest:login')

def delete_hospitaltype(request,did):
    if 'adminid' in request.session:
        disobj=HospitalType.objects.get(id=did)
        disobj.delete()
        return redirect('/Admin/hospitaltype/')
    else:
        return redirect('Guest:login')

def edit_hospitaltype(request,eid):
    if 'adminid' in request.session:
        editobj=HospitalType.objects.get(id=eid)
        disobj=HospitalType.objects.all()
        if request.method=='POST':
            hospitaltype2=request.POST.get("hospitaltype")
            editobj.hospitaltype=hospitaltype2
            editobj.save()
            return redirect('/Admin/hospitaltype/')
        else:
            return render(request,'Admin/HospitalType.html',{"dis":disobj,"editobj":editobj})
    else:
        return redirect('Guest:login')

def newshops(request):
    if 'adminid' in request.session:
        newshopsobj=NewShop.objects.filter(vstatus=0)
        return render(request,'Admin/NewShops.html',{"newshopsobj":newshopsobj})

def newhospitals(request):
    if 'adminid' in request.session:
        newhospitalsobj=NewHospital.objects.filter(vstatus=0)
        return render(request,'Admin/NewHospitals.html',{"newhospitalsobj":newhospitalsobj})
    else:
        return redirect('Guest:login')

def accepthos(request,aid):
    if 'adminid' in request.session:
        hosobj=NewHospital.objects.get(id=aid)
        name=hosobj.name
        email=hosobj.email
        password1=hosobj.password
        hosobj.vstatus='1'
        send_mail(
            'Respected Sir/Madam '+name,#subject
            "\rVerification Successfully Welcome to petpalace.\nYour password is "+password1  +"and Your Username is "+email+ ".\n This is from Petpalace Team thank you for signing upto our services. \r\n If you have any questions and if there is anything we can improve please reply to this email. \r\n We were always happy to help!. \r\n \r\nTeam Petpalace.\n Thank You.",#body
            settings.EMAIL_HOST_USER,
            [email],
        )
        hosobj.save()
        return redirect('Admin:newhospitals')
    else:
        return redirect('Guest:login')

def rejecthos(request,rid):
    if 'adminid' in request.session:
        hosobj=NewHospital.objects.get(id=rid)
        name=hosobj.name
        email=hosobj.email
        hosobj.vstatus='2'
        send_mail(
            'Respected Sir/Madam '+ name,#subject
            "\rSorry Your Verification Failed.Try to login after few hours.\n This is from Petpalace Team thank you for signing upto our services. \r\n If you have any questions and if there is anything we can improve please reply to this email. \r\n We were always happy to help!. \r\n \r\nTeam Petpalace.\n Thank You.",#body
            settings.EMAIL_HOST_USER,
            [email],
        )
        hosobj.save()
        return redirect('Admin:newhospitals')
    else:
        return redirect('Guest:login')

def acceptshop(request,aid):
    if 'adminid' in request.session:
        hosobj=NewShop.objects.get(id=aid)
        name=hosobj.name
        email=hosobj.email
        password1=hosobj.password
        hosobj.vstatus='1'
        send_mail(
            'Respected Sir/Madam '+name,#subject
            "\rVerification Successfully Welcome to petpalace.\nYour password is "+password1  +"and Your Username is "+email+ ".\n This is from Petpalace Team thank you for signing upto our services. \r\n If you have any questions and if there is anything we can improve please reply to this email. \r\n We were always happy to help!. \r\n \r\nTeam Petpalace.\n Thank You.",#body
            settings.EMAIL_HOST_USER,
            [email],
        )
        hosobj.save()
        return redirect('Admin:newshops')
    else:
        return redirect('Guest:login')

def rejectshop(request,rid):
    if 'adminid' in request.session:
        hosobj=NewShop.objects.get(id=rid)
        hosobj.vstatus='2'
        name=hosobj.name
        email=hosobj.email
        send_mail(
            'Respected Sir/Madam '+name,#subject
            "\rSorry Your Verification Failed.Try to login after few hours.\n This is from Petpalace Team thank you for signing upto our services. \r\n If you have any questions and if there is anything we can improve please reply to this email. \r\n We were always happy to help!. \r\n \r\nTeam Petpalace.\n Thank You.",#body
            settings.EMAIL_HOST_USER,
            [email],
        )
        hosobj.save()
        return redirect('Admin:newshops')
    else:
        return redirect('Guest:login')

def newusers(request):
    if 'adminid' in request.session:
        newusersobj=Newuser.objects.all()
        return render(request,'Admin/NewUsers.html',{"newusersobj":newusersobj})
    else:
        return redirect('Guest:login')

def accepthospitals(request):
    if 'adminid' in request.session:
        hosobj=NewHospital.objects.filter(vstatus=1)
        return render(request,'Admin/AcceptHospitals.html',{"hosobj":hosobj})
    else:
        return redirect('Guest:login')

    
def rejecthos_fromlist(request,rid):
    if 'adminid' in request.session:
            hosobj=NewHospital.objects.get(id=rid)
            hosobj.vstatus='2'
            hosobj.save()
            return redirect('Admin:accepthospitals')
    else:
        return redirect('Guest:login')

def rejecthospitals(request):
    if 'adminid' in request.session:
        hosobj=NewHospital.objects.filter(vstatus=2)
        return render(request,'Admin/RejectHospitals.html',{"hosobj":hosobj})
    else:
        return redirect('Guest:login')

def accepthos_fromlist(request,aid):
    if 'adminid' in request.session:
        hosobj=NewHospital.objects.get(id=aid)
        hosobj.vstatus='1'
        hosobj.save()
        return redirect('Admin:rejecthospitals')
    else:
        return redirect('Guest:login')

def acceptshops(request):
    if 'adminid' in request.session:
        hosobj=NewShop.objects.filter(vstatus=1)
        return render(request,'Admin/AcceptShops.html',{"hosobj":hosobj})
    else:
        return redirect('Guest:login')

    
def rejectshop_fromlist(request,rid):
    if 'adminid' in request.session:
        hosobj=NewShop.objects.get(id=rid)
        hosobj.vstatus='2'
        hosobj.save()
        return redirect('Admin:acceptshops') 
    else:
        return redirect('Guest:login')

def rejectshops(request):
    if 'adminid' in request.session:
        hosobj=NewShop.objects.filter(vstatus=2)
        return render(request,'Admin/RejectShops.html',{"hosobj":hosobj})
    else:
        return redirect('Guest:login')

def acceptshop_fromlist(request,aid):
    if 'adminid' in request.session:
        hosobj=NewShop.objects.get(id=aid)
        hosobj.vstatus='1'
        hosobj.save()
        return redirect('Admin:rejectshops')
    else:
        return redirect('Guest:login')

def homepage(request):
    if 'adminid' in request.session:
        return render(request,'Admin/Home.html')
    else:
        return redirect('Guest:login')


def viewuserfeedbacks(request):
    if 'adminid' in request.session:
        obj1=feedbackuser.objects.all()
        return render(request,'Admin/ViewUserFeedbacks.html',{"obj1":obj1})
    else:
        return redirect('Guest:login')

def viewhospitalfeedbacks(request):
    if 'adminid' in request.session:
        obj1=feedbackhospital.objects.all()
        return render(request,'Admin/ViewHospitalFeedbacks.html',{"obj1":obj1})
    else:
        return redirect('Guest:login')

def viewdoctorfeedbacks(request):
    if 'adminid' in request.session:
        obj1=feedbackdoctor.objects.all()
        return render(request,'Admin/ViewDoctorFeedbacks.html',{"obj1":obj1})
    else:
        return redirect('Guest:login')

def viewshopfeedbacks(request):
    if 'adminid' in request.session:
        obj1=feedbackshop.objects.all()
        return render(request,'Admin/ViewShopFeedbacks.html',{"obj1":obj1})
    else:
        return redirect('Guest:login')

def viewusercomplaints(request):
    if 'adminid' in request.session:
        obj1=complaintuser.objects.all()
        return render(request,'Admin/ViewUserComplaint.html',{"obj1":obj1})
    else:
        return redirect('Guest:login')

def viewshopcomplaints(request):
    if 'adminid' in request.session:
        obj1=complaintshop.objects.all()
        return render(request,'Admin/ViewShopComplaint.html',{"obj1":obj1})
    else:
        return redirect('Guest:login')

def viewhospitalcomplaints(request):
    if 'adminid' in request.session:
        obj1=complainthospital.objects.all()
        return render(request,'Admin/ViewHospitalComplaint.html',{"obj1":obj1})
    else:
        return redirect('Guest:login')

def viewdoctorcomplaints(request):
    if 'adminid' in request.session:
        obj1=complaintdoctor.objects.all()
        return render(request,'Admin/ViewDoctorComplaint.html',{"obj1":obj1})
    else:
        return redirect('Guest:login')

def logout(request):
    del request.session['adminid']
    return redirect('Guest:login')

def replyuser(request,cid):
    if 'adminid' in request.session:
        obj=complaintuser.objects.get(id=cid)
        if request.method == 'POST':
            rep=request.POST.get("reply")
            obj.reply=rep
            obj.status=1
            obj.save()
            return redirect ('Admin:UserComplaint')
        else:
            return render (request,'Admin/Reply.html')
    else:
        return redirect('Guest:login')
        

def replyshop(request,cid):
    if 'adminid' in request.session:
        obj=complaintshop.objects.get(id=cid)
        if request.method == 'POST':
            rep=request.POST.get("reply")
            obj.reply=rep
            obj.status=1
            obj.save()
            return redirect ('Admin:ShopComplaint')
        else:
            return render (request,'Admin/Reply.html')
    else:
        return redirect('Guest:login')



def replydoctor(request,cid):
    if 'adminid' in request.session:
        obj=complaintdoctor.objects.get(id=cid)
        if request.method == 'POST':
            rep=request.POST.get("reply")
            obj.reply=rep
            obj.status=1
            obj.save()
            return redirect ('Admin:DoctorComplaint')
        else:
            return render (request,'Admin/Reply.html')
    else:
        return redirect('Guest:login')



def replyhospital(request,cid):
    if 'adminid' in request.session:
        obj=complainthospital.objects.get(id=cid)
        if request.method == 'POST':
            rep=request.POST.get("reply")
            obj.reply=rep
            obj.status=1
            obj.save()
            return redirect ('Admin:HospitalComplaint')
        else:
            return render (request,'Admin/Reply.html')
    else:
        return redirect('Guest:login')

     

