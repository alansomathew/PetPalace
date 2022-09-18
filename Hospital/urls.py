from django.urls import path
from Hospital import views
app_name="Hospital"

urlpatterns = [
    
    path('Home/',views.homepage,name="home"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('myprofile/',views.myprofile,name="myprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),
    
    path('newdoctor/',views.newdoctor,name="newdoctor"),
    path('viewdoctors/',views.viewdoctors,name="viewdoctors"),

    path('deldoctor/<int:did>/',views.delete_doctor,name="DeleteDoctor"),
    path('feedbackhospital/',views.feedback,name="feedbackhospital"),
    path('complainthospital/',views.complaint,name="complainthospital"),
    path('viewadminfeedbacks/',views.viewadminfeedbacks,name="viewadminfeedbacks"),
    path('logout/',views.logout,name="logout"),
    path('viewadmincomplaints/',views.viewadmincomplaints,name="viewadmincomplaints"),
    path('viewdoctorbookings/',views.viewdoctorbookings,name="viewdoctorbookings"),

    
    

]