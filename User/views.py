from django.shortcuts import render, redirect
from Admin.models import BreedType, District, HospitalType, PetType, Place
from Admin.views import breedtype, hospitaltype
from django.core.mail import send_mail

from Guest.models import NewHospital, NewShop, Newuser
from Hospital.models import Newdoctor
from Shop.models import NewFoodItem, NewPets, NewProducts
from User.models import BookDoctor, BookFood, BookPet, BookProduct, Chat, complainttoshop1, complaintuser, feedbackuser, feedbackusertoshop, returnpet
from django.conf import settings

# Create your views here.


def homepage(request):
    if 'userid' in request.session:
        return render(request, 'User/Home.html')
    else:
        return redirect('Guest:login')


def editprofile(request):
    if 'userid' in request.session:
        editobj = Newuser.objects.get(id=request.session["userid"])

        if request.method == 'POST' and request.FILES:
            name = request.POST.get("name")
            contact = request.POST.get("contact")
            address = request.POST.get("address")
            photo = request.FILES.get("photo")
            editobj.name = name
            editobj.contact = contact
            editobj.address = address
            editobj.photo = photo
            editobj.save()
            return redirect('/User/Home/')
        else:
            return render(request, 'User/EditProfile.html', {"editobj": editobj})
    else:
        return redirect('Guest:login')


def changepassword(request):
    if 'userid' in request.session:
        editobj = Newuser.objects.get(id=request.session["userid"])
        if request.method == 'POST':
            curpass = request.POST.get("currentpassword")
            alpass = editobj.password
            if curpass == alpass:
                newpass = request.POST.get("newpassword")
                editobj.password = newpass
                editobj.save()
                return redirect('Guest:login')
            else:
                pass
        else:
            return render(request, 'User/ChangePassword.html')
    else:
        return redirect('Guest:login')


def myprofile(request):
    if 'userid' in request.session:
        obj1 = Newuser.objects.get(id=request.session["userid"])
        return render(request, 'User/MyProfile.html', {"obj1": obj1})
    else:
        return redirect('Guest:login')


def foodsearch(request):
    if 'userid' in request.session:
        breedobj2 = PetType.objects.all()
        obj = NewFoodItem.objects.all()
        print(obj)
        if request.method == "POST":
            breedtype2 = request.POST.get("breedtype")
            breedobj = BreedType.objects.get(id=breedtype2)
            obj = NewFoodItem.objects.filter(breedtype=breedobj)
            return render(request, 'User/FoodSearch.html', {"name": obj, "dis": breedobj2})
        else:
            return render(request, 'User/FoodSearch.html', {"name": obj, "dis": breedobj2})
    else:
        return redirect('Guest:login')


def viewmorefooditems(request, sid):
    if 'userid' in request.session:
        obj1 = NewFoodItem.objects.get(id=sid)
        return render(request, 'User/ViewmoreFooDitems.html', {"obj1": obj1})
    else:
        return redirect('Guest:login')


def productsearch(request):
    if 'userid' in request.session:
        breedobj2 = PetType.objects.all()
        obj = NewProducts.objects.all()
        print(obj)
        if request.method == "POST":
            breedtype2 = request.POST.get("breedtype")
            breedobj = BreedType.objects.get(id=breedtype2)
            obj = NewProducts.objects.filter(breedtype=breedobj)
            return render(request, 'User/ProductSearch.html', {"name": obj, "dis": breedobj2})
        else:
            return render(request, 'User/ProductSearch.html', {"name": obj, "dis": breedobj2})
    else:
        return redirect('Guest:login')


def viewmoreproductitems(request, sid):
    if 'userid' in request.session:
        obj1 = NewProducts.objects.get(id=sid)
        return render(request, 'User/ViewmoreProductitems.html', {"obj1": obj1})
    else:
        return redirect('Guest:login')


def shopsearch(request):
    if 'userid' in request.session:
        placeobj2 = District.objects.all()
        obj = NewShop.objects.filter(vstatus=1)
        print(obj)
        if request.method == "POST":
            place2 = request.POST.get("place")
            placeobj = Place.objects.get(id=place2)
            obj = NewShop.objects.filter(place=placeobj, vstatus=1)
            return render(request, 'User/ShopwiseSearch.html', {"name": obj, "dis": placeobj2})
        else:
            return render(request, 'User/ShopWiseSearch.html', {"name": obj, "dis": placeobj2})
    else:
        return redirect('Guest:login')


def viewpet(request, sid):
    if 'userid' in request.session:
        breedobj2 = PetType.objects.all()
        obj1 = NewShop.objects.get(id=sid)
        obj = NewPets.objects.filter(shop=sid)
        print(obj)
        if request.method == "POST":
            breedtype2 = request.POST.get("breedtype")
            breedobj = BreedType.objects.get(id=breedtype2)
            obj1 = NewPets.objects.filter(breedtype=breedobj)
            return render(request, 'User/ViewPet.html', {"obj2": obj1, "dis": breedobj2})
        else:
            return render(request, 'User/ViewPet.html', {"obj2": obj, "dis": breedobj2})
    else:
        return redirect('Guest:login')


def viewfood(request, sid):
    if 'userid' in request.session:
        breedobj2 = PetType.objects.all()
        obj1 = NewShop.objects.get(id=sid)

        obj = NewFoodItem.objects.filter(shop=sid)
        print(obj)
        if request.method == "POST":
            breedtype2 = request.POST.get("breedtype")
            breedobj = BreedType.objects.get(id=breedtype2)
            obj1 = NewFoodItem.objects.filter(breedtype=breedobj)
            return render(request, 'User/ViewFood.html', {"obj2": obj1, "dis": breedobj2})
        else:
            return render(request, 'User/ViewFood.html', {"obj2": obj, "dis": breedobj2})
    else:
        return redirect('Guest:login')


def viewproduct(request, sid):
    if 'userid' in request.session:
        breedobj2 = PetType.objects.all()
        obj1 = NewShop.objects.get(id=sid)

        obj = NewProducts.objects.filter(shop=sid)
        print(obj)
        if request.method == "POST":
            breedtype2 = request.POST.get("breedtype")
            breedobj = BreedType.objects.get(id=breedtype2)
            obj1 = NewProducts.objects.filter(breedtype=breedobj)
            return render(request, 'User/ViewProduct.html', {"obj2": obj1, "dis": breedobj2})
        else:
            return render(request, 'User/ViewProduct.html', {"obj2": obj, "dis": breedobj2})
    else:
        return redirect('Guest:login')


def takebuypet(request, sid):
    if 'userid' in request.session:
        obj1 = NewPets.objects.get(id=sid)
        editobj = Newuser.objects.get(id=request.session["userid"])
        if request.method == "POST":
            totalprice = request.POST.get("totalamount")
            quantity = int(request.POST.get("quantity"))
            BookPet.objects.create(
                quantity=quantity, totalprice=totalprice, pet=obj1, user=editobj)
            curstock = int(obj1.stock)
            newstock = curstock-quantity
            obj1.stock = newstock
            obj1.save()
            return redirect("User:paypet")
        else:
            return render(request, 'User/BookPet.html', {"obj1": obj1})
    else:
        return redirect('Guest:login')


def takebuyproduct(request, sid):
    if 'userid' in request.session:
        obj1 = NewProducts.objects.get(id=sid)
        editobj = Newuser.objects.get(id=request.session["userid"])
        if request.method == "POST":
            totalprice = request.POST.get("totalamount")
            quantity = int(request.POST.get("quantity"))
            BookProduct.objects.create(
                quantity=quantity, totalprice=totalprice, product=obj1, user=editobj)
            curstock = int(obj1.stock)
            newstock = curstock-quantity
            obj1.stock = newstock
            obj1.save()
            return redirect("User:payproduct")
        else:
            return render(request, 'User/BookProduct.html', {"obj1": obj1})
    else:
        return redirect('Guest:login')


def takebuyfood(request, sid):
    if 'userid' in request.session:
        obj1 = NewFoodItem.objects.get(id=sid)
        editobj = Newuser.objects.get(id=request.session["userid"])
        if request.method == "POST":
            totalprice = request.POST.get("totalamount")
            quantity = int(request.POST.get("quantity"))
            BookFood.objects.create(
                quantity=quantity, totalprice=totalprice, fooditem=obj1, user=editobj)
            curstock = int(obj1.stock)
            newstock = curstock-quantity
            obj1.stock = newstock
            obj1.save()
            return redirect("User:payfood")
        else:
            return render(request, 'User/BookFood.html', {"obj1": obj1})
    else:
        return redirect('Guest:login')


def paypet(request):
    if 'userid' in request.session:
        bobj = BookPet.objects.all().order_by("-id")[0]
        print(bobj)
        if request.method == "POST":
            newid = request.POST.get("txthidden")
            obj = BookPet.objects.get(id=newid)
            obj.pstatus = '1'
            email = obj.user.email
            name = obj.user.name
            send_mail(
                'Respected Sir/Madam '+name,  # subject
                "\rThank For Purchasing from petpalace.\nKindly  come to the shop and collect the pet in the next working day\n.\r\n If you have any questions and if there is anything we can improve please reply to this email. \r\n We were always happy to help!. \r\n \r\nTeam Petpalace.\n Thank You.",  # body
                settings.EMAIL_HOST_USER,
                [email],
            )
            obj.save()
            return redirect("User:viewpetbookings")
        else:
            return render(request, 'User/payment.html', {"bookobj": bobj})
    else:
        return redirect('Guest:login')


def payproduct(request):
    if 'userid' in request.session:
        bobj = BookProduct.objects.all().order_by("-id")[0]
        print(bobj)
        if request.method == "POST":
            newid = request.POST.get("txthidden")
            obj = BookProduct.objects.get(id=newid)
            obj.pstatus = '1'
            email = obj.user.email
            name = obj.user.name
            send_mail(
                'Respected Sir/Madam '+name,  # subject
                "\rThank For Purchasing from petpalace.\nYour product will be delivered within 7 working days\n.\r\n If you have any questions and if there is anything we can improve please reply to this email. \r\n We were always happy to help!. \r\n \r\nTeam Petpalace.\n Thank You.",  # body
                settings.EMAIL_HOST_USER,
                [email],
            )
            obj.save()
            return redirect("User:viewproductbookings")
        else:
            return render(request, 'User/payment.html', {"bookobj": bobj})
    else:
        return redirect('Guest:login')


def payfood(request):
    if 'userid' in request.session:
        bobj = BookFood.objects.all().order_by("-id")[0]
        print(bobj)
        if request.method == "POST":
            newid = request.POST.get("txthidden")
            obj = BookFood.objects.get(id=newid)
            obj.pstatus = '1'
            email1 = obj.user.email
            print(email1)
            name1 = obj.user.name
            print(name1)
            send_mail(
                'Respected Sir/Madam '+name1,  # subject
                "\rThank For Purchasing from petpalace.\nYour pets fooditem will be delivered within 7 working days\n.\r\n If you have any questions and if there is anything we can improve please reply to this email. \r\n We were always happy to help!. \r\n \r\nTeam Petpalace.\n Thank You.",  # body
                settings.EMAIL_HOST_USER,
                [email1],
            )
            obj.save()
            return redirect("User:viewfoodbookings")
        else:
            return render(request, 'User/payment.html', {"bookobj": bobj})
    else:
        return redirect('Guest:login')


def paypetlater(request, nid):
    if 'userid' in request.session:
        bobj = BookPet.objects.get(id=nid)
        if request.method == "POST":
            newid = request.POST.get("txthidden")
            obj = BookPet.objects.get(id=newid)
            obj.pstatus = '1'
            email = obj.user.email
            name = obj.user.name
            send_mail(
                'Respected Sir/Madam '+name,  # subject
                "\rThank For Purchasing from petpalace.\nKindly  come to the shop and collect the pet in the next working day\n.\r\n If you have any questions and if there is anything we can improve please reply to this email. \r\n We were always happy to help!. \r\n \r\nTeam Petpalace.\n Thank You.",  # body
                settings.EMAIL_HOST_USER,
                [email],
            )
            obj.save()
            return redirect("User:viewpetbookings")
        else:
            return render(request, 'User/payment.html', {"bookobj": bobj})
    else:
        return redirect('Guest:login')


def deletepetbook(request, did):
    if 'userid' in request.session:
        disobj = BookPet.objects.get(id=did)
        disobj.delete()
        return redirect('/User/viewpetbookings/')
    else:
        return redirect('Guest:login')


def payproductlater(request, nid):
    if 'userid' in request.session:
        bobj = BookProduct.objects.get(id=nid)
        if request.method == "POST":
            newid = request.POST.get("txthidden")
            obj = BookProduct.objects.get(id=newid)
            obj.pstatus = '1'
            email = obj.user.email
            name = obj.user.name
            send_mail(
                'Respected Sir/Madam '+name,  # subject
                "\rThank For Purchasing from petpalace.\nYour product will be delivered within 7 working days\n.\r\n If you have any questions and if there is anything we can improve please reply to this email. \r\n We were always happy to help!. \r\n \r\nTeam Petpalace.\n Thank You.",  # body
                settings.EMAIL_HOST_USER,
                [email],
            )
            obj.save()
            return redirect("User:viewproductbookings")
        else:
            return render(request, 'User/payment.html', {"bookobj": bobj})
    else:
        return redirect('Guest:login')


def deleteproductbook(request, did):
    if 'userid' in request.session:
        disobj = BookProduct.objects.get(id=did)
        disobj.delete()
        return redirect('/User/viewproductbookings/')
    else:
        return redirect('Guest:login')


def payfoodlater(request, nid):
    if 'userid' in request.session:
        bobj = BookFood.objects.get(id=nid)
        if request.method == "POST":
            newid = request.POST.get("txthidden")
            obj = BookFood.objects.get(id=newid)
            obj.pstatus = '1'
            email = obj.user.email
            name = obj.user.name
            send_mail(
                'Respected Sir/Madam '+name,  # subject
                "\rThank For Purchasing from petpalace.\nYour pets fooditem will be delivered within 7 working days\n.\r\n If you have any questions and if there is anything we can improve please reply to this email. \r\n We were always happy to help!. \r\n \r\nTeam Petpalace.\n Thank You.",  # body
                settings.EMAIL_HOST_USER,
                [email],
            )
            obj.save()
            return redirect("User:viewfoodbookings")
        else:
            return render(request, 'User/payment.html', {"bookobj": bobj})
    else:
        return redirect('Guest:login')


def deletefoodbook(request, did):
    if 'userid' in request.session:
        disobj = BookFood.objects.get(id=did)
        disobj.delete()
        return redirect('/User/viewfoodbookings/')
    else:
        return redirect('Guest:login')


def viewpetbookings(request):
    if 'userid' in request.session:
        userobj = Newuser.objects.get(id=request.session["userid"])
        obj1 = BookPet.objects.filter(user=userobj)
        return render(request, 'User/ViewPetBookings.html', {"obj1": obj1})
    else:
        return redirect('Guest:login')


def viewproductbookings(request):
    if 'userid' in request.session:
        userobj = Newuser.objects.get(id=request.session["userid"])
        obj1 = BookProduct.objects.filter(user=userobj)
        return render(request, 'User/ViewProductBookings.html', {"obj1": obj1})
    else:
        return redirect('Guest:login')


def viewfoodbookings(request):
    if 'userid' in request.session:
        userobj = Newuser.objects.get(id=request.session["userid"])
        obj1 = BookFood.objects.filter(user=userobj)
        return render(request, 'User/ViewFoodBookings.html', {"obj1": obj1})
    else:
        return redirect('Guest:login')


def feedback(request):
    if 'userid' in request.session:
        editobj = Newuser.objects.get(id=request.session["userid"])
        if request.method == "POST":
            feedback = request.POST.get("feedback")
            feedbackuser.objects.create(feedback=feedback, user=editobj)
            return redirect('/User/Home/')
        else:
            return render(request, 'User/Feedbackuser.html')
    else:
        return redirect('Guest:login')


def complaint(request):
    if 'userid' in request.session:
        editobj = Newuser.objects.get(id=request.session["userid"])
        if request.method == "POST" and request.FILES:
            complainttitle = request.POST.get("complainttitle")
            content = request.POST.get("content")
            attachment = request.FILES.get("attachment")

            complaintuser.objects.create(
                complainttitle=complainttitle, user=editobj, content=content, attachment=attachment)
            return redirect('/User/Home/')
        else:
            return render(request, 'User/UserComplaint.html')
    else:
        return redirect('Guest:login')


def logout(request):
    del request.session['userid']
    return redirect('Guest:login')


def hospitalsearch(request):
    if 'userid' in request.session:
        obj2 = HospitalType.objects.all()
        obj = NewHospital.objects.filter(vstatus=1)
        print(obj)
        if request.method == "POST":
            hospitaltype = request.POST.get("hospitaltype")
            obj1 = HospitalType.objects.get(id=hospitaltype)
            obj = NewHospital.objects.filter(hospitaltype=obj1, vstatus=1)
            return render(request, 'User/HospitalwiseSearch.html', {"name": obj, "dis": obj2})
        else:
            return render(request, 'User/HospitalwiseSearch.html', {"name": obj, "dis": obj2})
    else:
        return redirect('Guest:login')


def viewdoctor(request, sid):
    if 'userid' in request.session:
        obj1 = NewHospital.objects.get(id=sid)
        obj2 = Newdoctor.objects.filter(hospital=sid)
        return render(request, 'User/ViewDoctor.html', {"obj1": obj1, "obj2": obj2})
    else:
        return redirect('Guest:login')


def bookdoctor(request, sid):
    if 'userid' in request.session:
        obj1 = Newdoctor.objects.get(id=sid)
        editobj = Newuser.objects.get(id=request.session["userid"])
        if request.method == "POST":
            bookingdate = request.POST.get("bookingdate")
            bookingtime = request.POST.get("bookingtime")

            reason = request.POST.get("reason")
            consultationfee = request.POST.get("consultationfee")
            BookDoctor.objects.create(bookingtime=bookingtime, reason=reason, bookingdate=bookingdate,
                                      doctor=obj1, user=editobj, consultationfee=consultationfee)
            return redirect("User:viewdoctorbookings")
        else:
            return render(request, 'User/BookDoctor.html', {"obj1": obj1})
    else:
        return redirect('Guest:login')

# def paydoctor(request):
#     if 'userid' in request.session:
#         bobj=BookDoctor.objects.all().order_by("-id")[0]
#         print(bobj)
#         if request.method=="POST":
#             newid=request.POST.get("txthidden")
#             obj=BookDoctor.objects.get(id=newid)
#             obj.pstatus='1'
#             doctor=obj.doctor.name
#             print(doctor)
#             email1=obj.user.email
#             print(email1)
#             name1=obj.user.name
#             print(name1)
#             send_mail(
#         'Respected Sir/Madam '+name1,#subject
#         "\rThank For Booking Doctor"+doctor+ "from petpalace.\nHe will contact you soon.\r\n We were always happy to help!.\r\n \r\nTeam Petpalace.\nThank You.",#body
#         settings.EMAIL_HOST_USER,
#         [email1,],
#     )
#             obj.save()
#             return redirect("User:viewdoctorbookings")
#         else:
#             return render(request,'User/paymentdoctor.html',{"bookobj":bobj})
#     else:
#         return redirect('Guest:login')


def viewdoctorbookings(request):
    if 'userid' in request.session:
        userobj = Newuser.objects.get(id=request.session["userid"])
        obj1 = BookDoctor.objects.filter(user=userobj)
        return render(request, 'User/ViewDoctorBookings.html', {"obj1": obj1})
    else:
        return redirect('Guest:login')


def paydoctorlater(request, nid):
    if 'userid' in request.session:
        bobj = BookDoctor.objects.get(id=nid)
        if request.method == "POST":
            newid = request.POST.get("txthidden")
            obj = BookDoctor.objects.get(id=newid)
            obj.pstatus = '1'
            doctor = obj.doctor.name
            print(doctor)
            email1 = obj.user.email
            print(email1)
            name1 = obj.user.name
            print(name1)
            send_mail(
                'Respected Sir/Madam '+name1,  # subject
                "\rThank For Booking Dr "+doctor + \
                ".\nYour Booking status will be updated soon.\r\nTeam Petpalace.\nThank You.",  # body
                settings.EMAIL_HOST_USER,  # from
                [email1],  # to
            )
            obj.save()
            return redirect("User:viewdoctorbookings")
        else:
            return render(request, 'User/paymentdoctor.html', {"bookobj": bobj})
    else:
        return redirect('Guest:login')


def deletedoctorbook(request, did):
    if 'userid' in request.session:
        disobj = BookDoctor.objects.get(id=did)
        disobj.delete()
        return redirect('/User/viewdoctorbookings/')
    else:
        return redirect('Guest:login')


def viewadminfeedbacks(request):
    if 'userid' in request.session:

        userobj = Newuser.objects.get(id=request.session["userid"])
        obj1 = feedbackuser.objects.filter(user=userobj)
        return render(request, 'User/ViewAdminFeedbacks.html', {"obj1": obj1})
    else:
        return redirect('Guest:login')


def viewadmincomplaints(request):
    if 'userid' in request.session:

        userobj = Newuser.objects.get(id=request.session["userid"])
        obj1 = complaintuser.objects.filter(user=userobj)
        return render(request, 'User/ViewAdminComplaints.html', {"obj1": obj1})
    else:
        return redirect('Guest:login')


def complainttoshop(request, cid):
    if 'userid' in request.session:
        bobj = NewShop.objects.get(id=cid)
        editobj = Newuser.objects.get(id=request.session["userid"])
        if request.method == "POST" and request.FILES:
            complainttitle = request.POST.get("complainttitle")
            content = request.POST.get("content")
            attachment = request.FILES.get("attachment")

            complainttoshop1.objects.create(
                shop=bobj, complainttitle=complainttitle, user=editobj, content=content, attachment=attachment)
            return redirect('/User/Home/')
        else:
            return render(request, 'User/ComplaintToShop.html')
    else:
        return redirect('Guest:login')


def returnpet1(request, aid):
    if 'userid' in request.session:

        if request.method == "POST" and request.FILES:
            reason = request.POST.get("reason")
            attachment = request.FILES.get("attachment")
            hosobj = BookPet.objects.get(id=aid)

            shop = hosobj.pet.shop
            petname = hosobj.pet
            quantity = hosobj.quantity
            totalprice = hosobj.totalprice
            bookeddate = hosobj.bookeddate
            returnpet.objects.create(attachment=attachment, reason=reason, pet=petname, user=user,
                                     quantity=quantity, totalprice=totalprice, bookeddate=bookeddate, shop=shop)
            return redirect('/User/Home/')

        else:
            return render(request, 'User/ReturnPet.html')

    else:
        return redirect('Guest:login')


def viewcomplainttoshop(request):
    if 'userid' in request.session:
        userobj = Newuser.objects.get(id=request.session["userid"])
        obj1 = complainttoshop1.objects.filter(user=userobj)
        return render(request, 'User/ViewComplaintToShop.html', {"obj1": obj1})
    else:
        return redirect('Guest:login')


def feedbacktoshop(request, cid):
    if 'userid' in request.session:
        bobj = NewShop.objects.get(id=cid)
        editobj = Newuser.objects.get(id=request.session["userid"])
        if request.method == "POST":
            feedback = request.POST.get("feedback")
            feedbackusertoshop.objects.create(
                shop=bobj, feedback=feedback, user=editobj)
            return redirect('/User/Home/')
        else:
            return render(request, 'User/FeedbackToShop.html')
    else:
        return redirect('Guest:login')


def viewfeedbacktoshop(request):
    if 'userid' in request.session:
        userobj = Newuser.objects.get(id=request.session["userid"])
        obj1 = feedbackusertoshop.objects.filter(user=userobj)
        return render(request, 'User/ViewFeedbackToShop.html', {"obj1": obj1})
    else:
        return redirect('Guest:login')


def chatuser(request, cid):
    chatobj = BookDoctor.objects.get(id=cid)
    if request.method == "POST":
        cied = request.POST.get("cid")
        # print(cied)
        ciedobj = Newdoctor.objects.get(id=cied)
        sobj = Newuser.objects.get(id=request.session["userid"])
        content = request.POST.get("msg")
        # print(cied)
        # print(content)
        Chat.objects.create(
            from_user=sobj, to_doctor=ciedobj, content=content, from_doctor=None, to_user=None)
        return render(request, 'User/Chat.html', {"chatobj": chatobj})
    else:
        return render(request, 'User/Chat.html', {"chatobj": chatobj})


def loadchatuser(request):
    cid = request.GET.get("cid")
    request.session["cid"] = cid

    cid1 = request.session["cid"]
    # print(cid1)

    # print(cid)
    shopobj = Newdoctor.objects.get(id=cid)
    # print(userobj)
    sid = request.session["userid"]
    # print(sid)
    suserobj = Newuser.objects.get(id=request.session["userid"])
    # chatobj1 = Chat.objects.filter(Q(to_user=suserobj) | Q(
    #     from_user=suserobj), Q(to_shop=shopobj) | Q(from_shop=shopobj))
    # print(chatobj1)  # send message

    # print(chatobj2)  # recived msg
    chatobj = Chat.objects.raw(
        "select * from User_chat c inner join Guest_newuser u on (u.id=c.from_user_id) or (u.id=c.to_user_id) WHERE  c.from_doctor_id=%s or c.to_doctor_id=%s order by c.date", params=[(cid1), (cid1)])

    print(chatobj.query)

    return render(request, 'User/Load.html', {"obj": chatobj, "sid": sid, "shop": shopobj, "userobj": suserobj})
