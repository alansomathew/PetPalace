
from User import views
from django.urls import path

app_name = "User"

urlpatterns = [
    path('Home/', views.homepage, name="home"),
    path('editprofile/', views.editprofile, name="editprofile"),
    path('myprofile/', views.myprofile, name="myprofile"),
    path('changepassword/', views.changepassword, name="changepassword"),
    path('foodsearch/', views.foodsearch, name="foodsearch"),
    path('viewmorefooditems/<int:sid>/',
         views.viewmorefooditems, name="viewmore-fooditems"),
    path('productsearch/', views.productsearch, name="productsearch"),
    path('viewmoreproductitems/<int:sid>/',
         views.viewmoreproductitems, name="viewmore-productitems"),
    path('shopsearch/', views.shopsearch, name="shopsearch"),
    path('viewpet/<int:sid>/', views.viewpet, name="viewmore-pets"),
    path('viewfood/<int:sid>/', views.viewfood, name="viewmore-foods"),
    path('viewprodduct/<int:sid>/', views.viewproduct, name="viewmore-products"),
    path('takebuypet/<int:sid>/', views.takebuypet, name="takebuypet"),
    path('takebuyproduct/<int:sid>/', views.takebuyproduct, name="takebuyproduct"),
    path('takebuyfood/<int:sid>/', views.takebuyfood, name="takebuyfood"),
    path('viewpetbookings/', views.viewpetbookings, name="viewpetbookings"),
    path('viewproductbookings/', views.viewproductbookings,
         name="viewproductbookings"),
    path('viewfoodbookings/', views.viewfoodbookings, name="viewfoodbookings"),

    path('paypets/', views.paypet, name="paypet"),
    path('payproducts/', views.payproduct, name="payproduct"),
    path('payfoods/', views.payfood, name="payfood"),
    path('paypetlater/<int:nid>/', views.paypetlater, name="paypetlater"),
    path('payproductlater/<int:nid>/',
         views.payproductlater, name="payproductlater"),
    path('payfoodlater/<int:nid>/', views.payfoodlater, name="payfoodlater"),
    path('deleteproductorder/<int:did>/',
         views.deleteproductbook, name="deleteproductorder"),
    path('deletefoodorder/<int:did>/',
         views.deletefoodbook, name="deletefoodorder"),

    path('deletepetorder/<int:did>/', views.deletepetbook, name="deletepetorder"),
    path('deleteproductorder/<int:did>/',
         views.deleteproductbook, name="deleteproductorder"),
    path('feedbackuser/', views.feedback, name="feedbackuser"),
    path('logout/', views.logout, name="logout"),
    path('usercomplaint/', views.complaint, name="usercomplaint"),
    path('hospitalsearch/', views.hospitalsearch, name="hospitalsearch"),
    path('viewdoctors/<int:sid>/', views.viewdoctor, name="viewmore-doctors"),
    path('bookdoctor/<int:sid>/', views.bookdoctor, name="bookdoctor"),
    # path('paydoctor/',views.paydoctor,name="paydoctor"),
    path('viewdoctorbookings/', views.viewdoctorbookings,
         name="viewdoctorbookings"),
    path('paydoctorlater/<int:nid>/', views.paydoctorlater, name="paydoctorlater"),
    path('deletedoctorbook/<int:did>/',
         views.deletedoctorbook, name="deletedoctorbook"),
    path('viewadminfeedbacks/', views.viewadminfeedbacks,
         name="viewadminfeedbacks"),
    path('viewadmincomplaints/', views.viewadmincomplaints,
         name="viewadmincomplaints"),
    path('complainttoshop/<int:cid>/',
         views.complainttoshop, name="complainttoshop"),
    path('returnpet/<int:aid>/', views.returnpet1, name="returnpet"),
    path('viewcomplainttoshop/', views.viewcomplainttoshop,
         name="viewcomplainttoshop"),
    path('feedbacktoshop/<int:cid>/', views.feedbacktoshop, name="feedbacktoshop"),
    path('viewfeedbacktoshop/', views.viewfeedbacktoshop,
         name="viewfeedbacktoshop"),
    path('Chat/<int:cid>/', views.chatuser, name="Chat-user"),
    path('loadchat/', views.loadchatuser, name="load-chat"),

]
