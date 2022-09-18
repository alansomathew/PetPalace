from django.urls import path
from Shop import views
app_name="Shop"

urlpatterns = [
    path('Home/',views.homepage,name="home"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('myprofile/',views.myprofile,name="myprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),
    path('newpets/',views.newpets,name="newpets"),
    path('loadbreedtype/',views.loadbreedtype,name="load-breedtype"),
    path('delnewpets/<int:did>/',views.delete_newpets,name="delete-newpets"),
    path('newproducts/',views.newproducts,name="newproducts"),
    path('delnewproducts/<int:did>/',views.delete_newproducts,name="delete-newproducts"),
    path('newfooditem/',views.newfooditem,name="newfooditem"),
    path('deletenewfooditem/<int:did>/',views.delete_newfooditem,name="delete-newfooditem"),
    
    path('addpetstock/<int:rid>/',views.addpetstock,name="addstock-pets"),
    path('addproductstock/<int:rid>/',views.addproductstock,name="addstock-products"),
    path('addfoodstock/<int:rid>/',views.addfoodstock,name="addstock-foods"),
    path('shopviewpetbookings/',views.shopviewpetbookings,name="shopviewpetbookings"),
    path('shopviewproductbookings/',views.shopviewproductbookings,name="shopviewproductbookings"),
    path('shopviewfoodbookings/',views.shopviewfoodbookings,name="shopviewfoodbookings"),
    path('feedbackshop/',views.feedback,name="feedbackshop"),
    path('complaintshop/',views.complaint,name="complaintshop"),
    path('viewadminfeedbacks/',views.viewadminfeedbacks,name="viewadminfeedbacks"),
    path('viewadmincomplaints/',views.viewadmincomplaints,name="viewadmincomplaints"),
    path('logout/',views.logout,name="logout"),
    path('replyuser/<int:cid>/',views.replyuser,name="reply-user"),
    path('viewusercomplaints/',views.viewusercomplaints,name="UserComplaint"),
    path('viewpetreturnrequest/',views.viewpetreturnrequest,name="viewpetreturnrequest"),
    path('viewuserfeedbacks/',views.viewuserfeedbacks,name="viewuserfeedbacks"),
    
    path('replypetrequest/<int:cid>/',views.replypetrequest,name="reply-petrequest"),
    path('SetDelivery/<int:did>/',views.setDelivery,name="set-delivery"),
    path('SetDelivery1/<int:did>/',views.setDelivery1,name="set-delivery1"),
    path('SetDelivery2/<int:did>/',views.setDelivery2,name="set-delivery2")

]