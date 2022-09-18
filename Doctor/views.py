from django.shortcuts import render, redirect
from Doctor.models import complaintdoctor, feedbackdoctor

from Guest.models import NewHospital, Newuser
from Hospital.models import Newdoctor
from User.models import BookDoctor, Chat
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

def homepage(request):
    if 'doctorid' in request.session:

        return render(request, 'Doctor/Home.html')
    else:
        return redirect('Guest:login')


def editprofile(request):
    if 'doctorid' in request.session:

        viewobj1 = Newdoctor.objects.get(id=request.session["doctorid"])

        if request.method == 'POST' and request.FILES:
            name = request.POST.get("name")
            contact = request.POST.get("contact")

            address = request.POST.get("address")
            photo = request.FILES.get("photo")

            viewobj1.name = name
            viewobj1.contact = contact

            viewobj1.address = address
            viewobj1.photo = photo

            viewobj1.save()
            return redirect('/Doctor/Home/')
        else:
            return render(request, 'Doctor/EditProfile.html', {"editobj": viewobj1})
    else:
        return redirect('Guest:login')


def changepassword(request):
    if 'doctorid' in request.session:

        editobj = Newdoctor.objects.get(id=request.session["doctorid"])

        if request.method == 'POST':
            curpass = request.POST.get("currentpassword")
            alpass = editobj.password
            if curpass == alpass:
                newpass = request.POST.get("newpassword")
                editobj.password = newpass
                editobj.save()
                return redirect('Guest:login')
        else:
            return render(request, 'Doctor/ChangePassword.html')
    else:
        return redirect('Guest:login')


def myprofile(request):
    if 'doctorid' in request.session:

        obj1 = Newdoctor.objects.get(id=request.session["doctorid"])

        return render(request, 'Doctor/MyProfile.html', {"obj1": obj1})
    else:
        return redirect('Guest:login')


def feedback(request):
    if 'doctorid' in request.session:

        editobj = Newdoctor.objects.get(id=request.session["doctorid"])
        if request.method == "POST":
            feedback = request.POST.get("feedback")
            feedbackdoctor.objects.create(feedback=feedback, doctor=editobj)
            return redirect('/Doctor/Home/')

        else:
            return render(request, 'Doctor/Feedbackdoctor.html')
    else:
        return redirect('Guest:login')


def complaint(request):
    if 'doctorid' in request.session:
        editobj = Newdoctor.objects.get(id=request.session["doctorid"])
        if request.method == "POST" and request.FILES:
            complainttitle = request.POST.get("complainttitle")
            content = request.POST.get("content")
            attachment = request.FILES.get("attachment")
            complaintdoctor.objects.create(
                complainttitle=complainttitle, content=content, doctor=editobj, attachment=attachment)
            return redirect('/Doctor/Home/')
        else:
            return render(request, 'Doctor/DoctorComplaint.html')
    else:
        return redirect('Guest:login')


def logout(request):
    if 'doctorid' in request.session:
        del request.session['doctorid']
        return redirect('Guest:login')
    else:
        return redirect('Guest:login')


def viewadminfeedbacks(request):
    if 'doctorid' in request.session:
        obj1 = feedbackdoctor.objects.all()
        return render(request, 'Doctor/ViewAdminFeedbacks.html', {"obj1": obj1})
    else:
        return redirect('Guest:login')


def viewadmincomplaints(request):
    if 'doctorid' in request.session:
        obj1 = complaintdoctor.objects.all()
        return render(request, 'Doctor/ViewAdminComplaints.html', {"obj1": obj1})
    else:
        return redirect('Guest:login')


def viewdoctorbooking(request):
    if 'doctorid' in request.session:
        doctorobj = Newdoctor.objects.get(id=request.session["doctorid"])
        dobj = BookDoctor.objects.filter(doctor=doctorobj)
        return render(request, 'Doctor/ViewBookings.html', {"dobj": dobj})
    else:
        return redirect('Guest:login')


def acceptdoctor(request, aid):
    if 'doctorid' in request.session:
        userobj = BookDoctor.objects.get(id=aid)
        doctor = userobj.doctor.name
        name = userobj.user.name
        email1 = userobj.user.email
        userobj.vstatus = '1'
        send_mail(
            'Respected Sir/Madam '+name,  # subject
            "\rYour appointment for consulting Dr."+doctor + \
            " is successful.He will contact you soon. \r\n \r\n From Team Petpalace.\n Thank You.",  # body
            settings.EMAIL_HOST_USER,
            [email1],
        )
        userobj.save()
        return redirect('Doctor:viewdoctorbooking')
    else:
        return redirect('Guest:login')


def rejectdoctor(request, rid):
    if 'doctorid' in request.session:
        userobj = BookDoctor.objects.get(id=rid)
        doctor = userobj.doctor.name
        name = userobj.user.name
        email1 = userobj.user.email
        userobj.vstatus = '2'
        send_mail(
            'Respected Sir/Madam ' + name,  # subject
            "\r Your appointment for consulting dr."+doctor + \
            " is resheduled.Please take new appointment for consulting the doctor. \r\n \r\nThis is from Team Petpalace.\n Thank You.",  # body
            settings.EMAIL_HOST_USER,
            [email1],
        )
        userobj.save()
        return redirect('Doctor:viewdoctorbooking')
    else:
        return redirect('Guest:login')


def acceptedbookings(request):
    if 'doctorid' in request.session:
        hosobj = BookDoctor.objects.filter(vstatus=1)
        return render(request, 'Doctor/AcceptBookings.html', {"hosobj": hosobj})
    else:
        return redirect('Guest:login')


def chat(request, cid):
    chatobj = BookDoctor.objects.get(id=cid)
    if request.method == "POST":
        cied = request.POST.get("cid")
        # print(cied)
        ciedobj = Newuser.objects.get(id=cied)
        sobj = Newdoctor.objects.get(id=request.session["doctorid"])
        content = request.POST.get("msg")
        # print(cied)
        print(content)
        Chat.objects.create(
            from_doctor=sobj, to_user=ciedobj, content=content, from_user=None, to_doctor=None)
        return render(request, 'Doctor/Chat.html', {"chatobj": chatobj})
    else:
        return render(request, 'Doctor/Chat.html', {"chatobj": chatobj})


def loadchat(request):
    cid = request.GET.get("cid")
    request.session["cid"] = cid

    cid1 = request.session["cid"]
    # print(cid1)

    # print(cid)
    shopobj = Newuser.objects.get(id=cid)
    # print(userobj)
    sid = request.session["doctorid"]
    # print(sid)
    suserobj = Newdoctor.objects.get(id=request.session["doctorid"])
    # chatobj1 = Chat.objects.filter(Q(to_user=suserobj) | Q(
    #     from_user=suserobj), Q(to_shop=shopobj) | Q(from_shop=shopobj))
    # print(chatobj1)  # send message

    # print(chatobj2)  # recived msg
    chatobj = Chat.objects.raw(
        "select * from User_chat c inner join Hospital_newdoctor u on (u.id=c.from_doctor_id) or (u.id=c.to_doctor_id) WHERE  c.from_user_id=%s or c.to_user_id=%s order by c.date", params=[(cid1), (cid1)])

    print(chatobj.query)

    return render(request, 'Doctor/Load.html', {"obj": chatobj, "sid": sid, "shop": shopobj, "userobj": suserobj})
