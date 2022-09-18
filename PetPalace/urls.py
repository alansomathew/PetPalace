"""PetPalace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from Guest import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Admin/', include("Admin.urls")),
    path('Guest/', include("Guest.urls")),
    path('Shop/', include("Shop.urls")),
    path('User/', include("User.urls")),
    path('Hospital/', include("Hospital.urls")),
    path('Doctor/', include("Doctor.urls")),
    path('', views.home, name="home"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
