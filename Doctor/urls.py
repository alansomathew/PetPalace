from Doctor import views
from django.urls import path

app_name = "Doctor"

urlpatterns = [
    path('Home/', views.homepage, name="home"),
    path('editprofile/', views.editprofile, name="editprofile"),
    path('myprofile/', views.myprofile, name="myprofile"),
    path('changepassword/', views.changepassword, name="changepassword"),
    path('feedbackdoctor/', views.feedback, name="feedbackdoctor"),
    path('complaintdoctor/', views.complaint, name="complaintdoctor"),
    path('viewadminfeedbacks/', views.viewadminfeedbacks,
         name="viewadminfeedbacks"),
    path('viewadmincomplaints/', views.viewadmincomplaints,
         name="viewadmincomplaints"),
    path('logout/', views.logout, name="logout"),
    path('viewdoctorbooking/', views.viewdoctorbooking, name="viewdoctorbooking"),
    path('acceptdoctor/<int:aid>/', views.acceptdoctor, name="accept-user"),
    path('rejectdoctor/<int:rid>/', views.rejectdoctor, name="reject-user"),
    path('acceptedbookings/', views.acceptedbookings, name="acceptedbookings"),
    path('Chat/<int:cid>/', views.chat, name="Chat-doctor"),
    path('loadchat/', views.loadchat, name="load-chat"),


]
