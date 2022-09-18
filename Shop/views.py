
from django.shortcuts import render,redirect
from Admin.models import BreedType, PetType
from Admin.views import pettype

from Guest.models import NewShop
from Shop.models import NewFoodItem, NewPets, NewProducts, complaintshop, feedbackshop
from User.models import BookFood, BookPet, BookProduct, complainttoshop1, feedbackusertoshop, returnpet
from User.views import complainttoshop

# Create your views here.

def homepage(request):
    if 'shopid' in request.session:
        return render(request,'Shop/Home.html')
    else:
        return redirect('Guest:login')



def editprofile(request):
    if 'shopid' in request.session:
        editobj=NewShop.objects.get(id=request.session["shopid"])
    
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
            return redirect('/Shop/Home/')
        else:
                return render(request,'Shop/EditProfile.html',{"editobj":editobj})
    else:
        return redirect('Guest:login')


def changepassword(request):
    if 'shopid' in request.session:
        editobj=NewShop.objects.get(id=request.session["shopid"])
        if request.method=='POST':
            curpass=request.POST.get("currentpassword")
            alpass=editobj.password
            if curpass==alpass:
                newpass=request.POST.get("newpassword")
                editobj.password=newpass
                editobj.save()
                return redirect('Guest:login')
        else:
            return render(request,'Shop/ChangePassword.html')
    else:
        return redirect('Guest:login')


def myprofile(request):
    if 'shopid' in request.session:
        obj1=NewShop.objects.get(id=request.session["shopid"])
        return render(request,'Shop/MyProfile.html',{"obj1":obj1})
    else:
        return redirect('Guest:login')
        


def newpets(request):
    if 'shopid' in request.session:
        dis1=NewPets.objects.filter(shop=request.session["shopid"])
        dis=PetType.objects.all()
        if request.method=="POST" and request.FILES:
            breedtype2=request.POST.get("breedtype")
            breedobj=BreedType.objects.get(id=breedtype2)
            shopobj=NewShop.objects.get(id=request.session["shopid"])
            rate2=request.POST.get("rate")
            image2=request.FILES.get("image")
            license2=request.FILES.get("license")
            details2=request.POST.get("details")
            stock2=request.POST.get("stock")

            NewPets.objects.create(breedtype=breedobj,shop=shopobj,rate=rate2,image=image2,license=license2,details=details2,stock=stock2)
            
            return render(request,'Shop/NewPets.html',{"dis":dis,"dis1":dis1})
        else:
            return render(request,'Shop/NewPets.html',{"dis":dis,"dis1":dis1})
    else:
        return redirect('Guest:login')


def loadbreedtype(request):
    if 'shopid' in request.session:

        dis=request.GET.get("disd")
        breedobj=BreedType.objects.filter(pettype=dis)
        return render(request,'Shop/loadbreedtype.html',{"pla":breedobj})
    else:
        return redirect('Guest:login')
        

def delete_newpets(request,did):
    if 'shopid' in request.session:

        disobj=NewPets.objects.get(id=did)
        disobj.delete()
        return redirect('/Shop/newpets/')
    else:
        return redirect('Guest:login')
        


def newproducts(request):
    if 'shopid' in request.session:

        dis1=NewProducts.objects.filter(shop=request.session["shopid"])
        dis=PetType.objects.all()
        if request.method=="POST" and request.FILES:
            productname2=request.POST.get("productname")
            breedtype2=request.POST.get("breedtype")
            breedobj=BreedType.objects.get(id=breedtype2)
            shopobj=NewShop.objects.get(id=request.session["shopid"])
            rate2=request.POST.get("rate")
            image2=request.FILES.get("image")
            stock2=request.POST.get("stock")
            productdetails1=request.POST.get("productdetails")

            NewProducts.objects.create(productdetails=productdetails1,productname=productname2,breedtype=breedobj,shop=shopobj,rate=rate2,image=image2,stock=stock2)
            
            return render(request,'Shop/NewProducts.html',{"dis":dis,"dis1":dis1})
        else:
            return render(request,'Shop/NewProducts.html',{"dis":dis,"dis1":dis1})
    else:
        return redirect('Guest:login')




def delete_newproducts(request,did):
    if 'shopid' in request.session:

        disobj=NewProducts.objects.get(id=did)
        disobj.delete()
        return redirect('/Shop/newproducts/')
    else:
        return redirect('Guest:login')
        

def newfooditem(request):
    
    if 'shopid' in request.session:

        dis1=NewFoodItem.objects.filter(shop=request.session["shopid"])
        dis=PetType.objects.all()
        if request.method=="POST" and request.FILES:
            fooditemname2=request.POST.get("fooditemname")
            breedtype2=request.POST.get("breedtype")
            breedobj=BreedType.objects.get(id=breedtype2)
            shopobj=NewShop.objects.get(id=request.session["shopid"])
            rate2=request.POST.get("rate")
            image2=request.FILES.get("image")
            stock2=request.POST.get("stock")
            fooditemdetails1=request.POST.get("fooditemdetails")

            NewFoodItem.objects.create(fooditemname=fooditemname2,fooditemdetails=fooditemdetails1,breedtype=breedobj,shop=shopobj,rate=rate2,image=image2,stock=stock2)
            
            return render(request,'Shop/NewFoodItem.html',{"dis":dis,"dis1":dis1})
        else:
            return render(request,'Shop/NewFoodItem.html',{"dis":dis,"dis1":dis1})
    else:
        return redirect('Guest:login')



def delete_newfooditem(request,did):
    if 'shopid' in request.session:

        disobj=NewFoodItem.objects.get(id=did)
        disobj.delete()
        return redirect('/Shop/newfooditem/')
    else:
        return redirect('Guest:login')
        


def addpetstock(request,rid):
    if 'shopid' in request.session:

        dis1=NewPets.objects.get(id=rid)
        dis2=int(dis1.stock)

        if int(request.method=="POST"):
            stock1=int(request.POST.get("stock"))
            newstock=dis2+stock1
            dis1.stock=newstock
            dis1.save()
            return redirect('/Shop/newpets/')
        else:
            return render(request,'Shop/Stock.html')
    else:
        return redirect('Guest:login')



def addproductstock(request,rid):
    if 'shopid' in request.session:
        dis1=NewProducts.objects.get(id=rid)
        dis2=int(dis1.stock)

        if int(request.method=="POST"):
            stock1=int(request.POST.get("stock"))
            newstock=dis2+stock1
            dis1.stock=newstock
            dis1.save()
            return redirect('/Shop/newproducts/')
        else:
            return render(request,'Shop/Stock.html')
    else:
        return redirect('Guest:login')



def addfoodstock(request,rid):
    if 'shopid' in request.session:
        dis1=NewFoodItem.objects.get(id=rid)
        dis2=int(dis1.stock)

        if int(request.method=="POST"):
            stock1=int(request.POST.get("stock"))
            newstock=dis2+stock1
            dis1.stock=newstock
            dis1.save()
            return redirect('/Shop/newfooditem/')
        else:
            return render(request,'Shop/Stock.html')
    else:
        return redirect('Guest:login')



def shopviewpetbookings(request):
    if 'shopid' in request.session:
        shopobj=NewShop.objects.get(id=request.session["shopid"])
        bookobj=BookPet.objects.filter(pet__shop=shopobj)
        return render(request,'Shop/ShopviewPetbookings.html',{"obj1":bookobj})
    else:
        return redirect('Guest:login')



def shopviewproductbookings(request):
    if 'shopid' in request.session:
        shopobj=NewShop.objects.get(id=request.session["shopid"])
        bookobj=BookProduct.objects.filter(product__shop=shopobj)
        print(bookobj)
        return render(request,'Shop/ShopviewProductbookings.html',{"obj1":bookobj})
    else:
        return redirect('Guest:login')



def shopviewfoodbookings(request):
    if 'shopid' in request.session:
        shopobj=NewShop.objects.get(id=request.session["shopid"])
        bookobj=BookFood.objects.filter(fooditem__shop=shopobj)
        return render(request,'Shop/ShopviewFoodbookings.html',{"obj1":bookobj})
    else:
        return redirect('Guest:login')


def feedback(request):
    if 'shopid' in request.session:
        editobj=NewShop.objects.get(id=request.session["shopid"])
        if request.method=="POST":
            feedback=request.POST.get("feedback")
            feedbackshop.objects.create(feedback=feedback,shop=editobj)
            return redirect('/Shop/Home/')
        else:
            return render(request,'Shop/FeedbackShop.html')
    else:
        return redirect('Guest:login')

def complaint(request):
    if 'shopid' in request.session:
        editobj=NewShop.objects.get(id=request.session["shopid"])
        if request.method=="POST" and request.FILES:
            complainttitle=request.POST.get("complainttitle")
            content=request.POST.get("content")
            attachment1=request.FILES.get("attachment")
            print(attachment1)
            complaintshop.objects.create(attachment=attachment1,content=content,complainttitle=complainttitle,shop=editobj)
            return redirect('/Shop/Home/')
        else:
            return render(request,'Shop/ShopComplaint.html')
    else:
        return redirect('Guest:login')



def logout(request):
    del request.session['shopid']
    return redirect('Guest:login')


def viewadminfeedbacks(request):
    if 'shopid' in request.session:
        obj1=feedbackshop.objects.all()
        return render(request,'Shop/ViewAdminFeedbacks.html',{"obj1":obj1}) 
    else:
        return redirect('Guest:login')


def viewadmincomplaints(request):
    if 'shopid' in request.session:
        obj1=complaintshop.objects.all()
        return render(request,'Shop/ViewAdminComplaints.html',{"obj1":obj1}) 
    else:
        return redirect('Guest:login')

def replyuser(request,cid):
    if 'shopid' in request.session:
        obj=complainttoshop1.objects.get(id=cid)
        if request.method == 'POST':
            rep=request.POST.get("reply")
            obj.reply=rep
            obj.status=1
            obj.save()
            return redirect ('Shop:UserComplaint')
        else:
            return render (request,'Shop/Reply.html')
    else:
        return redirect('Guest:login')


def viewusercomplaints(request):
    if 'shopid' in request.session:
        shopobj=NewShop.objects.get(id=request.session["shopid"])
        obj1=complainttoshop1.objects.filter(shop=shopobj)
        return render(request,'Shop/ViewUserComplaints.html',{"obj1":obj1})
    else:
        return redirect('Guest:login')


def viewpetreturnrequest(request):
    if 'shopid' in request.session:
        obj1=returnpet.objects.all()
        return render(request,'Shop/ViewPetReturnRequest.html',{"obj1":obj1})
    else:
        return redirect('Guest:login')


def replypetrequest(request,cid):
    if 'shopid' in request.session:
        obj=returnpet.objects.get(id=cid)
        if request.method == 'POST':
            rep=request.POST.get("reply")
            obj.reply=rep
            obj.status=1
            obj.save()
            return redirect ('Shop:viewpetreturnrequest')
        else:
            return render (request,'Shop/ReplyPetRequest.html')
    else:
        return redirect('Guest:login')

def viewuserfeedbacks(request):
    if 'shopid' in request.session:
        shopobj=NewShop.objects.get(id=request.session["shopid"])
        obj1=feedbackusertoshop.objects.filter(shop=shopobj)
        return render(request,'Shop/ViewUserFeedbacks.html',{"obj1":obj1})
    else:
        return redirect('Guest:login')

def setDelivery(request,did):
    if 'shopid' in request.session:
        foodobj=BookFood.objects.get(id=did)
        if request.method=='POST':
            dat=request.POST.get("date")
            foodobj.deliverydate=dat
            foodobj.vstatus=1
            foodobj.save()
            return redirect("Shop:shopviewfoodbookings")
        else:
            return render(request,'Shop/SetDelivery.html')
    else:
        return redirect('Guest:login')


def setDelivery1(request,did):
    if 'shopid' in request.session:
        foodobj=BookPet.objects.get(id=did)
        if request.method=='POST':
            dat=request.POST.get("date")
            foodobj.deliverydate=dat
            foodobj.vstatus=1
            foodobj.save()
            return redirect("Shop:shopviewpetbookings")
        else:
            return render(request,'Shop/SetDelivery.html')
    else:
        return redirect('Guest:login')


def setDelivery2(request,did):
    if 'shopid' in request.session:
        foodobj=BookProduct.objects.get(id=did)
        if request.method=='POST':
            dat=request.POST.get("date")
            foodobj.deliverydate=dat
            foodobj.vstatus=1
            foodobj.save()
            return redirect("Shop:shopviewproductbookings")
        else:
            return render(request,'Shop/SetDelivery.html')
    else:
        return redirect('Guest:login')

