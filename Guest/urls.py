from django.urls import path

from Guest import views

app_name = "Guest"

urlpatterns = [
    path('newuser/', views.newuser, name="newuser"),
    path('loadplace/', views.loadplace, name="load-place"),
    path('newshop/', views.newshop, name="newshop"),
    path('newhospital/', views.newhospital, name="newhospital"),
    path('login/', views.Login, name="login"),
    path('newaccount/', views.newaccount, name="newaccount"),

    path('forgotpassword/', views.forgotpassword, name="forgotpassword"),





]
